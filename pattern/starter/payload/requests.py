#!/usr/bin/env python3
"""Flat owner CLI over the established request-bundle backend; no new state format.

All established commands pass through unchanged. `status` and `current` return
bounded current views without loading history into the caller's context.
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


def compact(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--team", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("command", choices=["status", "current"])
    parser.add_argument("id", nargs="?")
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
        snapshot = hashlib.sha256(wire([[r["id"], r["revision"]] for r in records])).hexdigest()
        if args.at_snapshot and snapshot != args.at_snapshot:
            raise ValueError("snapshot changed; restart paging")
        if args.command == "current":
            if args.id is None:
                raise ValueError("current requires a request ID")
            found = [r for r in records if r["id"] == args.id]
            if not found:
                raise ValueError("unknown request")
            items = [{k: v for k, v in found[0].items() if k != "history"}]
        else:
            if args.id is not None:
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
    if rest and rest[0] in {"status", "current"}:
        return compact(argv)
    if not argv or argv[0] != "--team":
        sys.argv[1:1] = ["--team", str(Path(__file__).resolve().parent)]
    return request_store.main()


if __name__ == "__main__":
    raise SystemExit(main())
