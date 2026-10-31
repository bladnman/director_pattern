#!/usr/bin/env python3
"""Bounded learning views over canonical request-bundle note events. No sidecar store.

Reads scan/validate canonical request histories and sources internally. Compact output
does not make that disk work constant. Caller authority and evidence remain supplied.
"""
import argparse
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True

PREFIX = "DIRECTOR_LEARNING_V1 "
ROOT = Path(__file__).resolve().parent.parent


def need(ok, message):
    if not ok:
        raise ValueError(message)


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def digest(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def text(value, label):
    need(isinstance(value, str) and 0 < len(value) <= 4000, label + " must be bounded nonempty text")
    return value


def validate(item, allow_legacy=False):
    need(isinstance(item, dict), "learning entry must be an object")
    common = {"schema", "id", "kind", "source_id", "source_sha256", "request_revision", "scope", "owner", "text"}
    extras = {"incident": {"hypothesis"}, "review": {"incidents", "proposals", "spend"},
              "rule": set(), "retire": {"knowledge_id"}, "decision": {"proposal_id", "decision"}}
    kind = item.get("kind")
    need(kind in extras and common <= item.keys() and not item.keys() - common - extras[kind], "unknown/missing learning fields")
    need(item["schema"] == 1, "unsupported learning schema")
    need(re.fullmatch(r"[a-z][a-z0-9-]{0,47}-[0-9a-f]{32}", item["id"]) is not None, "use a fresh UUID event ID")
    for key in ("source_id", "owner", "text"):
        text(item[key], key)
    need(isinstance(item["source_sha256"], str) and re.fullmatch(r"[0-9a-f]{64}", item["source_sha256"]), "source_sha256 is required")
    need(type(item["request_revision"]) is int and item["request_revision"] > 0, "invalid request revision")
    scope = item["scope"]
    need(isinstance(scope, dict) and set(scope) == {"tasks", "paths", "audiences"}, "scope requires tasks/paths/audiences")
    for name, values in scope.items():
        need(isinstance(values, list) and 0 < len(values) <= 20 and len(values) == len(set(values)), "invalid scope list")
        for value in values:
            text(value, "scope value")
            if name == "paths":
                need(value == "*" or (not value.startswith("/") and ".." not in Path(value).parts and "\\" not in value), "scope paths must be project relative")
    if kind == "incident":
        need(type(item.get("hypothesis")) is bool, "incident/proposal needs hypothesis boolean")
    if kind == "review":
        refs = item.get("incidents")
        need(isinstance(refs, list) and 0 < len(refs) <= 20 and all(isinstance(ref, dict) and set(ref) == {"id", "digest"} for ref in refs), "review needs explicit incident IDs/digests")
        need(len({ref["id"] for ref in refs}) == len(refs), "duplicate incident references")
        need(isinstance(item.get("spend"), dict), "review needs actual spend/settings or unknown values")
        proposals = item.get("proposals")
        need(isinstance(proposals, list) and len(proposals) <= 10, "review needs all proposals together (or empty list with reason)")
        for proposal in proposals:
            fields = {"id", "text", "scope", "hypothesis"}
            need(isinstance(proposal, dict) and (set(proposal) == fields | {"kind"} or allow_legacy and set(proposal) == fields), "proposal requires explicit kind: knowledge, routing or structure")
            need(proposal.get("kind") in {"knowledge", "routing", "structure"} or allow_legacy and "kind" not in proposal, "invalid proposal kind")
            text(proposal["id"], "proposal id")
            need(proposal["id"].startswith(item["id"] + "/"), "proposal IDs must use review-id/suffix")
            # Reuse full scope/text validation without creating another canonical event.
            validate({**{key: item[key] for key in common}, "kind": "incident", "scope": proposal["scope"], "text": proposal["text"], "hypothesis": proposal["hypothesis"]})
    if kind == "decision":
        text(item.get("proposal_id"), "proposal_id")
        need(item.get("decision") in {"accept", "reject", "retire"}, "decision must accept/reject/retire")
    if kind == "retire":
        text(item.get("knowledge_id"), "knowledge_id")
    need(len(encoded(item)) <= 8000, "learning entry exceeds 8000 bytes")
    return item


def collect(records, store):
    entries = []
    for record in records:
        sources = {source["source_id"] for source in record["sources"]}
        for index, event in enumerate(record["history"]):
            data = event["data"]
            if data.get("type") != "note" or not data.get("text", "").startswith(PREFIX):
                continue
            item = validate(json.loads(data["text"][len(PREFIX):]), allow_legacy=True)
            need(item["id"] == data["event_id"], "learning/event ID mismatch")
            need(item["source_id"] in sources and item["request_revision"] <= index, "learning source/revision is not prior canonical request evidence")
            source_event = next(source["event_id"] for source in record["sources"] if source["source_id"] == item["source_id"])
            need(any(h["event_id"] == source_event for h in record["history"][:item["request_revision"]]), "source was not attached at claimed request revision")
            need(store.read_source(item["source_id"])["input"]["sha256"] == item["source_sha256"], "canonical source hash mismatch")
            result = {**item, "digest": digest(item), "request_id": record["id"], "recorded_at": event["at"], "canonical_revision": index + 1}
            entries.append(result)
            if item["kind"] == "review":
                for proposal in item["proposals"]:
                    entries.append({**result, **proposal, "kind": "proposal", "proposal_kind": proposal.get("kind", "unclassified"), "review_id": item["id"], "digest": digest(proposal)})
    entries.sort(key=lambda item: (item["recorded_at"], item["request_id"], item["canonical_revision"]))
    ids = [item["id"] for item in entries]
    need(len(ids) == len(set(ids)), "duplicate learning IDs across requests")
    by_id = {item["id"]: item for item in entries}
    reviewed, decisions, retired = set(), {}, set()
    for item in entries:
        refs = [ref["id"] for ref in item["incidents"]] if item["kind"] == "review" else [item["review_id"]] if item["kind"] == "proposal" else [item["proposal_id"]] if item["kind"] == "decision" else [item["knowledge_id"]] if item["kind"] == "retire" else []
        expected = {"review": "incident", "proposal": "review", "decision": "proposal"}.get(item["kind"])
        for ref in refs:
            target = by_id.get(ref)
            need(target and (target["kind"] == expected or item["kind"] == "retire" and target["kind"] in {"proposal", "rule"}), "invalid learning reference kind")
            need(item["kind"] == "review" or (target["request_id"] == item["request_id"] and (target["canonical_revision"] < item["canonical_revision"] or item["kind"] == "proposal" and target["canonical_revision"] == item["canonical_revision"])), "invalid or future learning reference")
        if item["kind"] == "review":
            need(all(by_id[ref["id"]]["digest"] == ref["digest"] for ref in item["incidents"]), "review batch digest mismatch")
            ids = {ref["id"] for ref in item["incidents"]}
            need(not ids & reviewed, "incident batch was already reviewed")
            reviewed.update(ids)
        if item["kind"] == "decision":
            target = by_id[item["proposal_id"]]
            need(item["scope"] == target["scope"], "decision cannot broaden proposal scope")
            need(item["decision"] != "accept" or not target["hypothesis"], "hypotheses cannot be accepted as rules")
            prior = decisions.get(item["proposal_id"])
            need((prior is None and item["decision"] in {"accept", "reject"}) or (prior == "accept" and item["decision"] == "retire"), "competing decision; accepted rules require explicit retirement, terminal decisions remain history")
            need(item["proposal_id"] not in retired, "retired knowledge cannot be reaccepted")
            decisions[item["proposal_id"]] = item["decision"]
        if item["kind"] == "retire":
            target = by_id[item["knowledge_id"]]
            need(item["scope"] == target["scope"] and item["knowledge_id"] not in retired, "retirement must retain exact scope and occur once")
            need(target["kind"] == "rule" or decisions.get(target["id"]) == "accept", "only current accepted knowledge can retire")
            retired.add(item["knowledge_id"])
    for item in entries:
        if item["kind"] in {"proposal", "decision"}:
            target = item if item["kind"] == "proposal" else by_id[item["proposal_id"]]
            item["proposal_kind"] = target["proposal_kind"]
            item["classification_required"] = target["proposal_kind"] == "unclassified"
            accepted = decisions.get(item["id"]) == "accept" and item["id"] not in retired if item["kind"] == "proposal" else item["decision"] == "accept"
            item["implementation_required"] = accepted and target["proposal_kind"] != "knowledge"
    return entries


def matches(item, query, discovery=False):
    scope = item["scope"]
    for key, dimension in (("task", "tasks"), ("audience", "audiences")):
        if key in query and "*" not in scope[dimension] and query[key] not in scope[dimension]:
            return False
    path = query.get("path")
    if path is not None:
        need(isinstance(path, str) and not path.startswith("/") and ".." not in Path(path).parts, "query path must be project relative")
        def overlap(base):
            base, actual = base.rstrip("/"), path.rstrip("/")
            return base in {"*", "."} or base == actual or actual.startswith(base + "/") or (discovery and (actual == "." or base.startswith(actual + "/")))
        if not any(overlap(base) for base in scope["paths"]):
            return False
    return True


def page(items, query, snapshot, metrics):
    need(not query.get("at_snapshot") or query["at_snapshot"] == snapshot, "canonical snapshot changed; restart paging")
    limit, budget, offset = query.get("limit", 5), query.get("max_bytes", 12000), query.get("offset", 0)
    need(all(type(value) is int for value in (limit, budget, offset)) and 1 <= limit <= 20 and 512 <= budget <= 32000 and offset >= 0, "invalid page bounds")
    result = {"items": [], "total": len(items), "offset": offset, "next_offset": None, "snapshot": snapshot, "scan": metrics}
    for item in items[offset:offset + limit]:
        trial = {**result, "items": result["items"] + [item]}
        if len(encoded(trial)) + 100 > budget:
            need(result["items"], "first matching entry exceeds byte budget; raise max_bytes")
            break
        result["items"].append(item)
    end = offset + len(result["items"])
    if end < len(items):
        result["next_offset"] = end
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--store", type=Path, default=ROOT / ".director")
    parser.add_argument("--helper", type=Path, default=ROOT / ".director/request_store.py")
    parser.add_argument("action", choices=["pending", "proposals", "decisions", "reviews", "select", "selectors", "append"])
    parser.add_argument("--data-file", default="-")
    args = parser.parse_args()
    writer = None
    try:
        raw = sys.stdin.read() if args.data_file == "-" else Path(args.data_file).read_text()
        query = json.loads(raw or "{}")
        need(isinstance(query, dict), "query must be an object")
        spec = importlib.util.spec_from_file_location("canonical_request_store", args.helper)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        store = module.Store(args.store)
        if args.action == "append":
            # Every learning writer uses this lock across global read/validate/CAS.
            # Store.apply independently takes its native lock; no native lock is
            # already held, so unrelated foreground tracker operations stay safe.
            writer = os.open(args.store / ".learning-notes.lock", os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
            fcntl.flock(writer, fcntl.LOCK_EX | fcntl.LOCK_NB)
        records = store.records()
        entries = collect(records, store)
        snapshot = digest([[record["id"], record["revision"]] for record in records])
        metrics = {"request_records": len(records), "history_events": sum(len(record["history"]) for record in records), "learning_entries": len(entries), "cost": "full canonical histories and source/file integrity validation internally; bounded model output"}
        if args.action == "append":
            need(set(query) == {"request_id", "expected_revision", "entry"}, "append requires request_id/expected_revision/entry")
            # Legacy identical replay remains valid; only a NEW review must be typed.
            item = validate(query["entry"], allow_legacy=True)
            record = next((record for record in records if record["id"] == query["request_id"]), None)
            need(record is not None, "canonical request not found")
            event = {"event_id": item["id"], "type": "note", "text": PREFIX + encoded(item).decode(), "artifacts": [], "evidence": []}
            old = next((entry for entry in record["history"] if entry["event_id"] == item["id"]), None)
            if old:
                need(old["data"] == event, "event ID already used with different payload")
                fields = next((entry for entry in entries if entry["id"] == item["id"]), {})
                print(json.dumps({"saved": True, "idempotent": True, "request_id": record["id"], "revision": record["revision"], "entry_id": item["id"], **{key: fields[key] for key in ("proposal_kind", "classification_required", "implementation_required") if key in fields}}))
                return 0
            validate(item)
            if item["kind"] == "decision" and item["decision"] == "accept":
                target = next((entry for entry in entries if entry["id"] == item["proposal_id"]), None)
                need(target and target.get("proposal_kind") in {"knowledge", "routing", "structure"}, "proposal classification required before a new acceptance")
            need(record["revision"] == query["expected_revision"], "stale expected request revision")
            need(item["source_id"] in {source["source_id"] for source in record["sources"]} and item["request_revision"] <= record["revision"], "source/revision not canonical to request")
            # Validate references using a synthetic next history entry before the canonical CAS.
            trial = dict(record, history=record["history"] + [{"data": event, "event_id": item["id"], "at": "pending"}])
            trial_entries = collect([trial if current["id"] == record["id"] else current for current in records], store)
            saved = store.apply(record["id"], event, query["expected_revision"])
            fields = next(entry for entry in trial_entries if entry["id"] == item["id"])
            print(json.dumps({"saved": True, "idempotent": False, "request_id": saved["id"], "revision": saved["revision"], "entry_id": item["id"], **{key: fields[key] for key in ("proposal_kind", "classification_required", "implementation_required") if key in fields}}))
            return 0
        by_id = {item["id"]: item for item in entries}
        latest = {}
        for item in entries:
            if item["kind"] == "decision":
                latest[item["proposal_id"]] = item
        reviewed = {ref["id"] for item in entries if item["kind"] == "review" for ref in item["incidents"]}
        retired = {item["knowledge_id"] for item in entries if item["kind"] == "retire"}
        if args.action == "pending":
            items = [item for item in entries if item["kind"] == "incident" and item["id"] not in reviewed]
        elif args.action == "proposals":
            items = [item for item in entries if item["kind"] == "proposal" and (query.get("include_decided") or item["id"] not in latest or item["classification_required"] and item["id"] not in retired and latest[item["id"]]["decision"] == "accept")]
        elif args.action in {"decisions", "reviews"}:
            items = [item for item in entries if item["kind"] == args.action[:-1]]
        else:
            items = [{**by_id[ident], "acceptance": decision} for ident, decision in latest.items() if decision["decision"] == "accept" and ident not in retired and by_id[ident]["proposal_kind"] == "knowledge"]
            items += [item for item in entries if item["kind"] == "rule" and item["id"] not in retired]
        items = [item for item in items if (not query.get("request_id") or item["request_id"] == query["request_id"]) and matches(item, query, args.action == "selectors")]
        if args.action in {"select", "selectors"}:
            if args.action == "select":
                need(all(key in query for key in ("task", "path", "audience")), "select requires actual task/path/audience")
            else:
                items = [{"id": item["id"], "scope": item["scope"], "request_id": item["request_id"]} for item in items]
        print(encoded(page(items, query, snapshot, metrics)).decode())
        return 0
    except (ValueError, OSError, TypeError, KeyError, ImportError, AttributeError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2
    finally:
        if writer is not None:
            os.close(writer)


if __name__ == "__main__":
    sys.exit(main())
