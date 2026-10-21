"""Independent outcome/recovery fixtures; all stores and external state are disposable."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[2] / "pattern/tools/requests.py"
spec = importlib.util.spec_from_file_location("bundle_scenario_requests", SCRIPT)
requests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(requests)


class InterruptedFixture(RuntimeError):
    pass


class BundleScenarioTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.home = self.root / "source-project"
        requests.Store.init(self.home)
        self.store = requests.Store(self.home)
        self.serial = 0
        self.raw = "  Make a folder, research, a repository, and an app.\r\nKeep all four.\r\n"
        self.source = None

    def new(self, title, store=None, source=None):
        store = store or self.store
        self.serial += 1
        if source is None:
            if self.source is None:
                self.source = self.store.capture(self.raw, "original-message")["source_id"]
            source = self.source
        return store.create(title=title, event_id=f"request-{self.serial}", source_id=source)

    def event(self, record, event_type, store=None, **fields):
        store = store or self.store
        self.serial += 1
        return store.apply(record["id"], dict(event_id=f"decision-{self.serial}", type=event_type, **fields), record["revision"])

    def plan(self, record, store=None):
        return self.event(record, "plan", store, owner="assigned-worker", acceptance=[f"Deliver {record['title']}"], human_gate={"required": False})

    def review(self, record, store=None):
        if record["state"] == "inbox":
            record = self.plan(record, store)
        record = self.event(record, "dispatch", store, receipt={"kind": "agent", "id": "disposable-worker-receipt"})
        return self.event(record, "submit", store, evidence=["Disposable returned result and check"])

    def finish(self, record, store=None):
        record = self.review(record, store)
        return self.event(record, "accept", store, director="source-director", evidence=["Reviewed agreed scope and returned evidence"])

    def local(self, record):
        return {"project_id": self.store.project_id, "request_id": record["id"]}

    def tree_bytes(self, root):
        return {str(path.relative_to(root)): path.read_bytes() for path in root.rglob("*") if path.is_file()}

    def test_four_asks_restart_preserves_source_assets_and_external_boundary(self):
        original = self.root / "specification.bin"
        original.write_bytes(b"\x00\xff exact specification\r\n")
        source = self.store.capture(self.raw, "four-ask-source", [original])["source_id"]
        source_dir = self.home / "sources" / source
        captured_bytes = self.tree_bytes(source_dir)
        outcomes = [self.new(title, source=source) for title in ("folder", "research", "repository", "app")]
        local_asset = self.root / "research-notes.txt"
        local_asset.write_bytes(b"Local research\r\nwith exact bytes\x00")
        outcomes[1] = self.store.attach(outcomes[1]["id"], local_asset, "assets", "research-asset", outcomes[1]["revision"])
        asset_path = outcomes[1]["files"][0]["path"]
        for index in range(3):
            outcomes[index] = self.finish(outcomes[index])
        self.assertEqual((self.store.path(outcomes[1]["id"]).parent / asset_path).read_bytes(), local_asset.read_bytes())
        self.assertEqual(self.store.path(outcomes[1]["id"]).parent.parent.name, "archive")

        remote = self.root / "native-app-project"
        remote.mkdir()
        (remote / "native-state.json").write_bytes(b'{"APP-17":{"status":"executing","children":["APP-18"]}}\n')
        before_remote = self.tree_bytes(remote)
        app = self.plan(outcomes[3])
        app = self.event(app, "handoff_propose", handoff_id="app-delivery", target={"project_id": "native-app-project", "locator": str(remote)}, outcome="Deliver app", required=True, return_route="authorized result location", constraints="Agreed app scope; no publication", content="Exact source and specification supplied", acceptance=["App satisfies agreed scope"])
        app = self.event(app, "handoff_request", handoff_id="app-delivery", receipt="Authorized send receipt")
        self.assertNotEqual(app["state"], "blocked", "Sending is not acknowledgment")
        app = self.event(app, "handoff_acknowledge", handoff_id="app-delivery", receipt="Receiver acknowledged APP-17", owner="native app director", target={"project_id": "native-app-project", "request_id": "APP-17", "locator": str(remote)})
        app = self.event(app, "observe", handoff_id="app-delivery", status="executing", evidence=["Dated authorized observation"], observed_at="2026-10-16T12:00:00Z")

        restarted = subprocess.run([sys.executable, str(SCRIPT), "--team", str(self.home), "list"], capture_output=True, text=True, check=True)
        listing = {item["id"]: item for item in json.loads(restarted.stdout)}
        self.assertEqual([listing[r["id"]]["state"] for r in outcomes[:3]], ["done"] * 3)
        self.assertEqual(listing[app["id"]]["state"], "blocked")
        self.assertEqual(listing[app["id"]]["condition"], "waiting")
        self.assertEqual(listing[app["id"]]["current_liveness"], "unknown")
        self.store = requests.Store(self.home)
        app = self.store.read(app["id"])
        self.assertEqual(app["handoffs"][0]["target"]["request_id"], "APP-17")
        self.assertEqual(len(app["handoffs"][0]["observations"]), 1)
        self.assertEqual(self.tree_bytes(remote), before_remote)
        self.assertEqual(self.tree_bytes(source_dir), captured_bytes)
        self.assertEqual((source_dir / "input.txt").read_bytes(), self.raw.encode("utf-8"))
        self.assertEqual((source_dir / "attachments/specification.bin").read_bytes(), original.read_bytes())
        self.assertEqual(len(list((self.home / "sources").iterdir())), 1)
        self.assertEqual(sum(path.read_bytes() == self.raw.encode("utf-8") for path in (self.home / "sources").rglob("input.txt")), 1)
        self.assertTrue(all(r["sources"][0]["source_id"] == source for r in self.store.records()))

        app = self.event(app, "handoff_return", handoff_id="app-delivery", receipt="Delivered app result", evidence=["App artifact and receiver checks"])
        self.assertEqual(app["state"], "blocked", "Returned remote work is not local acceptance")
        app = self.event(app, "resume", reason="Result ready for source evaluation")
        app = self.review(app)
        with self.assertRaises(ValueError):
            self.event(app, "accept", director="source-director", evidence=["Local submission alone"])
        app = self.event(app, "handoff_accept", handoff_id="app-delivery", director="source-director", evidence=["Source evaluated agreed app deliverable"])
        app = self.event(app, "accept", director="source-director", evidence=["Accepted app outcome after integrated review"])
        self.assertEqual(app["state"], "done")
        self.assertEqual(self.tree_bytes(remote), before_remote)
        self.assertEqual(self.tree_bytes(source_dir), captured_bytes)

    def manage(self, record, handle="manager-handle-1"):
        record = self.event(record, "plan", owner="🐙 Contract", acceptance=["Fix reported bug", "Regression tests pass", "Release verified in production", "Customer thanked after verified success"], human_gate={"required": False})
        receipt = {"kind": "agent", "id": handle, "responsibility": "request-manager", "identity": "🐙 Contract", "requested": "Large/high", "selected": "unknown"}
        return self.event(record, "dispatch", receipt=receipt)

    def test_steering_keeps_same_manager_and_observed_handle_through_legal_replanning(self):
        for entry in ("active", "review", "blocked"):
            with self.subTest(entry=entry):
                record = self.manage(self.new(f"complete outcome steered while {entry}"))
                if entry == "review":
                    record = self.event(record, "submit", evidence=["Integrated manager submission"])
                steering = self.store.capture(f"Also cover the {entry} edge case.", f"steering-{entry}")["source_id"]
                if entry != "blocked":
                    with self.assertRaises(ValueError, msg="In-place active/review amendment is not supported"):
                        self.event(record, "amend", source_id=steering)
                record = self.event(record, "note", text="🐙 Contract handle manager-handle-1 observed live; partial diagnosis retained; steering delivered, incorporation pending")
                transition = {"active": "requeue", "review": "revise", "blocked": "block"}[entry]
                record = self.event(record, transition, reason="Replan with captured steering")
                record = self.event(record, "amend", source_id=steering)
                self.assertIsNone(record["execution_receipt"], "Replanning clears the current receipt")
                self.assertEqual(record["acceptance"], [])
                if entry == "blocked":
                    record = self.event(record, "resume", reason="Steering captured; replan same outcome")
                revised = ["Fix reported bug", f"Cover the {entry} edge case", "Regression tests pass", "Release verified in production", "Customer thanked after verified success"]
                record = self.event(record, "plan", owner="🐙 Contract", acceptance=revised, human_gate={"required": False})
                record = self.event(record, "dispatch", receipt={"kind": "agent", "id": "manager-handle-1", "responsibility": "request-manager", "identity": "🐙 Contract"})
                self.assertEqual(record["state"], "active")
                self.assertEqual(record["owner"], "🐙 Contract")
                self.assertEqual(record["acceptance"], revised)
                self.assertEqual(record["execution_receipt"]["id"], "manager-handle-1")
                self.assertEqual(record["execution_receipt"]["identity"], "🐙 Contract")
                self.assertEqual([s["source_id"] for s in record["sources"]][-1], steering)
                dispatches = [h for h in record["history"] if h["type"] == "dispatch"]
                self.assertEqual(len(dispatches), 2, "History retains the receipt cleared by replanning")
                self.assertEqual(dispatches[0]["data"]["receipt"]["selected"], "unknown")
                record = self.event(record, "submit", evidence=["Integrated outcome covering every obligation"])
                record = self.event(record, "accept", director="🎬 project Director", evidence=["Director evaluated full revised obligations"])
                self.assertEqual(record["director_acceptance"]["director"], "🎬 project Director")
        self.store.validate()

    def test_grouping_does_not_gate_but_required_dependency_reopen_does(self):
        child = self.new("independent child")
        grouped = self.new("related independent outcome")
        grouped = self.event(grouped, "link", link_id="group-only", kind="group", target=self.local(child))
        child = self.event(child, "link", link_id="reciprocal-group", kind="group", target=self.local(grouped))
        grouped = self.finish(grouped)
        self.assertEqual(grouped["state"], "done")
        self.assertEqual(self.store.read(child["id"])["state"], "inbox")

        parent = self.new("aggregate")
        parent = self.event(parent, "link", link_id="required-child", kind="depends_on", target=self.local(child))
        parent = self.review(parent)
        with self.assertRaises(ValueError):
            self.event(parent, "accept", director="source-director", evidence=["Child still pending"])
        child = self.finish(child)
        # Review of the parent is not a frozen dependency snapshot.
        child = self.event(child, "reopen", reason="Accepted child needs more work")
        with self.assertRaises(ValueError):
            self.event(parent, "accept", director="source-director", evidence=["Old child success must not qualify"])
        child = self.event(child, "cancel", reason="Child cannot be delivered")
        with self.assertRaises(ValueError):
            self.event(parent, "accept", director="source-director", evidence=["Canceled child is not success"])
        child = self.event(child, "reopen", reason="Delivery now possible")
        child = self.finish(child)
        parent = self.event(parent, "accept", director="source-director", evidence=["Required child is currently accepted"])
        self.assertEqual(parent["state"], "done")

    def test_only_required_cycles_gate_and_external_observation_needs_review(self):
        first, second = self.new("first"), self.new("second")
        first = self.event(first, "link", link_id="required-second", kind="depends_on", target=self.local(second))
        with self.assertRaises(ValueError):
            self.event(second, "link", link_id="required-first", kind="depends_on", target=self.local(first))
        second = self.event(second, "link", link_id="context-first", kind="related", target=self.local(first))
        external = self.new("external result consumer")
        external = self.event(external, "link", link_id="native-required", kind="depends_on", target={"project_id": "existing-video-tracker", "request_id": "VIDEO-778", "locator": "/not-accessed/by-helper"})
        external = self.event(external, "observe", link_id="native-required", status="done", evidence=["Receiver reported completion"], observed_at="2026-10-16T12:00:00Z")
        external = self.review(external)
        with self.assertRaises(ValueError):
            self.event(external, "accept", director="source-director", evidence=["Observation is not source evaluation"])
        external = self.event(external, "review_dependency", link_id="native-required", director="source-director", evidence=["Reviewed delivered artifact against required result"])
        external = self.event(external, "accept", director="source-director", evidence=["All required results evaluated"])
        self.assertEqual(external["state"], "done")

    def test_waiver_alone_cannot_make_original_required_delivery_successful(self):
        record = self.plan(self.new("original app delivery"))
        record = self.event(record, "handoff_propose", handoff_id="required-app", target={"project_id": "native-app-project", "request_id": "APP-17"}, outcome="Deliver original app", required=True, return_route="authorized result location", constraints="Original scope", content="Exact source supplied", acceptance=["Original app delivered"])
        with self.assertRaises(ValueError):
            self.event(record, "handoff_waive", handoff_id="required-app", director="source-director", reason="External delivery withdrawn")
        original_criteria = record["acceptance"]
        record = self.event(record, "handoff_waive", handoff_id="required-app", director="source-director", reason="Authorized replacement of app scope with research-only scope", revised_acceptance=["Deliver accepted research; app explicitly removed"])
        self.assertNotEqual(record["acceptance"], original_criteria)
        self.assertNotEqual(record["state"], "done")
        record = self.finish(record)
        self.assertEqual(record["state"], "done")
        self.assertEqual(record["acceptance"], ["Deliver accepted research; app explicitly removed"])

    def test_interrupted_folder_moves_and_asset_writes_recover_exactly_once(self):
        for operation in ("move", "asset"):
            for point in ("prepared", "files", "moved", "written"):
                with self.subTest(operation=operation, point=point):
                    home = self.root / f"{operation}-{point}"
                    requests.Store.init(home)
                    store = requests.Store(home)
                    source = store.capture("Disposable recovery source\r\n", "source")["source_id"]
                    record = self.new("recovery outcome", store, source)
                    asset = self.root / f"{operation}-{point}.bin"
                    asset.write_bytes(b"\x00\xff recovery content\r\n")
                    record = self.plan(record, store)
                    expected = record["revision"]
                    event = {"event_id": "interrupted-dispatch", "type": "dispatch", "receipt": {"kind": "agent", "id": "fixture-only-worker"}}
                    def interrupt(observed):
                        if observed == point:
                            raise InterruptedFixture(point)
                    store.fault = interrupt
                    with self.assertRaises(InterruptedFixture):
                        if operation == "move":
                            store.apply(record["id"], event, expected)
                        else:
                            store.attach(record["id"], asset, "assets", "interrupted-asset", expected)
                    cold = requests.Store(home)
                    with self.assertRaises(ValueError):
                        cold.read(record["id"])
                    cold.recover()
                    recovered = cold.read(record["id"])
                    self.assertEqual(recovered["revision"], expected + 1)
                    self.assertEqual(len(list((home / "requests").glob(f"*/{record['id']}"))), 1)
                    if operation == "move":
                        self.assertEqual(recovered["state"], "active")
                        repeated = cold.apply(record["id"], event, expected)
                    else:
                        receipt = recovered["files"][0]
                        self.assertEqual((cold.path(record["id"]).parent / receipt["path"]).read_bytes(), asset.read_bytes())
                        repeated = cold.attach(record["id"], asset, "assets", "interrupted-asset", expected)
                    self.assertEqual(repeated, recovered)
                    self.assertEqual(cold.validate(), {"valid": 1})
                    self.assertFalse((home / ".request-txn").exists())

    def test_conflicting_locations_source_tampering_and_symlinks_fail_closed(self):
        record = self.new("protected request")
        path = self.store.path(record["id"])
        duplicate = self.home / "requests/working" / record["id"]
        duplicate.parent.mkdir(parents=True)
        shutil.copytree(path.parent, duplicate)
        before = self.tree_bytes(self.home)
        with self.assertRaises(ValueError):
            self.store.read(record["id"])
        with self.assertRaises(ValueError):
            self.event(record, "note", text="Must not overwrite duplicates")
        self.assertEqual(self.tree_bytes(self.home), before)
        shutil.rmtree(duplicate)
        source_input = self.home / "sources" / self.source / "input.txt"
        original_source = source_input.read_bytes()
        source_input.write_bytes(b"tampered source")
        with self.assertRaises(ValueError):
            requests.Store(self.home).read(record["id"])
        source_input.write_bytes(original_source)
        external = self.root / "outside"
        external.mkdir()
        (external / "untouched.txt").write_bytes(b"Original external bytes")
        (path.parent / "assets").symlink_to(external, target_is_directory=True)
        file = self.root / "input.txt"
        file.write_bytes(b"New attachment")
        with self.assertRaises(ValueError):
            self.store.attach(record["id"], file, "assets", "escape-attempt", record["revision"])
        self.assertEqual(self.tree_bytes(external), {"untouched.txt": b"Original external bytes"})
        with self.assertRaises(ValueError):
            self.store.read("../outside")

    def test_misplaced_bundle_cannot_disappear_from_recovery_or_validation(self):
        record = self.new("must remain visible")
        bundle = self.store.path(record["id"]).parent
        destination = self.home / "requests/unknown-status" / record["id"]
        destination.parent.mkdir()
        bundle.rename(destination)
        before = self.tree_bytes(self.home)
        cold = requests.Store(self.home)
        with self.assertRaises(ValueError):
            cold.records()
        with self.assertRaises(ValueError):
            cold.validate()
        self.assertEqual(self.tree_bytes(self.home), before)


if __name__ == "__main__":
    unittest.main()
