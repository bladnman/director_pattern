"""Reinstalling the same starter over a block wrapped in the project's own marker pair.

UPDATES.md, "Update an installed block", step 2, lets a project put its own marker
lines (`<!-- director-pattern:start -->` / `<!-- director-pattern:end -->`) in place
of the shipped block's first and last lines, keeping the text between them byte for
byte. A same-revision reinstall must treat that as the installed block, not as
drift, and must still refuse when the text between the markers was edited.
Installer checks on temporary projects only; no agent behavior is shown here.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest

STARTER = Path(__file__).resolve().parents[2] / 'pattern/starter'
spec = importlib.util.spec_from_file_location('custom_markers_installer', STARTER / 'install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

STANDARD_START = '<!-- director-starter:2 -->\n'
STANDARD_END = '<!-- /director-starter:2 -->\n'
CUSTOM_START = '<!-- director-pattern:start -->\n'
CUSTOM_END = '<!-- director-pattern:end -->\n'
# The AGENTS.md refusal wording may change; every refusal of an implicit overwrite ends this way.
REFUSAL = 'no implicit overwrite'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def custom_block(block=None):
    """The shipped block with its first and last lines replaced by the project's marker pair."""
    block = installer.BLOCK if block is None else block
    assert block.startswith(STANDARD_START) and block.endswith(STANDARD_END)
    return CUSTOM_START + block[len(STANDARD_START):-len(STANDARD_END)] + CUSTOM_END


def drop_last_interior_line(block):
    body = block[:-len(CUSTOM_END)]
    return body[:body.rindex('\n', 0, len(body) - 1) + 1] + CUSTOM_END


class CustomMarkerReinstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name).resolve() / 'project'
        self.agents = self.project / 'AGENTS.md'
        installer.operation('install', self.project)
        self.assertEqual(self.agents.read_text(), installer.AGENTS)

    def tree(self):
        return {p.relative_to(self.project).as_posix(): p.read_bytes() for p in self.project.rglob('*') if p.is_file()}

    def wrap_in_custom_markers(self, record_block_hash=False):
        """Step 2 of "Update an installed block" for a project with its own marker pair, plus project text."""
        text = self.agents.read_text()
        self.assertEqual(text.count(installer.BLOCK), 1)
        self.agents.write_text('# Harbor project\n\nRelease approval stays with the owner.\n\n'
                               + text.replace(installer.BLOCK, custom_block())
                               + '\nRun `make check` before any commit.\n')
        if record_block_hash:
            # Step 3: the receipt's block baseline is the block as it stands, the project's marker lines included.
            receipt_path = self.project / '.director/install.json'
            receipt = json.loads(receipt_path.read_bytes())
            receipt['director_block_sha256'] = sha(custom_block().encode())
            receipt_path.write_text(json.dumps(receipt, indent=2) + '\n')

    def check(self):
        result = subprocess.run([sys.executable, '-B', str(self.project / '.director/startup_check.py')],
                                cwd=self.project, text=True, capture_output=True)
        return json.loads(result.stdout)

    # (a) ------------------------------------------------------------------------------------

    def test_custom_marker_block_reinstall_is_already_installed_and_writes_nothing(self):
        for recorded in (False, True):
            with self.subTest(receipt_block_hash_updated=recorded):
                self.setUp()
                self.wrap_in_custom_markers(record_block_hash=recorded)
                text = self.agents.read_text()
                self.assertNotIn(STANDARD_START, text)
                self.assertNotIn(STANDARD_END, text)
                self.assertEqual(text.count(CUSTOM_START), 1)
                self.assertEqual(text.count(CUSTOM_END), 1)
                if recorded:
                    # The fixture is a state the shipped check itself accepts.
                    result = self.check()
                    self.assertEqual((result['status'], result['director_block']), ('evidence_matched', 'unchanged'))
                    self.assertEqual(result['startup_hook']['marker'], 'director-pattern:start')
                before = self.tree()
                result = installer.operation('install', self.project)
                self.assertFalse(result['changed'])
                self.assertTrue(result['status'].startswith('same starter'), result['status'])
                self.assertEqual(self.tree(), before)
                self.assertEqual(self.agents.read_bytes(), before['AGENTS.md'])

    # (b) ------------------------------------------------------------------------------------

    def test_edited_text_between_custom_markers_is_still_drift_and_writes_nothing(self):
        interior = installer.BLOCK[len(STANDARD_START):-len(STANDARD_END)]
        self.assertIn('You route; workers execute.', interior)
        edits = {
            'wording changed': lambda b: b.replace('You route; workers execute.', 'Do it yourself.', 1),
            'line added inside': lambda b: b.replace(CUSTOM_END, 'Our own rule inside the block.\n' + CUSTOM_END),
            'last interior line dropped': drop_last_interior_line,
            'mixed marker pair': lambda b: b.replace(CUSTOM_END, STANDARD_END),
        }
        for name, edit in edits.items():
            with self.subTest(edit=name):
                self.setUp()
                self.wrap_in_custom_markers(record_block_hash=True)
                text = self.agents.read_text()
                edited = edit(custom_block())
                self.assertNotEqual(edited, custom_block())
                self.agents.write_text(text.replace(custom_block(), edited))
                before = self.tree()
                with self.assertRaisesRegex(ValueError, REFUSAL):
                    installer.operation('install', self.project)
                self.assertEqual(self.tree(), before)

    def test_missing_doubled_or_nested_block_is_refused_and_the_check_blocks(self):
        # States a same-revision reinstall used to pass while the shipped block's bytes appeared anywhere in
        # AGENTS.md. The check accepts exactly one supported marker pair, so the installer refuses them too.
        states = {
            'two standard blocks': lambda t: t.replace(installer.BLOCK, installer.BLOCK + '\n' + installer.BLOCK, 1),
            'custom markers around a standard block': lambda t: t.replace(installer.BLOCK, CUSTOM_START + installer.BLOCK + CUSTOM_END, 1),
            'block removed': lambda t: t.replace(installer.BLOCK + '\n', '', 1),
        }
        for name, change in states.items():
            with self.subTest(state=name):
                self.setUp()
                self.assertEqual(self.check()['status'], 'evidence_matched')
                text = self.agents.read_text()
                changed = change(text)
                self.assertNotEqual(changed, text)
                self.agents.write_text(changed)
                before = self.tree()
                with self.assertRaisesRegex(ValueError, REFUSAL):
                    installer.operation('install', self.project)
                self.assertEqual(self.tree(), before)
                self.assertEqual(self.check()['status'], 'blocked')
                self.assertEqual(self.tree(), before)

    # (c) ------------------------------------------------------------------------------------

    def test_standard_marker_reinstall_behaves_as_before(self):
        # Pristine reinstall.
        before = self.tree()
        self.assertFalse(installer.operation('install', self.project)['changed'])
        self.assertEqual(self.tree(), before)
        self.assertIn('- Read before your first reply: nothing yet.', installer.PROJECT_SECTION)
        # Project text around the standard block and edits in the project section are project-owned.
        self.agents.write_text('# Our project\n\n' + self.agents.read_text().replace(
            '- Read before your first reply: nothing yet.', '- Read before your first reply: `docs/RULES.md`.')
            + '\nOur own rules.\n')
        before = self.tree()
        self.assertFalse(installer.operation('install', self.project)['changed'])
        self.assertEqual(self.tree(), before)
        # An edit inside the standard block is drift, refused without writes.
        self.agents.write_text(self.agents.read_text().replace('You route; workers execute.', 'Do it yourself.', 1))
        before = self.tree()
        with self.assertRaisesRegex(ValueError, REFUSAL):
            installer.operation('install', self.project)
        self.assertEqual(self.tree(), before)


if __name__ == '__main__':
    unittest.main()
