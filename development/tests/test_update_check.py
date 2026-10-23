"""Daily discovery fixtures: no actual updater or real project state is executed."""
import concurrent.futures
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import time
import unittest

SPEC = importlib.util.spec_from_file_location("update_check", Path(__file__).resolve().parents[2] / "pattern/tools/update_check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)
OLD, NEW, TREE, CHANGED = (letter * 40 for letter in "abcd")


class DailyCheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / ".director"
        self.root.mkdir()
        (self.root / "receipts").mkdir()
        self.receipt = self.root / "receipts/current.json"
        self.receipt.write_text(json.dumps({"source": {"url": CHECK.SOURCE, "sha": OLD, "published": True},
                                           "managed_files": {"PROJECT.md": {"sha256": "local adaptation"}}}))
        self.calls = []

    def fetch(self, route):
        self.calls.append(route)
        if route == "/git/ref/heads/main":
            return {"object": {"sha": NEW}}
        return {"tree": [{"path": "pattern", "type": "tree", "sha": TREE if route.endswith(OLD) else CHANGED}]}

    def run_check(self, now=100_000, fetch=None):
        return CHECK.check(self.root, ".director/receipts/current.json", now=now, fetch=fetch or self.fetch)

    def test_absent_policy_defaults_to_notify_exact_message_and_daily_window(self):
        result = self.run_check()
        self.assertEqual(result["action"], "notify")
        self.assertEqual(result["message"], CHECK.MESSAGE)
        self.assertEqual(result["upstream_sha"], NEW)
        self.assertEqual(len(self.calls), 3)
        for now in (100_001, 100_000 + CHECK.DAY - 1, 90_000):
            self.assertEqual(self.run_check(now)["status"], "throttled")
        self.assertEqual(len(self.calls), 3)
        self.assertEqual(self.run_check(100_000 + CHECK.DAY)["action"], "notify")
        self.assertEqual(len(self.calls), 5, "Successful baseline cache saves one metadata read")
        self.assertFalse((self.root / "update-policy.json").exists())

    def test_website_only_commit_is_current_even_when_receipt_sha_is_newer_than_last_payload_commit(self):
        def site_only(route):
            data = self.fetch(route)
            if "tree" in data:
                data["tree"][0]["sha"] = TREE
            return data
        self.assertEqual(self.run_check(fetch=site_only)["status"], "current")
        self.assertEqual(len(self.calls), 3)

    def test_same_commit_is_current_with_two_requests(self):
        def same(route):
            return {"object": {"sha": OLD}} if route == "/git/ref/heads/main" else self.fetch(route)
        self.assertEqual(self.run_check(fetch=same)["status"], "current")
        self.assertEqual(len(self.calls), 1)

    def test_failure_and_interrupted_attempt_throttle_and_do_not_advance_receipt(self):
        original = self.receipt.read_bytes()
        def offline(route):
            self.calls.append(route)
            raise OSError("fixture offline")
        self.assertEqual(self.run_check(fetch=offline)["status"], "error")
        self.assertEqual(self.run_check()["status"], "throttled")
        self.assertEqual(len(self.calls), 1)
        self.assertEqual(original, self.receipt.read_bytes())
        cache = json.loads((self.root / ".update-check.json").read_text())
        cache["result"] = "checking"  # Process disappeared after reserving the attempt.
        (self.root / ".update-check.json").write_text(json.dumps(cache))
        self.assertEqual(self.run_check()["status"], "throttled")
        self.assertEqual(self.run_check(100_000 + CHECK.DAY)["action"], "notify")

    def test_automatic_off_notify_persist_and_same_day_policy_change_does_not_retry(self):
        self.run_check()
        CHECK.set_policy(self.root, "automatic", "sources/UR-fixture: always update director pattern", now=100_001)
        self.assertEqual(CHECK.policy(self.root)["mode"], "automatic")
        self.assertEqual(self.run_check(100_002)["status"], "throttled")
        self.assertEqual(self.run_check(100_000 + CHECK.DAY)["action"], "request_safe_update")
        CHECK.set_policy(self.root, "off", "sources/UR-fixture: stop update checks")
        calls = len(self.calls)
        self.assertEqual(self.run_check(100_000 + CHECK.DAY * 2)["status"], "off")
        self.assertEqual(len(self.calls), calls)
        CHECK.set_policy(self.root, "notify", "sources/UR-fixture: notify me")
        self.assertEqual(self.run_check(100_000 + CHECK.DAY * 2)["action"], "notify")
        # A fresh process reads the same policy, independent of helper module memory.
        cache_path = self.root / ".update-check.json"
        cache = json.loads(cache_path.read_text())
        cache["last_attempt"] = time.time()
        cache_path.write_text(json.dumps(cache))
        output = subprocess.run([sys.executable, str(CHECK.__file__), "--root", str(self.root), "check", "--receipt", ".director/receipts/current.json"], capture_output=True, text=True, check=True)
        self.assertEqual(json.loads(output.stdout)["status"], "throttled")

    def test_corrupt_or_unknown_cache_fails_closed_without_network_or_repair(self):
        for content in ('{bad', '{"schema_version":2}', '{"schema_version":1,"last_attempt":"yesterday"}', '{"schema_version":1,"last_attempt":NaN}', json.dumps({'schema_version':1, 'last_attempt':1, 'baseline': {'source_sha': OLD, 'pattern_tree_sha':'corrupt'}}), '{"schema_version":1,"baseline":false}'):
            with self.subTest(content=content):
                path = self.root / ".update-check.json"
                path.write_text(content)
                self.assertEqual(self.run_check()["status"], "error")
                self.assertEqual(path.read_text(), content)
                self.assertEqual(self.calls, [])

    def test_corrupt_policy_and_missing_authorization_fail_closed_and_throttle(self):
        for value in ({"schema_version": 2, "mode": "automatic"}, {"schema_version": 1, "mode": "automatic"}):
            with self.subTest(value=value):
                path = self.root / "update-policy.json"
                path.write_text(json.dumps(value))
                cache = self.root / ".update-check.json"
                cache.unlink(missing_ok=True)
                before = path.read_bytes()
                self.assertEqual(self.run_check()["status"], "error")
                self.assertEqual(self.run_check()["status"], "throttled")
                self.assertEqual(path.read_bytes(), before)
                self.assertEqual(self.calls, [])
                with self.assertRaises(CHECK.CheckError):
                    CHECK.set_policy(self.root, "notify", "fixture instruction")

    def test_concurrent_checks_make_one_attempt_and_notification(self):
        entered, release = threading.Event(), threading.Event()
        def slow(route):
            if route == "/git/ref/heads/main":
                entered.set()
                self.assertTrue(release.wait(3))
            return self.fetch(route)
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(self.run_check, fetch=slow)
            self.assertTrue(entered.wait(3))
            second = pool.submit(self.run_check)
            self.assertEqual(second.result(timeout=3)["status"], "busy")
            self.assertEqual(CHECK.set_policy(self.root, "automatic", "fixture instruction")["status"], "busy")
            release.set()
            self.assertEqual(first.result(timeout=3)["action"], "notify")
        self.assertEqual(len(self.calls), 3)
        self.assertEqual(self.run_check()["status"], "throttled")

    def test_only_explicit_receipt_is_used_and_legacy_missing_source_needs_review(self):
        (self.root / "receipts/newer.json").write_text('{"source":{"sha":"wrong"}}')
        self.assertEqual(self.run_check()["source_sha"], OLD)
        (self.root / ".update-check.json").unlink()
        self.receipt.write_text('{"source_sha":"' + OLD + '"}')
        self.assertEqual(self.run_check()["status"], "error")
        self.assertEqual(self.run_check()["status"], "throttled")

    def test_changed_receipt_uses_new_baseline_and_optional_tree_identity(self):
        self.run_check()
        value = json.loads(self.receipt.read_text())
        value["source"].update(sha=NEW, pattern_tree_sha=CHANGED)
        self.receipt.write_text(json.dumps(value))
        self.calls.clear()
        self.assertEqual(self.run_check(100_000 + CHECK.DAY)["status"], "current")
        self.assertEqual(len(self.calls), 2)

    def test_candidate_keeps_published_base_no_fake_promotion_and_all_project_state_is_untouched(self):
        value = json.loads(self.receipt.read_text())
        value["local_candidate"] = {"status": "unpublished", "based_on": OLD, "delta": "fixture source"}
        self.receipt.write_text(json.dumps(value))
        for path in ("PROJECT.md", "ROLE_INDEX.md", "config.json", "roles/custom.md", "requests/open/request.md", "sources/original/input.txt", "activity.md", "decisions.md", "tools/requests.py"):
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(("fixture adapted bytes " + path).encode())
        before = {p.relative_to(self.root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in self.root.rglob("*") if p.is_file()}
        CHECK.set_policy(self.root, "automatic", "fixture standing authorization")
        self.assertEqual(self.run_check()["action"], "request_safe_update")
        for path, digest in before.items():
            self.assertEqual(hashlib.sha256((self.root / path).read_bytes()).hexdigest(), digest)
        self.assertEqual(json.loads(self.receipt.read_text())["source"]["sha"], OLD)
        self.assertEqual(set(p.name for p in self.root.iterdir()) - set(Path(p).parts[0] for p in before), {"update-policy.json", ".update-check.json", ".update-check.lock"})

    def test_invalid_response_or_receipt_and_symlinks_fail_closed(self):
        original = self.receipt.read_bytes()
        for source in ({"url": CHECK.SOURCE, "sha": OLD, "published": False}, {"url": "https://elsewhere", "sha": OLD, "published": True}):
            self.receipt.write_text(json.dumps({"source": source}))
            (self.root / ".update-check.json").unlink(missing_ok=True)
            self.assertEqual(self.run_check()["status"], "error")
            self.assertEqual(self.calls, [])
        self.receipt.write_bytes(original)
        (self.root / ".update-check.json").unlink()
        self.assertEqual(self.run_check(fetch=lambda route: {"object": {"sha": NEW}} if route == "/git/ref/heads/main" else {"tree": [], "truncated": True})["status"], "error")
        (self.root / ".update-check.json").unlink()
        outside = Path(self.tmp.name) / "outside.json"
        outside.write_text('private fixture')
        (self.root / ".update-check.json").symlink_to(outside)
        self.assertEqual(self.run_check()["status"], "error")
        self.assertEqual(outside.read_text(), 'private fixture')


if __name__ == "__main__":
    unittest.main()
