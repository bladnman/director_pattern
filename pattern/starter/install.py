#!/usr/bin/env python3
"""Install starter 2 beside ordinary project files. No network or implicit migration."""
import argparse
try:
    import fcntl
except ImportError:
    fcntl = None
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import stat
import tempfile

SOURCE = Path(__file__).resolve().parent
GUARDS = (".director", ".producer", ".team", ".program", "requests", "AGENTS.md", "CLAUDE.md")
BRIDGE = """<!-- director-starter:2 -->
Read `.director/START.md` and the exact selected role package completely before
task work; preserve this project's and host's authority. Use an explicit bounded
worker assignment when supplied; otherwise serve as the project Director.
Delegate useful substantial execution/coordination to bounded subagents when
permitted. No mandatory manager, Recorder, learning or setup actor is required.
Load selected task instructions before action; recover incomplete reads.
<!-- /director-starter:2 -->
"""


def sha(data):
    return hashlib.sha256(data).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def manifest():
    value = json.loads((SOURCE / "manifest.json").read_bytes())
    require(value.get("format") == "director-flat-starter" and value.get("starter_version") == 2,
            "unknown starter manifest")
    names = value["payload"]
    require(isinstance(names, list) and len(names) == len(set(names)), "duplicate payload")
    for name in names:
        require(isinstance(name, str) and Path(name).name == name and name not in {".", ".."}, "unsafe payload path")
        require((SOURCE / "payload" / name).is_file() and not (SOURCE / "payload" / name).is_symlink(), "unsafe payload")
    return value


def runtime():
    spec = importlib.util.spec_from_file_location("flat_starter_runtime", SOURCE / "payload/state.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def files_for(target, initiator, opportunity, min_incidents=3):
    value = manifest()
    files = {".director/" + name: (SOURCE / "payload" / name).read_bytes() for name in value["payload"]}
    files["AGENTS.md"] = BRIDGE.encode()
    module = runtime()
    files[".director/state.json"] = module.encoded(module.initial_state(target / ".director", initiator, opportunity, min_incidents)) + b"\n"
    return value, files


def inventory(root):
    values = {}
    for path in root.rglob("*"):
        require(not path.is_symlink(), "symlink in managed installation")
        if path.is_file():
            values[path.relative_to(root).as_posix()] = sha(path.read_bytes())
    return values


def operation(mode, target, initiator="owner", opportunity="closure", min_incidents=3):
    require(fcntl is not None, "Starter helper needs POSIX fcntl (macOS/Linux); Windows runtime is not implemented")
    target = Path(target).absolute()
    require(not target.is_symlink(), "symlink target refused")
    target = target.resolve()
    value, files = files_for(target, initiator, opportunity, min_incidents)
    receipt_path = target / ".director/install.json"
    if receipt_path.exists():
        require(not receipt_path.is_symlink(), "unsafe receipt")
        receipt = json.loads(receipt_path.read_bytes())
        require(receipt.get("format") == value["format"] and receipt.get("starter_version") == 2,
                "existing installation is not this starter; migration requires review")
        require(receipt.get("manifest_sha256") == sha((SOURCE / "manifest.json").read_bytes()), "changed starter package; no implicit upgrade")
        static = {k: v for k, v in files.items() if k != ".director/state.json"}
        for name, data in static.items():
            path = target / name
            require(path.is_file() and not path.is_symlink() and path.read_bytes() == data,
                    "installed instruction drift; no implicit overwrite")
        current = json.loads((target / ".director/state.json").read_bytes())
        require(current.get("format") == value["format"] and current.get("starter_version") == 2, "incompatible current state")
        return {"operation": mode, "changed": False, "status": "same starter; mutable state and optional roles preserved", "target": str(target)}
    require(not target.exists() or target.is_dir(), "target must be a project directory")
    conflicts = [name for name in GUARDS
                 if (target / name).exists() or (target / name).is_symlink()]
    require(not conflicts, "existing startup/tracker needs reviewed integration: " + ", ".join(conflicts))
    report = {"operation": mode, "changed": True, "format": value["format"], "starter_version": 2,
              "target": str(target), "files": {p: {"sha256": sha(b), "bytes": len(b)} for p, b in files.items()},
              "payload_bytes": sum(len(b) for b in files.values()),
              "startup_bytes_director": sum(len(files[".director/" + p]) for p in ["START.md", "DIRECTOR.md"]) + len(files["AGENTS.md"]),
              "startup_bytes_worker": sum(len(files[".director/" + p]) for p in ["START.md", "WORKER.md"]) + len(files["AGENTS.md"])}
    if mode == "plan":
        return report
    target_created = not target.exists()
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".director-starter-stage-", dir=target.parent))
    try:
        for name, data in files.items():
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            path.chmod(0o600 if name.endswith("state.json") else 0o644)
        receipt = {"format": value["format"], "starter_version": 2, "target": str(target),
                   "target_created": target_created, "manifest_sha256": sha((SOURCE / "manifest.json").read_bytes()),
                   "managed": {name: sha(data) for name, data in files.items()},
                   "review_policy": {"initiator": initiator, "opportunity": opportunity,
                                     "min_incidents": min_incidents, "max_batch": 5, "max_bytes": 12000, "background": False}}
        (stage / ".director/install.json").write_text(json.dumps(receipt, indent=2) + "\n")
        staged_inventory = inventory(stage)
        require(staged_inventory == {**receipt["managed"], ".director/install.json": sha((stage / ".director/install.json").read_bytes())}, "stage verification failed")
        # Preserve ordinary notes/assets. Exclusive owned-path creation refuses conflicts.
        if target_created:
            target.mkdir()
        require(target.is_dir() and not any((target / name).exists() or (target / name).is_symlink() for name in GUARDS), "target changed concurrently")
        owned_directory = target / ".director"
        acquired = False
        try:
            owned_directory.mkdir()  # Atomic refusal if another installer acquired this name.
            acquired = True
            for child in (stage / ".director").iterdir():
                os.rename(child, owned_directory / child.name)
            # O_EXCL preserves an instruction file concurrently created by another author.
            with (target / "AGENTS.md").open("xb") as out:
                out.write(files["AGENTS.md"])
        except BaseException:
            # Only remove this install's bytes while they still equal the staged originals.
            current = target / ".director"
            if acquired and current.exists() and inventory(current) == {p.removeprefix(".director/"): d for p, d in staged_inventory.items() if p.startswith(".director/")}:
                shutil.rmtree(current)
            raise
        report.update(receipt=str(receipt_path), receipt_sha256=sha(receipt_path.read_bytes()))
        return report
    finally:
        shutil.rmtree(stage, ignore_errors=True)


def rollback(receipt_file):
    require(fcntl is not None, "Rollback needs POSIX fcntl (macOS/Linux)")
    path = Path(receipt_file).absolute()
    require(path.is_file() and not path.is_symlink(), "missing/unsafe install receipt")
    root = path.parent
    require(not (root / ".lock").is_symlink(), "unsafe writer lock")
    with (root / ".lock").open("a+b") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("store busy; rollback refused without changes") from None
        require(os.fstat(lock.fileno()).st_ino == (root / ".lock").stat().st_ino, "retired lock; retry")
        return rollback_locked(receipt_file)


def rollback_locked(receipt_file):
    receipt_path = Path(receipt_file).absolute()
    require(receipt_path.is_file() and not receipt_path.is_symlink(), "missing/unsafe install receipt")
    receipt = json.loads(receipt_path.read_bytes())
    target = Path(receipt["target"]).resolve()
    require(receipt_path.resolve() == target / ".director/install.json", "receipt does not belong to target")
    require(receipt.get("format") == "director-flat-starter" and receipt.get("starter_version") == 2, "unknown rollback format")
    expected = receipt["managed"]
    safe = {"AGENTS.md", ".director/state.json", *(".director/" + x for x in manifest()["payload"])}
    require(set(expected) == safe, "unsafe receipt managed paths")
    actual = {".director/" + name: value for name, value in inventory(target / ".director").items()}
    require((target / "AGENTS.md").is_file() and not (target / "AGENTS.md").is_symlink(), "changed startup file")
    actual["AGENTS.md"] = sha((target / "AGENTS.md").read_bytes())
    actual.pop(".director/.lock", None)  # Harmless lock created by a readonly query.
    require(set(actual) == safe | {".director/install.json"}, "new managed-area work present; rollback preserves it")
    require(all(actual.get(name) == digest for name, digest in expected.items()), "changed files/state; rollback requires preservation review")
    # Remove state before retiring the locked inode. Runtime rejects stale lock handles.
    (target / ".director/state.json").unlink()
    for name in (safe | {".director/install.json", ".director/.lock"}) - {".director/state.json"}:
        (target / name).unlink(missing_ok=True)
    (target / ".director").rmdir()
    if receipt["target_created"] and not list(target.iterdir()):
        target.rmdir()
    return {"operation": "rollback", "changed": True, "target": str(target)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["plan", "install", "rollback"])
    parser.add_argument("--target", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--review-initiator", choices=["owner", "user"], default="owner")
    parser.add_argument("--review-when", choices=["closure", "explicit"], default="closure")
    parser.add_argument("--review-min-incidents", type=int, default=3, help="review batching budget, not evidence of a rule")
    args = parser.parse_args()
    try:
        require(bool(args.receipt) if args.mode == "rollback" else bool(args.target), "supply --receipt for rollback, otherwise --target")
        result = rollback(args.receipt) if args.mode == "rollback" else operation(args.mode, args.target, args.review_initiator, args.review_when, args.review_min_incidents)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error)[:1000]}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
