import contextlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[2] / "pattern" / "tools"

def load(name):
    spec = importlib.util.spec_from_file_location(name, TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

requests = load("requests")

class RecorderTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.team = Path(self.temp.name) / ".team"
        self.team.mkdir()
        (self.team / "config.json").write_text(json.dumps({"schema_version": 1, "record_mode": "tracked"}))
        requests.Store.init(self.team)
        self.store = requests.Store(self.team)
        self.r = self.store.create("  Original request\r\n\n", "Example", "create-example")

    def apply(self, event_type, **data):
        e = dict(event_id=f"event-{self.r['revision']}", type=event_type, **data)
        self.r = self.store.apply(self.r["id"], e, self.r["revision"])
        return self.r

    def plan(self, required=False):
        return self.apply("plan", owner="worker-a", acceptance=["Useful outcome"], human_gate={"required": required})

    def active(self, required=False):
        self.plan(required)
        return self.apply("dispatch", receipt={"kind": "direct", "id": "director-session-1"})

    def test_raw_is_verbatim_and_amend_invalidates_plan(self):
        self.plan()
        self.apply("amend", raw_text="\tAddendum\r\n")
        self.assertEqual([(self.store.sources / r["source_id"] / "input.txt").read_bytes().decode("utf-8") for r in self.r["sources"]], ["  Original request\r\n\n", "\tAddendum\r\n"])
        with self.assertRaisesRegex(ValueError, "acceptance"):
            self.apply("dispatch", receipt={"kind": "direct", "id": "a"})

    def test_lifecycle_and_human_gate(self):
        with self.assertRaises(ValueError):
            self.apply("dispatch", receipt={"kind": "direct", "id": "a"})
        self.active(required=True)
        with self.assertRaises(ValueError):
            self.apply("amend", raw_text="new scope")
        with self.assertRaises(ValueError):
            self.apply("submit", evidence=[])
        self.apply("submit", evidence=["checks/output.txt"], artifacts=["result.txt"])
        with self.assertRaises(ValueError):
            self.apply("accept", director="director", evidence=["Reviewed result"], human_gate={"required": False})
        self.apply("accept", director="director", evidence=["Reviewed result"], human_gate={"status": "passed", "evidence": ["User approved preview"]})
        self.assertEqual(self.r["state"], "done")
        self.apply("reopen", reason="Acceptance criteria changed")
        self.assertEqual(self.r["state"], "queued")
        self.assertIsNone(self.r["director_acceptance"])
        self.assertIsNone(self.r["execution_receipt"])
        self.assertEqual(self.r["human_gate"]["status"], "pending")

    def test_review_revision_and_runner_recovery(self):
        self.active()
        self.apply("block", reason="Runner disappeared")
        self.apply("resume", reason="Re-dispatch needed")
        self.assertEqual(self.r["state"], "queued")
        self.assertIsNone(self.r["execution_receipt"])
        self.apply("dispatch", receipt={"kind": "agent", "id": "new-agent"})
        self.apply("submit", evidence=["Draft verified"])
        self.apply("revise", reason="Missing one criterion")
        self.assertEqual(self.r["state"], "queued")
        self.assertIsNone(self.r["execution_receipt"])
        self.apply("cancel", reason="No longer needed")
        self.assertEqual(self.r["state"], "canceled")

    def test_retry_and_stale_revision(self):
        event = {"event_id": "unique", "type": "note", "text": "Evidence"}
        self.r = self.store.apply(self.r["id"], event, 1)
        self.assertEqual(self.store.apply(self.r["id"], event, 1), self.r)
        with self.assertRaisesRegex(ValueError, "different payload"):
            self.store.apply(self.r["id"], dict(event, text="Changed"), 2)
        with self.assertRaisesRegex(ValueError, "Stale revision"):
            self.store.apply(self.r["id"], dict(event, event_id="new"), 1)
        self.assertEqual(self.store.create("  Original request\r\n\n", "Example", "create-example"), self.r)
        with self.assertRaisesRegex(ValueError, "different payload"):
            self.store.create("Changed original", "Example", "create-example")

    def command(self, *args):
        return [sys.executable, str(TOOLS / "requests.py"), "--team", str(self.team), *args]

    def test_cli_raw_and_concurrent_creates_and_updates(self):
        raw = Path(self.temp.name) / "raw.txt"
        raw.write_bytes(b"  Exact\r\n\r\n")
        jobs = [subprocess.Popen(self.command("create", "--raw-file", str(raw), "--title", "Concurrent", "--event-id", f"parallel-{n // 2}"), stdout=subprocess.PIPE, stderr=subprocess.PIPE) for n in range(8)]
        results = []
        for job in jobs:
            out, err = job.communicate(timeout=15)
            self.assertEqual(job.returncode, 0, err)
            results.append(json.loads(out))
        self.assertEqual(len({r["id"] for r in results}), 4)
        self.assertTrue(all((self.store.sources / r["sources"][0]["source_id"] / "input.txt").read_bytes() == b"  Exact\r\n\r\n" for r in results))
        jobs = []
        for n in range(6):
            event = Path(self.temp.name) / f"event-{n}.json"
            event.write_text(json.dumps({"event_id": f"concurrent-{n}", "type": "note", "text": "update"}))
            jobs.append(subprocess.Popen(self.command("apply", self.r["id"], "--event-file", str(event), "--expect-revision", "1"), stdout=subprocess.PIPE, stderr=subprocess.PIPE))
        outcomes = [job.communicate(timeout=15) for job in jobs]
        self.assertEqual(sum(job.returncode == 0 for job in jobs), 1)
        self.assertEqual(sum(b"Stale revision" in err for _, err in outcomes), 5)
        self.assertEqual(self.store.read(self.r["id"])["revision"], 2)
        self.assertEqual(len(self.store.records()), 5)

    def test_director_layout_cli_defaults_to_director_store(self):
        root = Path(self.temp.name) / ".director"
        (root / "tools").mkdir(parents=True)
        (root / "config.json").write_text(json.dumps({"schema_version": 1, "record_mode": "tracked"}))
        script = root / "tools/requests.py"
        script.write_bytes((TOOLS / "requests.py").read_bytes())
        raw = Path(self.temp.name) / "exact.txt"
        raw.write_bytes(b"  Director layout\r\n")
        cmd = [sys.executable, str(script)]
        subprocess.run(cmd + ["init"], capture_output=True, check=True)
        created = subprocess.run(cmd + ["create", "--raw-file", str(raw), "--title", "Director layout", "--event-id", "director-layout-create"], capture_output=True, check=True)
        record = json.loads(created.stdout)
        request_id = record["id"]
        self.assertEqual((root / "sources" / record["sources"][0]["source_id"] / "input.txt").read_bytes(), b"  Director layout\r\n")
        events = [
            {"event_id": "director-layout-plan", "type": "plan", "owner": "worker-layout", "acceptance": ["Worker result verified"], "human_gate": {"required": False}},
            {"event_id": "director-layout-dispatch", "type": "dispatch", "receipt": {"kind": "agent", "id": "worker-layout-1"}},
            {"event_id": "director-layout-submit", "type": "submit", "evidence": ["Worker verification complete"]},
            {"event_id": "director-layout-accept", "type": "accept", "director": "director", "evidence": ["Director evaluated worker result"]},
        ]
        revision = record["revision"]
        for index, event in enumerate(events):
            event_file = Path(self.temp.name) / f"director-event-{index}.json"
            event_file.write_text(json.dumps(event))
            updated = subprocess.run(cmd + ["apply", request_id, "--event-file", str(event_file), "--expect-revision", str(revision)], capture_output=True, check=True)
            record = json.loads(updated.stdout)
            revision = record["revision"]
        shown = subprocess.run(cmd + ["show", request_id], capture_output=True, check=True)
        self.assertEqual(json.loads(shown.stdout)["state"], "done")
        validated = subprocess.run(cmd + ["validate"], capture_output=True, check=True)
        self.assertEqual(json.loads(validated.stdout), {"valid": 1})
        self.assertTrue((root / "requests/archive" / request_id / "request.md").is_file())
        self.assertEqual(len(list((root / "requests").glob("*/*/request.md"))), 1)

    def test_store_rejects_symlinks_and_path_escape(self):
        with self.assertRaises(ValueError):
            self.store.read("../outside")
        path = self.store.path(self.r["id"])
        outside = Path(self.temp.name) / "outside.json"
        path.rename(outside)
        path.symlink_to(outside)
        with self.assertRaises(ValueError):
            self.store.read(self.r["id"])

    def test_validate_detects_altered_raw_and_state(self):
        path = self.store.path(self.r["id"])
        original = path.read_bytes()
        record = requests.parse_markdown(original)
        record["sources"][0]["source_id"] = "UR-" + "a" * 32
        path.write_bytes(requests.markdown(record))
        with self.assertRaisesRegex(ValueError, "replayed history"):
            self.store.read(self.r["id"])
        record = requests.parse_markdown(original)
        record["state"] = "done"
        path.write_bytes(requests.markdown(record))
        with self.assertRaises(ValueError):
            self.store.read(self.r["id"])

    def test_validate_rejects_receipt_state_and_history_header_drift(self):
        self.active()
        path = self.store.path(self.r["id"])
        original = path.read_bytes()
        mutations = [
            lambda r: r.update(execution_receipt="invented receipt"),
            lambda r: r.update(state="canceled"),
            lambda r: r["history"][0].update(type="note"),
            lambda r: r["history"][0].update(event_id="replacement-id"),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(mutation=index):
                record = requests.parse_markdown(original)
                mutate(record)
                path.write_bytes(requests.markdown(record))
                with self.assertRaises(ValueError):
                    self.store.read(self.r["id"])


    def test_init_preserves_config_and_rejects_legacy_without_rewrite(self):
        root = Path(self.temp.name) / "legacy"
        root.mkdir()
        config = {"schema_version": 1, "record_mode": "tracked", "custom": {"retain": True}}
        (root / "config.json").write_text(json.dumps(config))
        (root / "requests").mkdir()
        old = root / "requests/REQ-old.json"
        old.write_bytes(b'{"legacy":"preserve"}\n')
        before = {p.name: p.read_bytes() for p in (root / "config.json", old)}
        with self.assertRaisesRegex(ValueError, "Legacy flat JSON"):
            requests.Store.init(root)
        self.assertEqual({p.name: p.read_bytes() for p in (root / "config.json", old)}, before)
        old.unlink()
        result = requests.Store.init(root)
        self.assertEqual(result["custom"], config["custom"])
        self.assertEqual(requests.Store.init(root), result)
        with self.assertRaisesRegex(ValueError, "cannot be replaced"):
            requests.Store.init(root, "PROJ-" + "a" * 32)

    def test_init_and_open_refuse_a_predecessor_store_without_writing(self):
        root = Path(self.temp.name) / "predecessor"
        (root / "requests/pending").mkdir(parents=True)
        config = {"schema_version": 1, "record_mode": "tracked", "request_store": {"schema_version": 2, "format": "request-bundles", "project_id": "PROJ-" + "b" * 32}}
        (root / "config.json").write_text(json.dumps(config))
        raw = root / "raw.txt"
        raw.write_text("Fixture only")
        before = {p: p.read_bytes() for p in root.rglob("*") if p.is_file() and p.name != ".requests.lock"}
        for attempt in (lambda: requests.Store.init(root), lambda: requests.Store(root), lambda: requests.Store(root).create(raw="x", title="New", event_id="c1")):
            with self.assertRaisesRegex(ValueError, "director-request-bundles store required"):
                attempt()
        self.assertEqual({p: p.read_bytes() for p in root.rglob("*") if p.is_file() and p.name != ".requests.lock"}, before)

    def test_immutable_source_capture_exact_attachments_and_retry(self):
        original = Path(self.temp.name) / "original.bin"
        original.write_bytes(b"\x00original\xff")
        source = self.store.capture("\t Whole original\r\n \n", "capture-attached", [original])
        source_id = source["source_id"]
        self.assertEqual(self.store.capture("\t Whole original\r\n \n", "capture-attached", [original]), source)
        self.assertEqual((self.store.sources / source_id / "input.txt").read_bytes(), b"\t Whole original\r\n \n")
        r = self.store.create(title="Shared", event_id="shared", source_id=source_id)
        self.assertEqual(r["sources"][0]["source_id"], source_id)
        self.assertNotIn("raw_requests", r)
        self.assertEqual(source["attachments"][0]["original_name"], original.name)
        original.write_bytes(b"Changed outside source")
        self.assertEqual((self.store.sources / source_id / "attachments/original.bin").read_bytes(), b"\x00original\xff")
        with self.assertRaisesRegex(ValueError, "different payload"):
            self.store.capture("\t Whole original\r\n \n", "capture-attached", [original])
        (self.store.sources / source_id / "input.txt").write_bytes(b"tampered")
        with self.assertRaisesRegex(ValueError, "integrity"):
            self.store.read(r["id"])

    def test_capture_rejects_duplicate_names_and_symlink_ancestors(self):
        originals = []
        for directory in ("first", "second"):
            root = Path(self.temp.name) / directory
            root.mkdir()
            file = root / "same.txt"
            file.write_bytes(b"same")
            originals.append(file)
        with self.assertRaisesRegex(ValueError, "Duplicate original"):
            self.store.capture("raw", "duplicate-files", originals)
        alias = Path(self.temp.name) / "alias"
        alias.symlink_to(originals[0].parent, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            self.store.capture("raw", "alias-source", [alias / "same.txt"])

    def test_assets_travel_and_tamper_is_detected(self):
        file = Path(self.temp.name) / "proof.txt"
        file.write_bytes(b"exact evidence\r\n")
        self.r = self.store.attach(self.r["id"], file, "evidence", "proof-copy", 1)
        receipt = self.r["files"][0]
        self.assertEqual(self.store.attach(self.r["id"], file, "evidence", "proof-copy", 1), self.r)
        self.active()
        working = self.store.path(self.r["id"]).parent
        self.assertEqual(working.parent.name, "working")
        self.assertEqual((working / receipt["path"]).read_bytes(), b"exact evidence\r\n")
        self.apply("submit", evidence=[receipt["path"]])
        self.apply("accept", director="director", evidence=["Reviewed local evidence"])
        archived = self.store.path(self.r["id"]).parent
        self.assertEqual(archived.parent.name, "archive")
        self.assertEqual((archived / receipt["path"]).read_bytes(), b"exact evidence\r\n")
        (archived / receipt["path"]).write_bytes(b"altered")
        with self.assertRaisesRegex(ValueError, "integrity"):
            self.store.read(self.r["id"])

    def test_recovery_all_move_fault_points_are_explicit_and_idempotent(self):
        for point in ("prepared", "files", "moved", "written"):
            with self.subTest(point=point):
                r = self.store.create("raw", point, "fault-create-" + point)
                plan = {"event_id": "plan-" + point, "type": "plan", "owner": "worker", "acceptance": ["done"], "human_gate": {"required": False}}
                r = self.store.apply(r["id"], plan, 1)
                event = {"event_id": "dispatch-" + point, "type": "dispatch", "receipt": {"kind": "agent", "id": "worker"}}
                self.store.fault = lambda observed, target=point: (_ for _ in ()).throw(RuntimeError("crash")) if observed == target else None
                with self.assertRaises(RuntimeError):
                    self.store.apply(r["id"], event, 2)
                reopened = requests.Store(self.team)
                with self.assertRaisesRegex(ValueError, "recover"):
                    reopened.records()
                reopened.recover()
                reopened.recover()
                self.assertEqual(reopened.read(r["id"])["state"], "active")
                self.assertEqual(reopened.apply(r["id"], event, 2)["revision"], 3)
                self.store = reopened

    def test_recovery_attachment_capture_and_source_capture_faults(self):
        file = Path(self.temp.name) / "return.txt"
        file.write_bytes(b"external result\r\n")
        for point in ("prepared", "files", "moved", "written"):
            with self.subTest(kind="request-file", point=point):
                before = self.store.read(self.r["id"])
                self.store.fault = lambda observed, target=point: (_ for _ in ()).throw(RuntimeError("crash")) if observed == target else None
                event_id = "attach-fault-" + point
                with self.assertRaises(RuntimeError):
                    self.store.attach(before["id"], file, "assets", event_id, before["revision"])
                self.store = requests.Store(self.team)
                self.store.recover()
                after = self.store.attach(before["id"], file, "assets", event_id, before["revision"])
                self.assertEqual(after["revision"], before["revision"] + 1)
                self.assertEqual(len([f for f in after["files"] if f["original_name"] == file.name]), len(after["files"]))
        for point in ("prepared", "written"):
            with self.subTest(kind="source", point=point):
                self.store.fault = lambda observed, target=point: (_ for _ in ()).throw(RuntimeError("crash")) if observed == target else None
                with self.assertRaises(RuntimeError):
                    self.store.capture("exact\r\n", "source-fault-" + point, [file])
                self.store = requests.Store(self.team)
                self.store.recover()
                source = self.store.capture("exact\r\n", "source-fault-" + point, [file])
                self.assertEqual((self.store.sources / source["source_id"] / "input.txt").read_bytes(), b"exact\r\n")

    def test_recovery_preserves_unexpected_record_collision(self):
        self.plan()
        before_path = self.store.path(self.r["id"])
        self.store.fault = lambda point: (_ for _ in ()).throw(RuntimeError("crash")) if point == "prepared" else None
        with self.assertRaises(RuntimeError):
            self.apply("dispatch", receipt={"kind": "agent", "id": "worker"})
        before_path.write_bytes(b"Unexpected user content; preserve me")
        reopened = requests.Store(self.team)
        with self.assertRaisesRegex(ValueError, "collision"):
            reopened.recover()
        self.assertEqual(before_path.read_bytes(), b"Unexpected user content; preserve me")
        self.assertTrue(reopened.transaction.exists())

    def test_duplicate_and_directory_mismatch_are_rejected(self):
        import shutil
        path = self.store.path(self.r["id"]).parent
        duplicate = self.team / "requests/archive" / self.r["id"]
        duplicate.parent.mkdir()
        shutil.copytree(path, duplicate)
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.store.records()
        shutil.rmtree(duplicate)
        path.rename(duplicate)
        with self.assertRaisesRegex(ValueError, "Directory/state mismatch"):
            self.store.read(self.r["id"])

    def test_derived_markdown_body_is_not_an_editable_shadow_record(self):
        path = self.store.path(self.r["id"])
        path.write_bytes(path.read_bytes() + b"\nmanual user Markdown\n")
        with self.assertRaisesRegex(ValueError, "derived rendering"):
            self.store.read(self.r["id"])

    def test_completion_depends_only_on_explicit_required_links(self):
        other = self.store.create("raw", "Independent", "independent")
        target = {"project_id": self.store.project_id, "request_id": other["id"]}
        self.apply("link", link_id="group", kind="group", target=target)
        reciprocal = {"event_id": "back", "type": "link", "link_id": "back", "kind": "related", "target": {"project_id": self.store.project_id, "request_id": self.r["id"]}}
        self.store.apply(other["id"], reciprocal, 1)
        self.active()
        self.apply("submit", evidence=["result"])
        self.apply("accept", director="director", evidence=["reviewed"])
        self.assertEqual(self.r["state"], "done")
        self.assertEqual(self.store.read(other["id"])["state"], "inbox")

    def test_local_cancel_preserves_external_receipt_without_waiting_status(self):
        self.plan()
        self.apply("handoff_propose", handoff_id="external-app", target={"project_id": "peer-project"},
                   outcome="Deliver app", required=True, return_route="authorized return route",
                   constraints="agreed scope", content="source and attachments delivered",
                   acceptance=["working app"])
        self.apply("handoff_request", handoff_id="external-app", receipt="actual request receipt")
        self.apply("handoff_acknowledge", handoff_id="external-app", receipt="actual acknowledgment",
                   owner="peer director", target={"project_id": "peer-project", "request_id": "APP-17"})
        self.assertEqual(self.r["state"], "blocked")
        self.apply("cancel", reason="Source commitment canceled; receiver status remains unverified")
        listed = subprocess.run(self.command("list"), capture_output=True, check=True)
        summary = next(r for r in json.loads(listed.stdout) if r["id"] == self.r["id"])
        self.assertEqual((summary["state"], summary["condition"]), ("canceled", "canceled"))
        reloaded = requests.Store(self.team).read(self.r["id"])
        self.assertEqual(reloaded["handoffs"][0]["status"], "acknowledged")
        self.assertEqual(reloaded["handoffs"][0]["acknowledgment"]["receipt"], "actual acknowledgment")
        self.assertEqual(reloaded["handoffs"][0]["current_liveness"], "unknown")
