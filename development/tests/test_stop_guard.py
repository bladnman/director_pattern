"""Offline protocol/control fixtures with fake commands only; no semantic proof."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


GUARD = Path(__file__).resolve().parents[1] / "prototypes/stop_guard.py"
FINAL = "research and design are not finished"
SOURCE = "Complete research and design. Live experiments alone are held."


class StopGuardTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.home = self.root / ".director/stop-guard"
        self.home.mkdir(parents=True, mode=0o700)
        self.home.chmod(0o700)
        self.sha = hashlib.sha256(SOURCE.encode()).hexdigest()
        self.bound = dict(schema=1, binding_id="adopted-scope", assignment_generation="generation-1",
                          session_id="actual-test-session", actor_kind="project_director", status="active", root=str(self.root),
                          project_id="test-project", backend="explicit-read-only-test-route", request_ids=["terminal-parent"],
                          source_frontier=[dict(id="adopted-source", sha256=self.sha)], adoption_evidence="fixture-only")
        self.snap = dict(schema=1, binding_id=self.bound["binding_id"], assignment_generation="generation-1",
                         project_id="test-project", request_ids=["terminal-parent"], source_frontier=self.bound["source_frontier"],
                         complete=True, status="active", gaps=[],
                         items=[dict(request_id="terminal-parent", state="done", checkpoint=dict(
                             obligations=[dict(id="design", text="research and design", state="complete")],
                             next_action=None, controlling_wait=False))],
                         sources=[dict(id="adopted-source", sha256=self.sha, text=SOURCE)],
                         authorized_actions=[dict(id="design-action", request_id="terminal-parent", action="Continue documentary design")])
        self.answer = dict(decision="continue", reason="Fixture comparison only", remaining_obligation=dict(
            request_id="terminal-parent", text="research and design"), next_action="design-action", wait_assessment="runnable",
            evidence=dict(sources=[dict(source_id="adopted-source", start=0, end=28)], final=dict(start=0, end=len(FINAL))))
        self.script = self.home / "fake.py"
        self.script.write_text('''import json, pathlib, sys, time
home = pathlib.Path(__file__).parent
packet = json.load(sys.stdin)
mode = sys.argv[1]
(home / (mode + "-received.json")).write_text(json.dumps(packet))
control = json.loads((home / "fake-control.json").read_text())
fault = control.get(mode)
if fault == "timeout": time.sleep(2)
if fault == "huge": print("x" * 300000); sys.exit()
if fault == "malformed": print("not json"); sys.exit()
if fault == "stderr": print("PRIVATE BODY", file=sys.stderr); sys.exit(1)
print((home / (mode + ".json")).read_text())
''')
        self.cfg = dict(schema=1, root=str(self.root), private_dir=".director/stop-guard",
                        snapshot_argv=[sys.executable, str(self.script), "snapshot"],
                        evaluator_argv=[sys.executable, str(self.script), "evaluator"], timeout_seconds=1, max_bytes=32768)
        self.event = dict(hook_event_name="Stop", session_id="actual-test-session", cwd=str(self.root),
                          turn_id="turn-1", stop_hook_active=False, last_assistant_message=FINAL)
        self.put("fake-control.json", {})
        self.put("config.json", self.cfg)
        self.put("spec.json", self.bound)
        self.put("snapshot.json", self.snap)
        self.put("evaluator.json", self.answer)
        self.canonical = self.root / "canonical-test-sentinel"
        self.canonical.write_bytes(b"unchanged canonical task/source data")
        self.bind()

    def put(self, name, value):
        path = self.home / name
        path.write_text(json.dumps(value))
        path.chmod(0o600)

    def bind(self):
        process = subprocess.run([sys.executable, "-B", str(GUARD), "bind", "--config", str(self.home / "config.json"),
                                  "--binding", str(self.home / "spec.json")], capture_output=True)
        self.assertEqual(process.returncode, 0, process.stderr)

    def invoke(self, event=None):
        return subprocess.run([sys.executable, "-B", str(GUARD), "run", "--config", str(self.home / "config.json")],
                              input=json.dumps(self.event if event is None else event).encode(), capture_output=True)

    def run_guard(self, event=None, block=False):
        result = self.invoke(event)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload.get("decision") == "block", block, (payload, result.stderr))
        if not block:
            self.assertEqual(payload, {})
        self.assertNotIn(SOURCE.encode(), result.stdout + result.stderr)
        self.assertNotIn(FINAL.encode(), result.stdout + result.stderr)
        self.assertEqual(self.canonical.read_bytes(), b"unchanged canonical task/source data")
        return result

    def state(self):
        return json.loads((self.home / "state.json").read_text())

    def test_false_done_all_complete_and_unfinished_final_reach_evaluator(self):
        self.snap["status"] = "complete"
        self.put("snapshot.json", self.snap)
        self.run_guard(block=True)
        packet = json.loads((self.home / "evaluator-received.json").read_text())
        self.assertEqual(packet["last_assistant_message"], FINAL)
        self.assertEqual(packet["snapshot"]["items"][0]["state"], "done")
        self.assertEqual(packet["snapshot"]["items"][0]["checkpoint"]["obligations"][0]["state"], "complete")
        self.assertEqual(packet["snapshot"]["sources"][0]["text"], SOURCE)
        self.assertEqual(self.state()["corrections"], 1)
        self.assertEqual(self.state()["evaluator_calls"], 1)
        self.assertNotIn(FINAL, (self.home / "state.json").read_text())

    def test_without_evaluator_false_complete_is_missed(self):
        self.cfg["evaluator_argv"] = None
        self.put("config.json", self.cfg)
        state = self.state()
        # Test fixture establishes the changed config before its first run.
        state["config_digest"] = hashlib.sha256(json.dumps(self.cfg, ensure_ascii=False, sort_keys=True,
                                                          separators=(",", ":")).encode()).hexdigest()
        self.put("state.json", state)
        result = self.run_guard()
        self.assertIn(b"structural_only_false_complete_unchecked", result.stderr)

    def test_recorded_pending_authorized_action_structurally_blocks(self):
        self.snap["items"][0]["checkpoint"]["obligations"][0]["state"] = "pending"
        self.snap["items"][0]["checkpoint"]["next_action"] = "design-action"
        self.put("snapshot.json", self.snap)
        self.run_guard(block=True)
        self.assertFalse((self.home / "evaluator-received.json").exists())

    def test_partial_hold_with_runnable_documentary_action(self):
        self.snap["status"] = "partial_hold"
        self.put("snapshot.json", self.snap)
        self.run_guard(block=True)

    def test_true_pause_allows(self):
        self.snap["status"] = "paused"
        self.put("snapshot.json", self.snap)
        self.answer.update(decision="allow", remaining_obligation=None, next_action=None,
                           wait_assessment="paused", evidence=dict(sources=[], final=None))
        self.put("evaluator.json", self.answer)
        self.run_guard()
        self.assertTrue((self.home / "evaluator-received.json").exists())

    def test_genuine_wait_allows(self):
        self.snap["status"] = "waiting"
        self.put("snapshot.json", self.snap)
        self.answer.update(decision="allow", remaining_obligation=None, next_action=None,
                           wait_assessment="waiting", evidence=dict(sources=[], final=None))
        self.put("evaluator.json", self.answer)
        self.run_guard()

    def test_recorded_wait_cannot_suppress_semantic_comparison(self):
        self.snap["items"][0]["checkpoint"]["controlling_wait"] = True
        self.snap["status"] = "waiting"
        self.put("snapshot.json", self.snap)
        self.run_guard(block=True)

    def test_explicit_owner_binding_pause_is_free(self):
        self.bound["status"] = "paused"
        self.put("binding.json", self.bound)
        # Gate precedes operational state access and commands, regardless of digest.
        self.run_guard()
        self.assertEqual(self.state()["snapshot_calls"], 0)

    def test_contradictory_counters_never_create_new_call(self):
        state = self.state()
        state["evaluator_calls"] = 1
        self.put("state.json", state)
        self.run_guard()
        self.assertFalse((self.home / "snapshot-received.json").exists())

    def test_one_held_request_does_not_suppress_independent_false_complete(self):
        self.bound["request_ids"].append("held-experiment")
        self.put("binding.json", self.bound)
        state = self.state()
        state["binding_digest"] = hashlib.sha256(json.dumps(self.bound, ensure_ascii=False, sort_keys=True,
                                                            separators=(",", ":")).encode()).hexdigest()
        self.put("state.json", state)
        self.snap["status"] = "partial_hold"
        self.snap["request_ids"].append("held-experiment")
        self.snap["items"].append(dict(request_id="held-experiment", state="blocked", checkpoint=dict(
            obligations=[dict(id="held", text="Live experiment", state="waiting")], next_action=None, controlling_wait=True)))
        self.put("snapshot.json", self.snap)
        self.run_guard(block=True)

    def test_child_and_other_events_are_free(self):
        for kind in ("SubagentStop", "Interrupt", "UserPromptSubmit"):
            self.run_guard(self.event | {"hook_event_name": kind})
        self.run_guard(self.event | {"session_id": "bounded-child-session"})
        self.assertEqual(self.state()["snapshot_calls"], 0)

    def test_null_final_is_free(self):
        self.run_guard(self.event | {"last_assistant_message": None})
        self.assertEqual(self.state()["snapshot_calls"], 0)

    def test_quoted_historical_and_optional_inquiry_allow_via_evaluator(self):
        # Each subcase starts an explicitly separate fixture, never resets a live binding.
        self.answer.update(decision="allow", remaining_obligation=None, next_action=None,
                           wait_assessment="complete", evidence=dict(sources=[], final=None))
        self.put("evaluator.json", self.answer)
        self.run_guard(self.event | {"last_assistant_message": 'Historical quote: "research and design are not finished"; adopted work is complete. Optional inquiry remains.'})
        self.assertEqual(self.state()["evaluator_calls"], 1)

    def test_sufficient_bounded_completion_allows(self):
        self.snap["status"] = "complete"
        self.answer.update(decision="allow", remaining_obligation=None, next_action=None,
                           wait_assessment="complete", evidence=dict(sources=[], final=None))
        self.put("snapshot.json", self.snap)
        self.put("evaluator.json", self.answer)
        self.run_guard()

    def test_boolean_schema_is_rejected(self):
        self.snap["schema"] = True
        self.put("snapshot.json", self.snap)
        self.run_guard()
        self.assertFalse((self.home / "evaluator-received.json").exists())

    def test_binding_survives_done_and_new_turns_do_not_reset(self):
        self.run_guard(block=True)
        self.snap["items"][0]["checkpoint"]["obligations"][0]["text"] = "Model-written revised progress"
        self.put("snapshot.json", self.snap)
        self.run_guard(self.event | {"turn_id": "new-synthetic-turn", "stop_hook_active": True,
                                    "last_assistant_message": "Changed final and progress"})
        self.assertEqual(self.state()["corrections"], 1)
        self.assertEqual(self.state()["snapshot_calls"], 1)
        self.assertEqual(json.loads((self.home / "binding.json").read_text()), self.bound)

    def test_racing_processes_emit_at_most_one_block(self):
        args = [sys.executable, "-B", str(GUARD), "run", "--config", str(self.home / "config.json")]
        processes = [subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) for _ in range(4)]
        outputs = [p.communicate(json.dumps(self.event).encode()) for p in processes]
        self.assertEqual(sum(json.loads(out).get("decision") == "block" for out, _ in outputs), 1)

    def test_missing_existing_state_never_recreates_budget(self):
        (self.home / "state.json").unlink()
        self.run_guard()
        self.assertFalse((self.home / "state.json").exists())

    def test_corrupt_state_preserved_and_fail_open(self):
        (self.home / "state.json").write_bytes(b"corrupt-private-state")
        self.run_guard()
        self.assertEqual((self.home / "state.json").read_bytes(), b"corrupt-private-state")

    def test_duplicate_binding_cannot_reset(self):
        self.run_guard(block=True)
        process = subprocess.run([sys.executable, str(GUARD), "bind", "--config", str(self.home / "config.json"),
                                  "--binding", str(self.home / "spec.json")], capture_output=True)
        self.assertNotEqual(process.returncode, 0)
        self.assertEqual(self.state()["corrections"], 1)

    def test_source_frontier_change_is_unknown(self):
        self.snap["source_frontier"] = [dict(id="new-source", sha256="0" * 64)]
        self.put("snapshot.json", self.snap)
        self.run_guard()
        self.assertFalse((self.home / "evaluator-received.json").exists())

    def test_source_text_hash_mismatch_is_unknown(self):
        self.snap["sources"][0]["text"] = "changed source"
        self.put("snapshot.json", self.snap)
        self.run_guard()

    def test_bound_terminal_id_omission_is_unknown(self):
        self.snap["items"] = []
        self.put("snapshot.json", self.snap)
        self.run_guard()

    def test_snapshot_gap_is_unknown(self):
        self.snap["gaps"] = ["pending_native_journal"]
        self.put("snapshot.json", self.snap)
        self.run_guard()

    def test_evaluator_malformed_output_is_unknown(self):
        self.put("fake-control.json", {"evaluator": "malformed"})
        self.run_guard()
        self.assertEqual(self.state()["evaluator_calls"], 1)

    def test_evaluator_timeout_is_unknown_and_not_retried(self):
        self.put("fake-control.json", {"evaluator": "timeout"})
        self.run_guard()
        self.run_guard(self.event | {"turn_id": "turn-2"})
        self.assertEqual(self.state()["corrections"], 0)

    def test_unsupported_evidence_is_unknown(self):
        self.answer["evidence"]["sources"][0]["source_id"] = "unrelated-source"
        self.put("evaluator.json", self.answer)
        self.run_guard()

    def test_conflicting_wait_verdict_is_unknown(self):
        self.answer["wait_assessment"] = "paused"
        self.put("evaluator.json", self.answer)
        self.run_guard()

    def test_command_output_bound_and_stderr_privacy(self):
        self.put("fake-control.json", {"snapshot": "huge"})
        result = self.run_guard()
        self.assertLess(len(result.stdout + result.stderr), 200)

    def test_command_stderr_never_leaks(self):
        self.put("fake-control.json", {"snapshot": "stderr"})
        result = self.run_guard()
        self.assertNotIn(b"PRIVATE BODY", result.stdout + result.stderr)

    def test_symlink_state_is_rejected_without_target_write(self):
        (self.home / "state.json").unlink()
        (self.home / "state.json").symlink_to(self.canonical)
        self.run_guard()

    def test_deep_or_duplicate_json_is_fail_open(self):
        args = [sys.executable, str(GUARD), "run", "--config", str(self.home / "config.json")]
        for raw in (b'{"hook_event_name":"Stop","hook_event_name":"Stop"}', b'[' * 2000 + b'0' + b']' * 2000):
            result = subprocess.run(args, input=raw, capture_output=True)
            self.assertEqual(json.loads(result.stdout), {})
            self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
