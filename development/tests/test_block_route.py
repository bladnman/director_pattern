"""The standing Director block, its cards and the move from the START.md route.

Static text, file and installer checks only. None of this shows that an agent
re-reads, recovers or delegates after a compaction; that needs a live trial.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
import unittest
import unittest.mock

ROOT = Path(__file__).resolve().parents[2]
STARTER = ROOT / 'pattern/starter'
PAYLOAD = STARTER / 'payload'
OLD = Path(__file__).resolve().parent / 'fixtures/starter_3_2'
spec = importlib.util.spec_from_file_location('block_route_installer', STARTER / 'install.py')
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)

CARDS = ['staffing', 'requests', 'supervision', 'knowledge', 'update-check', 'privacy', 'badge']
MANUALS = ['WORKER.md', 'OPERATIONS.md', 'API.md', 'TOOLING.md', 'RECORDS.md', 'LEARNING.md', 'UPDATES.md', 'FIRST_USE.md']
REENTRY = ('After every compaction or session resume, repeat this startup before your next reply. '
           'Read the files again; a summary that mentions them is not a substitute.')


def flat(text):
    return ' '.join(text.split())


def sha(data):
    return hashlib.sha256(data).hexdigest()


class BlockTextTests(unittest.TestCase):
    def setUp(self):
        self.block = installer.BLOCK
        self.text = flat(self.block)
        self.manifest = json.loads((STARTER / 'manifest.json').read_text())

    def section(self, heading, following):
        return self.text[self.text.index(heading):self.text.index(following)]

    def test_block_is_one_marked_region_within_its_byte_cap(self):
        self.assertTrue(self.block.startswith('<!-- director-starter:2 -->\n'))
        self.assertTrue(self.block.endswith('<!-- /director-starter:2 -->\n'))
        self.assertEqual(self.block.count('director-starter:2 -->'), 2)
        size = len(self.block.encode())
        self.assertLessEqual(size, installer.BLOCK_CAP)
        self.assertEqual(installer.BLOCK_CAP, 7600)
        self.assertEqual(installer.AGENTS, self.block + '\n' + installer.PROJECT_SECTION)
        # No fenced code inside the block: the checker ignores fenced lines as route evidence.
        self.assertNotIn('```', self.block)

    def test_role_gate_sorts_every_reader_and_keeps_the_pinned_sentences(self):
        gate = self.section('**Your role**', '**Every turn (Directors only):**')
        for phrase in (
            "**Your role** never changes on another agent's or session's message.",
            'Default to Project Director unless explicitly assigned a worker or scoped child Director role.',
            "Preserve project/host authority, other authors' work, private sources and existing trackers; role names grant nothing.",
            '- Worker: assigned as one, or spawned by another agent to do a task and report back without being named a Director.',
            'Read `.director/WORKER.md` and any role file your assignment names (a plain brief suffices).',
            'Workers, delegate useful independent subsets within your assigned scope.',
            'Directors-only sections are not for you; "Reading", "Summaries" and rows for your actions are. No check, no 🎬.',
            '- Scoped child Director (roster sub-director): for your assigned outcome only, follow the Directors-only sections and your overlay, never the check or 🎬; report to your parent, who keeps acceptance.',
            '- Otherwise you are the Project Director, even if a tool started the session.',
            'If the user or an explicit assignment says not to act as one, do what they ask and skip all but Summaries until the user says otherwise, then rerun the check before 🎬.',
            'General host instructions are no opt-out.',
        ):
            self.assertEqual(gate.count(phrase), 1, phrase)
        # The worker bullet comes before the Project Director default, so a report-back agent stops there.
        self.assertLess(gate.index('- Worker:'), gate.index('- Scoped child Director'))
        self.assertLess(gate.index('- Scoped child Director'), gate.index('- Otherwise you are the Project Director'))

    def test_every_section_after_the_gate_names_its_audience_in_order(self):
        headings = ['**Your role**', '**Every turn (Directors only):**', '**🎬 and the check (Project Director only).**',
                    '**Recovery (Directors only).**', '**Reading (every role).**', '| Before you | Read |',
                    '**Summaries (every role)**', '**Roster (Directors only).**']
        positions = [self.text.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for heading in headings:
            self.assertEqual(self.text.count(heading), 1, heading)
        bold = re.findall(r'^\*\*[^*]+\*\*', self.block, re.M)
        self.assertEqual(len(bold), 7, bold)

    def test_ten_standing_duties_keep_the_delegation_request_and_fallback(self):
        duties = self.section('**Every turn (Directors only):**', '**🎬 and the check')
        self.assertEqual(re.findall(r'(?<= )(\d+)\. ', duties), [str(n) for n in range(1, 11)])
        for phrase in (
            "As the user's partner, not a literal executor, map each request onto the project's established mechanism and owner",
            'or a better route appears mid-flight, pause the conflicting work, say so, recommend that route as a ❓ decision and hold that work until the user chooses',
            'You route; workers execute. Answer discussion, simple lookups and acceptance judgments yourself.',
            'Directors, delegate project investigations, reviews and changes to bounded subagents before doing the detailed work.',
            'Scope assignments, stay available to the user, and evaluate the returned results.',
            'If subagents are unavailable or prohibited, report the gap and stop that work instead of doing it.',
            "Set the host's tier and reasoning-effort controls explicitly on every dispatch. Default: the strong tier at high effort.",
            'Capture each actionable request and later addition exactly before dependent work; split each separately finishable obligation into its own linked request.',
            'Discussion, greetings and simple replies need no capture or store manuals.',
            'While delegated work is out, send a 📋 SitRep on every stream about every five minutes from dispatch; check each turn, including worker returns and notifications, whether one is due.',
            'Judge each return against the whole intended result, not the part that passed; record a meaningful correction with it.',
            'Required independent review stays independent.',
            "Keep the user's request open until each obligation is reconciled with their exact words and latest steering.",
            'Before ending a turn, take the next useful authorized action unless a real pause, user-only decision or blocker applies.',
            "Mark a real question or decision ❓ (in a question tool's title, not repeated in chat) and an action only the user can take 🖐️ (say what and where); neither decorates progress. Higher-priority host formats win.",
            'Say what is unverified; submitted, verified, accepted and published differ.',
        ):
            self.assertEqual(duties.count(phrase), 1, phrase)
        self.assertNotIn('when permitted', duties)

    def test_brief_fields_match_the_staffing_card_in_order(self):
        fields = re.search(r'5\. Every brief states: (.*?)\. 6\. ', self.text).group(1).split('; ')
        self.assertEqual(fields, ['a fitting emoji Name', 'role', 'tier, effort and a one-line reason', 'scope',
                                  'file ownership', 'authority', 'expected result and checks', 'request IDs',
                                  'applicable knowledge', 'return route'])
        card = (PAYLOAD / 'cards/staffing.md').read_text()
        labels = re.findall(r'^- \*\*([^*]+):\*\*', card, re.M)
        self.assertEqual(labels, ['Emoji Name', 'Role', 'Tier, effort and a one-line reason', 'Scope', 'File ownership',
                                  'Authority', 'Expected result and checks', 'Request IDs', 'Applicable knowledge',
                                  'Return route'])

    def test_check_and_badge_paragraph_is_for_the_project_director_only(self):
        check = self.section('**🎬 and the check (Project Director only).**', '**Recovery (Directors only).**')
        for phrase in (
            "Before your first reply, even to a greeting, run the project section's check command, after any first-use step it lists.",
            'If it reports evidence_matched and you confirm its actor_must_confirm items, begin every reply with 🎬 until the next break; otherwise state the specific gap and answer without it.',
            'Asked about a missing badge, rerun the check.',
            '🎬 means only that.',
            'A host-required progress note first stays unbadged and claims nothing.',
        ):
            self.assertEqual(check.count(phrase), 1, phrase)

    def test_recovery_steps_live_in_the_block_not_on_a_card(self):
        recovery = self.section('**Recovery (Directors only).**', '**Reading (every role).**')
        # Trigger: every break and every new conversation, so work already out is found without a break.
        self.assertIn('After every compaction or session resume, and in every new conversation, before your first project action:', recovery)
        self.assertEqual(re.findall(r'(?<= )(\d)\. (\w+)', recovery)[:4],
                         [('1', 'Find'), ('2', 'Reconcile'), ('3', 'Resume'), ('4', 'Report')])
        for phrase in (
            '1. Find held work: the request IDs, workers and pending ❓ and 🖐️ items your summary or the user names;',
            "then the store's open requests and the continuation view of each request this task holds, even ones marked done (requests row).",
            '2. Reconcile each with current evidence: exact source, obligations, actual results, remaining gates.',
            'A finished milestone or "done" record does not finish the ask; correct a false "done" by the store\'s legal route, keeping its history.',
            '3. Resume ownership: every open outcome is still yours. Continue or rework existing workers by handle; never duplicate running work.',
            '4. Report in your next reply: "Re-entered: check run; N requests open; N workers out."',
            'With work out, send a 📋 SitRep now and time the next from it.',
        ):
            self.assertEqual(recovery.count(phrase), 1, phrase)
        # The steps are instructions in standing text: no file has to be opened to learn them.
        self.assertNotIn('cards/', recovery)
        self.assertNotIn('recovery.md', self.block)
        self.assertFalse((PAYLOAD / 'cards/recovery.md').exists())
        self.assertNotIn('cards/recovery.md', self.manifest['payload'])
        for path in [PAYLOAD / 'cards' / (name + '.md') for name in CARDS] + [PAYLOAD / name for name in MANUALS]:
            self.assertNotIn('recovery.md', path.read_text(), path.name)
        # Recovery is one of the startup steps repeated after a break.
        self.assertIn("This startup: the Project Director's check; a Director's Recovery steps; a worker's WORKER.md and role file; "
                      "a child's overlay or role file; the file your next action needs.", self.text)

    def test_reading_rule_keeps_the_reentry_sentence_first_and_defines_a_fresh_read(self):
        reading = self.section('**Reading (every role).**', '| Before you | Read |')
        self.assertEqual(self.text.count(REENTRY), 1)
        self.assertTrue(reading.startswith('**Reading (every role).** ' + REENTRY + ' This startup:'))
        for phrase in (
            'Either is a break.',
            'A run or read is fresh if your own, still shown and after the latest break (before any, the whole conversation counts); repeated means each step is fresh.',
            "Cards in cards/, WORKER.md and the table's manuals end with a line `END ` plus their path; a complete read reaches that line or, for a file without one, every line to its shown total length.",
            'Before acting under a card, a table manual or a file the project section or your assignment says to read, have a fresh complete read; wait for it before the command it governs.',
            'Read long files in bounded numbered ranges, each range.',
            'If a cut-off read cannot be recovered, stop that work and say so.',
            'Search hits, diffs, tails, summaries, hashes and quotes are not reads.',
        ):
            self.assertEqual(reading.count(phrase), 1, phrase)

    def test_summaries_carry_role_work_and_the_reentry_next_step(self):
        self.assertIn('**Summaries (every role)** state your role, any opt-out and whom you report to; copy exactly the open '
                      "request IDs, each live worker's emoji Name, handle and task, pending ❓ and 🖐️ items and the last "
                      'SitRep time; and begin next steps with "Earlier reads are gone: repeat startup before the next reply:" '
                      'and your startup steps, with the exact check command.', self.text)
        self.assertIn("**Roster (Directors only).** Staff from the project section's roster, or the file it names; "
                      "a role's own instructions are for its executor.", self.text)

    def test_table_names_only_shipped_files_and_every_card_has_a_trigger(self):
        rows = [line.split('|')[1:3] for line in self.block.splitlines() if line.startswith('| ') and 'Before you' not in line]
        self.assertEqual(len(rows), 7)
        named = set()
        for trigger, reads in rows:
            self.assertTrue(trigger.strip())
            found = re.findall(r'(cards/[a-z-]+\.md|[A-Z_]+\.md)', reads)
            self.assertTrue(found, reads)
            named.update(found)
        self.assertEqual({name for name in named if name.startswith('cards/')}, {'cards/' + name + '.md' for name in CARDS})
        self.assertEqual({name for name in named if not name.startswith('cards/')},
                         {'API.md', 'TOOLING.md', 'RECORDS.md', 'LEARNING.md', 'UPDATES.md', 'OPERATIONS.md', 'FIRST_USE.md'})
        for name in named | {'WORKER.md'}:
            self.assertIn(name, self.manifest['payload'], name)
            self.assertTrue((PAYLOAD / name).is_file(), name)
        triggers = flat(' '.join(trigger for trigger, _ in rows))
        for phrase in ('staff or brief work, set tier and effort, or add, rename or retire a role',
                       'capture, split or steer a request, or run a store command',
                       'supervise delegated work, evaluate a return, or end a turn with work out',
                       'look up knowledge for a task, record a correction, or close an outcome',
                       'as Project Director, begin project work when the check reports update discovery due; or discuss or plan a Director Pattern update, here or elsewhere',
                       'capture the first exact source, or change what Git tracks',
                       'handle a failed check, or change the check command or how this project installs or loads instructions'):
            self.assertIn(phrase, triggers)
        self.assertIn('before planning, all of UPDATES.md', self.text)
        self.assertIn('before the command, API.md, TOOLING.md, RECORDS.md', self.text)

    def test_project_section_is_project_owned_and_within_its_cap(self):
        section = installer.PROJECT_SECTION
        self.assertTrue(section.startswith('<!-- director-project -->\n'))
        self.assertTrue(section.endswith('<!-- /director-project -->\n'))
        self.assertLessEqual(len(section.encode()), installer.SECTION_CAP)
        text = flat(section)
        for phrase in ('Project-owned: written once at install; updates never replace it.',
                       '- Check command: `python3 .director/startup_check.py`',
                       '- Read before the work they govern: nothing yet.',
                       '- Request store: the bundled store, with the manuals named above.',
                       '- Role files: `.director/roles/<role>.md`; name the file in the brief.',
                       '| `general-worker` |', '| `sub-director` (scoped child Director) |',
                       'the Project Director keeps acceptance'):
            self.assertIn(phrase, text)

    def test_standing_text_and_cards_name_no_model(self):
        names = re.compile(r'\b(opus|sonnet|haiku|fable|gemini|llama|mistral|gpt[-0-9a-z.]*|o[0-9](-mini)?|claude(?!\.md))\b', re.I)
        texts = {'block': self.block, 'project section': installer.PROJECT_SECTION}
        for name in ['WORKER.md', 'START.md', 'DIRECTOR.md', 'OPERATIONS.md'] + ['cards/' + card + '.md' for card in CARDS]:
            texts[name] = (PAYLOAD / name).read_text()
        for label, text in texts.items():
            with self.subTest(text=label):
                self.assertIsNone(names.search(text), names.search(text))


class CardAndManualTests(unittest.TestCase):
    def test_cards_ship_in_the_manifest_and_end_with_their_end_line(self):
        manifest = json.loads((STARTER / 'manifest.json').read_text())
        shipped = sorted(name for name in manifest['payload'] if name.startswith('cards/'))
        self.assertEqual(shipped, sorted('cards/' + name + '.md' for name in CARDS))
        self.assertEqual(sorted(p.name for p in (PAYLOAD / 'cards').iterdir()), sorted(name + '.md' for name in CARDS))
        for name in CARDS:
            with self.subTest(card=name):
                raw = (PAYLOAD / 'cards' / (name + '.md')).read_text()
                lines = raw.splitlines()
                self.assertTrue(lines[0].startswith('# '))
                self.assertEqual(lines[1], '')
                # The opening line says who the card is for.
                self.assertRegex(lines[2], r'(For |Read before|for every role)')
                self.assertEqual(lines[-1], 'END cards/' + name + '.md')
                self.assertEqual(lines[-2], '')
                self.assertTrue(raw.endswith('\n') and not raw.endswith('\n\n'))
                self.assertEqual(raw.count('END cards/'), 1)
                self.assertLessEqual(len(raw.encode()), installer.CARD_CAP)

    def test_manuals_and_stubs_end_with_their_end_line(self):
        for name in MANUALS + ['START.md', 'DIRECTOR.md']:
            with self.subTest(manual=name):
                raw = (PAYLOAD / name).read_text()
                self.assertEqual(raw.splitlines()[-1], 'END ' + name)
                self.assertEqual(raw.splitlines()[-2], '')
                self.assertEqual(raw.count('\nEND ' + name + '\n'), 1)
        self.assertLessEqual(len((PAYLOAD / 'WORKER.md').read_bytes()), installer.WORKER_CAP)

    def test_start_and_director_are_redirect_stubs_without_rules(self):
        for name in ('START.md', 'DIRECTOR.md'):
            with self.subTest(stub=name):
                raw = (PAYLOAD / name).read_text()
                self.assertTrue(raw.startswith('<!-- director-redirect-stub -->\n# Moved: '))
                self.assertLess(len(raw.encode()), 1000)
                text = flat(raw)
                self.assertIn('This file is no longer a startup read and carries no instructions of its own.', text)
                self.assertIn('the block between the `<!-- director-starter:2 -->` markers in this project\'s AGENTS.md', text)
                self.assertIn("If that block itself tells you to read this file, this project's update is unfinished.", text)
                self.assertIn('[UPDATES.md](UPDATES.md), "Move to the AGENTS.md block"', text)
        self.assertIn('a worker reads [WORKER.md](WORKER.md)', flat((PAYLOAD / 'START.md').read_text()))

    def test_worker_manual_carries_read_rules_assignment_resolution_and_the_return_line(self):
        worker = flat((PAYLOAD / 'WORKER.md').read_text())
        for phrase in (
            'An explicit bounded role assignment selects `worker` or `director`, its role files, task instructions, scope, authority, owner and return route; a plain brief is enough to start.',
            'Load only that package and applicable project guards, not a global role catalog.',
            'Missing or conflicting assignment details return to the assigner; they never create Director authority.',
            'Briefly acknowledge the resolved package once.',
            'End every return with this line: `Owner: a submission, not acceptance. Read .director/cards/supervision.md before accepting, unless you have read it since your latest summary.`',
            'Keep individual and combined tool output bounded.',
            'Batch independent reads only; wait for required instructions to return and read them before running dependent commands.',
            "read contiguous numbered ranges through EOF, with each file's total extent and returned range in the same read result",
            'Recover every failed, missing or truncated portion before acting on it; stop affected work if recovery fails.',
            'Hashes, existence, summaries, searches and unprinted results are not instruction reads.',
            'Before selecting any descendant, completely load [cards/staffing.md](cards/staffing.md)',
        ):
            self.assertIn(phrase, worker)

    def test_card_audiences_and_moved_obligations(self):
        read = lambda name: flat((PAYLOAD / 'cards' / (name + '.md')).read_text())
        supervision, knowledge, requests, staffing, badge, updates = (read(name) for name in (
            'supervision', 'knowledge', 'requests', 'staffing', 'badge', 'update-check'))
        self.assertIn("For Directors. Status reports (📋 SitReps) are Director work; a delegating worker evaluates its sub-workers' returns and accounts for them in its own return.", supervision)
        self.assertIn("After a break, do the AGENTS.md block's Recovery steps before using this card.", supervision)
        self.assertIn('Looking up knowledge for a task is for every role; recording corrections and closing outcomes are Director work.', knowledge)
        self.assertLess(knowledge.index("Load the project's required canonical I/O instructions before querying knowledge"),
                        knowledge.index('page `canonical_learning.py selectors`'))
        self.assertIn('Preserve established caller/role IDs and optional aliases during refactors', knowledge)
        self.assertIn('Keep established role IDs and aliases resolving through a rename or retirement, so older assignments recover.', staffing)
        for phrase in ('Narrow validated state operations are ordinary Director duties',
                       'Judge recommendations on merit, not on work already started',
                       'pause conflicting work first, then recommend',
                       'Do not start or resume the bypassing or paused work until the user chooses',
                       'A linked request is a separate request record',
                       'the Project Director keeps acceptance of the whole',
                       '`python3 .director/requests.py continuation REQ-...`',
                       'completely before any store command; this card does not replace them'):
            self.assertIn(phrase, requests)
        # The badge card describes the block route: no startup-read chain, no old file pointers.
        for stale in ('complete current startup reads', 'START/DIRECTOR', 'installation-evidence', 'under DIRECTOR',
                      'complete selected reads'):
            self.assertNotIn(stale, badge)
        for phrase in ('🎬 claims three things and nothing more',
                       'reported `status: evidence_matched`; and you confirmed its `actor_must_confirm` items',
                       "Give the check's actual `gap` and an ordinary answer in the same turn, without 🎬.",
                       'The command was refused or could not run (permission, missing runtime)',
                       'A later badge or identity question reruns the currently possible check',
                       'After every compaction or session resume; when an opt-out ends; and when startup bytes change',
                       'Never rewrite a receipt to silence drift',
                       'Workers and scoped child Directors run no check, perform no root first-use setup and never show or inherit 🎬.'):
            self.assertIn(phrase, badge)
        for phrase in ('Before planning any Director Pattern update, in this or another project, read [UPDATES](../UPDATES.md) completely',
                       "another installation is updated only by its own project's Director",
                       "Never patch another installation's files from outside.",
                       "the startup check's `update_check` value is `due`"):
            self.assertIn(phrase, updates)

    def test_update_card_repeats_the_exact_notify_sentence(self):
        # Drift guard: the card restates part of UPDATES.md and the helper's own message.
        sentence = '**A new Director Pattern is available. Say “update director pattern” to install it.**'
        self.assertIn(sentence, flat((PAYLOAD / 'cards/update-check.md').read_text()))
        self.assertIn(sentence, flat((PAYLOAD / 'UPDATES.md').read_text()))
        self.assertIn('A new Director Pattern is available. Say “update director pattern” to install it.',
                      (PAYLOAD / 'update_check.py').read_text())
        card = (PAYLOAD / 'cards/update-check.md').read_text()
        for phrase in ('“always update director pattern”', '“notify me instead”', '“stop checking for updates”'):
            self.assertIn(phrase, card)
            self.assertIn(phrase.strip('“”').lower(), flat((PAYLOAD / 'UPDATES.md').read_text()).lower())

    def test_no_payload_text_routes_to_the_removed_sections(self):
        for path in sorted(PAYLOAD.rglob('*.md')):
            with self.subTest(file=path.name):
                text = path.read_text()
                self.assertNotIn('#staffing-and-maintained-roles', text)
                self.assertNotIn('#continuity-and-privacy', text)
                if path.name not in ('START.md', 'DIRECTOR.md', 'UPDATES.md', 'OPERATIONS.md'):
                    self.assertNotIn('START.md', text)
                    self.assertNotIn('DIRECTOR.md', text)
                for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', text):
                    if '://' not in link:
                        self.assertTrue((path.parent / link).exists(), link)
        operations = (PAYLOAD / 'OPERATIONS.md').read_text()
        for heading in ('## Installation evidence', '## Optional context-budget preflight'):
            self.assertIn(heading, operations)
        self.assertNotIn('## Staffing and maintained roles', operations)


class InstallAndUpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name).resolve() / 'project'
        self.home = self.project / '.director'

    def run_json(self, script, *args, ok=True):
        result = subprocess.run([sys.executable, '-B', str(script), *args], cwd=self.project, text=True, capture_output=True)
        self.assertEqual(result.returncode == 0, ok, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def tree(self, root=None):
        root = root or self.project
        return {p.relative_to(root).as_posix(): p.read_bytes() for p in root.rglob('*') if p.is_file()}

    def test_install_writes_block_then_project_section_and_reports_bytes(self):
        plan = installer.operation('plan', self.project)
        self.assertEqual(plan['standing_bytes']['director_block'], len(installer.BLOCK.encode()))
        self.assertEqual(plan['standing_bytes']['project_section'], len(installer.PROJECT_SECTION.encode()))
        self.assertEqual(plan['standing_bytes']['caps'], {'director_block': 7600, 'project_section': 3000, 'card': 6000, 'worker': 4500})
        self.assertEqual(sorted(plan['card_bytes']), sorted(name + '.md' for name in CARDS))
        self.assertEqual(plan['startup_bytes_director'], len(installer.AGENTS.encode()))
        installer.operation('install', self.project)
        agents = (self.project / 'AGENTS.md').read_text()
        self.assertEqual(agents, installer.AGENTS)
        self.assertTrue(agents.startswith('<!-- director-starter:2 -->\n'))
        self.assertLess(agents.index('<!-- /director-starter:2 -->'), agents.index('<!-- director-project -->'))
        receipt = json.loads((self.home / 'install.json').read_bytes())
        self.assertEqual(receipt['starter_revision'], '3.3')
        self.assertEqual(receipt['director_block_sha256'], sha(installer.BLOCK.encode()))
        for name in CARDS:
            self.assertIn('.director/cards/' + name + '.md', receipt['managed'])
        result = self.run_json(self.home / 'startup_check.py')
        self.assertEqual(result['status'], 'evidence_matched')
        self.assertEqual(result['startup_hook']['target'], '.director/WORKER.md')

    def test_over_cap_block_or_card_refuses_before_any_write(self):
        for attribute, value in (('BLOCK', installer.BLOCK.replace('<!-- /director-starter:2 -->', 'x' * 400 + '\n<!-- /director-starter:2 -->')),
                                 ('PROJECT_SECTION', installer.PROJECT_SECTION.replace('<!-- /director-project -->', 'x' * 3000 + '\n<!-- /director-project -->')),
                                 ('BLOCK', installer.BLOCK.replace('<!-- director-starter:2 -->\n', ''))):
            with self.subTest(attribute=attribute), unittest.mock.patch.object(installer, attribute, value):
                for mode in ('plan', 'install'):
                    with self.assertRaisesRegex(ValueError, 'byte cap|malformed'):
                        installer.operation(mode, self.project)
                self.assertFalse(self.project.exists())

    def test_project_section_edits_survive_reinstall_but_block_edits_are_drift(self):
        installer.operation('install', self.project)
        agents = self.project / 'AGENTS.md'
        agents.write_text('# Our project\n\n' + agents.read_text().replace(
            '- Read before the work they govern: nothing yet.', '- Read before the work they govern: `docs/RELEASE.md` before a release.')
            + '\nOur own rules.\n')
        before = self.tree()
        self.assertFalse(installer.operation('install', self.project)['changed'])
        self.assertEqual(before, self.tree())
        agents.write_text(agents.read_text().replace('You route; workers execute.', 'Do it yourself.'))
        with self.assertRaisesRegex(ValueError, 'drift'):
            installer.operation('install', self.project)

    def test_pristine_rollback_removes_the_cards_folder(self):
        self.project.mkdir()
        (self.project / 'notes.txt').write_text('Keep')
        installer.operation('install', self.project)
        installer.rollback(self.home / 'install.json')
        self.assertEqual(self.tree(), {'notes.txt': b'Keep'})

    def test_manifest_allows_only_flat_names_and_one_cards_folder(self):
        original = (STARTER / 'manifest.json').read_text()
        value = json.loads(original)
        for bad in ('../escape.md', 'cards/../WORKER.md', 'cards/nested/x.md', 'other/x.md', 'cards/x.py', '/abs.md'):
            with self.subTest(name=bad):
                broken = dict(value, payload=value['payload'] + [bad])
                with unittest.mock.patch.object(Path, 'read_bytes', lambda path, _b=json.dumps(broken).encode(), _o=Path.read_bytes:
                                                _b if path.name == 'manifest.json' else _o(path)):
                    with self.assertRaisesRegex(ValueError, 'unsafe payload'):
                        installer.manifest()

    # --- the documented move from a revision 3.2 installation -------------------------------

    def build_3_2(self):
        """A revision 3.2 installation with project-owned work, from the exact 3.2 startup files."""
        installer.operation('install', self.project)
        shutil.rmtree(self.home / 'cards')
        for name in ('START.md', 'DIRECTOR.md', 'OPERATIONS.md', 'WORKER.md', 'startup_check.py'):
            (self.home / name).write_bytes((OLD / name).read_bytes())
        for name in ('API.md', 'TOOLING.md', 'RECORDS.md', 'LEARNING.md', 'UPDATES.md', 'FIRST_USE.md'):
            path = self.home / name
            path.write_text(path.read_text().replace('\n\nEND ' + name + '\n', '\n'))
        bridge = (OLD / 'AGENTS.md').read_text()
        (self.project / 'AGENTS.md').write_text(bridge)
        old_manifest = json.loads((OLD / 'manifest.json').read_text())
        self.assertEqual(old_manifest['starter_revision'], '3.2')
        managed = {'AGENTS.md': sha(bridge.encode()), '.director/config.json': sha((self.home / 'config.json').read_bytes())}
        managed.update({'.director/' + name: sha((self.home / name).read_bytes()) for name in old_manifest['payload']})
        receipt = json.loads((self.home / 'install.json').read_bytes())
        receipt.update(starter_revision='3.2', managed=managed, managed_files=dict(managed),
                       manifest_sha256=sha((OLD / 'manifest.json').read_bytes()))
        del receipt['director_block_sha256'], receipt['project_section']
        (self.home / 'install.json').write_text(json.dumps(receipt, indent=2) + '\n')
        # The 3.2 installation is real: its own checker accepts it.
        self.assertEqual(self.run_json(self.home / 'startup_check.py')['status'], 'evidence_matched')
        # Project-owned content that the move must keep.
        (self.project / 'AGENTS.md').write_text('# Harbor project\n\nRelease approval stays with the owner.\n\n' + bridge
                                                + '\nRun `make check` before any commit.\n')
        (self.home / 'roles').mkdir()
        (self.home / 'roles/releaser.md').write_text('# releaser\nOwned responsibility.\n')
        (self.home / 'update-policy.json').write_text('{"schema_version":1,"mode":"off","authorization":"UR-1","changed_at":1}')
        raw = Path(self.temp.name) / 'input.txt'
        raw.write_bytes(b'Exact request\r\n')
        source = self.run_json(self.home / 'requests.py', 'capture', '--raw-file', str(raw), '--event-id', 'capture-' + uuid.uuid4().hex)
        self.run_json(self.home / 'requests.py', 'create', '--source-id', source['source_id'], '--title', 'Harbor', '--event-id', 'create-' + uuid.uuid4().hex)
        self.assertEqual(self.run_json(self.home / 'startup_check.py')['status'], 'evidence_matched')

    def move_to_block(self, through=7):
        """The file operations of UPDATES.md, "Move to the AGENTS.md block", steps 1 to 6."""
        manifest = json.loads((STARTER / 'manifest.json').read_text())
        backup = self.home / 'backups/20261111-move'                       # step 1
        backup.mkdir(parents=True)
        for name in ['AGENTS.md', '.director/install.json'] + ['.director/' + p for p in json.loads((OLD / 'manifest.json').read_text())['payload']]:
            target = backup / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(self.project / name, target)
        for name in manifest['payload']:                                   # step 2
            target = self.home / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((PAYLOAD / name).read_bytes())
        if through < 3:
            return
        agents = self.project / 'AGENTS.md'                                # step 3
        text = agents.read_text()
        start, end = text.index('<!-- director-starter:2 -->'), text.index('<!-- /director-starter:2 -->\n') + len('<!-- /director-starter:2 -->\n')
        section = installer.PROJECT_SECTION.replace(                       # step 4
            '- Check command: `python3 .director/startup_check.py`',
            '- Check command: `python3 .director/startup_check.py --receipt .director/receipts/update-3.3.json`').replace(
            '| `sub-director`', '| `releaser` | Cut a release | strong, high | Owner approves every release |\n| `sub-director`')
        agents.write_text(text[:start] + installer.BLOCK + '\n' + section + text[end:])
        self.assertLessEqual(len(section.encode()), 3000)                  # step 5 (caps only; host cap is not measured here)
        receipt = {'format': 'director-flat-starter', 'starter_version': 3, 'starter_revision': '3.3',   # step 6
                   'previous_starter_revision': '3.2',
                   'source': json.loads((self.home / 'install.json').read_bytes())['source'],
                   'managed_files': {'.director/' + name: sha((self.home / name).read_bytes()) for name in manifest['payload']},
                   'director_block_sha256': sha(installer.BLOCK.encode()), 'backup': '.director/backups/20261111-move'}
        (self.home / 'receipts').mkdir()
        (self.home / 'receipts/update-3.3.json').write_text(json.dumps(receipt, indent=2) + '\n')

    def test_a_3_2_installation_moves_to_the_block_and_keeps_project_content(self):
        self.build_3_2()
        owned = {name: data for name, data in self.tree().items()
                 if name.startswith(('.director/sources/', '.director/requests/', '.director/roles/'))
                 or name in ('.director/config.json', '.director/update-policy.json', '.director/install.json')}
        self.assertTrue(any(name.startswith('.director/sources/') for name in owned))
        self.move_to_block()
        after = self.tree()
        for name, data in owned.items():
            self.assertEqual(after[name], data, name)
        agents = (self.project / 'AGENTS.md').read_text()
        self.assertTrue(agents.startswith('# Harbor project\n\nRelease approval stays with the owner.\n\n<!-- director-starter:2 -->\n'))
        self.assertTrue(agents.endswith('<!-- /director-project -->\n\nRun `make check` before any commit.\n'))
        self.assertEqual(agents.count('<!-- director-starter:2 -->'), 1)
        self.assertIn(installer.BLOCK, agents)
        self.assertNotIn('.director/START.md', agents)
        # Step 7: the check command exactly as the project section states it.
        command = re.search(r'- Check command: `python3 ([^`]+)`', agents).group(1).split()
        result = self.run_json(self.project / command[0], *command[1:])
        self.assertEqual(result['status'], 'evidence_matched')
        self.assertEqual(result['startup_hook']['target'], '.director/WORKER.md')
        self.assertEqual(result['director_block'], 'unchanged')
        self.assertEqual(result['receipt'], '.director/receipts/update-3.3.json')
        self.assertEqual(result['update_check'], 'off')
        self.assertTrue(result['project_section']['within_cap'])
        self.assertEqual(self.run_json(self.home / 'requests.py', 'status')['total'], 1)
        # The bare command still names the 3.2 receipt, which has no card baselines: a named gap, not a pass.
        self.assertIn('baseline', self.run_json(self.home / 'startup_check.py', ok=False)['gap'])
        # Backups stay local under the installed ignore rule.
        self.assertIn('backups/', (self.home / '.gitignore').read_text())

    def test_a_move_interrupted_before_the_block_is_merged_blocks_with_a_named_gap(self):
        self.build_3_2()
        self.move_to_block(through=2)
        result = self.run_json(self.home / 'startup_check.py', ok=False)
        self.assertEqual(result['status'], 'blocked')
        self.assertIn('redirect stub', result['gap'])
        # Restoring the verified backup returns the working 3.2 route.
        backup = self.home / 'backups/20261111-move'
        for path in backup.rglob('*'):
            if path.is_file():
                shutil.copy2(path, self.project / path.relative_to(backup))
        shutil.rmtree(self.home / 'cards')
        self.assertEqual(self.run_json(self.home / 'startup_check.py')['status'], 'evidence_matched')

    def test_update_guide_documents_the_move(self):
        updates = flat((PAYLOAD / 'UPDATES.md').read_text())
        for phrase in ('### Move to the AGENTS.md block',
                       "From starter revision 3.3 the Director's standing rules are the marked block in AGENTS.md itself, with a project-owned section directly below it.",
                       "with the incoming block, byte for byte, from the pinned revision's `pattern/starter/agents/block.md`",
                       "The block's text is managed: do not edit it.",
                       "Move a project's own wording from inside the old block into the project section or the surrounding project text",
                       'add the project section once, starting from `pattern/starter/agents/project-section.md`',
                       'When a section already exists, never replace it; merge only what the update needs.',
                       'never trim project text silently',
                       '`director_block_sha256`, the SHA-256 of the block from its opening marker line through its closing marker line and newline',
                       'It must report `evidence_matched`, `startup_hook.target` ending in `WORKER.md` and `director_block: unchanged`.',
                       'finish the move or restore the backup; do not leave it mixed'):
            self.assertIn(phrase, updates)
        self.assertTrue((STARTER / 'agents/block.md').is_file() and (STARTER / 'agents/project-section.md').is_file())


if __name__ == '__main__':
    unittest.main()
