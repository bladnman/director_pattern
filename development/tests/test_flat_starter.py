"""Fresh starter-3 boundary and deferred canonical-note behavior, not model behavior.

The unsupported experimental-v2 test/source bytes remain in Git history. These
checks execute the current installation rather than bless its former flat store.
"""
import fcntl
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import uuid
import unittest
from unittest import mock

STARTER = Path(__file__).resolve().parents[2] / 'pattern/starter'
spec = importlib.util.spec_from_file_location('starter_installer', STARTER / 'install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)
SCOPE = {'tasks': ['slides'], 'paths': ['decks/customer'], 'audiences': ['customer']}


class StarterInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.target = Path(self.temp.name) / 'project'

    def tree(self):
        return {str(p.relative_to(self.target)): p.read_bytes() for p in self.target.rglob('*') if p.is_file()}

    def cli(self, script, *args, data=None, ok=True):
        cmd = [sys.executable, '-B', str(self.target / '.director' / script), *args]
        result = subprocess.run(cmd, input=json.dumps(data) if data is not None else None,
                                text=True, capture_output=True)
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        return json.loads(result.stdout) if result.returncode == 0 else result

    def install(self):
        return installer.operation('install', self.target)

    def test_plan_deterministic_and_notes_assets_preserved(self):
        self.target.mkdir()
        (self.target / 'meeting-notes.txt').write_bytes(b'Exact notes\r\n')
        (self.target / 'assets').mkdir()
        (self.target / 'assets/image.bin').write_bytes(b'\x00\xff')
        before = self.tree()
        self.assertEqual(installer.operation('plan', self.target), installer.operation('plan', self.target))
        result = self.install()
        self.assertTrue(result['changed'])
        for path, data in before.items(): self.assertEqual((self.target / path).read_bytes(), data)
        config = json.loads((self.target / '.director/config.json').read_bytes())
        self.assertEqual(config['request_store']['format'], 'director-request-bundles')
        self.assertFalse((self.target / '.director/state.json').exists())
        self.assertFalse((self.target / '.director/state.py').exists())
        self.assertEqual(self.cli('requests.py', 'validate'), {'valid': 0})
        receipt = json.loads((self.target / '.director/install.json').read_bytes())
        self.assertEqual(receipt['starter_version'], 3)
        # Instruction wording / static only: the readable revision is recorded beside the format number.
        self.assertEqual(receipt['starter_revision'], '3.4')
        self.assertEqual(result['starter_revision'], '3.4')
        self.assertEqual(receipt['technical_check']['acceptance'], 'not implied')
        for path, digest in receipt['managed'].items():
            self.assertEqual(hashlib.sha256((self.target / path).read_bytes()).hexdigest(), digest)

    def test_conflicting_startup_trackers_and_experimental_v2_refuse_without_writes(self):
        for name in installer.GUARDS:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp)
                path = target / name
                if name.endswith('.md'): path.write_bytes(b'Owned instructions\n')
                else: path.mkdir(); (path / 'retained').write_bytes(b'Private original')
                before = {str(p.relative_to(target)): p.read_bytes() for p in target.rglob('*') if p.is_file()}
                with self.assertRaisesRegex(ValueError, 'existing startup/tracker'):
                    installer.operation('install', target)
                self.assertEqual(before, {str(p.relative_to(target)): p.read_bytes() for p in target.rglob('*') if p.is_file()})

    def test_identical_reinstall_preserves_source_records_local_roles_and_policy(self):
        self.install()
        self.new_request()
        (self.target / '.director/roles').mkdir()
        (self.target / '.director/roles/local.md').write_text('Owned responsibility')
        (self.target / '.director/update-policy.json').write_text('{"schema_version":1,"mode":"off"}')
        before = self.tree()
        self.assertFalse(self.install()['changed'])
        self.assertEqual(self.tree(), before)
        (self.target / '.director/WORKER.md').write_text('Local adaptation')
        before = self.tree()
        with self.assertRaisesRegex(ValueError, 'drift'): self.install()
        self.assertEqual(self.tree(), before)

    def test_pristine_rollback_uses_native_writer_lock_and_preserves_unrelated_files(self):
        self.target.mkdir(); (self.target / 'notes.txt').write_text('Keep')
        self.install()
        lockpath = self.target / '.director/.requests.lock'
        with lockpath.open('a+b') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            before = self.tree()
            with self.assertRaisesRegex(ValueError, 'busy'):
                installer.rollback(self.target / '.director/install.json')
            self.assertEqual(self.tree(), before)
        installer.rollback(self.target / '.director/install.json')
        self.assertEqual((self.target / 'notes.txt').read_text(), 'Keep')
        self.assertFalse((self.target / '.director').exists())

    def test_older_receipt_without_starter_revision_is_still_a_known_format(self):
        # Receipts written before starter_revision existed stay valid; static fixture, not a migration test.
        self.install()
        receipt_path = self.target / '.director/install.json'
        receipt = json.loads(receipt_path.read_bytes())
        del receipt['starter_revision']
        receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')
        self.assertFalse(self.install()['changed'])
        installer.rollback(receipt_path)
        self.assertFalse((self.target / '.director').exists())

    def test_rollback_refuses_new_work(self):
        self.install(); self.new_request(); before = self.tree()
        with self.assertRaisesRegex(ValueError, 'new managed-area work'):
            installer.rollback(self.target / '.director/install.json')
        self.assertEqual(self.tree(), before)

    def event_id(self): return uuid.uuid4().hex

    def new_request(self):
        raw = Path(self.temp.name) / ('input-' + self.event_id() + '.txt'); raw.write_bytes(b'Exact source\r\n')
        event = 'capture-' + self.event_id()
        source = self.cli('requests.py', 'capture', '--raw-file', str(raw), '--event-id', event)
        sid = source['source_id']
        record = self.cli('requests.py', 'create', '--source-id', sid, '--title', 'Slides', '--event-id', 'create-' + self.event_id())
        return record, sid, source['input']['sha256']

    def append(self, record, sid, source_hash, kind='incident', **extra):
        entry = {'schema': 1, 'id': 'learning-' + self.event_id(), 'kind': kind, 'source_id': sid,
                 'source_sha256': source_hash, 'request_revision': record['revision'],
                 'scope': SCOPE, 'owner': 'fixture-owner', 'text': 'Scoped observed correction', **extra}
        query = {'request_id': record['id'], 'expected_revision': record['revision'], 'entry': entry}
        saved = self.cli('canonical_learning.py', 'append', data=query)
        return entry, query, saved

    def test_bounded_current_views_snapshot_wire_budget_and_no_history(self):
        self.install()
        records = [self.new_request()[0] for _ in range(3)]
        result = self.cli('requests.py', 'status', '--limit', '1', '--max-bytes', '1500')
        self.assertEqual(result['total'], 3); self.assertEqual(result['next_offset'], 1)
        self.assertNotIn('history', result['items'][0])
        current = self.cli('requests.py', 'current', records[0]['id'])
        self.assertNotIn('history', current['items'][0])
        self.new_request()
        self.cli('requests.py', 'status', '--at-snapshot', result['snapshot'], ok=False)
        result = subprocess.run([sys.executable, '-B', str(self.target / '.director/requests.py'), 'status', '--limit', '1', '--max-bytes', '1500'], capture_output=True)
        self.assertEqual(result.returncode, 0); self.assertLessEqual(len(result.stdout), 1500)

    def test_learning_save_is_atomic_replayable_and_recoverable_across_requests(self):
        self.install()
        for _ in range(3):
            record, sid, h = self.new_request()
            self.append(record, sid, h, hypothesis=False)
        pending = self.cli('canonical_learning.py', 'pending', data={})
        self.assertEqual(pending['total'], 3)
        # No save means no cursor movement. One review includes all durable output/proposals.
        self.assertEqual(self.cli('canonical_learning.py', 'pending', data={})['total'], 3)
        current = self.cli('requests.py', 'show', record['id'])
        entry, payload, saved = self.append(current, sid, h, kind='review',
            incidents=[{'id': i['id'], 'digest': i['digest']} for i in pending['items']],
            proposals=[], spend={'tokens': 'unknown', 'cost': 'unknown'})
        self.assertEqual(self.cli('canonical_learning.py', 'pending', data={})['total'], 0)
        self.assertTrue(self.cli('canonical_learning.py', 'append', data=payload)['idempotent'])
        self.assertEqual(self.cli('canonical_learning.py', 'reviews', data={})['items'][0]['id'], entry['id'])
        altered = json.loads(json.dumps(payload)); altered['entry']['text'] = 'Changed payload'
        self.cli('canonical_learning.py', 'append', data=altered, ok=False)

    def test_explicit_rule_scoped_discovery_select_and_retirement(self):
        self.install(); record, sid, h = self.new_request()
        rule, _, _ = self.append(record, sid, h, kind='rule')
        scopes = self.cli('canonical_learning.py', 'selectors', data={'path': 'decks'})
        self.assertEqual(scopes['total'], 1); self.assertNotIn('text', scopes['items'][0])
        self.assertEqual(self.cli('canonical_learning.py', 'select', data={'task':'slides','audience':'customer','path':'decks/customer/a.html'})['total'],1)
        self.assertEqual(self.cli('canonical_learning.py', 'select', data={'task':'slides','audience':'training','path':'decks/training/a.html'})['total'],0)
        record = self.cli('requests.py', 'show', record['id'])
        self.append(record, sid, h, kind='retire', knowledge_id=rule['id'])
        self.assertEqual(self.cli('canonical_learning.py', 'selectors', data={})['total'],0)

    def test_established_backend_has_only_the_reviewed_lock_fence_and_checker_is_exact(self):
        upstream = (STARTER.parent/'engine/tools/requests.py').read_text()
        installed = (STARTER/'payload/request_store.py').read_text()
        init_fence = '            if not lock.exists() or os.fstat(stream.fileno()).st_ino != lock.stat().st_ino:\n                fail("Retired writer lock; reopen the current installation")\n'
        write_fence = '            lock_path = safe(self.team / ".requests.lock")\n            if not lock_path.exists() or os.fstat(stream.fileno()).st_ino != lock_path.stat().st_ino:\n                fail("Retired writer lock; reopen the current installation")\n            if json.loads(safe(self.team / "config.json").read_bytes()) != self.config:\n                fail("Store configuration changed; reopen the current installation")\n'
        self.assertEqual(installed.replace(init_fence, '').replace(write_fence, ''), upstream)
        self.assertEqual((STARTER/'payload/update_check.py').read_bytes(), (STARTER.parent/'engine/tools/update_check.py').read_bytes())

    def test_windows_runtime_refuses_without_changes(self):
        with mock.patch.object(installer, 'fcntl', None):
            with self.assertRaisesRegex(ValueError, 'POSIX'): self.install()
        self.assertFalse(self.target.exists())


if __name__ == '__main__': unittest.main()
