#!/usr/bin/env python3
"""Install starter 3 beside ordinary project files. No network or implicit migration."""
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
import subprocess
import stat
import tempfile
import uuid

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
    require(value.get("format") == "director-flat-starter" and value.get("starter_version") == 3,
            "unknown starter manifest")
    names = value["payload"]
    require(isinstance(names, list) and len(names) == len(set(names)), "duplicate payload")
    for name in names:
        require(isinstance(name, str) and Path(name).name == name and name not in {".", ".."}, "unsafe payload path")
        require((SOURCE / "payload" / name).is_file() and not (SOURCE / "payload" / name).is_symlink(), "unsafe payload")
    return value


def runtime():
    spec = importlib.util.spec_from_file_location("flat_starter_runtime", SOURCE / "payload/request_store.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def files_for(target, initiator, opportunity, min_incidents=3, project_id=None):
    value = manifest()
    files = {".director/" + name: (SOURCE / "payload" / name).read_bytes() for name in value["payload"]}
    files["AGENTS.md"] = BRIDGE.encode()
    project_id = project_id or "PROJ-" + "0" * 32  # Plan placeholder only; never installed.
    config = {"schema_version": 1, "record_mode": "tracked", "request_store": {
        "schema_version": 2, "format": "director-request-bundles", "project_id": project_id}}
    files[".director/config.json"] = (json.dumps(config, indent=2, ensure_ascii=False) + "\n").encode()
    return value, files


def provenance(source_receipt=None):
    """Offline local evidence; an unverified transport is never called published."""
    if source_receipt is not None:
        transported = json.loads(Path(source_receipt).read_bytes())
        source = transported.get("source", {})
        expected = {name: sha((SOURCE / "payload" / name).read_bytes()) for name in manifest()["payload"]}
        require(transported.get("payload_sha256") == expected, "transport receipt does not match exact selected payload")
        require(source.get("url") == "https://github.com/bladnman/director_pattern" and isinstance(source.get("published"), bool), "invalid transport source")
        require(isinstance(source.get("sha"), str) and len(source["sha"]) == 40 and all(c in "0123456789abcdef" for c in source["sha"]), "transport needs full verified source SHA")
        return {**source, "evidence": "supplied verified transport receipt + exact payload hash comparison; caller attests publication evidence"}
    def git(*args):
        return subprocess.check_output(["git", "-C", str(SOURCE), *args], stderr=subprocess.DEVNULL).decode().strip()
    try:
        head = git("rev-parse", "HEAD")
        tree = git("rev-parse", "HEAD:pattern")
        remote = git("remote", "get-url", "origin").removesuffix(".git").rstrip("/")
        canonical = remote in {"https://github.com/bladnman/director_pattern", "git@github.com:bladnman/director_pattern"}
        head_published = canonical and subprocess.run(["git", "-C", str(SOURCE), "merge-base", "--is-ancestor", head, "refs/remotes/origin/main"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
        base = head if head_published else git("rev-parse", "refs/remotes/origin/main") if canonical else head
        published = canonical
        tree = git("rev-parse", base + ":pattern")
        dirty = head != base or bool(git("status", "--porcelain", "--", ":(top)pattern/"))
        return {"url": "https://github.com/bladnman/director_pattern", "sha": base, "checkout_sha": head,
                "published": published, "pattern_tree_sha": tree,
                "evidence": "local canonical origin/main ancestry; no install-time network",
                "local_delta": dirty}
    except (OSError, subprocess.CalledProcessError):
        return {"url": "https://github.com/bladnman/director_pattern", "published": False,
                "local_delta": "unknown", "evidence": "unverified transported source; active owner must resolve exact published baseline before safe update"}


def version_control(target, visibility):
    """Offline inspection. Visibility is supplied by actual host evidence, never guessed."""
    directory = target if target.exists() else target.parent
    while not directory.exists() and directory != directory.parent:
        directory = directory.parent
    try:
        subprocess.check_output(["git", "-C", str(directory), "rev-parse", "--show-toplevel"], stderr=subprocess.DEVNULL)
        remote = subprocess.check_output(["git", "-C", str(directory), "remote"], stderr=subprocess.DEVNULL).strip()
    except (OSError, subprocess.CalledProcessError):
        return {"available": False, "continuity": "not versioned; no cross-clone continuation/rollback by change; initialize only on user request", "warning": None}
    warning = "sources/ keeps exact messages and attachments; pushed public history stays readable after later deletion. Keep more local through project ignore rules if required." if remote and visibility != "private" else None
    return {"available": True, "remote": bool(remote), "visibility": visibility,
            "warning": warning, "awareness": "owner must relay once and record actual delivery before first source capture" if warning else "no public/unknown-remote warning due"}


def inventory(root):
    values = {}
    for path in root.rglob("*"):
        require(not path.is_symlink(), "symlink in managed installation")
        if path.is_file():
            values[path.relative_to(root).as_posix()] = sha(path.read_bytes())
    return values


def operation(mode, target, initiator="owner", opportunity="closure", min_incidents=3, source_receipt=None, remote_visibility="unknown"):
    require(fcntl is not None, "Starter helper needs POSIX fcntl (macOS/Linux); Windows runtime is not implemented")
    require(initiator in {"owner", "user"} and opportunity in {"closure", "explicit"} and type(min_incidents) is int and min_incidents > 0, "invalid review policy")
    require(remote_visibility in {"public", "private", "unknown"}, "invalid remote visibility")
    source_info = provenance(source_receipt)
    target = Path(target).absolute()
    require(not target.is_symlink(), "symlink target refused")
    target = target.resolve()
    value, files = files_for(target, initiator, opportunity, min_incidents)
    receipt_path = target / ".director/install.json"
    if receipt_path.exists():
        require(not receipt_path.is_symlink(), "unsafe receipt")
        receipt = json.loads(receipt_path.read_bytes())
        require(receipt.get("format") == value["format"] and receipt.get("starter_version") == 3,
                "existing installation is not this starter; migration requires review")
        require(receipt.get("manifest_sha256") == sha((SOURCE / "manifest.json").read_bytes()), "changed starter package; no implicit upgrade")
        static = {k: v for k, v in files.items() if k != ".director/config.json"}
        for name, data in static.items():
            path = target / name
            require(path.is_file() and not path.is_symlink() and path.read_bytes() == data,
                    "installed instruction drift; no implicit overwrite")
        current = runtime().Store(target / ".director")
        current.validate()
        return {"operation": mode, "changed": False, "status": "same starter; mutable state and optional roles preserved", "target": str(target)}
    require(not target.exists() or target.is_dir(), "target must be a project directory")
    conflicts = [name for name in GUARDS
                 if (target / name).exists() or (target / name).is_symlink()]
    require(not conflicts, "existing startup/tracker needs reviewed integration: " + ", ".join(conflicts))
    if mode != "plan":
        value, files = files_for(target, initiator, opportunity, min_incidents, "PROJ-" + uuid.uuid4().hex)
    report = {"operation": mode, "changed": True, "format": value["format"], "starter_version": 3,
              "target": str(target), "files": {p: {"sha256": sha(b), "bytes": len(b)} for p, b in files.items()},
              "payload_bytes": sum(len(b) for b in files.values()),
              "version_control": version_control(target, remote_visibility),
              "startup_bytes_director": sum(len(files[".director/" + p]) for p in ["START.md", "DIRECTOR.md"]) + len(files["AGENTS.md"]),
              "startup_bytes_worker": sum(len(files[".director/" + p]) for p in ["START.md", "WORKER.md"]) + len(files["AGENTS.md"])}
    if mode == "plan":
        report["files"][".director/config.json"]["sha256"] = None
        report["project_identity"] = "unallocated until first actual install; config bytes estimated with equal-length placeholder"
        return report
    target_created = not target.exists()
    target.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".director-starter-stage-", dir=target.parent))
    try:
        for name, data in files.items():
            path = stage / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            path.chmod(0o600 if name.endswith("config.json") else 0o644)
        receipt = {"format": value["format"], "starter_version": 3, "target": ".",
                   "target_created": target_created, "manifest_sha256": sha((SOURCE / "manifest.json").read_bytes()),
                   "managed": {name: sha(data) for name, data in files.items()},
                   "source": source_info,
                   "version_control": report["version_control"],
                   "technical_check": {"payload_hashes": "verified", "store": "validate required", "acceptance": "not implied", "native_startup": "unrun"},
                   "review_policy": {"initiator": initiator, "opportunity": opportunity,
                                     "min_incidents": min_incidents, "max_batch": 5, "max_bytes": 12000, "background": False}}
        runtime().Store(stage / ".director").validate()
        receipt["technical_check"]["store"] = "valid empty director-request-bundles"
        receipt["managed_files"] = dict(receipt["managed"])
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
    require(not (root / ".requests.lock").is_symlink(), "unsafe writer lock")
    with (root / ".requests.lock").open("a+b") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("store busy; rollback refused without changes") from None
        require(os.fstat(lock.fileno()).st_ino == (root / ".requests.lock").stat().st_ino, "retired lock; retry")
        return rollback_locked(receipt_file)


def rollback_locked(receipt_file):
    receipt_path = Path(receipt_file).absolute()
    require(receipt_path.is_file() and not receipt_path.is_symlink(), "missing/unsafe install receipt")
    receipt = json.loads(receipt_path.read_bytes())
    require(receipt.get("target") == ".", "unknown/nonportable target locator")
    target = receipt_path.parent.parent.resolve()
    require(receipt_path.resolve() == target / ".director/install.json", "receipt does not belong to target")
    require(receipt.get("format") == "director-flat-starter" and receipt.get("starter_version") == 3, "unknown rollback format")
    expected = receipt["managed"]
    safe = {"AGENTS.md", ".director/config.json", *(".director/" + x for x in manifest()["payload"])}
    require(set(expected) == safe, "unsafe receipt managed paths")
    actual = {".director/" + name: value for name, value in inventory(target / ".director").items()}
    require((target / "AGENTS.md").is_file() and not (target / "AGENTS.md").is_symlink(), "changed startup file")
    actual["AGENTS.md"] = sha((target / "AGENTS.md").read_bytes())
    actual.pop(".director/.requests.lock", None)  # Harmless lock created by a readonly query.
    require(set(actual) == safe | {".director/install.json"}, "new managed-area work present; rollback preserves it")
    require(all(actual.get(name) == digest for name, digest in expected.items()), "changed files/state; rollback requires preservation review")
    # Remove config before retiring the locked inode. Runtime rejects stale lock handles.
    (target / ".director/config.json").unlink()
    for name in (safe | {".director/install.json", ".director/.requests.lock"}) - {".director/config.json"}:
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
    parser.add_argument("--remote-visibility", choices=["public", "private", "unknown"], default="unknown", help="Actual host-verified visibility, optional; unknown is never inferred private")
    parser.add_argument("--source-receipt", type=Path, help="Optional verified transported source+exact payload hash receipt; no network")
    parser.add_argument("--review-initiator", choices=["owner", "user"], default="owner")
    parser.add_argument("--review-when", choices=["closure", "explicit"], default="closure")
    parser.add_argument("--review-min-incidents", type=int, default=3, help="review batching budget, not evidence of a rule")
    args = parser.parse_args()
    try:
        require(bool(args.receipt) if args.mode == "rollback" else bool(args.target), "supply --receipt for rollback, otherwise --target")
        result = rollback(args.receipt) if args.mode == "rollback" else operation(args.mode, args.target, args.review_initiator, args.review_when, args.review_min_incidents, args.source_receipt, args.remote_visibility)
        print(json.dumps(result, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error)[:1000]}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
