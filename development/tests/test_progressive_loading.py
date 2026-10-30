"""Static load-path/scenario regression harness; never proof of host behavior."""
import json
from pathlib import Path
import tempfile
import unittest

from development.startup_loading import (
    AUTHORITY, BASE, DIRECTOR_ACTION, INDEX, PATTERN, PROJECT, STARTUP,
    capability_protocols, inventory,
)
from development.tests.test_package import markdown_links


class ProgressiveLoadingTests(unittest.TestCase):
    def test_every_before_use_capability_reaches_its_independently_required_contracts(self):
        # Expectations name preserved obligations, independent of the table parser.
        expected = {
            'direction': {'engine/DIRECTION.md'},
            'staffing': {'engine/ROLES.md', 'engine/MODELS.md', 'engine/IDENTITIES.md',
                         'engine/ASSIGNMENT.md', 'engine/STATE.md'},
            'persistence': {'engine/STATE.md', 'engine/RECORDER.md',
                            'engine/references/RECORDS.md', 'engine/references/TOOLING.md'},
            'identity': {'engine/IDENTITIES.md'},
            'setup': {'engine/DIRECTION.md'},
            'updates': {'engine/references/UPDATES.md', 'engine/references/STARTUP.md',
                        'engine/references/BOUNDARY.md'},
            'maintenance': {'engine/ROLES.md'},
            'external action': set(),  # Local authority and selected runbook, not a generic permission.
        }
        actual = capability_protocols()
        self.assertEqual(set(actual), set(expected))
        for capability, required in expected.items():
            with self.subTest(capability=capability):
                self.assertTrue(actual[capability]['trigger'])
                self.assertLessEqual(required, actual[capability]['paths'])
                for path in actual[capability]['paths']:
                    self.assertTrue((PATTERN / path).is_file(), path)

    def test_all_reachable_reference_paths_stay_inside_manifest_payload(self):
        manifest = json.loads((PATTERN / 'manifest.json').read_text())
        payload = set(manifest['base_files']) | set(manifest['tracked_files'])
        # Start at every real generic definition and every triggered protocol.
        queue = {PATTERN / name for names in STARTUP.values() for name in names}
        queue.add(PATTERN / 'engine/RECORDER.md')
        queue |= {PATTERN / name for row in capability_protocols().values() for name in row['paths']}
        seen = set()
        while queue:
            document = queue.pop().resolve()
            if document in seen:
                continue
            seen.add(document)
            self.assertTrue(document.is_relative_to(PATTERN), document)
            self.assertIn(document.relative_to(PATTERN).as_posix(), payload)
            if document.suffix == '.md':
                for link in markdown_links(document):
                    target = (document.parent / link).resolve()
                    self.assertTrue(target.exists(), (document, link))
                    queue.add(target)
        self.assertTrue({(PATTERN / p).resolve() for p in DIRECTOR_ACTION} <= seen)
        self.assertIn((PATTERN / 'engine/references/TOOLING.md').resolve(), seen)

    def test_reply_and_staffing_scenarios_preserve_distinct_loading(self):
        for role in ('director', 'request-manager'):
            startup = STARTUP[role]
            self.assertFalse(startup & DIRECTOR_ACTION)
            # Inspect the actual startup declaration, not all advisory/action links.
            text = (PATTERN / next(p for p in startup if p.endswith(('DIRECTOR.md', 'REQUEST_MANAGER.md')))).read_text()
            required = text.split('Startup required:', 1)[1].split('\n\n', 1)[0]
            self.assertNotIn('DIRECTION.md', required)
            self.assertNotIn('MODELS.md', required)
            action = startup | capability_protocols()['direction']['paths'] | capability_protocols()['staffing']['paths']
            self.assertLessEqual(DIRECTOR_ACTION, action)
        worker = STARTUP['analysis-worker']
        self.assertFalse(worker & DIRECTOR_ACTION)
        self.assertIn('engine/WORKER.md', worker)
        self.assertNotIn('PROJECT.md', worker)

    def test_custom_unphased_and_triggered_guards_remain_reachable_after_engine_replacement(self):
        # A real filesystem fixture with nested local authority, a task runbook,
        # and a separately gated release runbook. This checks preservation and
        # reachability at both phases; it does not infer arbitrary prose semantics.
        import shutil
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / '.director'
            shutil.copytree(PATTERN / 'engine', root / 'engine')
            (root / 'roles').mkdir()
            fixtures = {
                'PROJECT.md': PROJECT, 'ROLE_INDEX.md': INDEX, 'AUTHORITY.md': AUTHORITY,
                'roles/reviewer.md': '# Reviewer\nStartup required: [shared](../AUTHORITY.md), [local](../LOCAL.md).\nTask required before review: [rules](../TASK_RULES.md).\nAction required before release: [gate](../RELEASE.md).\n',
                'LOCAL.md': '# Required local authority\nRead [nested guard](NESTED.md).\n',
                'NESTED.md': 'Do not expose confidential source material.\n',
                'TASK_RULES.md': '# Review rules\nRead [nested guard](NESTED.md).\n',
                'RELEASE.md': '# Release gate\nRead [nested guard](NESTED.md). Explicit user publication authority is required.\n',
            }
            for name, content in fixtures.items():
                (root / name).write_text(content)
            before = {name: (root / name).read_bytes() for name in fixtures}
            shutil.rmtree(root / 'engine')
            shutil.copytree(PATTERN / 'engine', root / 'engine')
            self.assertEqual(before, {name: (root / name).read_bytes() for name in fixtures})
            role = root / 'roles/reviewer.md'
            direct = set(markdown_links(role))
            self.assertEqual(direct, {'../AUTHORITY.md', '../LOCAL.md', '../TASK_RULES.md', '../RELEASE.md'})
            for branch in ('LOCAL.md', 'TASK_RULES.md', 'RELEASE.md'):
                self.assertEqual(set(markdown_links(root / branch)), {'NESTED.md'})
                self.assertIn('confidential', (root / 'NESTED.md').read_text())
            self.assertIn('Explicit user publication authority', (root / 'RELEASE.md').read_text())

    def test_chunk_evidence_fixture_detects_inner_and_outer_omission(self):
        # Trial-evaluation fixture only. Compare actual visible text/ranges with
        # a known source; this is neither an installed reader nor an agent check.
        source = "Authority 🦫\n" + "Preserve every guard.\n" * 80
        packets = [{'start': start, 'end': min(start + 71, len(source)),
                    'total': len(source), 'text': source[start:start + 71]}
                   for start in range(0, len(source), 71)]

        def complete(visible):
            try:
                received = json.loads(visible)
                cursor = 0
                for packet in received:
                    if packet.get('error') or packet['start'] != cursor:
                        return False
                    if packet['total'] != len(source) or packet['end'] <= cursor:
                        return False
                    if packet['text'] != source[cursor:packet['end']]:
                        return False
                    cursor = packet['end']
                return cursor == len(source)
            except (ValueError, KeyError, TypeError):
                return False

        visible = json.dumps(packets)
        # Individually small inner results can still overrun an outer budget.
        self.assertLess(max(len(json.dumps(p).encode()) for p in packets), 256)
        self.assertGreater(len(visible.encode()), 256)
        self.assertTrue(complete(visible))
        self.assertFalse(complete(visible[:len(visible) // 2]))  # Outer aggregate lost.
        self.assertFalse(complete(json.dumps(packets[:2] + packets[3:])))  # Missing range.
        damaged = [dict(p) for p in packets]
        damaged[2]['text'] = '[tool output elided]'
        self.assertFalse(complete(json.dumps(damaged)))  # Inner tool elision.
        damaged[2] = {'error': 'read failed'}
        self.assertFalse(complete(json.dumps(damaged)))
        self.assertTrue(complete(json.dumps(packets)))  # Recovery includes all text.

    def test_inventory_counts_actual_bytes_without_claiming_timing(self):
        rows = inventory()
        self.assertEqual(len(rows), 6)
        for role in STARTUP:
            baseline, candidate = [r for r in rows if r['role'] == role]
            self.assertEqual(baseline['project_fixture_bytes'], candidate['project_fixture_bytes'])
            self.assertGreater(candidate['shared_package_bytes'], 0)
            self.assertLessEqual(candidate['dependency_stages'], baseline['dependency_stages'])
        director = [r for r in rows if r['role'] == 'director']
        self.assertLess(director[1]['shared_package_bytes'], director[0]['shared_package_bytes'] / 2)


if __name__ == '__main__':
    unittest.main()
