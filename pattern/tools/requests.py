#!/usr/bin/env python3
"""Local request bundles. Python 3.10+, macOS/Linux; standard library only.

request.md is canonical: `---json\n`, one JSON object, `\n---\n`, and a
fully derived readable body. It is not arbitrary editable Markdown. Writers hold
one flock. A durable .request-txn intent bridges folder moves and record writes;
reads refuse pending recovery; recover (or the next mutation) finishes it.
This records director decisions, not authentication, agent liveness or transport.
"""
import argparse
import contextlib
import copy
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import uuid

STATES = {"inbox", "queued", "active", "review", "blocked", "done", "canceled"}
TERMINAL = {"done", "canceled"}
CONTAINERS = {"inbox": "pending", "queued": "pending", "active": "working", "review": "working", "blocked": "working", "done": "archive", "canceled": "archive"}
ID = re.compile(r"REQ-[0-9a-f]{32}\Z")
SOURCE_ID = re.compile(r"UR-[0-9a-f]{32}\Z")
PROJECT_ID = re.compile(r"PROJ-[0-9a-f]{32}\Z")
FORMAT = "request-bundles"
LINK_KINDS = {"group", "decomposes", "related", "depends_on"}


def fail(message):
    raise ValueError(message)


def nonempty(value, name):
    if not isinstance(value, str) or not value.strip():
        fail(f"{name} must be a nonempty string")
    return value


def strings(value, name, required=True):
    if not isinstance(value, list) or (required and not value):
        fail(f"{name} must be {'a nonempty' if required else 'a'} list of strings")
    for item in value:
        nonempty(item, name)
    return value


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def byte_digest(value):
    return hashlib.sha256(value).hexdigest()


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def safe(path):
    path = Path(os.path.abspath(path))
    # macOS exposes standard system aliases; canonicalize only these known roots,
    # then reject every other symlink component (including inside the store).
    if sys.platform == "darwin":
        for alias in ("/var", "/tmp", "/etc"):
            if str(path) == alias or str(path).startswith(alias + "/"):
                if Path(alias).is_symlink() and os.path.realpath(alias) == "/private" + alias:
                    path = Path("/private" + str(path))
                break
    for part in (path, *path.parents):
        if part.is_symlink():
            fail(f"Symlink is not supported: {part}")
    return path


def fsync_dir(path):
    fd = os.open(safe(path), os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def atomic_bytes(path, value):
    path = safe(path)
    fd, name = tempfile.mkstemp(prefix=".request-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(value)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        fsync_dir(path.parent)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def atomic_write(path, value):
    atomic_bytes(path, (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))


def name_component(value):
    nonempty(value, "filename")
    if value in {".", ".."} or "/" in value or "\\" in value or "\x00" in value:
        fail("Filename must be one safe path component")
    return value


def markdown(record):
    body = (f"# {record['title']}\n\n"
            f"Request: {record['id']}\nState: {record['state']}\n"
            f"Revision: {record['revision']}\nOwner: {record['owner'] or 'unassigned'}\n\n"
            "Sources: " + ", ".join(x["source_id"] for x in record["sources"]) + "\n\n"
            "This view is derived. Use the recorder to change the canonical JSON above.\n")
    return ("---json\n" + json.dumps(record, ensure_ascii=False, indent=2) + "\n---\n" + body).encode("utf-8")


def parse_markdown(data):
    if not data.startswith(b"---json\n"):
        fail("request.md requires the schema-2 JSON frontmatter envelope")
    try:
        encoded, _ = data[8:].split(b"\n---\n", 1)
        record = json.loads(encoded)
    except (ValueError, UnicodeError):
        fail("Damaged request.md JSON envelope")
    validate_record(record)
    if markdown(record) != data:
        fail("request.md body or encoding differs from canonical derived rendering")
    return record


def identity(value, local_project, request_required=True):
    if not isinstance(value, dict) or set(value) - {"project_id", "request_id", "locator"}:
        fail("target requires project_id, request_id and optional locator")
    for key in ("project_id", "request_id"):
        if key == "request_id" and key not in value and not request_required:
            continue
        token = nonempty(value.get(key), key)
        if len(token) > 256 or any(ord(c) < 32 for c in token) or "/" in token or "\\" in token or token in {".", ".."}:
            fail("External identity must be a bounded opaque token, not a path")
    if value["project_id"] == local_project and not ID.fullmatch(value.get("request_id", "")):
        fail("Local request identity requires bundled REQ ID")
    if "locator" in value:
        nonempty(value["locator"], "locator hint")
    return copy.deepcopy(value)


def history(event, at):
    return {"event_id": event["event_id"], "type": event["type"], "at": at, "payload_hash": digest(event), "data": copy.deepcopy(event)}


def retry(record, event):
    for previous in record["history"]:
        if previous["event_id"] == event["event_id"]:
            if previous["payload_hash"] != digest(event):
                fail("Event ID was already used with a different payload")
            return True
    return False


def initial(request_id, event, at):
    if set(event) != {"event_id", "type", "title", "source_id", "project_id"}:
        fail("Invalid create event fields")
    if not PROJECT_ID.fullmatch(event.get("project_id", "")) or not SOURCE_ID.fullmatch(event.get("source_id", "")):
        fail("Invalid create project/source identity")
    return dict(schema_version=2, project_id=event["project_id"], id=request_id,
                title=nonempty(event.get("title"), "title"), state="inbox", revision=1,
                created_at=at, updated_at=at,
                sources=[{"source_id": event["source_id"], "event_id": event["event_id"], "at": at}],
                owner=None, acceptance=[], human_gate={"required": False, "status": "not_required", "evidence": []},
                execution_receipt=None, director_acceptance=None, artifacts=[], evidence=[], blocked=None,
                files=[], links=[], handoffs=[], history=[])


def decision(e):
    return {"director": nonempty(e.get("director"), "director"), "reason": nonempty(e.get("reason"), "reason")}


def change(r, e, at):
    kind, state = e.get("type"), r["state"]
    allowed = {"plan": {"inbox", "queued"}, "dispatch": {"queued"}, "submit": {"active"},
               "accept": {"review"}, "block": {"queued", "active", "review"}, "resume": {"blocked"},
               "requeue": {"active", "blocked"}, "revise": {"review"}, "reopen": TERMINAL,
               "cancel": STATES - TERMINAL, "amend": {"inbox", "queued", "blocked"}, "note": STATES,
               "link": STATES - TERMINAL, "unlink": STATES - TERMINAL,
               "review_dependency": STATES - TERMINAL, "observe": STATES,
               "handoff_propose": {"queued", "active", "blocked"}, "handoff_request": STATES - TERMINAL,
               "handoff_acknowledge": STATES - TERMINAL, "handoff_return": STATES - TERMINAL,
               "handoff_accept": STATES - TERMINAL, "handoff_waive": STATES - TERMINAL, "attach": STATES}
    fields = {"plan": {"owner", "acceptance", "human_gate"}, "dispatch": {"receipt"}, "submit": {"evidence", "artifacts"},
              "accept": {"director", "evidence", "human_gate"}, "block": {"reason"}, "resume": {"reason"},
              "requeue": {"reason"}, "revise": {"reason"}, "reopen": {"reason"}, "cancel": {"reason"},
              "amend": {"source_id"}, "note": {"text", "artifacts", "evidence"},
              "link": {"link_id", "kind", "target"}, "unlink": {"link_id", "director", "reason"},
              "review_dependency": {"link_id", "director", "evidence"},
              "observe": {"link_id", "handoff_id", "status", "evidence", "observed_at"},
              "handoff_propose": {"handoff_id", "target", "outcome", "required", "return_route", "constraints", "content", "acceptance"},
              "handoff_request": {"handoff_id", "receipt"},
              "handoff_acknowledge": {"handoff_id", "receipt", "owner", "target"},
              "handoff_return": {"handoff_id", "receipt", "evidence"},
              "handoff_accept": {"handoff_id", "director", "evidence"},
              "handoff_waive": {"handoff_id", "director", "reason", "revised_acceptance"}, "attach": {"file"}}
    if kind not in allowed or state not in allowed[kind]:
        fail(f"Invalid transition: {state} + {kind}")
    if set(e) - fields[kind] - {"event_id", "type"}:
        fail(f"Unknown event fields: {sorted(set(e) - fields[kind] - {'event_id', 'type'})}")
    if kind == "plan":
        r["owner"] = nonempty(e.get("owner"), "owner")
        r["acceptance"] = strings(e.get("acceptance"), "acceptance")
        gate = e.get("human_gate")
        if not isinstance(gate, dict) or set(gate) != {"required"} or type(gate["required"]) is not bool:
            fail("plan human_gate must be {required: true|false}")
        r["human_gate"] = {"required": gate["required"], "status": "pending" if gate["required"] else "not_required", "evidence": []}
        r["state"] = "queued"
    elif kind == "dispatch":
        nonempty(r["owner"], "planned owner")
        strings(r["acceptance"], "planned acceptance")
        receipt = e.get("receipt")
        if not isinstance(receipt, dict) or receipt.get("kind") not in {"agent", "direct"}:
            fail("receipt requires kind: agent|direct")
        nonempty(receipt.get("id"), "receipt.id")
        r["execution_receipt"] = dict(receipt, at=at)
        r["state"] = "active"
    elif kind == "submit":
        r["evidence"].extend(strings(e.get("evidence"), "evidence"))
        r["artifacts"].extend(strings(e.get("artifacts", []), "artifacts", False))
        r["state"] = "review"
    elif kind == "accept":
        director = nonempty(e.get("director"), "director")
        evidence = strings(e.get("evidence"), "acceptance evidence")
        gate = e.get("human_gate")
        if r["human_gate"]["required"]:
            if not isinstance(gate, dict) or set(gate) != {"status", "evidence"} or gate.get("status") != "passed":
                fail("Recorded human gate requires status: passed and evidence; it cannot be waived")
            r["human_gate"].update(status="passed", evidence=strings(gate.get("evidence"), "human gate evidence"))
        elif gate is not None:
            fail("No human gate was planned; omit human_gate in accept")
        for h in r["handoffs"]:
            if h["required"] and h["status"] not in {"accepted", "waived"}:
                fail("Required handoff has not received explicit source acceptance")
        r["director_acceptance"] = {"director": director, "evidence": evidence, "at": at}
        r["evidence"].extend(evidence)
        r["state"] = "done"
    elif kind == "block":
        r["blocked"] = {"reason": nonempty(e.get("reason"), "reason"), "from_state": state, "at": at}
        r["state"] = "blocked"
    elif kind in {"resume", "requeue", "revise", "reopen"}:
        nonempty(e.get("reason"), "reason")
        r.update(state="queued", execution_receipt=None, director_acceptance=None, blocked=None)
        r["human_gate"].update(status="pending" if r["human_gate"]["required"] else "not_required", evidence=[])
        if kind == "reopen":
            for h in r["handoffs"]:
                if h["status"] == "accepted":
                    h["status"] = "returned"
                    h.pop("acceptance", None)
    elif kind == "cancel":
        nonempty(e.get("reason"), "reason")
        r.update(state="canceled", blocked=None)
    elif kind == "amend":
        if not SOURCE_ID.fullmatch(e.get("source_id", "")):
            fail("amend requires a captured source_id")
        r["sources"].append({"source_id": e["source_id"], "event_id": e["event_id"], "at": at})
        r.update(acceptance=[], execution_receipt=None, director_acceptance=None)
    elif kind == "note":
        nonempty(e.get("text"), "text")
        r["evidence"].extend(strings(e.get("evidence", []), "evidence", False))
        r["artifacts"].extend(strings(e.get("artifacts", []), "artifacts", False))
    elif kind == "link":
        link_id = nonempty(e.get("link_id"), "link_id")
        if any(x["link_id"] == link_id for x in r["links"]):
            fail("link_id already exists; use a new identity after removal")
        if e.get("kind") not in LINK_KINDS:
            fail("link kind must be group|decomposes|related|depends_on")
        r["links"].append({"link_id": link_id, "kind": e["kind"], "target": identity(e.get("target"), r["project_id"]), "at": at, "removed": None, "review": None, "observations": []})
    elif kind in {"unlink", "review_dependency"}:
        links = [x for x in r["links"] if x["link_id"] == e.get("link_id") and not x["removed"]]
        if len(links) != 1:
            fail("Unknown active link_id")
        link = links[0]
        if kind == "unlink":
            link["removed"] = dict(decision(e), at=at)
        else:
            if link["kind"] != "depends_on" or link["target"]["project_id"] == r["project_id"]:
                fail("review_dependency applies only to external required dependencies")
            link["review"] = {"director": nonempty(e.get("director"), "director"), "evidence": strings(e.get("evidence"), "review evidence"), "at": at}
    elif kind == "handoff_propose":
        handoff_id = nonempty(e.get("handoff_id"), "handoff_id")
        if any(x["handoff_id"] == handoff_id for x in r["handoffs"]):
            fail("handoff_id already exists")
        target = identity(e.get("target"), r["project_id"], request_required=False)
        if target["project_id"] == r["project_id"]:
            fail("Handoff target must be external")
        if type(e.get("required")) is not bool:
            fail("handoff required must be boolean")
        h = {"handoff_id": handoff_id, "target": target, "required": e["required"], "status": "proposed", "at": at, "observations": [], "current_liveness": "unknown"}
        for key in ("outcome", "return_route", "constraints", "content"):
            h[key] = nonempty(e.get(key), key)
        h["criteria"] = strings(e.get("acceptance"), "handoff acceptance")
        r["handoffs"].append(h)
    elif kind.startswith("handoff_"):
        matches = [x for x in r["handoffs"] if x["handoff_id"] == e.get("handoff_id")]
        if len(matches) != 1:
            fail("Unknown handoff_id")
        h = matches[0]
        if kind == "handoff_request":
            if h["status"] != "proposed":
                fail("Handoff request requires proposed status")
            h.update(status="requested", request={"receipt": nonempty(e.get("receipt"), "request receipt"), "at": at})
        elif kind == "handoff_acknowledge":
            if h["status"] != "requested":
                fail("Handoff acknowledgment requires requested status")
            target = identity(e.get("target", h["target"]), r["project_id"])
            if target["project_id"] != h["target"]["project_id"] or ("request_id" in h["target"] and target["request_id"] != h["target"]["request_id"]):
                fail("Acknowledgment cannot change the proposed receiver identity")
            h["target"] = target
            h.update(status="acknowledged", acknowledgment={"receipt": nonempty(e.get("receipt"), "acknowledgment receipt"), "owner": nonempty(e.get("owner"), "external owner"), "at": at})
            if h["required"]:
                r["blocked"] = {"reason": f"Waiting on acknowledged external owner {h['acknowledgment']['owner']} ({h['handoff_id']})", "from_state": state, "at": at}
                r["state"] = "blocked"
        elif kind == "handoff_return":
            if h["status"] != "acknowledged":
                fail("Handoff result requires acknowledgment")
            h.update(status="returned", result={"receipt": nonempty(e.get("receipt"), "result receipt"), "evidence": strings(e.get("evidence"), "returned evidence"), "at": at})
        elif kind == "handoff_accept":
            if h["status"] != "returned":
                fail("Source acceptance requires a returned result")
            h.update(status="accepted", acceptance={"director": nonempty(e.get("director"), "director"), "evidence": strings(e.get("evidence"), "source acceptance evidence"), "at": at})
        elif kind == "handoff_waive":
            if h["status"] == "waived":
                fail("Handoff already waived")
            waiver = dict(decision(e), at=at)
            if h["required"]:
                revised = strings(e.get("revised_acceptance"), "revised_acceptance")
                if revised == r["acceptance"]:
                    fail("Required handoff waiver must explicitly revise acceptance scope")
                waiver["previous_acceptance"] = r["acceptance"]
                waiver["revised_acceptance"] = revised
                r.update(state="queued", acceptance=revised, execution_receipt=None, director_acceptance=None, blocked=None)
                r["human_gate"].update(status="pending" if r["human_gate"]["required"] else "not_required", evidence=[])
            elif "revised_acceptance" in e:
                fail("Optional handoff waiver does not revise acceptance")
            h.update(status="waived", waiver=waiver)
    elif kind == "observe":
        if ("link_id" in e) == ("handoff_id" in e):
            fail("observe requires exactly one link_id or handoff_id")
        key = "link_id" if "link_id" in e else "handoff_id"
        matches = [x for x in r["links" if key == "link_id" else "handoffs"] if x[key] == e[key]]
        if len(matches) != 1:
            fail("Unknown observation target")
        matches[0]["observations"].append({"status": nonempty(e.get("status"), "observed status"), "evidence": strings(e.get("evidence"), "observation evidence"), "observed_at": nonempty(e.get("observed_at"), "observed_at"), "recorded_at": at, "current_liveness": "unknown"})
    elif kind == "attach":
        file = e.get("file")
        validate_file(file)
        if any(x["path"] == file["path"] for x in r["files"]):
            fail("File path already has a receipt")
        r["files"].append(copy.deepcopy(file))


def validate_file(file):
    if not isinstance(file, dict) or set(file) != {"path", "original_name", "size", "sha256"}:
        fail("Invalid file receipt")
    parts = file["path"].split("/")
    if len(parts) != 2 or parts[0] not in {"assets", "evidence", "attachments"}:
        fail("Invalid bounded file path")
    name_component(parts[1])
    name_component(file["original_name"])
    if type(file["size"]) is not int or file["size"] < 0 or not re.fullmatch(r"[a-f0-9]{64}", file["sha256"]):
        fail("Invalid file size/hash")


def validate_record(r):
    if not isinstance(r, dict) or r.get("schema_version") != 2 or not ID.fullmatch(r.get("id", "")) or r.get("state") not in STATES:
        fail("Invalid schema, ID, or state")
    if type(r.get("revision")) is not int or r["revision"] != len(r.get("history", [])) or r["revision"] < 1:
        fail("Revision must match nonempty history")
    seen, rebuilt = set(), None
    for entry in r["history"]:
        event_id = nonempty(entry.get("event_id"), "history event_id")
        data, at = entry.get("data", {}), nonempty(entry.get("at"), "history timestamp")
        if event_id in seen or entry.get("payload_hash") != digest(data):
            fail("Duplicate event ID or damaged history payload")
        if data.get("event_id") != event_id or data.get("type") != entry.get("type"):
            fail("History metadata differs from event")
        if rebuilt is None:
            if data.get("type") != "create":
                fail("First history event must create the request")
            rebuilt = initial(r["id"], data, at)
        else:
            change(rebuilt, data, at)
            rebuilt["revision"] += 1
            rebuilt["updated_at"] = at
        rebuilt["history"].append(entry)
        seen.add(event_id)
    if r != rebuilt:
        fail("Record fields differ from replayed history")
    for field in ("acceptance", "evidence", "artifacts"):
        strings(r.get(field), field, False)
    gate = r["human_gate"]
    if r["state"] in {"active", "review", "done"}:
        nonempty(r.get("owner"), "owner")
        strings(r["acceptance"], "acceptance")
        if not r.get("execution_receipt"):
            fail("Execution receipt required")
    if r["state"] in {"review", "done"}:
        strings(r["evidence"], "review evidence")
    if r["state"] == "blocked" and not r.get("blocked", {}).get("reason"):
        fail("Blocked reason required")
    if r["state"] == "done":
        if not r.get("director_acceptance", {}).get("director") or not r["director_acceptance"].get("evidence"):
            fail("Explicit director acceptance with evidence required")
        if gate["required"] and (gate["status"] != "passed" or not gate.get("evidence")):
            fail("Required human gate has not passed")


class Store:
    @classmethod
    def init(cls, team, project_id=None):
        team = safe(team)
        team.mkdir(parents=True, exist_ok=True)
        lock = safe(team / ".requests.lock")
        fd = os.open(lock, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, "a") as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            path = safe(team / "config.json")
            config = json.loads(path.read_bytes()) if path.exists() else {"schema_version": 1, "record_mode": "tracked"}
            if not isinstance(config, dict) or config.get("schema_version") != 1 or config.get("record_mode") != "tracked":
                fail("init requires schema_version 1, record_mode tracked; existing config was preserved")
            requests = safe(team / "requests")
            if requests.exists() and list(requests.glob("*.json")):
                fail("Legacy flat JSON request store found; preserved unchanged. Use a separate new store; explicit migration is not provided.")
            if "request_store" in config:
                store = cls(team)
                if project_id is not None and project_id != store.project_id:
                    fail("Existing project_id cannot be replaced")
                return copy.deepcopy(store.config)
            if requests.exists() and any(requests.iterdir()):
                fail("Unrecognized populated request store; preserved unchanged")
            project_id = project_id or "PROJ-" + uuid.uuid4().hex
            if not PROJECT_ID.fullmatch(project_id):
                fail("project_id must be PROJ- followed by 32 lowercase hex characters")
            config["request_store"] = {"schema_version": 2, "format": FORMAT, "project_id": project_id}
            atomic_write(path, config)
            return config

    def __init__(self, team):
        self.team = safe(team)
        self.config = json.loads(safe(self.team / "config.json").read_bytes())
        spec = self.config.get("request_store", {})
        if self.config.get("schema_version") != 1 or self.config.get("record_mode") != "tracked" or spec.get("schema_version") != 2 or spec.get("format") != FORMAT or not PROJECT_ID.fullmatch(spec.get("project_id", "")):
            fail("Schema-2 request-bundles store required; run init for an empty store. Legacy flat JSON is never migrated automatically.")
        self.project_id = spec["project_id"]
        self.directory = safe(self.team / "requests")
        self.sources = safe(self.team / "sources")
        self.transaction = safe(self.team / ".request-txn")

    def fault(self, point):
        """Override in disposable tests to raise at prepared/files/moved/written."""

    @contextlib.contextmanager
    def locked(self):
        fd = os.open(safe(self.team / ".requests.lock"), os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, "a") as stream:
            fcntl.flock(stream, fcntl.LOCK_EX)
            self._recover()
            yield

    def ready(self):
        if safe(self.transaction).exists():
            fail("Interrupted mutation pending; run recover (read-only commands do not repair)")
        safe(self.directory)
        if self.directory.exists():
            for entry in self.directory.iterdir():
                safe(entry)
                if entry.suffix == ".json":
                    fail("Legacy flat JSON files conflict with bundle store; preserved unchanged")
                if entry.name not in {"pending", "working", "archive"} or not entry.is_dir():
                    fail(f"Unrecognized request-root entry: {entry.name}; preserved for resolution")

    def _locate(self, request_id, required=True):
        if not ID.fullmatch(request_id):
            fail("ID must be REQ- followed by 32 lowercase hexadecimal characters")
        found = []
        for container in ("pending", "working", "archive"):
            parent = safe(self.directory / container)
            bundle = safe(parent / request_id)
            if bundle.exists():
                if not bundle.is_dir():
                    fail("Request bundle must be a directory")
                found.append(bundle)
        if len(found) > 1:
            fail("Duplicate request ID across containers; preserved for manual resolution")
        if not found:
            if required:
                fail(f"Request not found: {request_id}")
            return None
        return found[0]

    def path(self, request_id):
        self.ready()
        return safe(self._locate(request_id) / "request.md")

    def _read(self, request_id):
        bundle = self._locate(request_id)
        record = parse_markdown(safe(bundle / "request.md").read_bytes())
        if record["id"] != request_id or record["project_id"] != self.project_id:
            fail("Record identity differs from bundle/store")
        if bundle.parent.name != CONTAINERS[record["state"]]:
            fail("Directory/state mismatch")
        for source in record["sources"]:
            self.read_source(source["source_id"], _internal=True)
        for file in record["files"]:
            self._verify_file(bundle, file)
        self._check_tree(bundle)
        return record

    def read(self, request_id):
        self.ready()
        return self._read(request_id)

    def _records(self):
        ids = []
        for container in ("pending", "working", "archive"):
            parent = safe(self.directory / container)
            if parent.exists():
                for path in sorted(parent.iterdir()):
                    safe(path)
                    if not ID.fullmatch(path.name):
                        fail(f"Unrecognized request bundle: {path.name}")
                    ids.append(path.name)
        return [self._read(i) for i in sorted(ids)]

    def records(self):
        self.ready()
        return self._records()

    def _check_tree(self, directory):
        for current, dirs, files in os.walk(safe(directory), followlinks=False):
            for name in dirs + files:
                safe(Path(current) / name)

    def _verify_file(self, root, receipt):
        validate_file(receipt)
        data = safe(root / receipt["path"]).read_bytes()
        if len(data) != receipt["size"] or byte_digest(data) != receipt["sha256"]:
            fail(f"File integrity mismatch: {receipt['path']}")

    def read_source(self, source_id, _internal=False):
        if not _internal:
            self.ready()
        if not SOURCE_ID.fullmatch(source_id):
            fail("Invalid source_id")
        directory = safe(self.sources / source_id)
        return self._read_source_at(directory, source_id)

    def _read_source_at(self, directory, source_id):
        meta = json.loads(safe(directory / "source.json").read_bytes())
        if not isinstance(meta, dict) or set(meta) != {"schema_version", "source_id", "project_id", "event_id", "created_at", "input", "attachments", "payload_hash"} or meta["schema_version"] != 2 or meta["source_id"] != source_id or meta["project_id"] != self.project_id:
            fail("Invalid source metadata identity/schema")
        nonempty(meta["event_id"], "capture event_id")
        nonempty(meta["created_at"], "source capture time")
        data = safe(directory / "input.txt").read_bytes()
        nonempty(data.decode("utf-8"), "source input")
        if meta["input"] != {"size": len(data), "sha256": byte_digest(data)}:
            fail("Source input integrity mismatch")
        if not isinstance(meta["attachments"], list):
            fail("Source attachments must be a list")
        seen = set()
        for receipt in meta["attachments"]:
            validate_file(receipt)
            if not receipt["path"].startswith("attachments/") or receipt["path"] in seen:
                fail("Invalid or duplicate source attachment")
            seen.add(receipt["path"])
            self._verify_file(directory, receipt)
        if meta["payload_hash"] != digest({"input": meta["input"], "attachments": meta["attachments"]}):
            fail("Source capture payload integrity mismatch")
        self._check_tree(directory)
        return meta

    def capture(self, raw, event_id, attachments=()):
        nonempty(raw, "raw request")
        nonempty(event_id, "capture event_id")
        data = raw.encode("utf-8")
        files, names = [], set()
        for file in attachments:
            file = safe(file)
            name = name_component(file.name)
            if name in names:
                fail("Duplicate original attachment filename")
            names.add(name)
            content = file.read_bytes()
            receipt = {"path": "attachments/" + name, "original_name": name, "size": len(content), "sha256": byte_digest(content)}
            files.append((receipt, content))
        files.sort(key=lambda x: x[0]["path"])
        payload = {"input": {"size": len(data), "sha256": byte_digest(data)}, "attachments": [r for r, _ in files]}
        source_id = "UR-" + uuid.uuid5(uuid.NAMESPACE_URL, self.project_id + ":source:" + event_id).hex
        with self.locked():
            self.ready()
            target = safe(self.sources / source_id)
            if target.exists():
                old = self.read_source(source_id)
                if old["event_id"] != event_id or old["payload_hash"] != digest(payload):
                    fail("Capture event ID was already used with a different payload")
                return old
            meta = dict(schema_version=2, source_id=source_id, project_id=self.project_id, event_id=event_id, created_at=now(), **payload, payload_hash=digest(payload))
            stage = self._stage()
            bundle = stage / "bundle"
            bundle.mkdir()
            atomic_bytes(bundle / "input.txt", data)
            atomic_write(bundle / "source.json", meta)
            for receipt, content in files:
                (bundle / "attachments").mkdir(exist_ok=True)
                atomic_bytes(bundle / receipt["path"], content)
            self._prepare(stage, {"operation": "source", "source_id": source_id, "metadata": meta})
            self._recover()
            return meta

    def create(self, raw=None, title=None, event_id=None, source_id=None):
        nonempty(title, "title")
        nonempty(event_id, "event_id")
        if (raw is None) == (source_id is None):
            fail("create requires exactly one raw text or source_id")
        if raw is not None:
            source_id = self.capture(raw, "create-source:" + event_id)["source_id"]
        event = {"event_id": event_id, "type": "create", "title": title, "source_id": source_id, "project_id": self.project_id}
        request_id = "REQ-" + uuid.uuid5(uuid.NAMESPACE_URL, self.project_id + ":request:" + event_id).hex
        with self.locked():
            self.ready()
            self.read_source(source_id)
            if self._locate(request_id, required=False):
                record = self._read(request_id)
                retry(record, event)
                return record
            at = now()
            record = initial(request_id, event, at)
            record["history"].append(history(event, at))
            self._commit(None, record)
            return record

    def _check_links(self, record, accepting=False):
        records = {r["id"]: r for r in self._records()}
        records[record["id"]] = record
        graph = {}
        for r in records.values():
            edges = []
            for link in r["links"]:
                if link["removed"]:
                    continue
                target = link["target"]
                if target["project_id"] == self.project_id:
                    if target["request_id"] not in records:
                        fail("Local link target does not exist")
                    if link["kind"] == "depends_on":
                        edges.append(target["request_id"])
                if accepting and r["id"] == record["id"] and link["kind"] == "depends_on":
                    if target["project_id"] == self.project_id:
                        if records[target["request_id"]]["state"] != "done":
                            fail("Required local dependency is not done (canceled is not success)")
                    elif not link["review"]:
                        fail("External dependency requires explicit director-reviewed evidence")
            graph[r["id"]] = edges
        visiting, visited = set(), set()
        def visit(node):
            if node in visiting:
                fail("Required dependency cycle")
            if node in visited:
                return
            visiting.add(node)
            for target in graph[node]:
                visit(target)
            visiting.remove(node)
            visited.add(node)
        for node in graph:
            visit(node)

    def apply(self, request_id, event, expected):
        if not isinstance(event, dict):
            fail("Event must be an object")
        event = copy.deepcopy(event)
        nonempty(event.get("event_id"), "event_id")
        if event.get("type") == "attach":
            fail("Use attach command/API to capture file bytes with a receipt")
        if event.get("type") == "amend" and "raw_text" in event:
            raw = event.pop("raw_text")
            if "source_id" in event:
                fail("amend requires raw_text or source_id, not both")
            event["source_id"] = self.capture(raw, f"amend:{request_id}:{event['event_id']}")["source_id"]
        with self.locked():
            self.ready()
            before = self._read(request_id)
            if retry(before, event):
                return before
            if type(expected) is not int or before["revision"] != expected:
                fail(f"Stale revision: expected {expected}, actual {before['revision']}")
            after = self._changed(before, event)
            for source in after["sources"]:
                self.read_source(source["source_id"])
            self._check_links(after, event["type"] == "accept")
            self._commit(before, after)
            return after

    def _changed(self, before, event):
        after, at = copy.deepcopy(before), now()
        change(after, event, at)
        after["revision"] += 1
        after["updated_at"] = at
        after["history"].append(history(event, at))
        validate_record(after)
        return after

    def attach(self, request_id, file, kind, event_id, expected):
        if kind not in {"assets", "evidence"}:
            fail("Attachment kind must be assets|evidence")
        nonempty(event_id, "event_id")
        file = safe(file)
        name = name_component(file.name)
        content = file.read_bytes()
        receipt = {"path": f"{kind}/{digest(event_id)[:24]}-{name}", "original_name": name, "size": len(content), "sha256": byte_digest(content)}
        event = {"event_id": event_id, "type": "attach", "file": receipt}
        with self.locked():
            self.ready()
            before = self._read(request_id)
            if retry(before, event):
                return before
            if type(expected) is not int or before["revision"] != expected:
                fail(f"Stale revision: expected {expected}, actual {before['revision']}")
            target = safe(self._locate(request_id) / receipt["path"])
            if target.exists():
                fail("Attachment collision: unrecorded existing file preserved")
            after = self._changed(before, event)
            self._commit(before, after, content)
            return after

    def _stage(self):
        # Incomplete staging is not committed; readers ignore it. No canonical data
        # changes before intent publication. Crash leftovers may be inspected/deleted.
        return Path(tempfile.mkdtemp(prefix=".request-stage-", dir=self.team))

    def _prepare(self, stage, intent):
        atomic_write(stage / "intent.json", intent)
        fsync_dir(stage)
        if self.transaction.exists():
            fail("Transaction collision; existing intent preserved")
        os.rename(stage, self.transaction)
        fsync_dir(self.team)
        self.fault("prepared")

    def _commit(self, before, after, content=None):
        validate_record(after)
        stage = self._stage()
        if before is None:
            (stage / "bundle").mkdir()
            atomic_bytes(stage / "bundle/request.md", markdown(after))
        if content is not None:
            atomic_bytes(stage / "file", content)
        self._prepare(stage, {"operation": "request", "before": before, "after": after})
        self._recover()

    def recover(self):
        with self.locked():
            self.ready()
        return {"recovered": True}

    def _recover(self):
        if not safe(self.transaction).exists():
            return
        self._check_tree(self.transaction)
        intent = json.loads(safe(self.transaction / "intent.json").read_bytes())
        if not isinstance(intent, dict):
            fail("Invalid recovery intent; preserved")
        if intent.get("operation") == "source":
            if set(intent) != {"operation", "source_id", "metadata"} or not SOURCE_ID.fullmatch(intent.get("source_id", "")):
                fail("Invalid source recovery intent")
            source_id = intent["source_id"]
            staged, target = self.transaction / "bundle", safe(self.sources / source_id)
            if staged.exists() and target.exists():
                fail("Source recovery collision; both copies preserved")
            location = staged if staged.exists() else target
            if self._read_source_at(location, source_id) != intent["metadata"]:
                fail("Source recovery payload mismatch")
            if staged.exists():
                self.sources.mkdir(exist_ok=True)
                os.rename(staged, target)
                fsync_dir(self.sources)
            self.fault("written")
        elif intent.get("operation") == "request":
            if set(intent) != {"operation", "before", "after"}:
                fail("Invalid request recovery intent")
            before, after = intent["before"], intent["after"]
            validate_record(after)
            if after["project_id"] != self.project_id:
                fail("Foreign recovery identity")
            if before is not None:
                validate_record(before)
                if before["id"] != after["id"] or before["project_id"] != after["project_id"] or after["revision"] != before["revision"] + 1 or after["history"][:-1] != before["history"]:
                    fail("Recovery intent is not one validated revision")
            elif after["revision"] != 1:
                fail("Invalid create recovery revision")
            target = safe(self.directory / CONTAINERS[after["state"]] / after["id"])
            found = self._locate(after["id"], required=False)
            if before is None:
                staged = safe(self.transaction / "bundle")
                if found is not None and staged.exists():
                    fail("Create recovery collision; both copies preserved")
                if found is None:
                    if parse_markdown(safe(staged / "request.md").read_bytes()) != after:
                        fail("Create recovery payload mismatch")
                    target.parent.mkdir(parents=True, exist_ok=True)
                    safe(target.parent)
                    os.rename(staged, target)
                    fsync_dir(target.parent)
                    found = target
                elif found != target or safe(found / "request.md").read_bytes() != markdown(after):
                    fail("Create recovery collision; existing content preserved")
            else:
                if found is None or found.parent.name not in {CONTAINERS[before["state"]], CONTAINERS[after["state"]]}:
                    fail("Recovery request location is uncertain; preserved")
                self._check_tree(found)
                current = safe(found / "request.md").read_bytes()
                if current not in {markdown(before), markdown(after)}:
                    fail("Recovery record collision; unexpected content preserved")
                additions = after["files"][len(before["files"]):]
                if after["files"][:len(before["files"])] != before["files"] or len(additions) > 1:
                    fail("Invalid recovery file delta")
                if additions:
                    receipt = additions[0]
                    staged_file = safe(self.transaction / "file")
                    content = staged_file.read_bytes()
                    if len(content) != receipt["size"] or byte_digest(content) != receipt["sha256"]:
                        fail("Recovery staged file integrity mismatch")
                    destination = safe(found / receipt["path"])
                    destination.parent.mkdir(exist_ok=True)
                    if destination.exists():
                        self._verify_file(found, receipt)
                    else:
                        # Hard-link publication cannot overwrite an arbitrary file.
                        os.link(staged_file, destination)
                        fsync_dir(destination.parent)
                self.fault("files")
                if found != target:
                    if found.parent.name != CONTAINERS[before["state"]] or target.exists():
                        fail("Move recovery collision; existing content preserved")
                    target.parent.mkdir(parents=True, exist_ok=True)
                    safe(target.parent)
                    old_parent = found.parent
                    os.rename(found, target)
                    fsync_dir(old_parent)
                    fsync_dir(target.parent)
                    found = target
                self.fault("moved")
                if current != markdown(after):
                    atomic_bytes(found / "request.md", markdown(after))
            self.fault("written")
        else:
            fail("Unknown recovery operation; preserved")
        # Rename completion out of the active-intent name first: interrupted
        # cleanup never leaves a partial intent that could be replayed incorrectly.
        retired = self.team / (".request-complete-" + uuid.uuid4().hex)
        os.rename(self.transaction, retired)
        fsync_dir(self.team)
        shutil.rmtree(retired)

    def validate(self):
        self.ready()
        records = self._records()
        for r in records:
            self._check_links(r)
        if self.sources.exists():
            for path in self.sources.iterdir():
                safe(path)
                self.read_source(path.name)
        return {"valid": len(records)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--team", type=Path, default=Path(__file__).resolve().parents[1], help="installed .director directory")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init").add_argument("--project-id")
    capture = sub.add_parser("capture")
    capture.add_argument("--raw-file", required=True)
    capture.add_argument("--event-id", required=True)
    capture.add_argument("--attachment", action="append", default=[])
    sub.add_parser("source").add_argument("id")
    create = sub.add_parser("create")
    origin = create.add_mutually_exclusive_group(required=True)
    origin.add_argument("--raw-file")
    origin.add_argument("--source-id")
    create.add_argument("--title", required=True)
    create.add_argument("--event-id", required=True)
    apply = sub.add_parser("apply")
    apply.add_argument("id")
    apply.add_argument("--event-file", required=True)
    apply.add_argument("--expect-revision", required=True, type=int)
    attach = sub.add_parser("attach")
    attach.add_argument("id")
    attach.add_argument("--file", required=True)
    attach.add_argument("--kind", required=True, choices=["assets", "evidence"])
    attach.add_argument("--event-id", required=True)
    attach.add_argument("--expect-revision", required=True, type=int)
    sub.add_parser("show").add_argument("id")
    sub.add_parser("list").add_argument("--open", action="store_true")
    sub.add_parser("validate")
    sub.add_parser("recover")
    args = parser.parse_args()
    try:
        if args.command == "init":
            result = Store.init(args.team, args.project_id)
        else:
            store = Store(args.team)
            if args.command == "capture":
                result = store.capture(safe(args.raw_file).read_bytes().decode("utf-8"), args.event_id, args.attachment)
            elif args.command == "source":
                result = store.read_source(args.id)
            elif args.command == "create":
                raw = safe(args.raw_file).read_bytes().decode("utf-8") if args.raw_file else None
                result = store.create(raw, args.title, args.event_id, args.source_id)
            elif args.command == "apply":
                result = store.apply(args.id, json.loads(safe(args.event_file).read_bytes()), args.expect_revision)
            elif args.command == "attach":
                result = store.attach(args.id, args.file, args.kind, args.event_id, args.expect_revision)
            elif args.command == "show":
                result = store.read(args.id)
            elif args.command == "recover":
                result = store.recover()
            elif args.command == "validate":
                result = store.validate()
            else:
                result = [{**{k: r[k] for k in ("id", "title", "state", "revision", "owner")}, "condition": "waiting" if r["state"] not in TERMINAL and any(h["status"] == "acknowledged" and h["required"] for h in r["handoffs"]) else r["state"], "current_liveness": "unknown"} for r in store.records() if not args.open or r["state"] not in TERMINAL]
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, OSError, KeyError, TypeError, AttributeError, UnicodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
