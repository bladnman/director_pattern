#!/usr/bin/env python3
"""Starter 2 local records. Trusted callers supply authority; this is not a sandbox."""
import argparse
import copy
try:
    import fcntl
except ImportError:  # Instructions remain host-neutral; this local helper is POSIX.
    fcntl = None
import hashlib
import json
import os
from pathlib import Path
import tempfile
import time

FORMAT = "director-flat-starter"
VERSION = 2
READS = {"status", "select", "selectors", "pending", "review-batch", "request", "proposals", "reviews", "deferrals", "incidents"}
WRITES = {"capture", "update", "observe", "evaluate", "incident", "review-save", "decide", "accept-rule", "review-defer", "retire-knowledge"}


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(value).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value, label, maximum=2000):
    require(isinstance(value, str) and bool(value) and len(value.encode()) <= maximum,
            f"{label} must be nonempty text within {maximum} bytes")
    return value


def only(data, allowed):
    require(isinstance(data, dict), "expected a JSON object")
    require(not set(data) - set(allowed), "unknown fields: " + ", ".join(sorted(set(data) - set(allowed))))


def scope(value):
    only(value, {"tasks", "paths", "audiences"})
    require(set(value) == {"tasks", "paths", "audiences"}, "scope needs tasks, paths and audiences")
    for field, values in value.items():
        require(isinstance(values, list) and 0 < len(values) <= 20, "scope lists need 1..20 explicit values")
        for item in values:
            text(item, "scope " + field, 240)
            if field == "paths":
                require(not item.startswith("/") and ".." not in Path(item).parts, "scope path must be project-relative")
    return copy.deepcopy(value)


def initial_state(root, initiator="owner", opportunity="closure", min_incidents=3):
    require(initiator in {"owner", "user"}, "unknown review initiator")
    require(opportunity in {"closure", "explicit"}, "unknown review opportunity")
    require(isinstance(min_incidents, int) and 1 <= min_incidents <= 100, "review min_incidents must be 1..100")
    return {"format": FORMAT, "starter_version": VERSION, "schema_version": 1,
            "project_id": "P-" + digest(str(Path(root).resolve()).encode())[:24], "revision": 0,
            "requests": {}, "sources": {}, "incidents": [], "review_cursor": 0,
            "reviews": {}, "proposals": {}, "knowledge": {}, "operations": {},
            "review_policy": {"initiator": initiator, "opportunity": opportunity,
                              "min_incidents": min_incidents, "max_batch": 5, "max_bytes": 12000, "background": False},
            "review_deferrals": []}


def review_signal(state, explicit=False):
    pending = len(state["incidents"]) - state["review_cursor"]
    policy = state["review_policy"]
    return {"review_pending": pending > 0, "pending_incidents": pending,
            "review_due": pending > 0 and (explicit or (policy["initiator"] == "owner" and
                policy["opportunity"] == "closure" and pending >= policy["min_incidents"])),
            "review_policy": policy}


def atomic(path, data):
    """One durable replacement; readers see the old or complete new state."""
    fd, temporary = tempfile.mkstemp(prefix=".write-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fchmod(stream.fileno(), 0o600)
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def immutable(path, data):
    if path.exists():
        require(path.is_file() and not path.is_symlink() and path.read_bytes() == data,
                "immutable source conflict: " + str(path))
        return
    atomic(path, data)


def source_check(state, root, source_id):
    require(source_id in state["sources"], "unknown source")
    record = state["sources"][source_id]
    for item in [record, *record["attachments"]]:
        path = root / item["path"]
        require(path.is_file() and not path.is_symlink() and digest(path.read_bytes()) == item["sha256"],
                "source hash mismatch")
    return record


def request_check(state, data):
    request_id = data.get("request_id")
    require(request_id in state["requests"], "unknown request")
    request = state["requests"][request_id]
    require(type(data.get("expected_request_revision")) is int and data["expected_request_revision"] == request["revision"], "stale request revision")
    return request


def capture_material(data):
    """Pin supplied bytes once, for both semantic retry identity and persistence."""
    require(("text" in data) != ("source_file" in data), "supply exactly text or source_file")
    require("text" not in data or isinstance(data["text"], str), "text must be a UTF-8 string")
    require(isinstance(data.get("attachments", []), list), "attachments must be a list")
    raw = data["text"].encode("utf-8") if "text" in data else Path(data["source_file"]).read_bytes()
    raw.decode("utf-8")
    require(bool(raw), "source must not be empty")
    attachments = []
    for item in data.get("attachments", []):
        only(item, {"path", "name"})
        payload = Path(item["path"]).read_bytes()
        name = text(item.get("name", Path(item["path"]).name), "attachment name", 240)
        attachments.append((name, payload))
    return raw, attachments


def incident_add(state, root, item, request=None):
    only(item, {"source_id", "request_id", "request_revision", "scope", "evidence", "correction", "hypothesis"})
    source_check(state, root, item.get("source_id"))
    request_id = item.get("request_id") or (request or {}).get("id")
    require(request_id in state["requests"], "incident needs an existing request")
    req = state["requests"][request_id]
    revision = item.get("request_revision", req["revision"])
    require(type(revision) is int and 1 <= revision <= req["revision"], "invalid incident request revision")
    require(item["source_id"] in req["sources"], "incident source is outside request")
    source_revision = next(x["request_revision"] for x in req["history"] if
                           x.get("kind") == "source" and x.get("source_id") == item["source_id"])
    require(source_revision <= revision, "incident source did not exist at that request revision")
    require(isinstance(item.get("hypothesis", False), bool), "hypothesis must be boolean")
    value = {"seq": len(state["incidents"]) + 1, "source_id": item["source_id"],
             "request_id": request_id, "request_revision": revision, "scope": scope(item.get("scope")),
             "evidence": text(item.get("evidence"), "incident evidence"),
             "correction": text(item.get("correction"), "incident correction"),
             "hypothesis": item.get("hypothesis", False)}
    require(len(encoded(value)) <= 6000, "incident exceeds bounded 6000-byte record; link larger evidence")
    state["incidents"].append(value)
    return value["seq"]


def batch_token(state, values):
    return {"cursor": state["review_cursor"], "ids": [x["seq"] for x in values],
            "digest": digest(encoded(values))}


def limits(data):
    count, budget, offset = data.get("limit", 5), data.get("max_bytes", 12000), data.get("offset", 0)
    require(type(count) is int and 1 <= count <= 100, "limit must be 1..100")
    require(type(budget) is int and 512 <= budget <= 100000, "max_bytes must be 512..100000")
    require(type(offset) is int and offset >= 0, "offset must be nonnegative")
    return count, budget, offset


def page(state, data, items, extra=None, review=False):
    count, budget, offset = limits(data)
    require(not review or offset == 0, "review batches cannot skip pending evidence")
    require(type(data.get("at_revision", state["revision"])) is int and data.get("at_revision", state["revision"]) == state["revision"], "stale query revision")
    require(offset <= len(items), "offset outside result")
    result = {"revision": state["revision"], "items": [], "total": len(items),
              "next_offset": None, **(extra or {})}
    for item in items[offset:offset + count]:
        candidate = copy.deepcopy(result)
        candidate["items"].append(item)
        consumed = offset + len(candidate["items"])
        candidate["next_offset"] = consumed if consumed < len(items) else None
        if review:
            candidate["batch"] = batch_token(state, candidate["items"])
        if len(encoded(candidate)) + 1 > budget:
            require(bool(result["items"]), "first result exceeds byte budget; increase max_bytes")
            break
        result = candidate
    if review and "batch" not in result:
        result["batch"] = batch_token(state, [])
    require(len(encoded(result)) + 1 <= budget, "result metadata exceeds byte budget")
    result["omitted"] = len(items) - offset - len(result["items"])
    require(len(encoded(result)) + 1 <= budget, "result framing exceeds byte budget; increase max_bytes")
    return result


def read_action(state, action, data):
    common = {"limit", "max_bytes", "offset", "at_revision", "explicit_review"}
    if action == "selectors":
        only(data, common | {"path"})
        path = data.get("path")
        require(path is None or (isinstance(path, str) and not path.startswith("/") and ".." not in Path(path).parts), "invalid selector path")
        def overlaps(prefix):
            if path is None or prefix == "*":
                return True
            left, right = path.rstrip("/") or ".", prefix.rstrip("/") or "."
            return (left == "." or right == "." or left == right or
                    left.startswith(right + "/") or right.startswith(left + "/"))
        values = [{"id": entry["id"], "scope": copy.deepcopy(entry["scope"])}
                  for entry in state["knowledge"].values() if entry["current"] and
                  any(overlaps(p) for p in entry["scope"]["paths"])]
        return page(state, data, values)
    if action in {"proposals", "reviews", "deferrals", "incidents"}:
        only(data, common | {"proposal_id", "review_id", "include_decided"})
        if action == "proposals":
            values = [x for x in state["proposals"].values() if
                (x["decision"] is None or data.get("include_decided") is True or data.get("proposal_id") == x["id"]) and
                (not data.get("proposal_id") or data["proposal_id"] == x["id"])]
        elif action == "reviews":
            values = [{"id": key, "batch": item["batch"], "summary": item["output"]["summary"],
                       "reviewer": item["output"]["reviewer"], "spend": item["output"]["spend"],
                       "proposal_ids": item["proposal_ids"]} for key, item in state["reviews"].items()
                      if not data.get("review_id") or key == data["review_id"]]
        elif action == "incidents":
            ids = None
            if data.get("review_id"):
                require(data["review_id"] in state["reviews"], "unknown review")
                ids = state["reviews"][data["review_id"]]["batch"]["ids"]
            values = [x for x in state["incidents"] if ids is None or x["seq"] in ids]
        else:
            values = state["review_deferrals"]
        return page(state, data, values)
    if action == "request":
        only(data, common | {"request_id"})
        require(data.get("request_id") in state["requests"], "unknown request")
        req = state["requests"][data["request_id"]]
        # Explicit history paging is task/recovery work, never user startup.
        return page(state, data, req["history"], {"request": {k: v for k, v in req.items() if k not in {"history", "observations"}}})
    if action == "select":
        only(data, common | {"task", "path", "audience"})
        task, path, audience = text(data.get("task"), "task", 240), data.get("path", "."), text(data.get("audience"), "audience", 240)
        require(isinstance(path, str) and not path.startswith("/") and ".." not in Path(path).parts, "invalid query path")
        def matches(entry):
            s = entry["scope"]
            return ((task in s["tasks"] or "*" in s["tasks"]) and
                    (audience in s["audiences"] or "*" in s["audiences"]) and
                    any(p in {"*", "."} or path == p or path.startswith(p.rstrip("/") + "/") for p in s["paths"]))
        values = [x for x in state["knowledge"].values() if x["current"] and matches(x)]
        return page(state, data, values, {"query_scope": {"task": task, "path": path, "audience": audience}})
    only(data, common)
    if action == "review-batch":
        return page(state, data, state["incidents"][state["review_cursor"]:], review=True)
    extra = {**review_signal(state, data.get("explicit_review") is True),
             "pending_proposals": sum(p["decision"] is None for p in state["proposals"].values()),
             "review_policy": state["review_policy"], "knowledge_count": sum(k["current"] for k in state["knowledge"].values())}
    if action == "pending":
        values = [{"seq": x["seq"], "request_id": x["request_id"], "request_revision": x["request_revision"],
                   "scope": x["scope"]} for x in state["incidents"][state["review_cursor"]:]]
    else:
        values = [{k: v for k, v in r.items() if k in {"id", "revision", "summary", "owner", "status", "next_action", "handles", "pending_approvals"}}
                  for r in state["requests"].values() if r["status"] not in {"accepted", "canceled"}]
    return page(state, data, values, extra)


def mutate(state, root, action, data, pinned=None):
    common = {"op_id", "expected_revision"}
    result = {}
    if action == "capture":
        only(data, common | {"text", "source_file", "attachments", "request", "request_id", "expected_request_revision"})
        raw, supplied_attachments = pinned if pinned is not None else capture_material(data)
        source_id = "S-" + digest(data["op_id"].encode())[:24]
        attachments = []
        attachment_payloads = []
        for index, (name, payload) in enumerate(supplied_attachments):
            rel = f"sources/{source_id}/attachment-{index}"
            attachments.append({"name": name, "path": rel, "sha256": digest(payload), "bytes": len(payload)})
            attachment_payloads.append((rel, payload))
        if "request" in data:
            req = data["request"]
            only(req, {"id", "summary", "scope", "acceptance", "owner", "next_action"})
            request_id = text(req.get("id"), "request id", 120)
            require(request_id not in state["requests"], "request already exists")
            request = {"id": request_id, "revision": 1, "summary": text(req.get("summary"), "summary", 400),
                       "scope": scope(req.get("scope")), "acceptance": text(req.get("acceptance"), "acceptance"),
                       "owner": text(req.get("owner"), "owner", 240), "status": "active", "sources": [source_id],
                       "next_action": req.get("next_action", "evaluate requested outcome"), "handles": [],
                       "observations": [], "pending_approvals": [], "history": []}
        else:
            request = request_check(state, data)
        # Validate every supplied field/revision before creating any source files.
        text(request["next_action"], "next_action")
        directory = root / "sources" / source_id
        require(not (root / "sources").is_symlink() and not directory.is_symlink(), "unsafe source directory")
        directory.mkdir(parents=True, exist_ok=True)
        immutable(directory / "input.txt", raw)
        for rel, payload in attachment_payloads:
            immutable(root / rel, payload)
        state["sources"][source_id] = {"id": source_id, "path": f"sources/{source_id}/input.txt",
                                       "sha256": digest(raw), "bytes": len(raw), "attachments": attachments}
        if "request" in data:
            state["requests"][request_id] = request
        else:
            request["revision"] += 1
            request["sources"].append(source_id)
        request["history"].append({"kind": "source", "source_id": source_id, "request_revision": request["revision"]})
        result = {"source_id": source_id, "request_id": request["id"], "request_revision": request["revision"]}
    elif action in {"update", "observe", "evaluate"}:
        only(data, common | {"request_id", "expected_request_revision", "source_id", "changes", "observation", "evaluation", "incident"})
        request = request_check(state, data)
        source_check(state, root, data.get("source_id"))
        require(data["source_id"] in request["sources"], "source is outside request")
        changes = data.get("changes", {})
        only(changes, {"scope", "acceptance", "owner", "status", "next_action", "handles", "pending_approvals"})
        if "scope" in changes:
            changes["scope"] = scope(changes["scope"])
        if "status" in changes:
            require(changes["status"] in {"active", "review", "blocked", "accepted", "canceled"}, "invalid status")
            if changes["status"] == "accepted":
                require(action == "evaluate" and bool(data.get("evaluation")), "acceptance requires evaluate with an explicit judgment")
                require(changes.get("pending_approvals", request["pending_approvals"]) == [], "acceptance has unresolved approvals")
        for field in {"handles", "pending_approvals"} & changes.keys():
            require(isinstance(changes[field], list) and len(changes[field]) <= 50, "invalid " + field)
            for value in changes[field]:
                text(value, field, 500)
        for field in {"owner", "acceptance", "next_action"} & changes.keys():
            text(changes[field], field)
        event = {"kind": action, "source_id": data["source_id"], "changes": copy.deepcopy(changes)}
        if "observation" in data:
            only(data["observation"], {"handle", "status", "observed_at", "evidence"})
            observation = {k: text(data["observation"].get(k), k, 1000) for k in ["handle", "status", "observed_at", "evidence"]}
            request["observations"].append(observation)
            event["observation"] = observation
        if "evaluation" in data:
            event["evaluation"] = text(data["evaluation"], "evaluation")
        request.update(changes)
        request["revision"] += 1
        event["request_revision"] = request["revision"]
        request["history"].append(event)
        if data.get("incident") is not None:
            result["incident_seq"] = incident_add(state, root, data["incident"], request)
        result.update(request_id=request["id"], request_revision=request["revision"])
    elif action == "incident":
        only(data, common | {"incident"})
        result["incident_seq"] = incident_add(state, root, data.get("incident"))
    elif action == "review-save":
        only(data, common | {"batch", "review"})
        batch = data.get("batch")
        only(batch, {"cursor", "ids", "digest"})
        require(type(batch.get("cursor")) is int and batch["cursor"] == state["review_cursor"], "stale review cursor")
        ids = batch.get("ids")
        require(isinstance(ids, list) and 0 < len(ids) <= 100 and all(type(x) is int for x in ids), "review needs 1..100 contiguous incidents")
        values = state["incidents"][state["review_cursor"]:state["review_cursor"] + len(ids)]
        require(batch == batch_token(state, values), "review batch conflict or skipped evidence")
        review = data.get("review")
        only(review, {"summary", "reviewer", "spend", "proposals"})
        text(review.get("summary"), "review summary", 4000)
        text(review.get("reviewer"), "actual reviewer handle or explicit unknown", 500)
        require(isinstance(review.get("spend"), dict), "record review spend/overhead or explicit unknown")
        require(len(encoded(review)) <= 32000, "review output exceeds bounded 32000 bytes")
        proposals = review.get("proposals", [])
        require(isinstance(proposals, list) and len(proposals) <= 20, "too many proposals")
        review_id = "V-" + digest(data["op_id"].encode())[:24]
        proposal_ids = []
        for index, proposal in enumerate(proposals):
            only(proposal, {"kind", "claim", "scope", "basis", "hypothesis"})
            require(proposal.get("kind") in {"knowledge", "routing", "structure"}, "invalid proposal kind")
            require(isinstance(proposal.get("basis"), list) and proposal["basis"] and set(proposal["basis"]) <= set(ids), "proposal basis outside batch")
            require(isinstance(proposal.get("hypothesis", False), bool), "hypothesis must be boolean")
            entry = {"id": review_id + "-" + str(index + 1), "review_id": review_id,
                     "kind": proposal["kind"], "claim": text(proposal.get("claim"), "proposal claim", 2000),
                     "scope": scope(proposal.get("scope")), "basis": proposal["basis"],
                     "hypothesis": proposal.get("hypothesis", False), "decision": None}
            state["proposals"][entry["id"]] = entry
            proposal_ids.append(entry["id"])
        state["reviews"][review_id] = {"batch": batch, "output": review, "proposal_ids": proposal_ids}
        state["review_cursor"] += len(values)
        result.update(review_id=review_id, proposal_ids=proposal_ids, review_cursor=state["review_cursor"])
    elif action == "decide":
        only(data, common | {"proposal_id", "decision", "owner", "reason"})
        require(data.get("proposal_id") in state["proposals"], "unknown proposal")
        proposal = state["proposals"][data["proposal_id"]]
        decision = data.get("decision")
        require(decision in {"accept", "reject", "retire"}, "invalid decision")
        require((proposal["decision"] is None and decision != "retire") or
                (decision == "retire" and proposal["id"] in state["knowledge"] and state["knowledge"][proposal["id"]]["current"]), "proposal already decided or not current")
        require(not (decision == "accept" and proposal["hypothesis"]), "hypotheses are not accepted rules")
        owner, reason = text(data.get("owner"), "deciding owner", 240), text(data.get("reason"), "decision reason")
        proposal["decision"] = {"decision": decision, "owner": owner, "reason": reason, "revision": state["revision"] + 1}
        if decision == "accept" and proposal["kind"] == "knowledge":
            basis = [state["incidents"][seq - 1] for seq in proposal["basis"]]
            state["knowledge"][proposal["id"]] = {"id": proposal["id"], "claim": proposal["claim"],
                "scope": copy.deepcopy(proposal["scope"]), "current": True, "accepted_by": owner,
                "accepted_revision": state["revision"] + 1,
                "provenance": {"review_id": proposal["review_id"], "incidents": [
                    {**{k: item[k] for k in ("seq", "source_id", "request_id", "request_revision")},
                     "sha256": digest(encoded(item))} for item in basis]}}
        elif decision == "retire":
            state["knowledge"][proposal["id"]]["current"] = False
        result.update(proposal_id=proposal["id"], decision=decision,
                      implementation_required=decision == "accept" and proposal["kind"] != "knowledge")
        proposal.setdefault("decisions", []).append(copy.deepcopy(proposal["decision"]))
    elif action == "accept-rule":
        only(data, common | {"source_id", "request_id", "expected_request_revision", "claim", "scope", "owner", "reason"})
        req = request_check(state, data)
        source_check(state, root, data.get("source_id"))
        require(data["source_id"] in req["sources"], "rule source outside request")
        entry_id = "K-" + digest(data["op_id"].encode())[:24]
        state["knowledge"][entry_id] = {"id": entry_id, "claim": text(data.get("claim"), "explicit scoped rule", 2000),
            "scope": scope(data.get("scope")), "current": True, "accepted_by": text(data.get("owner"), "owner", 240),
            "reason": text(data.get("reason"), "explicit source decision reason"), "accepted_revision": state["revision"] + 1,
            "provenance": {"kind": "explicit-owner-supplied-rule", "source_id": data["source_id"],
                           "request_id": req["id"], "request_revision": req["revision"]}}
        result["knowledge_id"] = entry_id
    elif action == "review-defer":
        only(data, common | {"reason", "owner"})
        state["review_deferrals"].append({"reason": text(data.get("reason"), "real review deferral"),
            "owner": text(data.get("owner"), "owner", 240), "cursor": state["review_cursor"],
            "revision": state["revision"] + 1})
        result["review_ran"] = False
    elif action == "retire-knowledge":
        only(data, common | {"knowledge_id", "source_id", "request_id", "expected_request_revision", "owner", "reason"})
        req = request_check(state, data)
        source_check(state, root, data.get("source_id"))
        require(data["source_id"] in req["sources"], "retirement source outside request")
        require(data.get("knowledge_id") in state["knowledge"], "unknown knowledge")
        entry = state["knowledge"][data["knowledge_id"]]
        require(entry["current"], "knowledge already retired")
        decision = {"decision": "retire", "owner": text(data.get("owner"), "owner", 240),
            "reason": text(data.get("reason"), "retirement reason"), "source_id": data["source_id"],
            "request_id": req["id"], "request_revision": req["revision"], "revision": state["revision"] + 1}
        entry.setdefault("decisions", []).append(decision)
        entry["current"] = False
        result["knowledge_id"] = entry["id"]
    return result


def execute(root, action, data):
    start = time.monotonic()
    require(fcntl is not None, "This helper requires POSIX fcntl (macOS/Linux); no supported Windows writer is installed")
    root = Path(root)
    require(not root.is_symlink(), "unsafe starter root")
    root = root.resolve()
    require(root.is_dir() and (root / "state.json").is_file() and not (root / "state.json").is_symlink()
            and not (root / ".lock").is_symlink(), "missing or unsafe starter store")
    preliminary = json.loads((root / "state.json").read_bytes())
    require(preliminary.get("format") == FORMAT and preliminary.get("starter_version") == VERSION,
            "incompatible store; no automatic migration")
    with (root / ".lock").open("a+b") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("store busy; retry the same operation") from None
        require(os.fstat(lock.fileno()).st_ino == (root / ".lock").stat().st_ino,
                "retired lock/store; retry against the current installation")
        state_path = root / "state.json"
        state = json.loads(state_path.read_bytes())
        require(state.get("format") == FORMAT and state.get("starter_version") == VERSION and state.get("schema_version") == 1,
                "incompatible store; no automatic migration")
        if action in READS:
            return read_action(state, action, data)
        require(action in WRITES, "unknown action")
        op_id = text(data.get("op_id"), "op_id", 160)
        pinned = capture_material(data) if action == "capture" else None
        identity = {"action": action, "data": data}
        if pinned is not None:
            identity["capture_bytes"] = {"source": digest(pinned[0]),
                "attachments": [{"name": name, "sha256": digest(payload)} for name, payload in pinned[1]]}
        fingerprint = digest(encoded(identity))
        if op_id in state["operations"]:
            operation = state["operations"][op_id]
            require(operation["digest"] == fingerprint, "op_id conflict")
            return {**operation["receipt"], "replayed": True}
        require(type(data.get("expected_revision")) is int and data["expected_revision"] == state["revision"], "stale state revision")
        result = mutate(state, root, action, data, pinned)
        state["revision"] += 1
        receipt = {"revision": state["revision"], "op_id": op_id, "action": action,
                   **review_signal(state),
                   "prepare_seconds": round(time.monotonic() - start, 6), **result}
        state["operations"][op_id] = {"digest": fingerprint, "receipt": receipt}
        # Output and cursor live in this same replacement: no separate ack can lose evidence.
        payload = encoded(state) + b"\n"
        atomic(state_path, payload)
        return {**receipt, "state_bytes": len(payload)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=sorted(READS | WRITES | {"help"}), help="help prints the installed exact JSON API")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--data-file", default="-", help="JSON file, or - for stdin (empty means {})")
    args = parser.parse_args()
    import sys
    try:
        if args.action == "help":
            print((Path(__file__).resolve().parent / "API.md").read_text())
            return 0
        raw = sys.stdin.buffer.read() if args.data_file == "-" else Path(args.data_file).read_bytes()
        data = json.loads(raw) if raw.strip() else {}
        require(isinstance(data, dict), "input must be a JSON object")
        print(encoded(execute(args.root, args.action, data)).decode())
        return 0
    except (ValueError, TypeError, KeyError, OSError, UnicodeError) as error:
        print(json.dumps({"error": str(error)[:1000]}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
