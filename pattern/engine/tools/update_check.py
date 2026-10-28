#!/usr/bin/env python3
"""Project-local daily discovery. No payload downloads, installation, or request-store I/O."""
import argparse
import contextlib
import fcntl
import json
import math
import os
from pathlib import Path
import re
import tempfile
import time
import urllib.request

API = "https://api.github.com/repos/bladnman/director_pattern"
SOURCE = "https://github.com/bladnman/director_pattern"
DAY = 24 * 60 * 60
MESSAGE = 'A new Director Pattern is available. Say “update director pattern” to install it.'
MODES = {"notify", "automatic", "off"}
SHA = re.compile(r"[0-9a-f]{40}\Z")


class CheckError(ValueError):
    pass


def sha(value):
    if not isinstance(value, str) or not SHA.fullmatch(value):
        raise CheckError("Expected a full lowercase Git SHA")
    return value


def read_json(path, default=None):
    if path.is_symlink():
        raise CheckError(f"Refusing symlink: {path.name}")
    if not path.exists():
        return default
    if path.stat().st_size > 2_000_000:
        raise CheckError(f"Oversized local metadata: {path.name}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise CheckError(f"Expected object: {path.name}")
    return value


def atomic_json(path, value):
    if path.is_symlink():
        raise CheckError(f"Refusing symlink: {path.name}")
    fd, temporary = tempfile.mkstemp(prefix=".update-check-", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, indent=2, sort_keys=True)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


@contextlib.contextmanager
def lock(root):
    # One nonblocking lock covers check and preference writes on this machine.
    # Never unlink it: another process may already hold its inode.
    path = root / ".update-check.lock"
    fd = os.open(path, os.O_RDWR | os.O_CREAT | os.O_NOFOLLOW, 0o600)
    try:
        try:
            fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            yield False
            return
        yield True
    finally:
        os.close(fd)


def policy(root):
    value = read_json(root / "update-policy.json", {"schema_version": 1, "mode": "notify"})
    if value.get("schema_version") != 1 or value.get("mode") not in MODES:
        raise CheckError("Unsupported update policy; preserve it for review")
    if value["mode"] == "automatic" and (not isinstance(value.get("authorization"), str) or not value["authorization"].strip()):
        raise CheckError("Automatic policy needs a recorded user authorization source")
    return value


def set_policy(root, mode, authorization, now=None):
    if mode not in MODES or not authorization.strip():
        raise CheckError("A supported mode and user-source reference are required")
    with lock(root) as acquired:
        if not acquired:
            return {"status": "busy", "action": "none"}
        existing = policy(root)  # Do not overwrite an unknown schema or corrupted policy.
        value = dict(existing, schema_version=1, mode=mode,
                     authorization=authorization, changed_at=time.time() if now is None else now)
        atomic_json(root / "update-policy.json", value)
        # Deliberately do not reset last_attempt or launch a same-day retry.
        return {"status": "policy_saved", "mode": mode, "action": "none"}


def github_json(route):
    request = urllib.request.Request(API + route, headers={
        "Accept": "application/vnd.github+json", "User-Agent": "Director-Pattern-update-check",
        "X-GitHub-Api-Version": "2022-11-28"})
    # No credentials, retries, redirects to alternate sources, or source-code fetches.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, request, fp, code, msg, headers, newurl):
            raise CheckError("Unexpected GitHub redirect")
    with urllib.request.build_opener(NoRedirect()).open(request, timeout=8) as response:
        body = response.read(1_000_001)
        if len(body) > 1_000_000:
            raise CheckError("Oversized GitHub metadata")
        value = json.loads(body)
    if not isinstance(value, dict):
        raise CheckError("Unexpected GitHub response")
    return value


def pattern_tree(commit, fetch):
    data = fetch("/git/trees/" + sha(commit))
    if data.get("truncated") or not isinstance(data.get("tree"), list):
        raise CheckError("Incomplete GitHub tree metadata")
    entries = [entry for entry in data["tree"] if entry.get("path") == "pattern"]
    if len(entries) != 1 or entries[0].get("type") != "tree":
        raise CheckError("Published revision has no unambiguous pattern tree")
    return sha(entries[0].get("sha"))


def installed_source(root, receipt_path):
    # The Director supplies PROJECT's exact current pointer. No newest-file guesses.
    receipt = Path(receipt_path)
    if not receipt.is_absolute():
        receipt = root.parent / receipt
    receipt = receipt.absolute()
    if not receipt.resolve().is_relative_to(root.resolve()):
        raise CheckError("Receipt must be inside this installation")
    value = read_json(receipt)
    if value is None:
        raise CheckError("Installed receipt is missing; review PROJECT's pointer")
    source = value.get("source")
    if not isinstance(source, dict) or source.get("url", "").rstrip("/") != SOURCE:
        raise CheckError("Receipt needs source.url and source.sha for the canonical repository")
    if source.get("published") is not True:
        raise CheckError("Receipt needs an authoritative published base; retain local deltas separately")
    revision = sha(source.get("sha"))
    tree = source.get("pattern_tree_sha")
    if tree is not None:
        tree = sha(tree)
    return revision, tree


def check(root, receipt_path, *, now=None, fetch=github_json):
    root = Path(root).resolve(strict=True)
    now = time.time() if now is None else now
    if not isinstance(now, (int, float)) or not math.isfinite(now) or now < 0:
        raise CheckError("Invalid current time")
    with lock(root) as acquired:
        if not acquired:
            return {"status": "busy", "action": "none"}
        cache_usable = False
        try:
            cache = read_json(root / ".update-check.json", {"schema_version": 1})
            if cache.get("schema_version") != 1:
                raise CheckError("Unsupported daily cache; preserve it for review")
            if "baseline" in cache:
                baseline = cache["baseline"]
                if not isinstance(baseline, dict):
                    raise CheckError("Invalid cached baseline; preserve cache for review")
                sha(baseline.get("source_sha"))
                sha(baseline.get("pattern_tree_sha"))
            last = cache.get("last_attempt")
            if last is not None:
                if not isinstance(last, (int, float)) or not math.isfinite(last) or last < 0:
                    raise CheckError("Invalid last_attempt; preserve cache for review")
                if now - last < DAY:
                    return {"status": "throttled", "action": "none", "last_attempt": last, "next_check_at": last + DAY}
            cache_usable = True
            mode = policy(root)["mode"]
            if mode == "off":
                return {"status": "off", "action": "none"}
            # Persist before network/receipt work; interruption/failure also consumes this window.
            cache.update(last_attempt=now, result="checking")
            atomic_json(root / ".update-check.json", cache)
            previous, baseline_tree = installed_source(root, receipt_path)
            main = sha(fetch("/git/ref/heads/main").get("object", {}).get("sha"))
            incoming_tree = pattern_tree(main, fetch)
            if baseline_tree is None:
                saved = cache.get("baseline", {})
                if isinstance(saved, dict) and saved.get("source_sha") == previous:
                    baseline_tree = sha(saved.get("pattern_tree_sha"))
                else:
                    baseline_tree = incoming_tree if previous == main else pattern_tree(previous, fetch)
            cache["baseline"] = {"source_sha": previous, "pattern_tree_sha": baseline_tree}
            available = incoming_tree != baseline_tree
            result = {"status": "available" if available else "current", "action": "none",
                      "mode": mode, "source_sha": previous, "upstream_sha": main,
                      "upstream_pattern_tree_sha": incoming_tree, "next_check_at": now + DAY}
            if available:
                if mode == "notify":
                    result.update(action="notify", message=MESSAGE)
                else:
                    result["action"] = "request_safe_update"
            cache.update(result=result, last_success=now)
            atomic_json(root / ".update-check.json", cache)
            return result
        except (CheckError, OSError, ValueError, TypeError, AttributeError) as error:
            # Corrupt cache cannot safely establish a daily window: no network and no repair.
            # If our attempt reservation succeeded, retain its timestamp and failure.
            if cache_usable:
                cache["last_attempt"] = now
                cache["result"] = {"status": "error", "error": str(error)}
                atomic_json(root / ".update-check.json", cache)
            return {"status": "error", "action": "none", "error": str(error),
                    "next_check_at": now + DAY if cache_usable else None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2],
                        help="Installed .director directory")
    commands = parser.add_subparsers(dest="command", required=True)
    daily = commands.add_parser("check")
    daily.add_argument("--receipt", required=True, help="Exact PROJECT receipt pointer, relative to project root")
    preference = commands.add_parser("set-policy")
    preference.add_argument("mode", choices=sorted(MODES))
    preference.add_argument("--authorization", required=True, help="Reference to the user's policy instruction")
    args = parser.parse_args()
    try:
        root = args.root.resolve(strict=True)
        result = (check(root, args.receipt) if args.command == "check" else
                  set_policy(root, args.mode, args.authorization))
    except (CheckError, OSError, ValueError) as error:
        result = {"status": "error", "action": "none", "error": str(error)}
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 1 if result["status"] == "error" else 0


if __name__ == "__main__":
    raise SystemExit(main())
