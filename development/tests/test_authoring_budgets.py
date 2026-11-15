"""Maintainer authoring budgets for the standing text this repository ships.

AGENTS.md, "Maintaining this repository": before publishing a starter revision, keep the
shipped `agents/block.md` as small as it can be, near 8,000 bytes, with past 10,000 as the alarm;
each card under 6,500, WORKER.md under 4,500 and the project-section template under 3,000.
These are our authoring budgets, checked here before we publish; the pattern never ships
them as limits on a project's AGENTS.md, block or section (R10, November 14, 2026). For the
block, near 8,000 is a target this test cannot judge; it fails only past the 10,000 alarm
(R1, November 14, 2026, starter revision 3.6).

Static byte measurements of source files only. They say nothing about what a host loads.
"""
import importlib.util
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
STARTER = ROOT / 'pattern/starter'
PAYLOAD = STARTER / 'payload'

# The budgets, as AGENTS.md states them. The block's is an alarm, not its target: the target is
# "as small as it can be, near 8,000 bytes", which is an authoring judgment; a block past 10,000 fails.
BLOCK_BUDGET = 10000
CARD_BUDGET = 6500
WORKER_BUDGET = 4500
SECTION_TEMPLATE_BUDGET = 3000


def flat(text):
    return ' '.join(text.split())


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def shipped_sizes():
    """Bytes of every shipped file a budget covers, with its budget, keyed by source path."""
    manifest = json.loads((STARTER / 'manifest.json').read_text())
    sizes = {'agents/block.md': (len((STARTER / 'agents/block.md').read_bytes()), BLOCK_BUDGET),
             'agents/project-section.md': (len((STARTER / 'agents/project-section.md').read_bytes()), SECTION_TEMPLATE_BUDGET),
             'payload/WORKER.md': (len((PAYLOAD / 'WORKER.md').read_bytes()), WORKER_BUDGET)}
    for name in manifest['payload']:
        if name.startswith('cards/'):
            sizes['payload/' + name] = (len((PAYLOAD / name).read_bytes()), CARD_BUDGET)
    return sizes


def over_budget(sizes):
    return sorted(name for name, (size, budget) in sizes.items() if size > budget)


class AuthoringBudgetTests(unittest.TestCase):
    def test_maintainer_rule_states_the_budgets_this_test_checks(self):
        # Drift guard: the constants above are the ones the maintainer rule names.
        rules = flat((ROOT / 'AGENTS.md').read_text())
        self.assertIn('Before publishing a starter revision, keep the shipped `agents/block.md` as small as it can be, '
                      'near 8,000 bytes; past 10,000 is the alarm to cut it back. Keep each card under 6,500 bytes, '
                      'WORKER.md under 4,500 and the project-section template under 3,000.', rules)
        self.assertIn("These are our authoring budgets, checked here before we publish; never ship them as limits on a "
                      "project's AGENTS.md, block or section.", rules)
        self.assertEqual((BLOCK_BUDGET, CARD_BUDGET, WORKER_BUDGET, SECTION_TEMPLATE_BUDGET), (10000, 6500, 4500, 3000))

    def test_shipped_block_cards_worker_and_section_template_fit_their_budgets(self):
        sizes = shipped_sizes()
        # Every shipped card is measured, not a hand-kept list.
        self.assertEqual(sum(1 for name in sizes if name.startswith('payload/cards/')), 7)
        for name, (size, budget) in sorted(sizes.items()):
            with self.subTest(file=name, bytes=size, budget=budget):
                self.assertLessEqual(size, budget)
        self.assertEqual(over_budget(sizes), [])

    def test_a_file_one_byte_over_its_budget_fails_the_check(self):
        # The oracle catches an over-budget shipped file: each budget is exceeded by exactly one byte in turn.
        sizes = shipped_sizes()
        for name, (_, budget) in sorted(sizes.items()):
            with self.subTest(file=name):
                grown = dict(sizes, **{name: (budget + 1, budget)})
                self.assertEqual(over_budget(grown), [name])
                at_budget = dict(sizes, **{name: (budget, budget)})
                self.assertEqual(over_budget(at_budget), [])

    def test_budgets_are_not_shipped_as_limits_on_a_project(self):
        # The installer and the check carry no byte-cap constant or report field for a project's text.
        installer = load('budget_installer', STARTER / 'install.py')
        for constant in ('BLOCK_CAP', 'SECTION_CAP', 'CARD_CAP', 'WORKER_CAP'):
            self.assertFalse(hasattr(installer, constant), constant)
        checker = load('budget_startup_check', PAYLOAD / 'startup_check.py')
        self.assertFalse(hasattr(checker, 'SECTION_CAP'))
        checker_source = (PAYLOAD / 'startup_check.py').read_text()
        # Read and output bounds stay: they are safety limits on the checker's own I/O, not a size rule for a project.
        for token in ('within_cap', "'cap'", 'project section exceeds'):
            self.assertNotIn(token, checker_source, token)
        self.assertNotIn('caps', (STARTER / 'install.py').read_text())
        # No shipped startup text or install guide states one of the budget numbers or a byte cap to a project.
        # A mention of the host's own instruction cap is the host's limit, not ours, and stays allowed.
        texts = [STARTER / 'agents/block.md', STARTER / 'agents/project-section.md',
                 STARTER / 'README.md', ROOT / 'pattern/README.md']
        texts += sorted(PAYLOAD.glob('*.md')) + sorted((PAYLOAD / 'cards').glob('*.md'))
        number = re.compile(r'\b(?:8,000|10,000|6,500|4,500|3,000)\b')
        for path in texts:
            with self.subTest(file=path.relative_to(ROOT).as_posix()):
                text = flat(path.read_text())
                self.assertIsNone(number.search(text), number.search(text))
                for phrase in ('byte cap', 'over-cap', 'over cap', 'within_cap', 'stay within'):
                    self.assertNotIn(phrase, text.lower(), phrase)


if __name__ == '__main__':
    unittest.main()
