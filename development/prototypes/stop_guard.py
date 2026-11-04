#!/usr/bin/env python3
"""Unactivated Stop command prototype; no backend or evaluator is supplied.

The explicit bind operation alone creates control state. A run can consume one
snapshot, one optional evaluation and one correction for that immutable binding.
This is operational metadata, never a canonical task store or authority service.
"""
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import selectors
import signal
import stat
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager


CAP = 262144
ENV_GUARD = "DIRECTOR_STOP_PROTOTYPE_ACTIVE"


class Gap(Exception):
    pass


def require(condition, code="invalid_protocol"):
    if not condition:
        raise Gap(code)


def exact(value, keys):
    require(type(value) is dict and set(value) == set(keys.split()))


def string(value):
    require(type(value) is str and 0 < len(value.encode("utf-8")) <= 4096)


def strings(value):
    require(type(value) is list and 0 < len(value) <= 64)
    for item in value:
        string(item)
    require(len(set(value)) == len(value))


def encode(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(encode(value)).hexdigest()


def decode(raw, cap=CAP):
    require(len(raw) <= cap, "size_limit")
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate_key")
            result[key] = value
        return result
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                           parse_constant=lambda _: (_ for _ in ()).throw(Gap("invalid_json")))
        def depth(item, level=0):
            require(level <= 20, "nesting_limit")
            if isinstance(item, dict):
                for child in item.values():
                    depth(child, level + 1)
            elif isinstance(item, list):
                for child in item:
                    depth(child, level + 1)
        depth(value)
        return value
    except (ValueError, UnicodeError, RecursionError):
        raise Gap("invalid_json") from None


def safe_path(path, root=None):
    path = Path(os.path.abspath(path))
    if root is not None:
        require(path.is_relative_to(root), "unsafe_path")
    for part in [path, *path.parents]:
        if part.exists() or part.is_symlink():
            require(not part.is_symlink(), "unsafe_path")
    return path


def read(path, cap=CAP, private=True):
    path = safe_path(path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, "rb") as stream:
        before = os.fstat(stream.fileno())
        require(stat.S_ISREG(before.st_mode), "unsafe_file")
        if private:
            require(before.st_uid == os.getuid() and not before.st_mode & 0o077, "private_permissions")
        require(before.st_size <= cap, "size_limit")
        raw = stream.read(cap + 1)
        after = os.fstat(stream.fileno())
        require((before.st_ino, before.st_size, before.st_mtime_ns, before.st_ctime_ns) ==
                (after.st_ino, after.st_size, after.st_mtime_ns, after.st_ctime_ns), "file_changed")
        require(path.stat().st_ino == after.st_ino, "file_changed")
    return decode(raw, cap)


def atomic(path, value):
    safe_path(path)
    raw = encode(value)
    require(len(raw) <= CAP, "size_limit")
    fd, name = tempfile.mkstemp(prefix=".stop-", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
        directory = os.open(path.parent, os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def config(path):
    value = read(path)
    exact(value, "schema root private_dir snapshot_argv evaluator_argv timeout_seconds max_bytes")
    require(type(value["schema"]) is int and value["schema"] == 1)
    root = safe_path(value["root"])
    require(root.is_dir() and str(root) == value["root"], "unsafe_root")
    private = value["private_dir"]
    require(type(private) is str and private.startswith(".director/") and
            ".." not in Path(private).parts and not Path(private).is_absolute(), "unsafe_path")
    home = safe_path(root / private, root)
    require(safe_path(path) == home / "config.json", "config_location")
    require(home.is_dir() and not home.stat().st_mode & 0o077, "private_permissions")
    for argv in [value["snapshot_argv"], value["evaluator_argv"]]:
        if argv is not None:
            strings(argv)
            require(Path(argv[0]).is_absolute(), "absolute_executable_required")
    require(value["snapshot_argv"] is not None)
    require(type(value["timeout_seconds"]) in (int, float) and 0 < value["timeout_seconds"] <= 10)
    require(type(value["max_bytes"]) is int and 1024 <= value["max_bytes"] <= CAP)
    return value, root, home


@contextmanager
def locked(home):
    path = safe_path(home / "control.lock", home)
    fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW | os.O_NONBLOCK, 0o600)
    try:
        info = os.fstat(fd)
        require(stat.S_ISREG(info.st_mode) and info.st_uid == os.getuid() and
                not info.st_mode & 0o077, "unsafe_lock")
        deadline = time.monotonic() + 0.25
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                require(time.monotonic() < deadline, "lock_busy")
                time.sleep(0.01)
        yield
    finally:
        os.close(fd)


def frontier(value):
    require(type(value) is list and 0 < len(value) <= 64)
    ids = []
    for source in value:
        exact(source, "id sha256")
        string(source["id"])
        sha = source["sha256"]
        require(type(sha) is str and len(sha) == 64 and all(c in "0123456789abcdef" for c in sha))
        ids.append(source["id"])
    require(len(set(ids)) == len(ids))


def binding(value, root):
    exact(value, "schema binding_id assignment_generation session_id actor_kind status root project_id backend request_ids source_frontier adoption_evidence")
    require(type(value["schema"]) is int and value["schema"] == 1 and value["root"] == str(root))
    for key in ("binding_id", "assignment_generation", "session_id", "project_id", "backend", "adoption_evidence"):
        string(value[key])
    require(value["actor_kind"] == "project_director", "not_root_owner")
    require(value["status"] in ("active", "paused", "canceled"))
    strings(value["request_ids"])
    frontier(value["source_frontier"])


def bind(config_path, spec_path):
    cfg, root, home = config(config_path)
    value = read(safe_path(spec_path, home), cfg["max_bytes"])
    binding(value, root)
    with locked(home):
        require(not (home / "binding.json").exists() and not (home / "state.json").exists(), "already_bound")
        # A crash between these writes leaves a binding without state: run fails open.
        atomic(home / "binding.json", value)
        atomic(home / "state.json", {"schema": 1, "binding_digest": digest(value),
               "config_digest": digest(cfg), "snapshot_calls": 0, "evaluator_calls": 0,
               "corrections": 0, "diagnostic": "bound", "last_final_sha256": None})


def execute(argv, payload, cfg, root):
    """No shell, bounded pipes/time, discarded stderr, killed process group on error."""
    raw = encode(payload)
    require(len(raw) <= cfg["max_bytes"], "input_size_limit")
    env = dict(os.environ, **{ENV_GUARD: "1"})
    process = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                               stderr=subprocess.DEVNULL, cwd=root, env=env, start_new_session=True)
    output, offset = bytearray(), 0
    deadline = time.monotonic() + cfg["timeout_seconds"]
    try:
        with selectors.DefaultSelector() as selector:
            for pipe, event in [(process.stdin, selectors.EVENT_WRITE), (process.stdout, selectors.EVENT_READ)]:
                os.set_blocking(pipe.fileno(), False)
                selector.register(pipe, event)
            while selector.get_map():
                require(time.monotonic() < deadline, "command_timeout")
                for key, _ in selector.select(min(0.05, max(0, deadline - time.monotonic()))):
                    if key.fileobj is process.stdin:
                        offset += os.write(process.stdin.fileno(), raw[offset:offset + 4096])
                        if offset == len(raw):
                            selector.unregister(process.stdin)
                            process.stdin.close()
                    else:
                        chunk = os.read(process.stdout.fileno(), 4096)
                        output.extend(chunk)
                        require(len(output) <= cfg["max_bytes"], "command_output_limit")
                        if not chunk:
                            selector.unregister(process.stdout)
            require(process.wait(timeout=max(0.001, deadline - time.monotonic())) == 0, "command_failed")
        return decode(bytes(output), cfg["max_bytes"])
    except subprocess.TimeoutExpired:
        raise Gap("command_timeout") from None
    finally:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()
        for pipe in (process.stdin, process.stdout):
            if not pipe.closed:
                pipe.close()


def snapshot(value, bound):
    exact(value, "schema binding_id assignment_generation project_id request_ids source_frontier complete status gaps items sources authorized_actions")
    require(type(value["schema"]) is int and value["schema"] == 1 and value["complete"] is True, "incomplete_snapshot")
    for key in ("binding_id", "assignment_generation", "project_id", "request_ids", "source_frontier"):
        require(value[key] == bound[key], "binding_or_source_changed")
    require(value["gaps"] == [], "snapshot_gap")
    require(value["status"] in ("active", "partial_hold", "paused", "canceled", "waiting", "complete"))
    require(type(value["sources"]) is list and len(value["sources"]) == len(bound["source_frontier"]))
    for source, expected in zip(value["sources"], bound["source_frontier"]):
        exact(source, "id sha256 text")
        require({k: source[k] for k in ("id", "sha256")} == expected, "source_changed")
        require(type(source["text"]) is str and hashlib.sha256(source["text"].encode()).hexdigest() == source["sha256"], "source_changed")
    require(type(value["authorized_actions"]) is list and len(value["authorized_actions"]) <= 64)
    action_ids = []
    for action in value["authorized_actions"]:
        exact(action, "id request_id action")
        string(action["id"])
        string(action["action"])
        require(action["request_id"] in bound["request_ids"])
        action_ids.append(action["id"])
    require(len(set(action_ids)) == len(action_ids))
    require(type(value["items"]) is list and [i.get("request_id") for i in value["items"] if type(i) is dict] == bound["request_ids"])
    for item in value["items"]:
        exact(item, "request_id state checkpoint")
        require(item["state"] in ("inbox", "queued", "active", "blocked", "review", "done", "canceled"))
        cp = item["checkpoint"]
        exact(cp, "obligations next_action controlling_wait")
        require(type(cp["controlling_wait"]) is bool)
        require(cp["next_action"] is None or cp["next_action"] in action_ids)
        require(type(cp["obligations"]) is list and len(cp["obligations"]) <= 64)
        for obligation in cp["obligations"]:
            exact(obligation, "id text state")
            string(obligation["id"])
            string(obligation["text"])
            require(obligation["state"] in ("pending", "waiting", "complete"))
    return value


def verdict(value, snap, final):
    exact(value, "decision reason remaining_obligation next_action wait_assessment evidence")
    require(value["decision"] in ("allow", "continue", "unknown"))
    string(value["reason"])
    require(value["wait_assessment"] in ("runnable", "paused", "waiting", "complete", "unknown"))
    exact(value["evidence"], "sources final")
    if value["decision"] != "continue":
        return value["decision"]
    require(value["wait_assessment"] == "runnable", "conflicting_verdict")
    remaining = value["remaining_obligation"]
    exact(remaining, "request_id text")
    string(remaining["text"])
    require(remaining["request_id"] in snap["request_ids"])
    require(type(value["next_action"]) is str and any(
        action["id"] == value["next_action"] and action["request_id"] == remaining["request_id"]
        for action in snap["authorized_actions"]), "unsupported_action")
    def span(value, text):
        exact(value, "start end")
        require(type(value["start"]) is int and type(value["end"]) is int and
                0 <= value["start"] < value["end"] <= len(text), "invalid_evidence_span")
    span(value["evidence"]["final"], final)
    sources = value["evidence"]["sources"]
    require(type(sources) is list and 0 < len(sources) <= 64, "missing_source_evidence")
    for evidence in sources:
        exact(evidence, "source_id start end")
        source = next((s for s in snap["sources"] if s["id"] == evidence["source_id"]), None)
        require(source is not None, "unsupported_source")
        span({k: evidence[k] for k in ("start", "end")}, source["text"])
    return "continue"


def run(config_path, event):
    require(not os.environ.get(ENV_GUARD), "nested_invocation")
    require(type(event) is dict and event.get("hook_event_name") == "Stop", "not_stop")
    for key in ("session_id", "cwd", "turn_id"):
        string(event.get(key))
    require(type(event.get("stop_hook_active")) is bool, "invalid_event")
    final = event.get("last_assistant_message")
    require(type(final) is str and final.strip(), "missing_final")
    cfg, root, home = config(config_path)
    bound = read(home / "binding.json", cfg["max_bytes"])
    binding(bound, root)
    require(event["session_id"] == bound["session_id"] and event["cwd"] == str(root), "unbound_session")
    require(bound["status"] == "active", "binding_paused_or_canceled")
    with locked(home):
        state = read(home / "state.json", cfg["max_bytes"])
        exact(state, "schema binding_digest config_digest snapshot_calls evaluator_calls corrections diagnostic last_final_sha256")
        require(type(state["schema"]) is int and state["schema"] == 1 and state["binding_digest"] == digest(bound) and
                state["config_digest"] == digest(cfg), "state_binding_changed")
        for key in ("snapshot_calls", "evaluator_calls", "corrections"):
            require(type(state[key]) is int and 0 <= state[key] <= 1, "invalid_state")
        require(state["evaluator_calls"] <= state["snapshot_calls"] and
                state["corrections"] <= state["snapshot_calls"], "invalid_state")
        require(type(state["diagnostic"]) is str and len(state["diagnostic"]) <= 80, "invalid_state")
        require(state["last_final_sha256"] is None or (type(state["last_final_sha256"]) is str and len(state["last_final_sha256"]) == 64), "invalid_state")
        def save(code):
            state["diagnostic"] = code
            atomic(home / "state.json", state)
        try:
            require(state["snapshot_calls"] == 0 and state["corrections"] == 0, "allowance_exhausted")
            state["snapshot_calls"] = 1
            state["last_final_sha256"] = hashlib.sha256(final.encode()).hexdigest()
            save("snapshot_started")
            snap = snapshot(execute(cfg["snapshot_argv"], {"binding": bound}, cfg, root), bound)
            structural = snap["status"] in ("active", "partial_hold", "complete") and any(
                not item["checkpoint"]["controlling_wait"] and
                any(o["state"] == "pending" for o in item["checkpoint"]["obligations"]) and
                any(a["id"] == item["checkpoint"]["next_action"] and a["request_id"] == item["request_id"]
                    for a in snap["authorized_actions"])
                for item in snap["items"])
            if structural:
                decision = "continue"
            elif cfg["evaluator_argv"] is not None:
                state["evaluator_calls"] = 1
                save("evaluation_started")
                decision = verdict(execute(cfg["evaluator_argv"],
                    {"binding": bound, "snapshot": snap, "last_assistant_message": final}, cfg, root), snap, final)
            else:
                decision = "unknown"
            if decision == "continue":
                state["corrections"] = 1
                save("correction_consumed")
                return {"decision": "block", "reason": "Reconcile the explicitly bound adopted outcome through its existing continuation/source route. Inspect the supported unfinished obligation and take the available authorized next action, preserving user holds and approval boundaries."}
            save("evaluator_" + decision if cfg["evaluator_argv"] else "structural_only_false_complete_unchecked")
            diagnostic(state["diagnostic"])
            return {}
        except Gap as error:
            save(str(error))
            raise


def diagnostic(code):
    # Only fixed internal codes reach stderr, never exception text from commands.
    sys.stderr.write("stop_guard: " + code[:80] + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=("bind", "run"))
    parser.add_argument("--config", required=True)
    parser.add_argument("--binding")
    args = parser.parse_args()
    try:
        if args.operation == "bind":
            require(args.binding is not None, "binding_required")
            bind(args.config, args.binding)
            result = {"bound": True}
        else:
            result = run(args.config, decode(sys.stdin.buffer.read(CAP + 1)))
        sys.stdout.buffer.write(encode(result) + b"\n")
        return 0
    except (Gap, OSError, ValueError, TypeError, KeyError, RecursionError, BrokenPipeError) as error:
        diagnostic(str(error) if isinstance(error, Gap) else "unavailable_or_invalid")
        sys.stdout.write("{}\n")
        return 1 if args.operation == "bind" else 0


if __name__ == "__main__":
    sys.exit(main())
