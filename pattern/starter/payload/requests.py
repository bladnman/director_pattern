#!/usr/bin/env python3
"""Flat owner CLI over the established request-bundle backend; no new state format.

All established commands pass through unchanged. `status`, `current` and
`continuation` return bounded views over the existing validated store.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
sys.dont_write_bytecode = True
import request_store


def wire(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


CHECKPOINT_FAMILY = "DIRECTOR_CONTINUATION_"
CHECKPOINT_PREFIX = "DIRECTOR_CONTINUATION_V1 "


def checkpoint_data(text):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate checkpoint JSON key")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError("invalid JSON constant")

    return json.loads(text, object_pairs_hook=unique_object,
                      parse_constant=reject_constant)


def validate_checkpoint(data, request_id):
    def require(condition, message):
        if not condition:
            raise ValueError(message)

    def text(value):
        return isinstance(value, str) and bool(value.strip())

    def texts(value):
        return isinstance(value, list) and all(text(item) for item in value)

    require(isinstance(data, dict) and set(data) == {
        "schema", "request_id", "source_ids", "outcome", "obligations", "next_action", "wait"
    }, "invalid checkpoint fields")
    require(type(data["schema"]) is int and data["schema"] == 1, "invalid checkpoint schema")
    require(data["request_id"] == request_id, "checkpoint request ID differs")
    sources = data["source_ids"]
    require(texts(sources) and sources
            and all(request_store.SOURCE_ID.fullmatch(source) for source in sources), "invalid checkpoint sources")
    require(text(data["outcome"]), "checkpoint outcome required")
    obligations = data["obligations"]
    require(isinstance(obligations, list) and obligations, "checkpoint obligations required")
    ids = set()
    for obligation in obligations:
        require(isinstance(obligation, dict) and set(obligation) == {"id", "text", "state", "evidence"},
                "invalid obligation fields")
        require(text(obligation["id"]) and obligation["id"] not in ids, "invalid or duplicate obligation ID")
        ids.add(obligation["id"])
        require(text(obligation["text"]) and obligation["state"] in ("pending", "complete", "waiting")
                and texts(obligation["evidence"]), "invalid obligation text/state/evidence")
        require(obligation["state"] != "complete" or obligation["evidence"], "complete obligation needs evidence")
    for field, keys in (("next_action", {"owner", "action"}), ("wait", {"reason", "resume_when"})):
        value = data[field]
        require(value is None or (isinstance(value, dict) and set(value) == keys
                                  and all(text(value[key]) for key in keys)), f"invalid checkpoint {field}")
    require(all(obligation["state"] == "complete" for obligation in obligations)
            or data["next_action"] is not None or data["wait"] is not None,
            "unfinished obligations need a next action or wait")


def continuation_item(record, request_id, project_id):
    item = ({k: v for k, v in record.items() if k != "history"} if record else
            {"id": request_id, "project_id": project_id})
    item.update(current_liveness="unknown", checkpoint=None, gaps=[])
    gaps = item["gaps"]
    if record is None:
        gaps.append("request_missing")
    else:
        candidates = [(revision, entry) for revision, entry in enumerate(record["history"], 1)
                      if entry["type"] == "note" and entry["data"]["text"].startswith(CHECKPOINT_FAMILY)]
        if not candidates:
            gaps.append("checkpoint_missing")
        else:
            revision, entry = candidates[-1]
            text = entry["data"]["text"]
            checkpoint = {"event_id": entry["event_id"], "revision": revision, "at": entry["at"], "data": None}
            item["checkpoint"] = checkpoint
            if not text.startswith(CHECKPOINT_PREFIX):
                gaps.append("checkpoint_unsupported_version")
                checkpoint["text"] = text
            else:
                try:
                    checkpoint["data"] = checkpoint_data(text[len(CHECKPOINT_PREFIX):])
                    validate_checkpoint(checkpoint["data"], request_id)
                except (ValueError, TypeError, RecursionError) as error:
                    gaps.append("checkpoint_invalid")
                    checkpoint.update(data=None, text=text, error=str(error))
                else:
                    data = checkpoint["data"]
                    if data["source_ids"] != [source["source_id"] for source in record["sources"]]:
                        gaps.append("source_frontier_changed")
                    if record["state"] in request_store.TERMINAL and any(
                            obligation["state"] != "complete" for obligation in data["obligations"]):
                        gaps.append("terminal_with_unfinished_obligations")
            if any(event["type"] != "note" for event in record["history"][revision:]):
                gaps.append("events_after_checkpoint")
    item["reconciliation_required"] = bool(gaps)
    return item


def compact(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--team", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("command", choices=["status", "current", "continuation"])
    parser.add_argument("ids", nargs="*")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--max-bytes", type=int, default=12000)
    parser.add_argument("--at-snapshot")
    args = parser.parse_args(argv)
    try:
        if not (args.offset >= 0 and 1 <= args.limit <= 20 and 512 <= args.max_bytes <= 32000):
            raise ValueError("invalid page bounds")
        store = request_store.Store(args.team)
        records = store.records()  # Replay/source validation grows with the store, not model context.
        versions = [[r["id"], r["revision"]] for r in records]
        snapshot = hashlib.sha256(wire([args.ids, versions] if args.command == "continuation" else versions)).hexdigest()
        if args.at_snapshot and snapshot != args.at_snapshot:
            raise ValueError("snapshot changed; restart paging")
        if args.command == "current":
            if len(args.ids) != 1:
                raise ValueError("current requires a request ID")
            found = [r for r in records if r["id"] == args.ids[0]]
            if not found:
                raise ValueError("unknown request")
            items = [{k: v for k, v in found[0].items() if k != "history"}]
        elif args.command == "continuation":
            if not args.ids or len(set(args.ids)) != len(args.ids) or any(
                    not request_store.ID.fullmatch(request_id) for request_id in args.ids):
                raise ValueError("continuation requires unique request IDs")
            by_id = {record["id"]: record for record in records}
            items = [continuation_item(by_id.get(request_id), request_id, store.project_id) for request_id in args.ids]
        else:
            if args.ids:
                raise ValueError("status takes no request ID")
            items = [{k: r[k] for k in ("id", "title", "state", "revision", "owner")}
                     | {"current_liveness": "unknown"} for r in records if r["state"] not in request_store.TERMINAL]
        result = {"items": [], "total": len(items), "offset": args.offset,
                  "next_offset": None, "snapshot": snapshot,
                  "scan": "all bundle histories/sources validated internally; bounded returned context"}
        for item in items[args.offset:args.offset + args.limit]:
            trial = {**result, "items": result["items"] + [item], "next_offset": len(items)}
            if len(wire(trial)) + 1 > args.max_bytes:
                if not result["items"]:
                    raise ValueError("current item exceeds byte budget; use the exact request/source via deferred API or raise max-bytes")
                break
            result["items"].append(item)
        end = args.offset + len(result["items"])
        if end < len(items):
            result["next_offset"] = end
        if len(wire(result)) + 1 > args.max_bytes:
            raise ValueError("response exceeds byte budget")
        sys.stdout.buffer.write(wire(result) + b"\n")
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 1


def main():
    argv = sys.argv[1:]
    rest = argv[2:] if len(argv) >= 2 and argv[0] == "--team" else argv
    if rest and rest[0] in {"status", "current", "continuation"}:
        return compact(argv)
    if not argv or argv[0] != "--team":
        sys.argv[1:1] = ["--team", str(Path(__file__).resolve().parent)]
    return request_store.main()


if __name__ == "__main__":
    raise SystemExit(main())
