"""Disposable starter storage/install invariants; actual-agent trials stay separate."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

STARTER = Path(__file__).resolve().parents[2] / 'pattern/starter'
spec = importlib.util.spec_from_file_location('flat_starter_state', STARTER / 'payload/state.py')
state = importlib.util.module_from_spec(spec)
spec.loader.exec_module(state)
SCOPE = {'tasks': ['slides'], 'paths': ['decks'], 'audiences': ['customer']}


class StarterStateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / '.director'
        self.root.mkdir()
        state.atomic(self.root / 'state.json', state.encoded(state.initial_state(self.root)) + b'\n')
        self.serial = 0

    def stored(self):
        return json.loads((self.root / 'state.json').read_bytes())

    def tree(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob('*')
                if p.is_file() and p.name != '.lock'}

    def write(self, action, **data):
        self.serial += 1
        payload = {'op_id': f'test-op-{self.serial}', 'expected_revision': self.stored()['revision'], **data}
        return state.execute(self.root, action, payload), payload

    def capture(self, request_id='r1', raw='Exact original\r\n\n', **extra):
        return self.write('capture', text=raw, request={
            'id': request_id, 'summary': 'Customer slides', 'scope': copy.deepcopy(SCOPE),
            'acceptance': 'Usable scoped deck', 'owner': 'fixture-owner',
            'next_action': 'produce the artifact'}, **extra)

    def incident(self, request_id):
        result, _ = self.capture(request_id)
        correction, _ = self.write('capture', text='Use the public name on customer slides.\n',
            request_id=request_id, expected_request_revision=1)
        return self.write('incident', incident={
            'source_id': correction['source_id'], 'request_id': request_id, 'request_revision': 2,
            'scope': copy.deepcopy(SCOPE), 'evidence': 'Synthetic corrected artifact independently checked',
            'correction': 'Customer slides use the supplied public name; training can retain the internal name.',
            'hypothesis': False})

    def review_payload(self, batch, hypothesis=False, kind='knowledge'):
        return {'batch': copy.deepcopy(batch), 'review': {
            'summary': 'Three controlled customer-deck corrections support one scoped rule.',
            'reviewer': 'fixture-reviewer', 'spend': {'tokens': 'unknown', 'cost': 'unknown'},
            'proposals': [{'kind': kind, 'claim': 'Use the supplied public name on customer slides.',
                'scope': copy.deepcopy(SCOPE), 'basis': batch['ids'], 'hypothesis': hypothesis}]}}

    def three_incidents(self):
        for number in range(3):
            self.incident(f'outcome-{number}')
        return state.execute(self.root, 'review-batch', {'limit': 3, 'max_bytes': 12000})['batch']

    def test_exact_sources_attachments_steering_and_idempotent_revision_receipts(self):
        attachment = Path(self.temp.name) / 'binary.dat'
        attachment.write_bytes(b'\x00\xff\r\n')
        receipt, payload = self.capture(attachments=[{'path': str(attachment), 'name': 'original.bin'}])
        source = self.stored()['sources'][receipt['source_id']]
        self.assertEqual((self.root / source['path']).read_bytes(), b'Exact original\r\n\n')
        self.assertEqual((self.root / source['attachments'][0]['path']).read_bytes(), attachment.read_bytes())
        before = self.tree()
        replay = state.execute(self.root, 'capture', payload)
        self.assertTrue(replay['replayed'])
        self.assertEqual(replay['source_id'], receipt['source_id'])
        self.assertEqual(replay['request_revision'], 1)
        self.assertEqual(self.tree(), before)
        with self.assertRaisesRegex(ValueError, 'op_id conflict'):
            state.execute(self.root, 'capture', {**payload, 'text': 'Changed original'})
        self.assertEqual(self.tree(), before)
        amendment, _ = self.write('capture', text='Tiny correction\r\n', request_id='r1', expected_request_revision=1)
        req = self.stored()['requests']['r1']
        self.assertEqual(req['revision'], 2)
        self.assertEqual(req['sources'], [receipt['source_id'], amendment['source_id']])
        self.assertEqual((self.root / source['path']).read_bytes(), b'Exact original\r\n\n')

    def test_same_capture_operation_rejects_changed_external_source_or_attachment_bytes(self):
        source = Path(self.temp.name) / 'user-input.txt'
        attachment = Path(self.temp.name) / 'user-attachment.bin'
        source.write_bytes(b'Exact first user input\r\n')
        attachment.write_bytes(b'first attachment')
        payload = {'op_id': 'external-source-op', 'expected_revision': 0, 'source_file': str(source),
            'attachments': [{'path': str(attachment), 'name': 'original.bin'}],
            'request': {'id': 'external', 'summary': 'Source conflict test', 'scope': SCOPE,
                        'acceptance': 'Preserve original exact bytes', 'owner': 'owner'}}
        captured = state.execute(self.root, 'capture', payload)
        before = self.tree()
        source.write_bytes(b'Changed bytes at the same source path\n')
        with self.assertRaisesRegex(ValueError, 'conflict'):
            state.execute(self.root, 'capture', payload)
        self.assertEqual(self.tree(), before)
        source.write_bytes(b'Exact first user input\r\n')
        attachment.write_bytes(b'changed attachment')
        with self.assertRaisesRegex(ValueError, 'conflict'):
            state.execute(self.root, 'capture', payload)
        self.assertEqual(self.tree(), before)
        self.assertIn(captured['source_id'], self.stored()['sources'])

    def test_stale_invalid_and_duplicate_capture_do_not_change_committed_records(self):
        receipt, _ = self.capture()
        before = self.stored()
        cases = [
            ('update', {'request_id': 'r1', 'expected_request_revision': 0, 'source_id': receipt['source_id'], 'changes': {'status': 'accepted'}}),
            ('update', {'request_id': 'r1', 'expected_request_revision': 1, 'source_id': receipt['source_id'], 'changes': {'status': 'invented'}}),
            ('capture', {'text': 'Stale steering', 'request_id': 'r1', 'expected_request_revision': 0}),
            ('capture', {'text': 'Duplicate outcome', 'request': {'id': 'r1', 'summary': 'Duplicate', 'scope': SCOPE, 'acceptance': 'x', 'owner': 'owner'}}),
        ]
        for action, values in cases:
            with self.subTest(action=action, values=values):
                with self.assertRaises((ValueError, TypeError, KeyError)):
                    self.write(action, **values)
                self.assertEqual(self.stored(), before)
        with self.assertRaisesRegex(ValueError, 'stale state revision'):
            state.execute(self.root, 'update', {'op_id': 'stale-global', 'expected_revision': 0,
                'request_id': 'r1', 'expected_request_revision': 1, 'source_id': receipt['source_id'], 'changes': {}})
        self.assertEqual(self.stored(), before)

    def test_bounded_current_views_and_readonly_review_do_not_advance_cursor(self):
        for n in range(7):
            self.incident(f'request-{n}')
        before = self.tree()
        view = state.execute(self.root, 'status', {'limit': 2, 'max_bytes': 2500})
        self.assertLessEqual(len(state.encoded(view)), 2500)
        self.assertEqual(len(view['items']), 2)
        self.assertEqual(view['next_offset'], 2)
        self.assertEqual(view['total'], 7)
        self.assertNotIn('history', json.dumps(view))
        self.assertNotIn('correction', json.dumps(view))
        batch = state.execute(self.root, 'review-batch', {'limit': 3, 'max_bytes': 12000})
        self.assertEqual(batch['batch']['ids'], [1, 2, 3])
        self.assertEqual(self.stored()['review_cursor'], 0)
        pending = state.execute(self.root, 'pending', {'limit': 2, 'max_bytes': 2500})
        self.assertTrue(pending['review_due'])
        self.assertEqual(pending['pending_incidents'], 7)
        self.assertEqual(self.tree(), before)
        with self.assertRaisesRegex(ValueError, 'cannot skip'):
            state.execute(self.root, 'review-batch', {'offset': 1})
        with self.assertRaisesRegex(ValueError, 'stale query'):
            state.execute(self.root, 'status', {'at_revision': 0})

    def test_saved_proposal_and_review_are_bounded_and_available_to_a_fresh_process(self):
        batch = self.three_incidents()
        saved, _ = self.write('review-save', **self.review_payload(batch))
        for action, query in [('proposals', {'proposal_id': saved['proposal_ids'][0]}),
                              ('reviews', {'review_id': saved['review_id']}),
                              ('incidents', {'review_id': saved['review_id']})]:
            result = subprocess.run([sys.executable, str(STARTER / 'payload/state.py'), action,
                '--root', str(self.root), '--data-file', '-'], input=json.dumps({**query, 'max_bytes': 12000}),
                text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            view = json.loads(result.stdout)
            self.assertTrue(view['items'])
            self.assertLessEqual(len(result.stdout.encode()), 12001)
            self.assertNotIn('history', json.dumps(view))
            if action == 'proposals':
                self.assertEqual(view['items'][0]['scope'], SCOPE)
                self.assertEqual(view['items'][0]['basis'], [1, 2, 3])
                self.assertIn('public name', view['items'][0]['claim'])
            elif action == 'reviews':
                self.assertEqual(view['items'][0]['proposal_ids'], saved['proposal_ids'])
                self.assertIn('controlled', view['items'][0]['summary'])

    def test_cli_read_honors_actual_utf8_wire_budget(self):
        for number in range(3):
            self.capture(f'wire-{number}', raw='Bounded wire example')
        full = state.execute(self.root, 'status', {'limit': 3, 'max_bytes': 12000})
        budget = len(state.encoded(full)) + 1  # helper budgets the trailing newline too
        self.assertGreaterEqual(budget, 512)
        result = subprocess.run([sys.executable, str(STARTER / 'payload/state.py'), 'status',
            '--root', str(self.root), '--data-file', '-'],
            input=json.dumps({'limit': 3, 'max_bytes': budget}), text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(len(json.loads(result.stdout)['items']), 3)
        self.assertLessEqual(len(result.stdout.encode()), budget)

    def test_review_rejects_changed_or_skipped_prefix_without_silent_loss(self):
        batch = self.three_incidents()
        before = self.tree()
        for broken in [{**batch, 'cursor': 1}, {**batch, 'ids': [2, 3]}, {**batch, 'digest': '0' * 64}]:
            with self.subTest(batch=broken):
                with self.assertRaises(ValueError):
                    self.write('review-save', **self.review_payload(broken))
                self.assertEqual(self.tree(), before)
        self.assertEqual(self.stored()['review_cursor'], 0)
        self.assertEqual(self.stored()['reviews'], {})

    def test_asynchronous_review_survives_foreground_changes_and_appended_evidence(self):
        batch = self.three_incidents()
        revision_when_frozen = self.stored()['revision']
        # Foreground work advances state while the unchanged prefix is reviewed.
        self.incident('new-foreground-outcome')
        payload = {'op_id': 'async-review', 'expected_revision': revision_when_frozen,
                   **self.review_payload(batch)}
        before = self.tree()
        with self.assertRaisesRegex(ValueError, 'stale state revision'):
            state.execute(self.root, 'review-save', payload)
        self.assertEqual(self.tree(), before)
        payload['expected_revision'] = self.stored()['revision']
        result = state.execute(self.root, 'review-save', payload)
        self.assertEqual(result['review_cursor'], 3)
        self.assertEqual(state.execute(self.root, 'review-batch', {})['batch']['ids'], [4])
        self.assertEqual(self.stored()['reviews'][result['review_id']]['batch'], batch)

    def test_injected_before_and_after_commit_failures_preserve_review_and_replay(self):
        batch = self.three_incidents()
        payload = {'op_id': 'crash-review', 'expected_revision': self.stored()['revision'],
                   **self.review_payload(batch)}
        before = self.tree()
        with mock.patch.object(state, 'atomic', side_effect=OSError('injected before replace')):
            with self.assertRaises(OSError):
                state.execute(self.root, 'review-save', payload)
        self.assertEqual(self.tree(), before)
        original = state.atomic
        def committed_then_lost_receipt(path, data):
            original(path, data)
            raise OSError('injected receipt loss after durable replace')
        with mock.patch.object(state, 'atomic', side_effect=committed_then_lost_receipt):
            with self.assertRaises(OSError):
                state.execute(self.root, 'review-save', payload)
        committed = self.stored()
        self.assertEqual(committed['review_cursor'], 3)
        self.assertEqual(len(committed['reviews']), 1)
        replay = state.execute(self.root, 'review-save', payload)
        self.assertTrue(replay['replayed'])
        self.assertEqual(self.stored(), committed)
        self.assertEqual(len(self.stored()['proposals']), 1)

    def test_accepted_knowledge_remains_current_and_task_path_audience_scoped(self):
        batch = self.three_incidents()
        saved, _ = self.write('review-save', **self.review_payload(batch))
        query = {'task': 'slides', 'path': 'decks/customer.html', 'audience': 'customer'}
        self.assertEqual(state.execute(self.root, 'select', query)['items'], [])
        proposal = saved['proposal_ids'][0]
        self.write('decide', proposal_id=proposal, decision='accept', owner='fixture-owner',
                   reason='Supported by the three controlled customer-only corrections.')
        found = state.execute(self.root, 'select', query)['items']
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0]['scope'], SCOPE)
        for changed in [{'audience': 'training'}, {'task': 'code'}, {'path': 'unrelated/customer.html'}]:
            self.assertEqual(state.execute(self.root, 'select', {**query, **changed})['items'], [])
        before = self.tree()
        with self.assertRaises(ValueError):
            self.write('decide', proposal_id=proposal, decision='accept', owner='owner', reason='x',
                       scope={'tasks': ['*'], 'paths': ['*'], 'audiences': ['*']})
        self.assertEqual(self.tree(), before)
        self.write('decide', proposal_id=proposal, decision='retire', owner='fixture-owner', reason='Superseded with dated evidence retained.')
        self.assertEqual(state.execute(self.root, 'select', query)['items'], [])
        self.assertIn(proposal, self.stored()['knowledge'])
        self.assertEqual(len(self.stored()['proposals'][proposal]['decisions']), 2)

    def test_unknown_task_vocabulary_can_discover_bounded_scopes_without_claim_history(self):
        original, _ = self.capture()
        self.write('accept-rule', source_id=original['source_id'], request_id='r1', expected_request_revision=1,
            claim='Use public names on customer slides.', scope=copy.deepcopy(SCOPE), owner='owner',
            reason='Explicit scoped fixture instruction.')
        guessed = state.execute(self.root, 'select', {'task': 'presentations', 'path': 'decks/one.html', 'audience': 'external'})
        self.assertEqual(guessed['items'], [])
        catalog = state.execute(self.root, 'selectors', {'path': 'decks/one.html', 'limit': 1, 'max_bytes': 2000})
        self.assertEqual(len(catalog['items']), 1)
        self.assertEqual(set(catalog['items'][0]), {'id', 'scope'})
        self.assertEqual(catalog['items'][0]['scope'], SCOPE)
        self.assertNotIn('claim', json.dumps(catalog))
        self.assertNotIn('history', json.dumps(catalog))
        canonical = catalog['items'][0]['scope']
        found = state.execute(self.root, 'select', {'task': canonical['tasks'][0], 'path': 'decks/one.html',
            'audience': canonical['audiences'][0]})
        self.assertEqual(len(found['items']), 1)

    def test_scope_discovery_includes_descendants_without_widening_exact_applicability(self):
        original, _ = self.capture()
        child = {'tasks': ['slides'], 'paths': ['decks/customer'], 'audiences': ['customer']}
        sibling = {'tasks': ['slides'], 'paths': ['decks2/training'], 'audiences': ['training']}
        for number, scoped in enumerate([child, sibling]):
            self.write('accept-rule', source_id=original['source_id'], request_id='r1', expected_request_revision=1,
                claim=f'Scoped rule {number}', scope=scoped, owner='owner', reason='Explicit fixture decision.')
        found = state.execute(self.root, 'selectors', {'path': 'decks/', 'max_bytes': 3000})['items']
        self.assertEqual([x['scope'] for x in found], [child])
        self.assertEqual(len(state.execute(self.root, 'selectors', {'path': '.'})['items']), 2)
        query = {'task': 'slides', 'audience': 'customer'}
        self.assertEqual(state.execute(self.root, 'select', {**query, 'path': 'decks'})['items'], [])
        self.assertEqual(len(state.execute(self.root, 'select', {**query, 'path': 'decks/customer/one.html'})['items']), 1)

    def test_direct_owner_rule_retirement_preserves_source_and_decision_history(self):
        original, _ = self.capture()
        accepted, _ = self.write('accept-rule', source_id=original['source_id'], request_id='r1',
            expected_request_revision=1, claim='Use public names on customer slides.', scope=copy.deepcopy(SCOPE),
            owner='fixture-owner', reason='Explicit controlled owner instruction.')
        knowledge_id = accepted['knowledge_id']
        query = {'task': 'slides', 'path': 'decks/demo.html', 'audience': 'customer'}
        self.assertEqual(len(state.execute(self.root, 'select', query)['items']), 1)
        addendum, _ = self.write('capture', text='Retire the old scoped rule; keep its history.',
            request_id='r1', expected_request_revision=1)
        self.write('retire-knowledge', knowledge_id=knowledge_id, source_id=addendum['source_id'],
            request_id='r1', expected_request_revision=2, owner='fixture-owner',
            reason='A new supported direction supersedes the prior wording.')
        self.assertEqual(state.execute(self.root, 'select', query)['items'], [])
        retained = self.stored()['knowledge'][knowledge_id]
        self.assertEqual(retained['provenance']['source_id'], original['source_id'])
        self.assertEqual(retained['decisions'][-1]['source_id'], addendum['source_id'])
        self.assertFalse(retained['current'])
        before = self.tree()
        with self.assertRaisesRegex(ValueError, 'already retired'):
            self.write('retire-knowledge', knowledge_id=knowledge_id, source_id=addendum['source_id'],
                request_id='r1', expected_request_revision=2, owner='owner', reason='Duplicate new operation.')
        self.assertEqual(self.tree(), before)

    def test_acceptance_requires_supplied_evaluation_and_no_outstanding_approval(self):
        original, _ = self.capture()
        base = {'request_id': 'r1', 'expected_request_revision': 1, 'source_id': original['source_id']}
        before = self.tree()
        with self.assertRaisesRegex(ValueError, 'requires evaluate'):
            self.write('update', **base, changes={'status': 'accepted'})
        with self.assertRaisesRegex(ValueError, 'requires evaluate'):
            self.write('evaluate', **base, changes={'status': 'accepted'})
        self.assertEqual(self.tree(), before)
        self.write('update', **base, changes={'pending_approvals': ['Owner review remains']})
        base['expected_request_revision'] = 2
        before = self.tree()
        with self.assertRaisesRegex(ValueError, 'unresolved approvals'):
            self.write('evaluate', **base, evaluation='Artifact checked; approval still unresolved.', changes={'status': 'accepted'})
        self.assertEqual(self.tree(), before)
        self.write('evaluate', **base, evaluation='Supplied fixture owner approval and artifact evaluation complete.',
            changes={'status': 'accepted', 'pending_approvals': []})
        self.assertEqual(self.stored()['requests']['r1']['status'], 'accepted')
        self.assertEqual(self.stored()['requests']['r1']['history'][-1]['evaluation'],
            'Supplied fixture owner approval and artifact evaluation complete.')

    def test_hypothesis_is_not_promoted_and_structural_acceptance_does_not_create_roles(self):
        batch = self.three_incidents()
        saved, _ = self.write('review-save', **self.review_payload(batch, hypothesis=True))
        before = self.tree()
        with self.assertRaisesRegex(ValueError, 'hypotheses'):
            self.write('decide', proposal_id=saved['proposal_ids'][0], decision='accept', owner='owner', reason='Not sufficient.')
        self.assertEqual(self.tree(), before)
        # Separate installation for the structural proposal keeps the evidence prefix real.
        self.incident('structure-case')
        new_batch = state.execute(self.root, 'review-batch', {})['batch']
        saved, _ = self.write('review-save', **self.review_payload(new_batch, kind='structure'))
        accepted, _ = self.write('decide', proposal_id=saved['proposal_ids'][0], decision='accept', owner='owner', reason='Authorized proposal only; implementation separate.')
        self.assertTrue(accepted['implementation_required'])
        self.assertEqual(self.stored()['knowledge'], {})
        self.assertFalse((self.root / 'roles').exists())


class StarterInstallationTests(unittest.TestCase):
    def command(self, *args):
        return subprocess.run([sys.executable, str(STARTER / 'install.py'), *args], text=True, capture_output=True)

    def tree(self, root):
        return {str(p.relative_to(root)): p.read_bytes() for p in root.rglob('*') if p.is_file()}

    def test_empty_install_then_identical_noop_preserves_live_state_and_optional_roles(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            first = self.command('install', '--target', str(root))
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)
            self.assertTrue((root / '.director/START.md').is_file())
            (root / '.director/roles').mkdir()
            (root / '.director/roles/art.md').write_bytes(b'Existing project Art authority.\n')
            store = root / '.director'
            payload = {'op_id': 'installed-source', 'expected_revision': 0, 'text': 'A real mutable fixture source.',
                'request': {'id': 'pending', 'summary': 'Pending', 'scope': SCOPE, 'acceptance': 'Finish', 'owner': 'owner'}}
            state.execute(store, 'capture', payload)
            before = self.tree(root)
            again = self.command('install', '--target', str(root))
            self.assertEqual(again.returncode, 0, again.stdout + again.stderr)
            self.assertEqual(self.tree(root), before)

    def test_plan_and_refused_conflicting_install_preserve_every_byte(self):
        for files in [{'.producer/config.json': b'{"format":"retained-tracker"}\n'}, {'.director/legacy.md': b'Existing authority\r\n'}]:
            with self.subTest(files=files), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                for rel, raw in files.items():
                    p = root / rel; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(raw)
                before = self.tree(root)
                had_director = (root / '.director').exists()
                planned = self.command('plan', '--target', str(root))
                self.assertEqual(self.tree(root), before)
                refused = self.command('install', '--target', str(root))
                self.assertNotEqual(refused.returncode, 0, refused.stdout + refused.stderr)
                self.assertEqual(self.tree(root), before)
                self.assertEqual((root / '.director').exists(), had_director)

    def test_first_use_with_existing_meeting_notes_preserves_ordinary_project_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            notes = root / 'meeting-notes.txt'
            notes.write_bytes(b'Exact meeting notes\r\nwith an asset\r\n')
            asset = root / 'reference.bin'
            asset.write_bytes(b'\x00\xffunchanged')
            installed = self.command('install', '--target', str(root))
            self.assertEqual(installed.returncode, 0, installed.stdout + installed.stderr)
            self.assertEqual(notes.read_bytes(), b'Exact meeting notes\r\nwith an asset\r\n')
            self.assertEqual(asset.read_bytes(), b'\x00\xffunchanged')
            self.assertTrue((root / '.director/START.md').is_file())

    def test_rollback_refuses_an_actual_live_writer_lock_then_removes_only_owned_files(self):
        import fcntl
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            notes = root / 'meeting-notes.txt'; notes.write_bytes(b'Preserved outside install.\n')
            installed = self.command('install', '--target', str(root))
            self.assertEqual(installed.returncode, 0, installed.stdout + installed.stderr)
            receipt = root / '.director/install.json'
            with (root / '.director/.lock').open('a+b') as lock:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                before = self.tree(root)
                refused = self.command('rollback', '--receipt', str(receipt))
                self.assertNotEqual(refused.returncode, 0)
                self.assertRegex(refused.stdout + refused.stderr, 'busy|lock')
                self.assertEqual(self.tree(root), before)
            rolled = self.command('rollback', '--receipt', str(receipt))
            self.assertEqual(rolled.returncode, 0, rolled.stdout + rolled.stderr)
            self.assertEqual(notes.read_bytes(), b'Preserved outside install.\n')
            self.assertFalse((root / '.director').exists())
            self.assertFalse((root / 'AGENTS.md').exists())

    def test_payload_is_separately_manifested_and_self_contained(self):
        manifest = json.loads((STARTER / 'manifest.json').read_text())
        declared = set(manifest['payload'])
        actual = {p.name for p in (STARTER / 'payload').iterdir() if p.is_file()}
        self.assertEqual(actual, declared)
        self.assertFalse(any(name in declared for name in ['ROLE_INDEX.md', 'REQUEST_MANAGER.md', 'RECORDER.md']))
        for name in declared:
            self.assertTrue((STARTER / 'payload' / name).is_file())
        legacy = json.loads((STARTER.parent / 'manifest.json').read_text())
        self.assertFalse(any(p.startswith('starter/') for p in legacy['base_files'] + legacy['tracked_files']))


if __name__ == '__main__':
    unittest.main()
