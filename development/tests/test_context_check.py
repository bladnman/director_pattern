"""Installed, model-free byte qualification; these tests do not probe native admission."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
HELPER = ROOT / 'pattern/starter/payload/context_check.py'
module_spec = importlib.util.spec_from_file_location('context_check', HELPER)
helper = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(helper)


class ContextCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'AGENTS.md').write_bytes(b'abcdefghij')
        (self.root / 'nested').mkdir()
        (self.root / 'nested/AGENTS.md').write_bytes(b'klmnop')
        self.spec = {'schema': 1, 'chain': [
            {'path': 'AGENTS.md', 'required_through_bytes': 8},
            {'path': 'nested/AGENTS.md', 'required_through_bytes': 3}],
            'cap': {'bytes': 16, 'provenance': 'effective'},
            'evidence': 'caller-observation: selected route and cap'}
        self.spec_file = self.root / 'spec.json'

    def run_check(self, ok=True, bound=12000):
        self.spec_file.write_text(json.dumps(self.spec))
        before = {p.relative_to(self.root): (p.read_bytes(), p.stat().st_mtime_ns)
                  for p in self.root.rglob('*') if p.is_file()}
        result = subprocess.run([sys.executable, '-B', str(HELPER), '--root', str(self.root),
                                 '--spec', str(self.spec_file), '--max-output-bytes', str(bound)],
                                capture_output=True)
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        self.assertEqual(result.stderr, b'')
        self.assertLessEqual(len(result.stdout), max(bound, helper.MIN_OUTPUT))
        after = {p.relative_to(self.root): (p.read_bytes(), p.stat().st_mtime_ns)
                 for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(before, after)
        response = json.loads(result.stdout)
        self.assertEqual(response['actual_admission'], 'unqualified')
        return response

    def test_exact_cap_complete_hashes_raw_counts_and_readonly(self):
        result = self.run_check()
        self.assertEqual(result['declared_budget'], 'under')
        self.assertEqual(result['total_raw_bytes'], 16)
        self.assertEqual(result['total_counted_bytes'], 16)
        self.assertEqual([r['cumulative_raw_bytes'] for r in result['files']], [10, 16])
        self.assertEqual([r['cumulative_counted_bytes'] for r in result['files']], [10, 16])
        row = result['files'][0]
        self.assertEqual(row['sha256'], hashlib.sha256(b'abcdefghij').hexdigest())
        self.assertEqual(row['predicted_raw_budget'],
                         {'status': 'read', 'read_interval': [0, 10], 'omitted_interval': [10, 10]})
        self.assertTrue(all(r['required_boundary_fits'] for r in result['files']))
        self.assertIn('global versus project', ' '.join(result['limits']))

    def test_overflow_later_file_partial_and_required_boundary_outside_cut(self):
        self.spec['cap']['bytes'] = 12
        result = self.run_check()
        self.assertEqual(result['declared_budget'], 'over')
        row = result['files'][1]
        self.assertEqual(row['predicted_raw_budget'],
                         {'status': 'truncated', 'read_interval': [0, 2], 'omitted_interval': [2, 6]})
        self.assertFalse(row['required_boundary_fits'])
        self.assertEqual(row['cumulative_counted_bytes'], 12)

    def test_required_boundary_exact_cut_and_later_omission(self):
        self.spec['cap']['bytes'] = 8
        result = self.run_check()
        self.assertTrue(result['files'][0]['required_boundary_fits'])
        self.assertEqual(result['files'][1]['predicted_raw_budget'],
                         {'status': 'omitted', 'read_interval': [0, 0], 'omitted_interval': [0, 6]})
        self.assertFalse(result['files'][1]['required_boundary_fits'])

    def test_order_is_explicit_no_autodiscovery(self):
        (self.root / 'AGENTS.override.md').write_bytes(b'ignored override')
        self.spec['chain'].reverse()
        self.spec['cap']['bytes'] = 6
        result = self.run_check()
        self.assertEqual([r['path'] for r in result['files']], ['nested/AGENTS.md', 'AGENTS.md'])
        self.assertEqual(result['files'][0]['predicted_raw_budget']['status'], 'read')
        self.assertEqual(result['files'][1]['predicted_raw_budget']['status'], 'omitted')

    def test_multibyte_raw_cut_does_not_claim_valid_utf8_slice_or_return_content(self):
        data = 'a🎯é'.encode('utf-8')
        (self.root / 'AGENTS.md').write_bytes(data)
        self.spec['chain'] = [{'path': 'AGENTS.md', 'required_through_bytes': 5}]
        self.spec['cap']['bytes'] = 3
        result = self.run_check()
        self.assertEqual(result['total_raw_bytes'], 7)
        self.assertEqual(result['files'][0]['sha256'], hashlib.sha256(data).hexdigest())
        self.assertEqual(result['files'][0]['predicted_raw_budget']['read_interval'], [0, 3])
        self.assertFalse(result['files'][0]['required_boundary_fits'])
        self.assertIn('not valid or semantically complete', ' '.join(result['limits']))
        self.assertNotIn('🎯', json.dumps(result, ensure_ascii=False))

    def test_cap_provenance_and_nulls_never_qualify_native_admission(self):
        for provenance in ('effective', 'default', 'unknown'):
            for cap in (12, None):
                with self.subTest(provenance=provenance, cap=cap):
                    self.spec['cap'] = {'bytes': cap, 'provenance': provenance}
                    result = self.run_check()
                    unknown = cap is None or provenance == 'unknown'
                    self.assertEqual(result['declared_budget'], 'unknown' if unknown else 'over')
                    self.assertEqual(result['prediction_basis'], 'unknown' if unknown else
                                     'conditional_default' if provenance == 'default' else 'declared_effective')
                    if unknown:
                        self.assertIsNone(result['total_counted_bytes'])
                        self.assertIsNone(result['files'][0]['required_boundary_fits'])
                        self.assertEqual(result['files'][0]['predicted_raw_budget']['status'], 'unknown')

    def test_missing_required_boundary_is_explicit_unknown(self):
        self.spec['chain'][0]['required_through_bytes'] = None
        self.assertIsNone(self.run_check()['files'][0]['required_boundary_fits'])

    def test_invalid_cap_and_boundary_types_and_outside_file(self):
        for value in (0, -1, True, '100', 1.5, helper.MAX_CAP + 1):
            with self.subTest(cap=value):
                self.spec['cap']['bytes'] = value
                self.run_check(ok=False)
        self.spec['cap']['bytes'] = 16
        for value in (-1, True, '8', 11):
            with self.subTest(boundary=value):
                self.spec['chain'][0]['required_through_bytes'] = value
                self.run_check(ok=False)

    def test_aggregate_boundary_fit_only_covers_positive_assertions(self):
        for boundary in (None, 0):
            self.spec['chain'] = [{'path': 'AGENTS.md', 'required_through_bytes': boundary}]
            result = self.run_check()
            self.assertIsNone(result['asserted_required_boundaries_fit'])
            self.assertEqual(result['asserted_boundary_count'], 0)
            self.assertEqual(result['unasserted_path_count'], 1)
        self.spec['chain'] = [{'path': 'AGENTS.md', 'required_through_bytes': None},
                              {'path': 'nested/AGENTS.md', 'required_through_bytes': 3}]
        result = self.run_check()
        self.assertTrue(result['asserted_required_boundaries_fit'])
        self.assertEqual(result['asserted_boundary_count'], 1)
        self.assertEqual(result['unasserted_path_count'], 1)
        self.spec['cap']['bytes'] = 12
        self.assertFalse(self.run_check()['asserted_required_boundaries_fit'])
        self.spec['cap']['provenance'] = 'unknown'
        self.assertIsNone(self.run_check()['asserted_required_boundaries_fit'])

    def test_unsafe_paths_missing_nonregular_and_duplicates_fail(self):
        for name in ('/etc/passwd', '../AGENTS.md', 'nested/../AGENTS.md', './AGENTS.md',
                     'nested//AGENTS.md', 'missing.md', 'nested', 'bad\npath'):
            with self.subTest(name=name):
                self.spec['chain'][0]['path'] = name
                self.run_check(ok=False)
        self.spec['chain'][0]['path'] = 'nested/AGENTS.md'
        self.assertIn('duplicate', self.run_check(ok=False)['gap'])

    def test_symlink_file_directory_root_and_spec_are_rejected(self):
        (self.root / 'linked.md').symlink_to(self.root / 'AGENTS.md')
        (self.root / 'linked-dir').symlink_to(self.root / 'nested')
        for name in ('linked.md', 'linked-dir/AGENTS.md'):
            self.spec['chain'][0]['path'] = name
            self.run_check(ok=False)
        self.spec['chain'][0]['path'] = 'AGENTS.md'
        self.spec_file.write_text(json.dumps(self.spec))
        (self.root / 'linked-spec.json').symlink_to(self.spec_file)
        with self.assertRaises(OSError):
            helper.load_spec(self.root / 'linked-spec.json')
        with self.assertRaises(OSError):
            helper.check(self.root / 'linked-dir', self.spec)

    def test_fifo_is_rejected_without_blocking(self):
        os.mkfifo(self.root / 'pipe')
        self.spec['chain'][0]['path'] = 'pipe'
        self.run_check(ok=False)

    def test_access_denied_and_change_during_measurement(self):
        original = helper.open_selected
        with patch.object(helper, 'open_selected', side_effect=PermissionError):
            with self.assertRaises(PermissionError):
                helper.check(self.root, self.spec)
        calls = 0

        def changed(fd, name):
            nonlocal calls
            calls += 1
            if calls == 2:
                (self.root / 'AGENTS.md').write_bytes(b'CHANGED!!!')
            return original(fd, name)

        with patch.object(helper, 'open_selected', side_effect=changed):
            with self.assertRaisesRegex(ValueError, 'changed'):
                helper.check(self.root, self.spec)

    def test_same_size_write_inside_read_is_rejected(self):
        original = helper.os.read
        changed = False

        def concurrent_write(fd, count):
            nonlocal changed
            data = original(fd, count)
            if not changed:
                changed = True
                (self.root / 'AGENTS.md').write_bytes(b'CHANGED!!!')
            return data

        with patch.object(helper.os, 'read', side_effect=concurrent_write):
            with self.assertRaisesRegex(ValueError, 'changed'):
                helper.check(self.root, self.spec)

    def test_file_and_total_read_bounds(self):
        (self.root / 'AGENTS.md').write_bytes(b'x' * (helper.MAX_FILE + 1))
        self.assertIn('bound', self.run_check(ok=False)['gap'])
        for index in range(5):
            (self.root / str(index)).write_bytes(b'x' * helper.MAX_FILE)
        self.spec['chain'] = [{'path': str(i), 'required_through_bytes': None} for i in range(5)]
        self.assertIn('bound', self.run_check(ok=False)['gap'])

    def test_output_bound_refuses_whole_report_instead_of_truncating(self):
        result = self.run_check(ok=False, bound=256)
        self.assertEqual(result['status'], 'blocked')
        self.assertIn('output bound', result['gap'])
        self.assertNotIn('files', result)

    def test_strict_spec_schema_and_private_content_errors(self):
        self.spec['unexpected'] = 'secret source'
        self.run_check(ok=False)
        del self.spec['unexpected']
        self.spec['chain'] = []
        self.run_check(ok=False)
        self.spec['chain'] = [{'path': 'AGENTS.md', 'required_through_bytes': 0}]
        self.spec['evidence'] = ' '
        self.run_check(ok=False)
        self.spec['evidence'] = 'caller:route'
        (self.root / 'AGENTS.md').write_bytes(b'private-secret\xff')
        result = self.run_check(ok=False)
        self.assertNotIn('private-secret', json.dumps(result))

    def test_malformed_duplicate_and_oversized_json_are_bounded(self):
        for data in (b'{"schema":1,"schema":1}', b'{"secret-source":', b' ' * (helper.MAX_SPEC + 1)):
            self.spec_file.write_bytes(data)
            result = subprocess.run([sys.executable, '-B', str(HELPER), '--root', str(self.root),
                                     '--spec', str(self.spec_file), '--max-output-bytes', '256'], capture_output=True)
            self.assertEqual(result.returncode, 1)
            self.assertLessEqual(len(result.stdout), 256)
            self.assertEqual(json.loads(result.stdout)['status'], 'blocked')
            self.assertNotIn(b'secret-source', result.stdout)

    def test_manifest_selects_helper_without_installing_development_runtime(self):
        manifest = json.loads((ROOT / 'pattern/starter/manifest.json').read_text())
        self.assertIn('context_check.py', manifest['payload'])
        self.assertNotIn('startup_loading.py', manifest['payload'])
        self.assertNotIn('development', HELPER.read_text())


if __name__ == '__main__':
    unittest.main()
