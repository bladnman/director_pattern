"""Generated first-use lifecycle boundaries, not native instruction uptake.

These are synthetic transported packages, built without installing and then
deleting configured state. Native generator/conversation evidence is separate.
"""
import fcntl
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import select
import shutil
import subprocess
import sys
import tempfile
import unittest
import uuid


REPO = Path(__file__).resolve().parents[2]
PAYLOAD = REPO / 'pattern/starter/payload'
INSTANCE = '.director/INSTANCE.json'
PROVENANCE = '.director/PROVENANCE.json'
RECEIPT = '.director/receipts/RECEIPT_setup.json'
JOURNAL = '.director/.first-use.json'
NATIVE = {'kind': 'director-request-bundles',
          'helper': '.director/tools/requests.py', 'config': '.director/config.json'}
VIDEO_GUARDS = ['.director/adapters/video.md', '.team/roles/director-startup.md',
                '.director/PROJECT.md', '.director/TEMPLATE.md', '.team/TEAM.md',
                'docs/DIRECTOR.md', 'docs/PROCESS.md', 'docs/CHANNEL.md']
VIDEO_PLACEHOLDERS = ['requests/.gitkeep', 'requests/archive/.gitkeep',
                      'requests/working/.gitkeep', 'requests/user-requests/.gitkeep',
                      'walks/.gitkeep']
HOOK = ('<!-- director-starter:2 -->\n'
        'Read .director/START.md before the first ordinary reply.\n'
        '<!-- /director-starter:2 -->\n')


def sha(data):
    return hashlib.sha256(data).hexdigest()


class FirstUseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.serial = 0

    def write(self, project, name, value):
        path = project / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value if isinstance(value, bytes) else value.encode())

    def save(self, project, name, value):
        self.write(project, name, json.dumps(value, indent=2) + '\n')

    def read(self, project, name):
        return json.loads((project / name).read_bytes())

    def tree(self, project):
        result = {}
        for path in sorted(project.rglob('*')):
            name = str(path.relative_to(project))
            if path.is_symlink():
                result[name] = ('symlink', os.readlink(path))
            elif path.is_file():
                result[name] = ('file', path.read_bytes())
            elif path.is_dir():
                result[name] = ('directory',)
        return result

    def seed(self, profile='code', generated=True, git=False):
        self.serial += 1
        project = self.base / ('project-' + str(self.serial))
        project.mkdir()
        # Copy the actual implementation and preserved native API, never Store.init.
        for name in ['START.md', 'DIRECTOR.md', 'OPERATIONS.md', 'startup_check.py',
                     'first_use.py', 'FIRST_USE.md']:
            self.write(project, '.director/' + name, (PAYLOAD / name).read_bytes())
        for name in ['PROJECT.md', 'TEMPLATE.md']:
            self.write(project, '.director/' + name,
                       'Synthetic project-owned authority; preserve its existing tracker.\n')
        self.write(project, 'AGENTS.md', HOOK)
        self.write(project, '.director/.gitignore',
                   'INSTANCE.json\n.first-use.json\n.first-use.lock\n.requests.lock\n'
                   'receipts/\nPROJECT.local.md\n')
        self.write(project, 'notes.txt', b'Existing ordinary project asset\r\n')
        guards = ['.director/PROJECT.md', '.director/TEMPLATE.md']
        backend = NATIVE.copy()
        optional = []
        if profile == 'vids':
            backend = {'kind': 'project-contract', 'path': '.director/PROJECT.md'}
            guards = VIDEO_GUARDS.copy()
            optional = ['.director/PROJECT.local.md']
            for name in guards:
                if not (project / name).exists():
                    self.write(project, name, 'Synthetic video authority; existing native tracker.\n')
            self.write(project, '.program/README.md', 'Existing video tracker API.\n')
            self.write(project, '.team/RECORDS.md', 'Preserve native source and recording rules.\n')
            self.write(project, 'journal/seed.md', b'Reviewed generic video journal seed\n')
            self.write(project, '.gitignore', '/requests/\n/walks/\n/journal/\n'
                       '/.team/activity/\n/.team/improvements/\n/.team/config.json\n')
        else:
            for name in ['tools/requests.py', 'engine/tools/requests.py']:
                self.write(project, '.director/' + name, (REPO / 'pattern' / name).read_bytes())
        managed = {str(p.relative_to(project)): sha(p.read_bytes())
                   for p in project.rglob('*') if p.is_file() and p.name != 'notes.txt'}
        provenance = {
            'schema_version': 1, 'kind': 'generic-template-transport-provenance',
            'template': profile, 'not_configured_project_state': True,
            'not_setup_acceptance': True, 'generated_setup_receipt': RECEIPT,
            # Deliberately synthetic pin: fixture shape does not authenticate source.
            'source': {'url': 'https://github.com/bladnman/director_pattern',
                       'sha': '1' * 40, 'pattern_tree_sha': '2' * 40,
                       'published': True, 'local_delta': True},
            'managed_files': managed,
            'first_use': {'schema': 1, 'instance_path': INSTANCE, 'receipt': RECEIPT,
                          'backend': backend, 'hook_source': 'AGENTS.md',
                          'guards': guards, 'optional_guards': optional}}
        self.save(project, PROVENANCE, provenance)
        if generated:
            self.mark(project)
        if git:
            subprocess.run(['git', 'init', '-q', str(project)], check=True, capture_output=True)
        return project

    def mark(self, project):
        provenance = self.read(project, PROVENANCE)
        self.save(project, INSTANCE, {
            'schema': 1, 'kind': 'generated-template-instance',
            'generation_id': str(uuid.uuid4()), 'template_id': provenance['template'],
            'root_path': str(project), 'provenance_sha256': sha((project / PROVENANCE).read_bytes())})

    def revise_transport(self, project, change):
        value = self.read(project, PROVENANCE)
        change(value)
        self.save(project, PROVENANCE, value)
        self.mark(project)

    def argv(self, project):
        return [sys.executable, '-B', str(project / '.director/first_use.py'), 'ensure',
                '--root', '.director', '--instance', INSTANCE, '--provenance', PROVENANCE]

    def ensure(self, project, ok=True):
        result = subprocess.run(self.argv(project), cwd=project, text=True,
                                capture_output=True, timeout=15)
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        self.assertLessEqual(len(result.stdout.encode()), 4096)
        self.assertNotIn('Traceback', result.stderr)
        return json.loads(result.stdout)

    def check(self, project, contract=False, ok=True, extra=()):
        argv = [sys.executable, '-B', str(project / '.director/startup_check.py'),
                '--root', '.director', '--receipt', RECEIPT]
        argv += (['--backend-contract', '.director/PROJECT.md'] if contract else
                 ['--config', '.director/config.json'])
        for guard in self.read(project, PROVENANCE)['first_use']['guards']:
            argv += ['--guard', guard]
        argv += list(extra)
        result = subprocess.run(argv, cwd=project, text=True, capture_output=True, timeout=10)
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def test_generic_seed_has_no_initialization_authority_or_side_effects(self):
        project = self.seed(generated=False)
        before = self.tree(project)
        self.assertEqual(self.ensure(project, ok=False)['status'], 'blocked')
        self.assertEqual(before, self.tree(project))

    def test_two_generated_instances_allocate_distinct_real_native_identities(self):
        ids = []
        for profile in ['code', 'brain']:
            project = self.seed(profile)
            provenance = (project / PROVENANCE).read_bytes()
            result = self.ensure(project)
            self.assertEqual(result['status'], 'prepared')
            config = self.read(project, '.director/config.json')
            ids.append(config['request_store']['project_id'])
            self.assertRegex(ids[-1], r'^PROJ-[0-9a-f]{32}$')
            self.assertEqual(config['request_store']['format'], 'director-request-bundles')
            self.assertEqual(self.check(project)['status'], 'evidence_matched')
            receipt = self.read(project, RECEIPT)
            self.assertEqual(receipt['project_id'], ids[-1])
            self.assertEqual(receipt['technical_check']['native_startup'], 'unrun')
            self.assertEqual(receipt['technical_check']['human_acceptance'], 'unrun')
            self.assertIn('unpublished candidate', receipt['technical_check']['payload_publication'])
            self.assertIn('not performed', receipt['privacy']['source_warning_delivery'])
            self.assertEqual((project / PROVENANCE).read_bytes(), provenance)
            self.assertEqual((project / 'notes.txt').read_bytes(), b'Existing ordinary project asset\r\n')
            self.assertFalse((project / '.director/state.json').exists())
            self.assertFalse((project / '.director/update-policy.json').exists())
        self.assertNotEqual(*ids)

    def test_repeat_and_completed_move_preserve_identity_and_receipt_without_writes(self):
        project = self.seed()
        original = self.ensure(project)['project_id']
        before = self.tree(project)
        self.assertEqual(self.ensure(project)['status'], 'existing')
        self.assertEqual(before, self.tree(project))
        moved = self.base / 'moved'
        project.rename(moved)
        self.assertEqual(self.ensure(moved)['project_id'], original)
        self.assertEqual(before, self.tree(moved))
        self.assertEqual(self.check(moved)['status'], 'evidence_matched')

    def test_uninitialized_marker_cannot_be_replayed_after_copy_or_move(self):
        project = self.seed()
        copied = self.base / 'copied'
        shutil.copytree(project, copied)
        before = self.tree(copied)
        self.assertIn('another generation root', self.ensure(copied, ok=False)['gap'])
        self.assertEqual(before, self.tree(copied))

    def test_renamed_template_id_is_distinct_from_content_profile(self):
        project = self.seed()
        marker = self.read(project, INSTANCE)
        marker['template_id'] = 'my-reviewed-code-stencil'
        self.save(project, INSTANCE, marker)
        self.assertEqual(self.read(project, PROVENANCE)['template'], 'code')
        self.ensure(project)
        self.assertEqual(self.read(project, RECEIPT)['template'], 'my-reviewed-code-stencil')
        self.assertEqual(self.check(project)['status'], 'evidence_matched')

    def test_template_labels_are_nonempty_and_bounded_by_utf8_bytes(self):
        for field in ['selected', 'profile']:
            for label in ['', ' ', 'é' * 129]:
                with self.subTest(field=field, label=label[:10]):
                    project = self.seed()
                    if field == 'selected':
                        marker = self.read(project, INSTANCE)
                        marker['template_id'] = label
                        self.save(project, INSTANCE, marker)
                    else:
                        self.revise_transport(project, lambda p: p.update(template=label))
                    before = self.tree(project)
                    self.ensure(project, ok=False)
                    self.assertEqual(before, self.tree(project))

    def test_existing_config_without_owned_intent_is_preserved_and_not_reinitialized(self):
        project = self.seed()
        config = {'schema_version': 1, 'record_mode': 'tracked', 'request_store': {
            'schema_version': 2, 'format': 'director-request-bundles', 'project_id': 'PROJ-' + 'a' * 32}}
        self.save(project, '.director/config.json', config)
        before = self.tree(project)
        self.assertIn('existing config', self.ensure(project, ok=False)['gap'])
        self.assertEqual(before, self.tree(project))

    def test_existing_custom_or_pending_canonical_state_is_never_overwritten(self):
        for name in ['.producer/config.json', '.program/state.json', '.director/state.json',
                     '.director/.request-txn', '.director/requests/user-record.md',
                     '.team/private.md', 'requests/owned.md']:
            with self.subTest(name=name):
                project = self.seed()
                self.write(project, name, b'Existing user-owned canonical bytes\n')
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))

    def test_unknown_backend_or_unreviewed_optional_guard_cannot_initialize(self):
        project = self.seed()
        self.revise_transport(project, lambda p: p['first_use'].update(backend={'kind': 'unknown'}))
        before = self.tree(project)
        self.ensure(project, ok=False)
        self.assertEqual(before, self.tree(project))
        project = self.seed('vids')
        self.write(project, '.director/PROJECT.local.md', b'Unreviewed customization\n')
        before = self.tree(project)
        self.assertIn('baseline', self.ensure(project, ok=False)['gap'])
        self.assertEqual(before, self.tree(project))

    def test_completed_project_guard_composition_uses_checker_without_rebaselining(self):
        project = self.seed()
        original = self.ensure(project)['project_id']
        self.write(project, '.director/PROJECT.md', b'Current project instructions changed legitimately.\n')
        before = self.tree(project)
        self.assertEqual(self.ensure(project)['project_id'], original)
        self.assertEqual(before, self.tree(project))
        snapshots = self.check(project)['project_instruction_snapshots']
        self.assertEqual(next(v['snapshot'] for v in snapshots if v['path'] == '.director/PROJECT.md'), 'changed')

    def test_corrupt_completed_receipt_cannot_disable_identity_binding_or_forge_acceptance(self):
        project = self.seed()
        self.ensure(project)
        original = self.read(project, RECEIPT)
        mutations = {
            'null identity': lambda r: r.update(project_id=None),
            'missing identity': lambda r: r.pop('project_id'),
            'malformed identity': lambda r: r.update(project_id='PROJ-invalid'),
            'different identity': lambda r: r.update(project_id='PROJ-' + 'c' * 32),
            'schema': lambda r: r.update(schema_version=True),
            'source': lambda r: r['source'].update(sha='3' * 40),
            'backend': lambda r: r.update(backend={'kind': 'project-contract', 'path': 'AGENTS.md'}),
            'managed map': lambda r: r['managed_files'].pop('.director/START.md'),
            'native acceptance': lambda r: r['technical_check'].update(native_startup='passed'),
            'human acceptance': lambda r: r['technical_check'].update(human_acceptance='passed'),
            'warning delivery': lambda r: r['privacy'].update(source_warning_delivery='delivered'),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                receipt = json.loads(json.dumps(original))
                mutate(receipt)
                self.save(project, RECEIPT, receipt)
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))
        project = self.seed('vids')
        self.ensure(project)
        receipt = self.read(project, RECEIPT)
        receipt['project_id'] = 'PROJ-' + 'd' * 32
        self.save(project, RECEIPT, receipt)
        before = self.tree(project)
        self.ensure(project, ok=False)
        self.assertEqual(before, self.tree(project))

    def test_normal_readonly_checker_rejects_generated_receipt_missing_native_identity(self):
        project = self.seed()
        self.ensure(project)
        original = self.read(project, RECEIPT)
        for identity in [None, 'missing', 'PROJ-invalid', 'PROJ-' + 'e' * 32]:
            with self.subTest(identity=identity):
                receipt = json.loads(json.dumps(original))
                if identity == 'missing':
                    del receipt['project_id']
                else:
                    receipt['project_id'] = identity
                self.save(project, RECEIPT, receipt)
                before = self.tree(project)
                self.check(project, ok=False)
                self.assertEqual(before, self.tree(project))
                if identity == 'PROJ-' + 'e' * 32:
                    actual = self.read(project, '.director/config.json')['request_store']['project_id']
                    self.check(project, ok=False, extra=['--expect-project-id', actual])

    def test_normal_readonly_checker_rejects_bundled_identity_on_custom_receipt(self):
        project = self.seed('vids')
        self.ensure(project)
        receipt = self.read(project, RECEIPT)
        receipt['project_id'] = 'PROJ-' + 'f' * 32
        self.save(project, RECEIPT, receipt)
        before = self.tree(project)
        self.check(project, contract=True, ok=False)
        self.assertEqual(before, self.tree(project))

    def test_normal_checker_generated_header_backend_and_unsupported_claims_are_readonly_gaps(self):
        project = self.seed()
        self.ensure(project)
        original = self.read(project, RECEIPT)
        mutations = {
            'schema': lambda r: r.update(schema_version=True),
            'generation': lambda r: r.update(generation_id='invalid'),
            'profile': lambda r: r.update(template=''),
            'provenance': lambda r: r.update(provenance_sha256='invalid'),
            'source tree': lambda r: r['source'].update(pattern_tree_sha='invalid'),
            'source delta': lambda r: r['source'].update(local_delta='unknown'),
            'backend route': lambda r: r['backend'].update(config='.producer/config.json'),
            'managed shape': lambda r: r.update(managed_files=[]),
            'template flag': lambda r: r.update(not_setup_acceptance=True),
            'native claim': lambda r: r['technical_check'].update(native_startup='passed'),
            'human claim': lambda r: r['technical_check'].update(human_acceptance='passed'),
            'warning claim': lambda r: r['privacy'].update(source_warning_delivery='delivered'),
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                receipt = json.loads(json.dumps(original))
                mutate(receipt)
                self.save(project, RECEIPT, receipt)
                before = self.tree(project)
                self.check(project, ok=False)
                self.assertEqual(before, self.tree(project))

    def test_generated_receipt_does_not_adopt_legacy_config_format_or_other_contract(self):
        project = self.seed()
        self.ensure(project)
        config = self.read(project, '.director/config.json')
        config['request_store']['format'] = 'request-bundles'
        self.save(project, '.director/config.json', config)
        before = self.tree(project)
        self.check(project, ok=False)
        self.assertEqual(before, self.tree(project))
        project = self.seed('vids')
        self.ensure(project)
        receipt = self.read(project, RECEIPT)
        receipt['backend']['path'] = '.director/TEMPLATE.md'
        self.save(project, RECEIPT, receipt)
        before = self.tree(project)
        self.check(project, contract=True, ok=False)
        self.assertEqual(before, self.tree(project))

    def test_bad_source_binding_marker_or_partial_copy_refuses_before_writes(self):
        for mutation in ['source', 'digest', 'profile', 'uuid', 'partial']:
            with self.subTest(mutation=mutation):
                project = self.seed()
                if mutation == 'source':
                    self.revise_transport(project, lambda p: p['source'].update(url='https://invalid.example/source'))
                elif mutation == 'partial':
                    (project / '.director/DIRECTOR.md').unlink()
                else:
                    marker = self.read(project, INSTANCE)
                    marker[{'digest': 'provenance_sha256', 'profile': 'template_id', 'uuid': 'generation_id'}[mutation]] = '' if mutation == 'profile' else 'invalid'
                    self.save(project, INSTANCE, marker)
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))

    def test_drift_and_symlinks_never_bless_or_write_through_user_files(self):
        for name in ['.director/START.md', '.director/tools/requests.py', '.director/PROJECT.md']:
            with self.subTest(drift=name):
                project = self.seed()
                self.write(project, name, b'Changed, unreviewed bytes\n')
                before = self.tree(project)
                self.assertIn('drift', self.ensure(project, ok=False)['gap'])
                self.assertEqual(before, self.tree(project))
        for name in [INSTANCE, '.director/PROJECT.md', '.director/receipts']:
            with self.subTest(symlink=name):
                project = self.seed()
                path = project / name
                external = self.base / ('external-' + str(self.serial))
                if name.endswith('receipts'):
                    external.mkdir()
                else:
                    external.write_bytes(path.read_bytes())
                    path.unlink()
                path.symlink_to(external)
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))
                if external.is_dir():
                    self.assertEqual(list(external.iterdir()), [])

    def test_malformed_or_oversized_transport_is_bounded_and_readonly(self):
        for raw in [b'{"a":1,"a":2}', b'{"a":NaN}', b' ' * 128001, b'{"a":' + b'[' * 1500 + b'0' + b']' * 1500 + b'}']:
            with self.subTest(prefix=raw[:20]):
                project = self.seed()
                self.write(project, PROVENANCE, raw)
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))

    def test_video_contract_preserves_reviewed_seed_and_never_creates_second_store(self):
        for git in [False, True]:
            with self.subTest(git=git):
                project = self.seed('vids', git=git)
                before_record = (project / 'journal/seed.md').read_bytes()
                self.assertIsNone(self.ensure(project)['project_id'])
                self.assertEqual(self.check(project, contract=True)['status'], 'evidence_matched')
                self.assertEqual((project / 'journal/seed.md').read_bytes(), before_record)
                for name in ['.director/config.json', '.director/requests', '.director/sources', '.director/.requests.lock']:
                    self.assertFalse((project / name).exists(), name)

    def video_placeholders(self):
        project = self.seed('vids')
        for name in VIDEO_PLACEHOLDERS:
            self.write(project, name, b'')
        self.revise_transport(project, lambda p: p['managed_files'].update({
            name: sha(b'') for name in VIDEO_PLACEHOLDERS}))
        return project

    def test_actual_video_empty_placeholder_shape_is_not_user_state(self):
        project = self.video_placeholders()
        before = {name: (project / name).read_bytes() for name in VIDEO_PLACEHOLDERS}
        self.assertIsNone(self.ensure(project)['project_id'])
        self.assertEqual(self.check(project, contract=True)['status'], 'evidence_matched')
        self.assertEqual(before, {name: (project / name).read_bytes() for name in VIDEO_PLACEHOLDERS})
        self.assertFalse((project / '.director/config.json').exists())
        self.assertFalse((project / '.director/.requests.lock').exists())

    def test_video_placeholders_never_excuse_real_or_unreviewed_canonical_data(self):
        for change in ['hash-listed record', 'nonempty placeholder', 'unreviewed placeholder',
                       'unreviewed empty directory', 'symlink']:
            with self.subTest(change=change):
                project = self.video_placeholders()
                if change == 'hash-listed record':
                    self.write(project, 'requests/user-request.md', b'Real request data\n')
                    self.revise_transport(project, lambda p: p['managed_files'].update({
                        'requests/user-request.md': sha(b'Real request data\n')}))
                elif change == 'nonempty placeholder':
                    self.write(project, 'requests/.gitkeep', b'User bytes')
                    self.revise_transport(project, lambda p: p['managed_files'].update({
                        'requests/.gitkeep': sha(b'User bytes')}))
                elif change == 'unreviewed placeholder':
                    self.write(project, 'walks/new/.gitkeep', b'')
                elif change == 'unreviewed empty directory':
                    (project / 'requests/new-user-directory').mkdir()
                else:
                    external = self.base / ('outside-placeholder-' + str(self.serial))
                    external.write_bytes(b'')
                    path = project / 'walks/.gitkeep'
                    path.unlink()
                    path.symlink_to(external)
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))

    def test_video_privacy_prerequisites_fail_readonly_for_missing_exclusion_or_tracked_private_path(self):
        for tracked in [False, True]:
            with self.subTest(tracked=tracked):
                project = self.seed('vids', git=True)
                if tracked:
                    subprocess.run(['git', '-C', str(project), 'add', '-f', '--', 'journal/seed.md'], check=True)
                else:
                    self.write(project, '.gitignore', b'')
                    self.revise_transport(project, lambda p: p['managed_files'].update({'.gitignore': sha(b'')}))
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))

    def module(self, project):
        spec = importlib.util.spec_from_file_location('first_use_test_' + str(self.serial), project / '.director/first_use.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def crash(self, project, point):
        runner = ('import importlib.util,os,sys\n'
                  's=importlib.util.spec_from_file_location("crash_first_use",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)\n'
                  'def fault(point):\n'
                  ' if point==sys.argv[2]: os._exit(92)\n'
                  'm.fault=fault\nm.ensure(m.Path(".director"))\n')
        result = subprocess.run([sys.executable, '-B', '-c', runner, str(project / '.director/first_use.py'), point],
                                cwd=project, capture_output=True, timeout=15)
        self.assertEqual(result.returncode, 92, result.stdout + result.stderr)

    def test_process_death_at_each_committed_boundary_recovers_same_owned_identity(self):
        for point in ['intent', 'initialized', 'receipt']:
            with self.subTest(point=point):
                project = self.seed()
                self.crash(project, point)
                intended = self.read(project, JOURNAL)['project_id']
                self.assertRegex(intended, r'^PROJ-[0-9a-f]{32}$')
                self.assertEqual(self.ensure(project)['project_id'], intended)
                self.assertEqual(self.read(project, '.director/config.json')['request_store']['project_id'], intended)
                self.assertEqual(self.check(project)['status'], 'evidence_matched')

    def test_owned_recovery_refuses_user_config_change_without_overwrite(self):
        project = self.seed()
        self.crash(project, 'initialized')
        config = self.read(project, '.director/config.json')
        config['user_setting'] = 'preserve me'
        self.save(project, '.director/config.json', config)
        before = self.tree(project)
        self.ensure(project, ok=False)
        self.assertEqual(before, self.tree(project))
        self.assertFalse((project / RECEIPT).exists())

    def test_receipt_loss_recovers_only_exact_empty_owned_state_without_init(self):
        project = self.seed()
        identity = self.ensure(project)['project_id']
        config = (project / '.director/config.json').read_bytes()
        intent = (project / JOURNAL).read_bytes()
        (project / RECEIPT).unlink()  # Actual completed-instance receipt-loss case.
        result = self.ensure(project)
        self.assertEqual(result['project_id'], identity)
        self.assertTrue(result['recovered_owned_intent'])
        self.assertEqual((project / '.director/config.json').read_bytes(), config)
        self.assertEqual((project / JOURNAL).read_bytes(), intent)
        technical = self.read(project, RECEIPT)['technical_check']
        self.assertIn('no initialization', technical['backend_operation'])
        self.assertTrue(technical['recovered_owned_intent'])
        # Own intent does not authorize reconstruction over later user data.
        (project / RECEIPT).unlink()
        self.write(project, '.director/sources/user.txt', b'Later exact source\n')
        before = self.tree(project)
        self.ensure(project, ok=False)
        self.assertEqual(before, self.tree(project))

    def test_changed_generation_or_provenance_cannot_reuse_an_owned_intent(self):
        for change in ['generation', 'provenance', 'malformed-intent']:
            with self.subTest(change=change):
                project = self.seed()
                self.crash(project, 'intent')
                if change == 'generation':
                    self.mark(project)
                elif change == 'provenance':
                    self.revise_transport(project, lambda p: p.update(new_annotation='changed transport'))
                else:
                    self.save(project, JOURNAL, {'project_id': 'PROJ-' + 'b' * 32})
                before = self.tree(project)
                self.ensure(project, ok=False)
                self.assertEqual(before, self.tree(project))

    def test_native_writer_contention_does_not_allocate_intent_or_replace_lock(self):
        project = self.seed()
        path = project / '.director/.requests.lock'
        with path.open('a+b') as stream:
            inode = os.fstat(stream.fileno()).st_ino
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.assertIn('busy', self.ensure(project, ok=False)['gap'])
            self.assertEqual(path.stat().st_ino, inode)
            self.assertFalse((project / JOURNAL).exists())
            self.assertFalse((project / '.director/config.json').exists())

    def test_native_code_drift_after_durable_intent_is_not_executed(self):
        project = self.seed()
        module = self.module(project)
        sentinel = project / 'unreviewed-code-executed'

        def fault(point):
            if point == 'intent':
                self.write(project, '.director/tools/requests.py',
                           'from pathlib import Path\nPath(' + repr(str(sentinel)) + ').touch()\n')

        module.fault = fault
        with self.assertRaisesRegex(ValueError, 'drift'):
            module.ensure(project / '.director')
        self.assertFalse(sentinel.exists())
        self.assertFalse((project / '.director/config.json').exists())
        self.assertFalse((project / RECEIPT).exists())

    def test_unreviewed_video_runtime_addition_requires_owner_recovery(self):
        project = self.seed('vids')
        self.write(project, 'requests/user-work.md', b'New native video work\n')
        before = self.tree(project)
        self.assertIn('canonical', self.ensure(project, ok=False)['gap'])
        self.assertEqual(before, self.tree(project))
        self.revise_transport(project, lambda p: p['managed_files'].update({
            'requests/user-work.md': sha((project / 'requests/user-work.md').read_bytes())}))
        before = self.tree(project)
        self.ensure(project, ok=False)  # A hash baseline cannot bless user requests as a seed.
        self.assertEqual(before, self.tree(project))
        project = self.seed('vids')
        self.write(project, 'journal/new-user-entry.md', b'Unreviewed new journal\n')
        before = self.tree(project)
        self.assertIn('runtime data', self.ensure(project, ok=False)['gap'])
        self.assertEqual(before, self.tree(project))

    def test_concurrent_first_chats_serialize_one_intent_and_one_identity(self):
        project = self.seed()
        runner = ('import importlib.util,sys\n'
                  's=importlib.util.spec_from_file_location("held_first_use",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)\n'
                  'def fault(point):\n'
                  ' if point=="intent": print("intent committed",flush=True);sys.stdin.read(1)\n'
                  'm.fault=fault\nm.ensure(m.Path(".director"))\n')
        child = subprocess.Popen([sys.executable, '-B', '-c', runner, str(project / '.director/first_use.py')],
                                 cwd=project, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE, text=True)
        self.addCleanup(lambda: child.poll() is None and child.kill())
        self.assertTrue(select.select([child.stdout], [], [], 5)[0], 'first writer did not reach committed intent')
        self.assertEqual(child.stdout.readline().strip(), 'intent committed')
        intended = self.read(project, JOURNAL)['project_id']
        self.assertIn('busy', self.ensure(project, ok=False)['gap'])
        stdout, stderr = child.communicate('x', timeout=15)
        self.assertEqual(child.returncode, 0, stdout + stderr)
        self.assertEqual(self.ensure(project)['project_id'], intended)
        self.assertEqual(self.read(project, RECEIPT)['project_id'], intended)
        self.assertEqual(self.check(project)['status'], 'evidence_matched')


if __name__ == '__main__':
    unittest.main()
