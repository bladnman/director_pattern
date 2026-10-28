"""Disposable record guarantees supporting supervision; no model/liveness classifier."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[2] / "pattern/tools/requests.py"
spec = importlib.util.spec_from_file_location("supervision_requests", SCRIPT)
requests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(requests)


class SupervisionRecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / ".director"
        requests.Store.init(self.root)
        self.store = requests.Store(self.root)
        self.serial = 0
        self.source = self.store.capture("Deliver the complete two-part change.", "source")["source_id"]

    def create(self, title):
        self.serial += 1
        return self.store.create(title=title, event_id=f"create-{self.serial}", source_id=self.source)

    def event(self, record, event_type, **fields):
        self.serial += 1
        return self.store.apply(record["id"], {"event_id": f"event-{self.serial}", "type": event_type, **fields}, record["revision"])

    def target(self, record):
        return {"project_id": self.store.project_id, "request_id": record["id"]}

    def active(self, record, owner):
        record = self.event(record, "plan", owner=owner, acceptance=[record["title"]], human_gate={"required": False})
        return self.event(record, "dispatch", receipt={"kind": "agent", "id": f"fixture-{owner}"})

    def finish(self, record):
        record = self.event(record, "submit", evidence=["Disposable artifact inspected"])
        return self.event(record, "accept", director="fixture-director", evidence=["Required scope evaluated"])

    def test_required_children_and_backreferences_survive_rework_and_relocation(self):
        parent = self.active(self.create("Complete integrated change"), "parent-manager")
        children = [self.active(self.create(title), owner) for title, owner in (("Behavior", "behavior-owner"), ("Checks", "checks-owner"))]
        parent_id = self.target(parent)
        for number, child in enumerate(children):
            parent = self.event(parent, "link", link_id=f"required-{number}", kind="depends_on", target=self.target(child))
            children[number] = self.event(child, "link", link_id="parent-reference", kind="related", target=parent_id)
            children[number] = self.event(children[number], "note", text=json.dumps({
                "parent": parent_id, "requirement": child["title"], "owner": child["owner"],
                "observed_at": "2026-10-27T20:00:00Z", "status": "active", "evidence": "Synthetic dispatch only; current liveness unknown",
            }, sort_keys=True))
        children[0] = self.finish(children[0])
        children[1] = self.event(children[1], "submit", evidence=["Incomplete check report"])
        parent = self.event(parent, "submit", evidence=["Behavior accepted; check return awaits evaluation"])
        with self.assertRaisesRegex(ValueError, "Required local dependency is not done"):
            self.event(parent, "accept", director="fixture-director", evidence=["One child is still review"])

        child = self.event(children[1], "revise", reason="Missing integration check; same owner rework")
        child = self.active(child, "checks-owner")
        child = self.finish(child)
        # A fresh Store resolves moved bundles by stable identity, including the
        # reciprocal informational backreference and dated requirement evidence.
        recovered = requests.Store(self.root)
        returned = recovered.read(child["id"])
        self.assertEqual(returned["owner"], "checks-owner")
        self.assertEqual(returned["links"][0]["target"], parent_id)
        notes = [row for row in returned["history"] if row["type"] == "note"]
        self.assertEqual(json.loads(notes[0]["data"]["text"])["parent"], parent_id)
        self.assertEqual(recovered.path(child["id"]).parent.parent.name, "archive")
        self.assertEqual(recovered.read(parent["id"])["state"], "review")
        parent = self.event(parent, "accept", director="fixture-director", evidence=["Both required child outcomes evaluated and done"])
        self.assertEqual(parent["state"], "done")
        self.assertEqual(self.store.validate(), {"valid": 3})

    def test_status_note_and_restart_do_not_turn_dispatch_into_live_or_done(self):
        parent = self.active(self.create("Supervise assigned work"), "manager")
        child = self.active(self.create("Finite fixture task"), "worker")
        parent = self.event(parent, "note", text=json.dumps({
            "assignment": "fixture-task", "child": self.target(child), "handle": "fixture-worker",
            "last_observation": "2026-10-27T20:01:00Z", "status": "active", "next": "Check actual host handle before replacing",
        }))
        before_receipt = child["execution_receipt"]
        child = self.event(child, "note", text="User requested status; work remains open pending actual host observation")
        self.assertEqual(child["state"], "active")
        self.assertEqual(child["execution_receipt"], before_receipt)
        listing = json.loads(subprocess.check_output([sys.executable, str(SCRIPT), "--team", str(self.root), "list", "--open"], text=True))
        self.assertEqual({row["state"] for row in listing}, {"active"})
        self.assertEqual({row["current_liveness"] for row in listing}, {"unknown"})
        self.assertEqual({row["id"] for row in listing}, {parent["id"], child["id"]})
        # Reading/recovering the records neither starts another attempt nor changes
        # the parent commitment. Actual continuation remains a host/owner action.
        self.assertEqual(requests.Store(self.root).read(child["id"])["execution_receipt"], before_receipt)
        self.assertEqual(requests.Store(self.root).read(parent["id"])["state"], "active")
        self.assertEqual(len(self.store.records()), 2)


if __name__ == "__main__":
    unittest.main()
