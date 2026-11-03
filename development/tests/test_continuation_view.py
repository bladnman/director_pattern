"""Independent continuation data regressions through a disposable installed CLI.

These fixtures expose recorded contradictions; they do not run an agent, inspect
live children, infer omitted intent, or establish that an owner continues work.
"""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
STARTER = ROOT / "pattern/starter"
PREFIX = "DIRECTOR_CONTINUATION_V1 "


class ContinuationViewTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name)
        self.project = self.base / "project"
        self.serial = 0
        installed = subprocess.run(
            [sys.executable, "-B", str(STARTER / "install.py"), "install", "--target", str(self.project)],
            capture_output=True, text=True,
        )
        self.assertEqual(installed.returncode, 0, installed.stderr)
        self.home = self.project / ".director"
        self.cli = self.home / "requests.py"

    def identity(self):
        self.serial += 1
        return f"continuation-{self.serial:032x}"

    def command(self, *arguments, reject=False, contains=None):
        result = subprocess.run(
            [sys.executable, "-B", str(self.cli), *map(str, arguments)],
            capture_output=True,
        )
        self.last_process = result
        if reject:
            self.assertNotEqual(result.returncode, 0, result.stdout)
            if contains:
                self.assertIn(contains.lower(), result.stderr.decode().lower())
            return result
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        return json.loads(result.stdout)

    def capture(self, raw=b"Deliver the whole adopted outcome.\r\n"):
        raw_file = self.base / (self.identity() + ".txt")
        raw_file.write_bytes(raw)
        return self.command("capture", "--raw-file", raw_file, "--event-id", self.identity())["source_id"]

    def new(self, title="complete adopted outcome", source=None):
        return self.command("create", "--title", title, "--source-id", source or self.capture(),
                            "--event-id", self.identity())

    def event(self, record, event_type, *, event_id=None, expected=None, reject=False, contains=None, **fields):
        event_file = self.base / (self.identity() + ".json")
        event_file.write_text(json.dumps({"event_id": event_id or self.identity(), "type": event_type, **fields}))
        return self.command("apply", record["id"], "--event-file", event_file, "--expect-revision",
                            record["revision"] if expected is None else expected, reject=reject, contains=contains)

    def plan(self, record, criteria=None, human=False):
        return self.event(record, "plan", owner="fixture-outcome-owner",
                          acceptance=criteria or ["research, design, implementation and independent review"],
                          human_gate={"required": human})

    def finish(self, record):
        if record["state"] == "inbox":
            record = self.plan(record)
        record = self.event(record, "dispatch", receipt={"kind": "agent", "id": "synthetic-returned-child"})
        record = self.event(record, "submit", evidence=["synthetic partial exploration artifact"],
                            artifacts=["outputs/exploration.txt"])
        return self.event(record, "accept", director="fixture-root", evidence=["synthetic milestone accepted"])

    def data(self, record, **changes):
        value = {
            "schema": 1,
            "request_id": record["id"],
            "source_ids": [source["source_id"] for source in record["sources"]],
            "outcome": "Deliver the whole adopted outcome",
            "obligations": [{"id": "C1", "text": "Complete independent review", "state": "pending", "evidence": []}],
            "next_action": {"owner": "fixture-outcome-owner", "action": "Assign independent review"},
            "wait": None,
        }
        return value | changes

    def checkpoint(self, record, data=None, text=None):
        return self.event(record, "note", text=text if text is not None else PREFIX + json.dumps(data or self.data(record)))

    def item(self, record):
        result = self.command("continuation", record["id"])
        self.assertEqual(result["total"], 1)
        return result["items"][0]

    def tree(self):
        return {str(path.relative_to(self.home)): path.read_bytes()
                for path in self.home.rglob("*") if path.is_file()}

    def test_done_parent_and_idle_children_do_not_hide_remaining_parent_work(self):
        source = self.capture()
        children = [self.finish(self.new(title, source)) for title in ("bounded research", "bounded alternatives")]
        parent = self.finish(self.new("whole adopted outcome", source))
        parent = self.event(parent, "note", text=json.dumps({
            "children": [{"id": child["id"], "observed_state": "returned", "live": False} for child in children],
            "acknowledgment": "Research and design are not finished; experiments alone are held",
        }))
        parent = self.checkpoint(parent)
        before = self.tree()
        item = self.item(parent)
        self.assertEqual(item["state"], "done")
        self.assertEqual(item["checkpoint"]["data"]["obligations"][0]["state"], "pending")
        self.assertEqual(item["checkpoint"]["data"]["next_action"]["action"], "Assign independent review")
        self.assertIn("terminal_with_unfinished_obligations", item["gaps"])
        self.assertTrue(item["reconciliation_required"])
        self.assertEqual(item["current_liveness"], "unknown")
        self.assertEqual(item["acceptance"], parent["acceptance"])
        self.assertEqual(item["artifacts"], parent["artifacts"])
        self.assertNotIn("history", item)
        self.assertEqual(before, self.tree())

    def test_independent_bound_outcomes_include_done_sibling_and_exclude_backlog(self):
        done = self.finish(self.new("accepted independent outcome"))
        done = self.checkpoint(done, self.data(done, obligations=[{
            "id": "C1", "text": "Accepted outcome", "state": "complete", "evidence": ["accepted artifact"],
        }], next_action=None))
        pending = self.checkpoint(self.plan(self.new("remaining independent outcome")))
        unrelated = self.new("unrelated backlog")
        result = self.command("continuation", pending["id"], done["id"])
        self.assertEqual(result["total"], 2)
        by_id = {item["id"]: item for item in result["items"]}
        self.assertEqual(set(by_id), {done["id"], pending["id"]})
        self.assertNotIn(unrelated["id"], json.dumps(result["items"]))
        self.assertEqual(by_id[done["id"]]["gaps"], [])
        self.assertFalse(by_id[done["id"]]["reconciliation_required"])
        self.assertEqual(by_id[pending["id"]]["gaps"], [])

    def test_missing_checkpoint_and_missing_bound_record_are_explicit(self):
        record = self.event(self.new(), "note", text="Ordinary commentary has no checkpoint convention")
        item = self.item(record)
        self.assertIsNone(item["checkpoint"])
        self.assertIn("checkpoint_missing", item["gaps"])
        missing = "REQ-" + "f" * 32
        result = self.command("continuation", record["id"], missing)
        by_id = {item["id"]: item for item in result["items"]}
        self.assertEqual(set(by_id), {record["id"], missing})
        self.assertIn("request_missing", by_id[missing]["gaps"])
        self.assertTrue(by_id[missing]["reconciliation_required"])

    def test_latest_malformed_or_unsupported_checkpoint_never_falls_back(self):
        record = self.checkpoint(self.new())
        old_event = record["history"][-1]["event_id"]
        for text, gap in ((PREFIX + "{", "checkpoint_invalid"),
                          ("DIRECTOR_CONTINUATION_V2 {}", "checkpoint_unsupported_version"),
                          (PREFIX + "[]", "checkpoint_invalid"),
                          (PREFIX + "[" * 1500 + "0" + "]" * 1500, "checkpoint_invalid")):
            with self.subTest(text=text):
                record = self.checkpoint(record, text=text)
                latest = record["history"][-1]
                item = self.item(record)
                self.assertIn(gap, item["gaps"])
                self.assertEqual(item["checkpoint"]["event_id"], latest["event_id"])
                self.assertNotEqual(item["checkpoint"]["event_id"], old_event)
                self.assertEqual(item["checkpoint"]["revision"], record["revision"])
                self.assertTrue(item["reconciliation_required"])
                self.assertIsNone(item["checkpoint"]["data"])

    def test_checkpoint_shape_errors_are_gaps_not_silently_accepted(self):
        record = self.new()
        invalid = [
            {"schema": 2}, {"request_id": "REQ-" + "e" * 32}, {"unexpected": "field"},
            {"source_ids": []},
            {"obligations": [{"id": "C1", "text": "claim", "state": "complete", "evidence": []}]},
            {"obligations": [{"id": "C1", "text": "claim", "state": "running", "evidence": []}]},
            {"obligations": [{"id": "same", "text": "a", "state": "pending", "evidence": []}] * 2},
            {"next_action": None, "wait": None},
            {"next_action": {"owner": "fixture", "action": ""}},
        ]
        for change in invalid:
            with self.subTest(change=change):
                record = self.checkpoint(record, self.data(record, **change))
                self.assertIn("checkpoint_invalid", self.item(record)["gaps"])

    def test_source_frontier_and_non_note_events_require_reconciliation(self):
        original = self.capture(b"Original full outcome.\r\n")
        record = self.checkpoint(self.plan(self.new(source=original)))
        checkpoint_revision = record["revision"]
        # Commentary changes the record revision but does not obsolete its scope.
        record = self.event(record, "note", text="Status question answered; current work is unchanged")
        item = self.item(record)
        self.assertEqual(item["gaps"], [])
        self.assertEqual(item["checkpoint"]["revision"], checkpoint_revision)
        steering = self.capture(b"Also deliver a separate acceptance report.\r\n")
        record = self.event(record, "amend", source_id=steering)
        record = self.plan(record, criteria=["original outcome", "separate acceptance report"])
        item = self.item(record)
        self.assertIn("source_frontier_changed", item["gaps"])
        self.assertIn("events_after_checkpoint", item["gaps"])
        self.assertEqual([row["source_id"] for row in item["sources"]], [original, steering])
        self.assertEqual(item["acceptance"], ["original outcome", "separate acceptance report"])
        self.assertEqual((self.home / "sources" / original / "input.txt").read_bytes(), b"Original full outcome.\r\n")
        record = self.checkpoint(record)
        self.assertEqual(self.item(record)["gaps"], [])
        # Replanning against the same exact sources still invalidates an old plan.
        record = self.plan(record, criteria=["revised criteria against same sources"])
        self.assertIn("events_after_checkpoint", self.item(record)["gaps"])

    def test_source_frontier_preserves_native_repeated_source_ids_and_order(self):
        original = self.capture(b"Original.\n")
        steering = self.capture(b"Later exact addendum.\n")
        record = self.plan(self.new(source=original))
        for source in (steering, original):
            record = self.event(record, "amend", source_id=source)
            record = self.plan(record)
        record = self.checkpoint(record)
        item = self.item(record)
        self.assertEqual(item["checkpoint"]["data"]["source_ids"], [original, steering, original])
        self.assertEqual(item["gaps"], [])
        record = self.checkpoint(record, self.data(record, source_ids=[original, original, steering]))
        self.assertIn("source_frontier_changed", self.item(record)["gaps"])

    def test_duplicate_json_keys_and_duplicate_cli_bindings_fail_visibly(self):
        record = self.new()
        text = PREFIX + json.dumps(self.data(record))[:-1] + ',"schema":1}'
        record = self.checkpoint(record, text=text)
        item = self.item(record)
        self.assertIn("checkpoint_invalid", item["gaps"])
        self.assertIn("duplicate", item["checkpoint"]["error"])
        before = self.tree()
        self.command("continuation", record["id"], record["id"], reject=True)
        self.command("continuation", reject=True)
        self.command("continuation", "not-a-request-id", reject=True)
        self.assertEqual(before, self.tree())

    def test_pause_and_mixed_hold_are_exposed_without_a_stop_verdict(self):
        record = self.plan(self.new())
        wait = {"reason": "User holds experiments", "resume_when": "Explicit experiment authorization"}
        held = self.data(record, obligations=[{
            "id": "validation", "text": "Run held experiments", "state": "waiting", "evidence": [],
        }], next_action=None, wait=wait)
        record = self.checkpoint(record, held)
        self.assertEqual(self.item(record)["checkpoint"]["data"], held)
        mixed = self.data(record, obligations=[
            {"id": "validation", "text": "Run held experiments", "state": "waiting", "evidence": []},
            {"id": "design", "text": "Finish authorized design", "state": "pending", "evidence": []},
        ], wait=wait)
        record = self.checkpoint(record, mixed)
        item = self.item(record)
        self.assertEqual(item["checkpoint"]["data"], mixed)
        self.assertEqual(item["gaps"], [])
        for field in ("safe_to_stop", "complete", "authorized", "should_continue"):
            self.assertNotIn(field, item)

    def test_paging_bounds_snapshot_binding_and_store_immutability(self):
        records = [self.checkpoint(self.new("outcome " + str(index))) for index in range(3)]
        ids = [record["id"] for record in records]
        before = self.tree()
        first = self.command("continuation", *ids, "--limit", 1, "--max-bytes", 12000)
        self.assertLessEqual(len(self.last_process.stdout), 12000)
        self.assertEqual(first["total"], 3)
        self.assertEqual(first["next_offset"], 1)
        second = self.command("continuation", *ids, "--offset", 1, "--limit", 1,
                              "--at-snapshot", first["snapshot"])
        self.assertNotEqual(first["items"][0]["id"], second["items"][0]["id"])
        self.command("continuation", *ids[:2], "--at-snapshot", first["snapshot"], reject=True, contains="snapshot")
        self.command("continuation", *ids, "--max-bytes", 512, reject=True, contains="budget")
        self.assertEqual(before, self.tree())
        self.event(records[0], "note", text="new observed progress")
        self.command("continuation", *ids, "--offset", 2, "--at-snapshot", first["snapshot"],
                     reject=True, contains="snapshot")

    def test_oversized_unicode_checkpoint_is_not_truncated(self):
        record = self.new()
        data = self.data(record, outcome="界" * 3000)
        record = self.checkpoint(record, data)
        before = self.tree()
        self.command("continuation", record["id"], "--max-bytes", 1500, reject=True, contains="budget")
        item = self.command("continuation", record["id"], "--max-bytes", 32000)["items"][0]
        self.assertEqual(item["checkpoint"]["data"]["outcome"], data["outcome"])
        self.assertLessEqual(len(self.last_process.stdout), 32000)
        self.assertEqual(before, self.tree())

    def test_all_source_integrity_is_checked_and_failed_read_does_not_repair(self):
        original = self.capture(b"Exact original.\r\n")
        record = self.plan(self.new(source=original))
        record = self.event(record, "amend", source_id=self.capture(b"Intact latest steering.\r\n"))
        record = self.checkpoint(self.plan(record))
        (self.home / "sources" / original / "input.txt").write_bytes(b"corrupt old original")
        before = self.tree()
        self.command("continuation", record["id"], reject=True, contains="integrity")
        self.assertEqual(before, self.tree())

    def test_pending_native_transaction_refuses_without_hidden_recovery(self):
        record = self.checkpoint(self.plan(self.new()))
        spec = importlib.util.spec_from_file_location("continuation_fixture_backend", self.home / "request_store.py")
        backend = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(backend)
        store = backend.Store(self.home)
        def interrupt(point):
            if point == "files":
                raise RuntimeError("controlled interruption")
        store.fault = interrupt
        with self.assertRaisesRegex(RuntimeError, "controlled interruption"):
            store.apply(record["id"], {"event_id": self.identity(), "type": "dispatch",
                                      "receipt": {"kind": "agent", "id": "synthetic-fixture"}}, record["revision"])
        self.assertTrue((self.home / ".request-txn").exists())
        before = self.tree()
        self.command("continuation", record["id"], reject=True, contains="recover")
        self.assertEqual(before, self.tree())

    def test_native_mutation_retry_cas_and_existing_views_stay_compatible(self):
        record = self.plan(self.new())
        event_id = self.identity()
        updated = self.event(record, "note", event_id=event_id, text="canonical note retry")
        self.assertEqual(self.event(record, "note", event_id=event_id, text="canonical note retry"), updated)
        self.event(record, "note", text="stale new write", reject=True, contains="stale")
        self.event(updated, "note", event_id=event_id, text="conflicting retry", reject=True)
        current = self.command("current", record["id"])["items"][0]
        self.assertNotIn("history", current)
        self.assertEqual(current["revision"], updated["revision"])
        done = self.finish(updated)
        self.assertEqual(self.command("status")["total"], 0)
        self.assertEqual(self.command("current", done["id"])["items"][0]["state"], "done")
        self.assertEqual(self.command("validate"), {"valid": 1})

    def test_checkpoint_does_not_bypass_required_human_or_dependency_gates(self):
        child = self.new("required dependency")
        parent = self.plan(self.new("human gated outcome"), human=True)
        project_id = json.loads((self.home / "config.json").read_text())["request_store"]["project_id"]
        parent = self.event(parent, "link", link_id="required", kind="depends_on",
                            target={"project_id": project_id, "request_id": child["id"]})
        parent = self.checkpoint(parent, self.data(parent, obligations=[{
            "id": "C1", "text": "Claimed complete", "state": "complete", "evidence": ["untrusted fixture assertion"],
        }], next_action=None))
        item = self.item(parent)
        self.assertEqual(item["human_gate"], parent["human_gate"])
        self.assertEqual(item["links"], parent["links"])
        parent = self.event(parent, "dispatch", receipt={"kind": "agent", "id": "fixture"})
        parent = self.event(parent, "submit", evidence=["synthetic return"])
        self.event(parent, "accept", director="fixture", evidence=["checkpoint assertion is not acceptance"], reject=True)
        self.assertEqual(self.command("show", parent["id"])["state"], "review")


if __name__ == "__main__":
    unittest.main()
