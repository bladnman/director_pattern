"""Independent contract checks through a freshly installed default.

No network or live project store is used. Optional DIRECTOR_PARITY_EVIDENCE keeps
installed fixtures and exact subprocess receipts for independent inspection.
These checks establish local data behavior, not host startup or human acceptance.
"""
import importlib.util
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path
import select
import subprocess
import sys
import tempfile
import time
import unittest


ROOT = Path(__file__).resolve().parents[2]
STARTER = ROOT / "pattern/starter"


class InstalledBehaviorParity(unittest.TestCase):
    def setUp(self):
        evidence = os.environ.get("DIRECTOR_PARITY_EVIDENCE")
        if evidence:
            destination = Path(evidence)
            destination.mkdir(parents=True, exist_ok=True)
            self.base = Path(tempfile.mkdtemp(prefix=self._testMethodName + "-", dir=destination))
        else:
            temporary = tempfile.TemporaryDirectory()
            self.addCleanup(temporary.cleanup)
            self.base = Path(temporary.name)
        self.project = self.base / "project"
        self.serial = 0
        self.run_process([sys.executable, str(STARTER / "install.py"), "install", "--target", str(self.project)])
        self.home = self.project / ".director"
        self.cli = self.home / "requests.py"

    def run_process(self, command, *, reject=False, decode=True):
        started_at, started = datetime.now(timezone.utc).isoformat(), time.perf_counter()
        result = subprocess.run(command, capture_output=True, text=True, cwd=ROOT)
        with (self.base / "calls.jsonl").open("a") as stream:
            stream.write(json.dumps({"command": command, "returncode": result.returncode,
                                     "stdout": result.stdout, "stderr": result.stderr,
                                     "started_at": started_at, "elapsed_seconds": time.perf_counter() - started}) + "\n")
        if reject:
            self.assertNotEqual(result.returncode, 0, result.stdout)
            return result
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout) if decode else result

    def git(self, *arguments, reject=False):
        return self.run_process(["git", "-c", "core.excludesFile=/dev/null", "-c", "core.hooksPath=/dev/null",
                                 "-c", "commit.gpgsign=false", "-c", "user.name=Disposable parity fixture",
                                 "-c", "user.email=parity@example.invalid", "-C", str(self.project),
                                 *map(str, arguments)], reject=reject, decode=False)

    def install_git_fixture(self, name, *, ignored=False, private=False):
        self.project = self.base / name
        self.project.mkdir()
        self.git("init", "-q")
        if ignored:
            (self.project / ".gitignore").write_bytes(b"# Explicit project privacy choice\n/.director/sources/\n/.director/requests/\n")
        self.git("remote", "add", "origin", "https://example.invalid/synthetic-repository.git")
        args = [sys.executable, str(STARTER / "install.py"), "install", "--target", str(self.project)]
        if private:
            args += ["--remote-visibility", "private"]
        self.run_process(args)
        self.home = self.project / ".director"
        self.cli = self.home / "requests.py"

    def command(self, *arguments, reject=False, error_contains=None):
        result = self.run_process([sys.executable, str(self.cli), *map(str, arguments)], reject=reject)
        if error_contains:
            self.assertIn(error_contains.lower(), result.stderr.lower())
        return result

    def identity(self):
        self.serial += 1
        return f"parity-{self.serial:032x}"

    def capture(self, raw=b"  Original obligation.\r\nKeep exact bytes.\r\n", attachment=None):
        event = self.identity()
        path = self.base / (event + ".txt")
        path.write_bytes(raw)
        args = ["capture", "--raw-file", path, "--event-id", event]
        if attachment:
            args += ["--attachment", attachment]
        return self.command(*args)["source_id"]

    def new(self, title="deliver complete outcome", source=None):
        return self.command("create", "--title", title, "--source-id", source or self.capture(), "--event-id", self.identity())

    def event(self, record, event_type, *, reject=False, error_contains=None, event=None, expected=None, **fields):
        value = event or dict(event_id=self.identity(), type=event_type, **fields)
        path = self.base / (self.identity() + ".json")
        path.write_text(json.dumps(value))
        return self.command("apply", record["id"], "--event-file", path,
                            "--expect-revision", record["revision"] if expected is None else expected,
                            reject=reject, error_contains=error_contains)

    def plan(self, record, owner="initial-owner", criteria=None, human=False):
        return self.event(record, "plan", owner=owner, acceptance=criteria or ["all original obligations"], human_gate={"required": human})

    def review(self, record):
        if record["state"] == "inbox":
            record = self.plan(record)
        record = self.event(record, "dispatch", receipt={"kind": "agent", "id": "fixture-worker"})
        return self.event(record, "submit", evidence=["artifact checked against criteria"])

    def accept(self, record, **fields):
        return self.event(record, "accept", director="fixture-owner", evidence=["independent outcome evaluation"], **fields)

    def bundle(self, record):
        return next((self.home / "requests").glob("*/" + record["id"]))

    def module(self, name):
        spec = importlib.util.spec_from_file_location("parity_" + name, self.home / (name + ".py"))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def test_default_installs_established_format_and_exact_backend(self):
        config = json.loads((self.home / "config.json").read_text())
        self.assertEqual(config["schema_version"], 1)
        self.assertEqual(config["request_store"]["schema_version"], 2)
        self.assertEqual(config["request_store"]["format"], "director-request-bundles")
        self.assertFalse((self.home / "state.json").exists())
        self.assertFalse((self.home / "state.py").exists())
        for name in ("request_store.py", "canonical_learning.py", "update_check.py"):
            self.assertEqual((self.home / name).read_bytes(), (STARTER / "payload" / name).read_bytes())
        self.assertEqual(self.command("validate"), {"valid": 0})

    def test_replanning_retains_initial_owner_criteria_source_and_latest_truth(self):
        original = self.capture()
        record = self.plan(self.new(source=original))
        addendum = self.capture(b"Add a second obligation.\r\n")
        record = self.event(record, "amend", source_id=addendum)
        record = self.plan(record, owner="authorized-replacement", criteria=["original plus second obligation"])
        shown = self.command("show", record["id"])
        initial = next(item for item in shown["history"] if item["type"] == "plan")
        self.assertEqual(initial["data"]["owner"], "initial-owner")
        self.assertEqual(initial["data"]["acceptance"], ["all original obligations"])
        self.assertEqual([s["source_id"] for s in shown["sources"]], [original, addendum])
        current = self.command("current", record["id"])["items"][0]
        self.assertNotIn("history", current)
        self.assertEqual(current["owner"], "authorized-replacement")
        self.assertEqual(current["acceptance"], ["original plus second obligation"])
        self.assertEqual((self.home / "sources" / original / "input.txt").read_bytes(), b"  Original obligation.\r\nKeep exact bytes.\r\n")

    def test_accepted_addendum_requires_reopen_and_is_visible_as_pending(self):
        done = self.accept(self.review(self.new()))
        unaffected = self.accept(self.review(self.new("unaffected accepted result")))
        source = self.capture(b"Correction to accepted result.\n")
        self.event(done, "amend", source_id=source, reject=True, error_contains="Invalid transition")
        reopened = self.event(done, "reopen", reason="new captured correction")
        reopened = self.event(reopened, "amend", source_id=source)
        pending = self.command("status")
        self.assertEqual([item["id"] for item in pending["items"]], [done["id"]])
        self.assertEqual(pending["items"][0]["current_liveness"], "unknown")
        self.assertEqual(self.command("show", unaffected["id"])["state"], "done")
        self.assertIn(source, json.dumps(self.command("current", reopened["id"])))

    def test_corrupt_earlier_source_cannot_hide_behind_good_addendum(self):
        original = self.capture()
        record = self.plan(self.new(source=original))
        record = self.event(record, "amend", source_id=self.capture(b"valid later source"))
        record = self.review(self.plan(record))
        (self.home / "sources" / original / "input.txt").write_bytes(b"tampered original")
        for arguments in (("show", record["id"]), ("current", record["id"]), ("status",), ("validate",)):
            self.command(*arguments, reject=True, error_contains="integrity")
        self.event(record, "accept", director="owner", evidence=["later good source alone is insufficient"], reject=True, error_contains="integrity")

    def test_submission_and_required_human_evidence_cannot_be_skipped(self):
        record = self.plan(self.new(), human=True)
        record = self.event(record, "dispatch", receipt={"kind": "agent", "id": "worker"})
        self.event(record, "accept", director="owner", evidence=["premature"], reject=True, error_contains="Invalid transition")
        self.event(record, "submit", evidence=[], reject=True, error_contains="evidence")
        record = self.event(record, "submit", evidence=["actual return"])
        self.event(record, "accept", director="owner", evidence=["reviewed"], reject=True, error_contains="human gate")
        self.assertEqual(self.command("show", record["id"])["revision"], record["revision"])
        done = self.accept(record, human_gate={"status": "passed", "evidence": ["explicit fixture human decision"]})
        self.assertEqual(done["state"], "done")

    def test_required_dependency_cycle_and_current_acceptance_gate(self):
        parent, child = self.new("parent"), self.new("child")
        project = json.loads((self.home / "config.json").read_text())["request_store"]["project_id"]
        target = lambda r: {"project_id": project, "request_id": r["id"]}
        parent = self.event(parent, "link", link_id="required", kind="depends_on", target=target(child))
        self.event(child, "link", link_id="cycle", kind="depends_on", target=target(parent), reject=True, error_contains="cycle")
        parent = self.review(parent)
        self.event(parent, "accept", director="owner", evidence=["child not delivered"], reject=True)
        child = self.accept(self.review(child))
        child = self.event(child, "reopen", reason="child acceptance withdrawn")
        self.event(parent, "accept", director="owner", evidence=["stale child success"], reject=True)
        child = self.event(child, "cancel", reason="delivery currently impossible")
        self.event(parent, "accept", director="owner", evidence=["cancellation is not delivery"], reject=True)
        child = self.event(child, "reopen", reason="delivery possible again")
        child = self.accept(self.review(child))
        self.assertEqual(self.accept(parent)["state"], "done")

    def test_external_send_ack_return_and_local_evaluation_are_distinct(self):
        remote = self.base / "remote-native.json"
        remote.write_bytes(b'{"native":"untouched"}\n')
        record = self.plan(self.new())
        record = self.event(record, "handoff_propose", handoff_id="external", target={"project_id": "native", "locator": str(remote)}, outcome="deliver external result", required=True, return_route="authorized return", constraints="no publication", content="exact scope", acceptance=["external result verified"])
        record = self.event(record, "handoff_request", handoff_id="external", receipt="synthetic authorized-send receipt")
        self.assertEqual(record["state"], "queued")
        record = self.event(record, "handoff_acknowledge", handoff_id="external", receipt="synthetic receiver ack", owner="remote owner", target={"project_id": "native", "request_id": "APP-1"})
        self.assertEqual(record["state"], "blocked")
        record = self.event(record, "handoff_return", handoff_id="external", receipt="synthetic artifact receipt", evidence=["returned artifact"])
        self.assertEqual(record["state"], "blocked")
        record = self.review(self.event(record, "resume", reason="evaluate return"))
        self.event(record, "accept", director="owner", evidence=["not yet evaluated external result"], reject=True)
        record = self.event(record, "handoff_accept", handoff_id="external", director="owner", evidence=["external artifact evaluated"])
        self.assertEqual(self.accept(record)["state"], "done")
        self.assertEqual(remote.read_bytes(), b'{"native":"untouched"}\n')

    def test_source_attachment_hash_is_checked_after_restart(self):
        asset = self.base / "original.bin"
        asset.write_bytes(b"\x00\xff exact source attachment\r\n")
        source = self.capture(attachment=asset)
        record = self.new(source=source)
        captured = self.home / "sources" / source / "attachments" / asset.name
        self.assertEqual(captured.read_bytes(), asset.read_bytes())
        captured.write_bytes(b"altered attachment")
        self.command("show", record["id"], reject=True, error_contains="integrity")
        self.command("validate", reject=True, error_contains="integrity")

    def test_request_attachment_moves_with_bundle_and_hash_is_checked(self):
        record = self.new()
        asset = self.base / "local.bin"
        asset.write_bytes(b"\x00 local evidence\r\n")
        record = self.command("attach", record["id"], "--file", asset, "--kind", "evidence", "--event-id", self.identity(), "--expect-revision", record["revision"])
        done = self.accept(self.review(record))
        captured = self.bundle(done) / done["files"][0]["path"]
        self.assertEqual(captured.read_bytes(), asset.read_bytes())
        self.assertEqual(self.bundle(done).parent.name, "archive")
        captured.write_bytes(b"changed")
        self.command("show", done["id"], reject=True, error_contains="integrity")

    def test_exact_replay_stale_revision_and_changed_event_are_distinct(self):
        initial = self.new()
        event = dict(event_id=self.identity(), type="plan", owner="worker", acceptance=["complete"], human_gate={"required": False})
        planned = self.event(initial, "plan", event=event)
        self.assertEqual(self.event(initial, "plan", event=event), planned)
        self.event(initial, "note", text="new stale mutation", reject=True, error_contains="Stale revision")
        self.event(planned, "plan", event={**event, "owner": "different"}, reject=True)
        self.assertEqual(self.command("show", initial["id"]), planned)

    def test_interrupted_installed_backend_requires_explicit_recovery(self):
        record = self.plan(self.new())
        event = dict(event_id=self.identity(), type="dispatch", receipt={"kind": "agent", "id": "actual-fixture-handle"})
        # The installed backend is imported solely to inject an actual journal
        # interruption; all reads/recovery/replay still use the installed CLI.
        backend = self.module("request_store")
        store = backend.Store(self.home)
        def interrupt(point):
            if point == "files":
                raise RuntimeError("controlled interruption")
        store.fault = interrupt
        with self.assertRaisesRegex(RuntimeError, "controlled interruption"):
            store.apply(record["id"], event, record["revision"])
        self.assertTrue((self.home / ".request-txn").exists())
        self.command("current", record["id"], reject=True, error_contains="recover")
        self.command("validate", reject=True, error_contains="recover")
        self.command("recover")
        recovered = self.command("show", record["id"])
        self.assertEqual(recovered["state"], "active")
        self.assertEqual(recovered["revision"], record["revision"] + 1)
        self.assertEqual(self.event(record, "dispatch", event=event), recovered)
        self.assertEqual(self.command("validate"), {"valid": 1})

    def test_bounded_status_snapshot_rejects_mixed_revision_pages(self):
        for i in range(3):
            self.new("outcome " + str(i))
        first = self.command("status", "--limit", 1, "--max-bytes", 1024)
        self.assertEqual(first["total"], 3)
        self.assertEqual(first["next_offset"], 1)
        self.assertLessEqual(len(json.dumps(first, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()) + 1, 1024)
        second = self.command("status", "--offset", 1, "--limit", 1, "--at-snapshot", first["snapshot"])
        self.assertNotEqual(first["items"][0]["id"], second["items"][0]["id"])
        self.new("newly captured obligation")
        self.command("status", "--offset", 2, "--at-snapshot", first["snapshot"], reject=True, error_contains="snapshot changed")

    def test_installed_updater_failure_window_preferences_and_manifest_receipt(self):
        updater = self.module("update_check")
        receipt = self.home / "install.json"
        value = json.loads(receipt.read_text())
        manifest = json.loads((STARTER / "manifest.json").read_text())
        self.assertTrue({".director/" + p for p in manifest["payload"]}.issubset(value["managed_files"]))
        # Synthetic published provenance enables a deterministic metadata test;
        # the real candidate receipt is never modified or promoted to published.
        value["source"] = {"url": updater.SOURCE, "sha": "a" * 40, "published": True}
        pointer = self.home / "fixture-published.json"
        pointer.write_text(json.dumps(value))
        calls = []
        def offline(route):
            calls.append(route)
            raise OSError("controlled offline")
        before = receipt.read_bytes()
        run = lambda now, fetch: updater.check(self.home, ".director/fixture-published.json", now=now, fetch=fetch)
        self.assertEqual(run(100000, offline)["status"], "error")
        updater.set_policy(self.home, "automatic", "synthetic explicit user authorization", now=100001)
        self.assertEqual(run(100002, offline)["status"], "throttled")
        self.assertEqual(run(100000 + updater.DAY - 1, offline)["status"], "throttled")
        self.assertEqual(len(calls), 1)
        self.assertEqual(run(100000 + updater.DAY, offline)["status"], "error")
        updater.set_policy(self.home, "off", "synthetic stop instruction")
        self.assertEqual(run(100000 + 2 * updater.DAY, offline)["status"], "off")
        self.assertEqual(len(calls), 2)
        updater.set_policy(self.home, "notify", "synthetic notification instruction")
        def same(route):
            calls.append(route)
            if route == "/git/ref/heads/main":
                return {"object": {"sha": "a" * 40}}
            return {"tree": [{"path": "pattern", "type": "tree", "sha": "b" * 40}]}
        self.assertEqual(run(100000 + 2 * updater.DAY, same)["status"], "current")
        self.assertEqual(receipt.read_bytes(), before)
        self.assertEqual(self.command("validate"), {"valid": 0})

    def test_trackable_default_survives_local_clone_without_auto_staging(self):
        self.install_git_fixture("shareable")
        asset = self.base / "portable.bin"
        asset.write_bytes(b"\x00 exact portable attachment\r\n")
        source = self.capture(attachment=asset)
        record = self.plan(self.new(source=source))
        config = (self.home / "config.json").read_bytes()
        receipt = json.loads((self.home / "install.json").read_text())
        awareness = receipt["version_control"]
        self.assertEqual(awareness["visibility"], "unknown")
        self.assertTrue(awareness["warning"])
        self.assertIn("relay once", awareness["awareness"])
        for path in ("config.json", "install.json", f"sources/{source}/input.txt",
                     f"sources/{source}/attachments/{asset.name}",
                     str((self.bundle(record) / "request.md").relative_to(self.home))):
            self.git("check-ignore", "--no-index", ".director/" + path, reject=True)
        self.assertEqual(self.git("ls-files").stdout, "", "installation/capture must never stage user sources")
        for path in (".requests.lock", ".request-txn", "backups/example", ".update-check.json"):
            self.git("check-ignore", "--no-index", ".director/" + path)
        self.git("add", "--all")  # Explicit harness authorization, never installer behavior.
        staged = self.git("ls-files").stdout.splitlines()
        self.assertIn(".director/config.json", staged)
        self.assertIn(f".director/sources/{source}/input.txt", staged)
        self.assertNotIn(".director/.requests.lock", staged)
        self.git("commit", "-q", "-m", "Disposable continuity fixture")
        clone = self.base / "local-clone"
        self.git("clone", "-q", "--no-hardlinks", str(self.project), str(clone))
        self.project, self.home = clone, clone / ".director"
        self.cli = self.home / "requests.py"
        self.assertEqual((self.home / "config.json").read_bytes(), config)
        self.assertEqual(self.command("show", record["id"]), record)
        self.assertEqual((self.home / "sources" / source / "attachments" / asset.name).read_bytes(), asset.read_bytes())
        self.assertEqual(json.loads((self.home / "install.json").read_text())["version_control"], awareness)
        self.command("recover")
        self.assertEqual(self.command("validate"), {"valid": 1})
        continued = self.new("continuation on cloned checkout")
        self.assertEqual(continued["project_id"], record["project_id"])
        self.assertNotEqual(continued["id"], record["id"])
        self.assertEqual(self.command("validate"), {"valid": 2})

    def test_existing_explicit_private_ignore_is_preserved(self):
        self.install_git_fixture("private-choice", ignored=True, private=True)
        expected = b"# Explicit project privacy choice\n/.director/sources/\n/.director/requests/\n"
        self.assertEqual((self.project / ".gitignore").read_bytes(), expected)
        record = self.new()
        source = record["sources"][0]["source_id"]
        self.git("check-ignore", "--no-index", f".director/sources/{source}/input.txt")
        self.git("check-ignore", "--no-index", str((self.bundle(record) / "request.md").relative_to(self.project)))
        receipt = json.loads((self.home / "install.json").read_text())
        self.assertEqual(receipt["version_control"]["visibility"], "private")
        self.assertFalse(receipt["version_control"]["warning"])
        before = (self.home / "install.json").read_bytes()
        again = self.run_process([sys.executable, str(STARTER / "install.py"), "install", "--target", str(self.project), "--remote-visibility", "private"])
        self.assertFalse(again["changed"])
        self.assertEqual((self.project / ".gitignore").read_bytes(), expected)
        self.assertEqual((self.home / "install.json").read_bytes(), before)
        self.assertEqual(self.git("ls-files").stdout, "")

    def test_fresh_reinstall_at_same_path_allocates_new_identity_but_noop_preserves(self):
        first = (self.home / "config.json").read_bytes()
        self.run_process([sys.executable, str(STARTER / "install.py"), "install", "--target", str(self.project)])
        self.assertEqual((self.home / "config.json").read_bytes(), first)
        self.run_process([sys.executable, str(STARTER / "install.py"), "rollback", "--receipt", str(self.home / "install.json")])
        self.run_process([sys.executable, str(STARTER / "install.py"), "install", "--target", str(self.project)])
        old = json.loads(first)["request_store"]["project_id"]
        new = json.loads((self.home / "config.json").read_bytes())["request_store"]["project_id"]
        self.assertRegex(new, r"^PROJ-[a-f0-9]{32}$")
        self.assertNotEqual(old, new, "a filesystem path is not a unique project identity")

    def test_old_lock_descriptor_cannot_write_into_reinstalled_project(self):
        ready_read, ready_write = os.pipe()
        release_read, release_write = os.pipe()
        # A real process opens the old inode, then the harness controls its
        # pre-flock wait. This is a deterministic race probe, not natural timing.
        script = '''
import importlib.util,json,os,pathlib,sys
sys.dont_write_bytecode=True
home=pathlib.Path(sys.argv[1]); ready=int(sys.argv[2]); release=int(sys.argv[3])
spec=importlib.util.spec_from_file_location("installed_backend",home/"request_store.py")
backend=importlib.util.module_from_spec(spec);spec.loader.exec_module(backend)
store=backend.Store(home); real_flock=backend.fcntl.flock
def held_flock(stream,operation):
    os.write(ready,(json.dumps({"inode":os.fstat(stream.fileno()).st_ino,"project_id":store.project_id})+"\\n").encode())
    os.read(release,1)
    return real_flock(stream,operation)
backend.fcntl.flock=held_flock
try:
    store.capture("STALE WRITER MUST NOT SURVIVE", "parity-ffffffffffffffffffffffffffffffff")
except ValueError as error:
    print(json.dumps({"rejected":str(error)}))
else:
    print(json.dumps({"unexpected_write":True}));sys.exit(3)
'''
        child = subprocess.Popen([sys.executable, "-c", script, str(self.home), str(ready_write), str(release_read)],
                                 pass_fds=(ready_write, release_read), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        os.close(ready_write)
        os.close(release_read)
        try:
            self.assertTrue(select.select([ready_read], [], [], 10)[0], "writer did not reach opened-inode checkpoint")
            checkpoint = json.loads(os.read(ready_read, 4096))
            self.run_process([sys.executable, str(STARTER / "install.py"), "rollback", "--receipt", str(self.home / "install.json")])
            self.run_process([sys.executable, str(STARTER / "install.py"), "install", "--target", str(self.project)])
            fresh = self.new("fresh project work must survive stale writer")
            self.assertNotEqual(fresh["project_id"], checkpoint["project_id"])
            self.assertNotEqual((self.home / ".requests.lock").stat().st_ino, checkpoint["inode"])
            before = {str(p.relative_to(self.project)): p.read_bytes() for p in self.project.rglob("*") if p.is_file()}
            os.write(release_write, b"x")
            stdout, stderr = child.communicate(timeout=10)
            (self.base / "stale-writer.json").write_text(json.dumps({"checkpoint": checkpoint, "returncode": child.returncode,
                                                                   "stdout": stdout, "stderr": stderr}, indent=2))
            self.assertEqual(child.returncode, 0, stderr)
            self.assertIn("Retired writer lock", json.loads(stdout)["rejected"])
            after = {str(p.relative_to(self.project)): p.read_bytes() for p in self.project.rglob("*") if p.is_file()}
            self.assertEqual(before, after)
            self.assertEqual(self.command("show", fresh["id"]), fresh)
            self.assertEqual(self.command("validate"), {"valid": 1})
        finally:
            if child.poll() is None:
                child.kill()
                child.communicate()
            os.close(ready_read)
            os.close(release_write)

    def test_learning_types_preserve_proposals_without_promoting_organization_changes(self):
        scope = {"tasks": ["customer-deck"], "paths": ["decks/customer"], "audiences": ["customers"]}

        def learning(action, data, reject=False):
            path = self.base / (self.identity() + ".json")
            path.write_text(json.dumps(data))
            return self.run_process([sys.executable, str(self.home / "canonical_learning.py"), action,
                                     "--data-file", str(path)], reject=reject)

        def entry(record, kind, **fields):
            source = record["sources"][0]["source_id"]
            return {"schema": 1, "id": self.identity(), "kind": kind, "source_id": source,
                    "source_sha256": hashlib.sha256((self.home / "sources" / source / "input.txt").read_bytes()).hexdigest(),
                    "request_revision": record["revision"], "scope": scope, "owner": "fixture-owner",
                    "text": "Synthetic scoped proposal; implementation and authority remain separate", **fields}

        def append(record, item, reject=False):
            return learning("append", {"request_id": record["id"], "expected_revision": record["revision"],
                                       "entry": item}, reject=reject)

        records = [self.new("learning evidence " + str(i)) for i in range(3)]
        for record in records:
            append(record, entry(record, "incident", hypothesis=False))
        pending = learning("pending", {})
        self.assertEqual(pending["total"], 3)
        record = self.command("show", records[-1]["id"])
        review = entry(record, "review", incidents=[{"id": i["id"], "digest": i["digest"]} for i in pending["items"]],
                       proposals=[], spend={"tokens": "unknown", "cost": "unknown"})
        for kind in ("knowledge", "routing", "structure"):
            review["proposals"].append({"id": review["id"] + "/" + kind, "kind": kind,
                                        "text": kind + " proposal only", "scope": scope, "hypothesis": False})
        append(record, review)
        self.assertTrue(append(record, review)["idempotent"], "cross-request review retry must not consume twice")
        self.assertEqual(learning("pending", {})["total"], 0)
        record = self.command("show", record["id"])
        broadened = entry(record, "decision", proposal_id=review["proposals"][0]["id"], decision="accept",
                          scope={**scope, "audiences": ["*"]})
        self.assertIn("scope", append(record, broadened, reject=True).stderr)
        for proposal in review["proposals"]:
            decision = entry(record, "decision", proposal_id=proposal["id"], decision="accept")
            receipt = append(record, decision)
            self.assertEqual(receipt["proposal_kind"], proposal["kind"])
            self.assertFalse(receipt["classification_required"])
            self.assertEqual(receipt["implementation_required"], proposal["kind"] != "knowledge")
            record = self.command("show", record["id"])
        query = {"task": "customer-deck", "path": "decks/customer/new.html", "audience": "customers"}
        knowledge = review["id"] + "/knowledge"
        self.assertEqual([i["id"] for i in learning("select", query)["items"]], [knowledge])
        self.assertEqual([i["id"] for i in learning("selectors", {})["items"]], [knowledge])
        proposals = learning("proposals", {"include_decided": True})["items"]
        self.assertEqual({i["proposal_kind"] for i in proposals}, {"knowledge", "routing", "structure"})
        history_before_retirement = record["history"]
        for kind in ("routing", "structure"):
            ident = review["id"] + "/" + kind
            append(record, entry(record, "retire", knowledge_id=ident))
            record = self.command("show", record["id"])
            retired = next(i for i in learning("proposals", {"include_decided": True})["items"] if i["id"] == ident)
            self.assertEqual(retired["proposal_kind"], kind)
            self.assertFalse(retired["implementation_required"], "retired proposals must not report current pending implementation")
            historical_acceptance = next(i for i in learning("decisions", {})["items"] if i["proposal_id"] == ident)
            self.assertTrue(historical_acceptance["implementation_required"], "historical acceptance retains its original meaning")
        self.assertEqual(record["history"][:len(history_before_retirement)], history_before_retirement)
        self.assertEqual([i["id"] for i in learning("select", query)["items"]], [knowledge])
        self.assertEqual([i["id"] for i in learning("selectors", {})["items"]], [knowledge])

        # Existing pre-typing canonical notes retain their exact native wire
        # bytes. Inject them through the installed bundle CLI, as old writers
        # did; do not ask the new adapter to invent a classification.
        legacy = self.new("legacy unclassified proposal")
        append(legacy, entry(legacy, "incident", hypothesis=False))
        legacy = self.command("show", legacy["id"])
        old_pending = learning("pending", {})
        old_review = entry(legacy, "review", incidents=[{"id": i["id"], "digest": i["digest"]} for i in old_pending["items"]],
                           proposals=[], spend={"tokens": "unknown", "cost": "unknown"})
        old_id = old_review["id"] + "/legacy"
        old_review["proposals"] = [{"id": old_id, "text": "Historical structure proposal, type was not stored",
                                    "scope": scope, "hypothesis": False}]
        self.assertIn("kind", append(legacy, old_review, reject=True).stderr)

        def historical_note(record, item):
            return self.event(record, "note", event={"event_id": item["id"], "type": "note",
                              "text": "DIRECTOR_LEARNING_V1 " + json.dumps(item, ensure_ascii=False, sort_keys=True,
                                                                           separators=(",", ":")),
                              "evidence": [], "artifacts": []})

        old_review_anchor = legacy
        legacy = historical_note(legacy, old_review)
        old_decision = entry(legacy, "decision", proposal_id=old_id, decision="accept")
        self.assertIn("classif", append(legacy, old_decision, reject=True).stderr.lower())
        old_decision_anchor = legacy
        legacy = historical_note(legacy, old_decision)
        before = self.bundle(legacy).joinpath("request.md").read_bytes()
        self.assertTrue(append(old_review_anchor, old_review)["idempotent"])
        self.assertTrue(append(old_decision_anchor, old_decision)["idempotent"])
        retained = next(i for i in learning("proposals", {"include_decided": True})["items"] if i["id"] == old_id)
        self.assertEqual(retained["proposal_kind"], "unclassified")
        self.assertTrue(retained["classification_required"])
        self.assertTrue(retained["implementation_required"])
        old_acceptance = next(i for i in learning("decisions", {})["items"] if i["proposal_id"] == old_id)
        self.assertEqual(old_acceptance["proposal_kind"], "unclassified")
        self.assertTrue(old_acceptance["classification_required"])
        self.assertTrue(old_acceptance["implementation_required"])
        self.assertEqual([i["id"] for i in learning("select", query)["items"]], [knowledge])
        self.assertEqual([i["id"] for i in learning("selectors", {})["items"]], [knowledge])
        self.assertEqual(self.bundle(legacy).joinpath("request.md").read_bytes(), before)
        self.assertFalse((self.project / "roles").exists())
        self.assertEqual(self.command("validate"), {"valid": 4})


if __name__ == "__main__":
    unittest.main()
