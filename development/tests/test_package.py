"""Check package isolation and declared payload links, not agent installation behavior."""
import io
import json
import ast
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import unittest
from urllib.parse import unquote, urlsplit


PATTERN = Path(__file__).resolve().parents[2] / "pattern"
LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)\n]+))(?:\s+"[^"\n]*")?\s*\)')


def markdown_links(path):
    """Local inline links/images with simple paths; ignore URLs and anchor-only links."""
    text = path.read_text(encoding="utf-8")
    # Examples in fenced code blocks are not document dependencies.
    text = re.sub(r"(?ms)^```[^\n]*\n.*?^```[^\n]*$", "", text)
    for match in LINK.finditer(text):
        target = match.group(1) or match.group(2)
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        yield unquote(parts.path)


ROOT = PATTERN.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"

# This public checkout holds no Director installation (November 14, 2026): the maintainer's installation, store,
# exact sources and receipts live in a private sibling workspace. Root AGENTS.md is maintainer rules only, so no
# startup marker, project section, standing-rule text or private ID may come back into it, and the ignores stay as a
# guard against an accidental re-add.
STARTUP_MARKERS = ("director-starter", "director-project", "director-pattern:start", "director-pattern:end")
PRIVATE_ID = re.compile(r"\b(?:PROJ|REQ|UR)-")
# Every published startup text an installation could paste back: the current block and section, the 3.3 block and
# section, the 3.2 bridge, and the v1 hook. Their wording, not only their markers, must stay out of root AGENTS.md.
STARTUP_TEXTS = (PATTERN / "starter/agents/block.md", PATTERN / "starter/agents/project-section.md",
                 FIXTURES / "starter_3_3/block.md", FIXTURES / "starter_3_3/project-section.md",
                 FIXTURES / "starter_3_2/AGENTS.md")


def flat(text):
    return " ".join(text.split())


def startup_lines():
    """Distinctive lines of every published startup text, whitespace-normalized."""
    install = (PATTERN / "INSTALL-v1.md").read_text(encoding="utf-8")
    hook = re.search(r"<!-- director-pattern:start -->(.*?)<!-- director-pattern:end -->", install, re.S)
    assert hook is not None, "INSTALL-v1 must carry the marked startup hook"
    texts = [path.read_text(encoding="utf-8") for path in STARTUP_TEXTS] + [hook.group(1)]
    return {flat(line) for text in texts for line in text.splitlines() if len(flat(line)) >= 40}


class PackageBoundaryTests(unittest.TestCase):
    def manifest(self, root):
        manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema_version"], 1)
        paths = []
        for key in ("base_files", "tracked_files"):
            self.assertIsInstance(manifest[key], list)
            self.assertTrue(manifest[key], key)
            for name in manifest[key]:
                self.assertIsInstance(name, str)
                path = PurePosixPath(name)
                self.assertTrue(name and not path.is_absolute(), name)
                self.assertNotIn("..", path.parts, name)
                self.assertNotIn("\\", name, name)
                self.assertEqual(path.as_posix(), name, name)
                target = (root / name).resolve()
                self.assertTrue(target.is_relative_to(root.resolve()), name)
                self.assertTrue(target.is_file(), name)
                paths.append(name)
        self.assertEqual(len(paths), len(set(paths)), "Duplicate declared payload file")
        return manifest

    def check_links(self, root):
        count = 0
        for document in root.rglob("*.md"):
            for target in markdown_links(document):
                count += 1
                resolved = (document.parent / target).resolve()
                label = f"{document.relative_to(root)} -> {target}"
                self.assertTrue(resolved.is_relative_to(root.resolve()), label)
                self.assertTrue(resolved.exists(), label)
        self.assertGreater(count, 0, "Link checks must exercise actual package links")

    def test_declared_files_are_safe_and_present(self):
        self.manifest(PATTERN)

    def test_pattern_subtree_is_standalone(self):
        with tempfile.TemporaryDirectory() as temporary:
            isolated = Path(temporary) / "pattern"
            shutil.copytree(PATTERN, isolated)
            self.assertEqual(list(Path(temporary).iterdir()), [isolated])
            for authoring_path in ("AGENTS.md", "development", ".reference"):
                self.assertFalse((isolated / authoring_path).exists(), authoring_path)
            self.manifest(isolated)
            self.check_links(isolated)

    def test_every_contract_and_hooked_file_is_base_payload(self):
        manifest = self.manifest(PATTERN)
        guidance = {"README.md", "INSTALL.md", "README-v1.md", "INSTALL-v1.md"}
        # The flat starter has its own manifest and install boundary; it is not
        # silently added to the existing engine package.
        contracts = {p.relative_to(PATTERN).as_posix() for p in PATTERN.rglob("*.md")
                     if not p.is_relative_to(PATTERN / "starter")} - guidance
        self.assertLessEqual(contracts, set(manifest["base_files"]), "Lean installs must be self-contained")
        install = (PATTERN / "INSTALL-v1.md").read_text(encoding="utf-8")
        hook = re.search(r"<!-- director-pattern:start -->(.*?)<!-- director-pattern:end -->", install, re.S)
        assert hook is not None, "INSTALL must carry the marked startup hook"
        named = set(re.findall(r"\b[A-Z_]+\.md\b", hook.group(1)))
        self.assertEqual(named, {"PATTERN.md"}, "The common hook routes through the bootstrap, not selected role duties")
        self.assertLessEqual(named, set(manifest["base_files"]), "Startup hook names only installed files")

    def test_common_bootstrap_does_not_load_director_policies(self):
        # Structural contract boundary; does not measure size or imitate role behavior.
        bridge = set(markdown_links(PATTERN / "PATTERN.md"))
        self.assertIn("engine/PATTERN.md", bridge)
        bootstrap = (PATTERN / "engine/PATTERN.md").read_text()
        startup = bootstrap.split("## Required capability protocols")[0]
        common = {m.group(1) or m.group(2) for m in LINK.finditer(startup)}
        self.assertIn("WORKER.md", common)
        self.assertTrue(common.isdisjoint({"DIRECTION.md", "DIRECTOR.md", "REQUEST_MANAGER.md", "STATE.md", "MODELS.md"}))
        for definition in ("DIRECTOR.md", "REQUEST_MANAGER.md"):
            self.assertIn("DIRECTION.md", set(markdown_links(PATTERN / "engine" / definition)))
        self.assertNotIn("DIRECTION.md", set(markdown_links(PATTERN / "engine/WORKER.md")))

    def test_public_checkout_claims_no_local_installation(self):
        # Oracle O2, static half: text and filesystem wiring only. A fresh host session getting maintainer rules
        # only, with no check and no 🎬, is the live half and is not shown here.
        authoring = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("# Maintaining this repository", authoring)
        self.assertIn("## Tinka", authoring)
        for marker in STARTUP_MARKERS:
            self.assertFalse(marker in authoring, f"root AGENTS.md must carry no {marker} marker")
        self.assertIsNone(PRIVATE_ID.search(authoring), "root AGENTS.md must carry no project, request or source ID")
        # Wording sentinels catch a block pasted back without its markers, or re-wrapped.
        text = flat(authoring)
        for line in sorted(startup_lines()):
            self.assertFalse(line in text, f"root AGENTS.md must not carry published startup text: {line[:80]}")
        for route in ("Default to Project Director", "- Check command:", "startup_check.py", ".director/WORKER.md",
                      "## Local Director installation", "🎬"):
            self.assertFalse(route in authoring, f"root AGENTS.md must not carry startup route text: {route}")
        # No installation in this checkout, and the guard ignores stay.
        self.assertFalse((ROOT / ".director").exists(), "the public checkout must hold no .director/")
        ignores = (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines()
        self.assertIn("/.director/", ignores)
        self.assertIn(".reference/", ignores)

    @unittest.skipUnless(shutil.which("git"), "git is required for the tracked-file checks")
    def test_public_clone_tracks_no_installation_and_still_ignores_one(self):
        # What a clone of HEAD gets (git archive), what is staged for the next commit (the index), and that the
        # root .gitignore itself, not a machine-local exclude, ignores both folders.
        git = ["git", "-c", f"core.excludesFile={os.devnull}", "-C", str(ROOT)]
        top = subprocess.run(git + ["rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if top.returncode or Path(top.stdout.strip()).resolve() != ROOT.resolve():
            self.skipTest("not run from this repository's own Git work tree")
        private = lambda name: bool({".director", ".reference"} & set(PurePosixPath(name).parts))
        archive = subprocess.run(git + ["archive", "--format=tar", "HEAD"], capture_output=True, check=True).stdout
        with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as exported:
            names = exported.getnames()
        self.assertIn("AGENTS.md", names)
        self.assertEqual([n for n in names if private(n)], [], "a clone of HEAD must hold no .director or .reference")
        staged = subprocess.run(git + ["ls-files", "-z"], capture_output=True, text=True, check=True).stdout.split("\0")
        self.assertIn("AGENTS.md", staged)
        self.assertEqual([n for n in staged if private(n)], [], "the index must hold no .director or .reference")
        probes = [".director/x", ".director/requests/x.json", ".reference/x"]
        run = subprocess.run(git + ["check-ignore", "-v", "--no-index", *probes], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        matched = {}
        for row in run.stdout.splitlines():
            rule, path = row.split("\t", 1)
            source, _, pattern = rule.split(":", 2)
            matched[path] = (source, pattern)
        for path in probes:
            self.assertEqual(matched.get(path, (None,))[0], ".gitignore", path)
            self.assertFalse(matched[path][1].startswith("!"), path)

    def test_flat_payload_links_resolve_inside_an_installed_copy(self):
        # Kept from the earlier source-hook test: the starter payload copied into a .director/ reaches its real
        # foundations and cards there, without a hidden v1 engine or index. Reference wiring, not agent reads.
        manifest = json.loads((PATTERN / "starter/manifest.json").read_text())
        with tempfile.TemporaryDirectory() as temporary:
            installed = Path(temporary) / ".director"
            for name in manifest["payload"]:
                target = installed / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(PATTERN / "starter/payload" / name, target)
            for name in ("START.md", "DIRECTOR.md", "WORKER.md", *(n for n in manifest["payload"] if n.startswith("cards/"))):
                document = installed / name
                for link in markdown_links(document):
                    resolved = (document.parent / link).resolve()
                    self.assertTrue(resolved.is_relative_to(installed.resolve()), (name, link))
                    self.assertTrue(resolved.exists(), (name, link))
            self.assertFalse((installed / "engine").exists())

    def test_loaded_hook_explicitly_requests_director_delegation_with_host_precedence(self):
        # Guards the host-loaded entrypoint itself; it cannot prove host permission.
        install = (PATTERN / "INSTALL-v1.md").read_text(encoding="utf-8")
        hook = re.search(r"<!-- director-pattern:start -->(.*?)<!-- director-pattern:end -->", install, re.S)
        self.assertIsNotNone(hook)
        text = " ".join(hook.group(1).split())
        self.assertIn("Default to Project Director unless explicitly assigned a worker or scoped child Director role", text)
        self.assertIn("Directors, delegate project investigations, reviews and changes to bounded subagents before doing the detailed work", text)
        self.assertIn("Scope assignments, stay available to the user, and evaluate the returned results", text)
        self.assertIn("Preserve project/host authority", text)

    def test_flat_installed_route_requests_subagents_without_repeated_user_permission(self):
        # Exercise the block actually emitted by the recommended installer, not
        # merely the retained legacy guide. This is instruction wiring, not uptake.
        text = " ".join((PATTERN / "starter/agents/block.md").read_text(encoding="utf-8").split())
        self.assertIn("Default to Project Director unless explicitly assigned a worker or scoped child Director role", text)
        # Revision 3.4 drops the "Directors," vocative inside the Directors-only duties; the sentence is unchanged otherwise.
        self.assertIn("Delegate project investigations, reviews and changes to bounded subagents before doing the detailed work", text)
        self.assertIn("Scope assignments, stay available to the user and evaluate returns", text)
        self.assertIn("Preserve project, host and user authority", text)
        self.assertNotIn("when permitted", text)
        self.assertNotIn("no mandatory", text)
        self.assertIn("Workers, delegate useful independent subsets within your assigned scope", text)
        installer = (PATTERN / "starter/install.py").read_text(encoding="utf-8")
        self.assertIn('BLOCK = (SOURCE / "agents/block.md").read_text(encoding="utf-8")', installer)
        self.assertIn('files["AGENTS.md"] = AGENTS.encode()', installer)

    def test_flat_bridge_repeats_startup_after_compaction_or_resume(self):
        # Standing-text wiring only (November 9); it cannot prove an agent re-reads after compaction.
        reentry = ("After every compaction or session resume, repeat this startup before your next reply. "
                   "Read the files again; a summary that mentions them is not a substitute.")
        raw = (PATTERN / "starter/agents/block.md").read_text(encoding="utf-8")
        block = " ".join(raw.split())
        self.assertEqual(block.count(reentry), 1)
        # Revision 3.3: the sentence opens the every-role Reading rule, and "this startup" is listed right after it.
        self.assertIn("**Reading (every role).** " + reentry + " This startup: the Project Director's first-reply reads and check; "
                      "a Director's Recovery; a worker's WORKER.md and role file; a child's overlay or role file; "
                      "the file your next action needs.", block)
        self.assertIn("repeated means each step is fresh", block)
        self.assertIn("Search hits, diffs, tails, summaries, hashes, quotes, file existence and unprinted results are not reads.", block)
        # The installer writes this block and then the project section into AGENTS.md, so an installed project's
        # loaded text carries the sentence exactly once, in the block's Reading rule. Read from the starter payload
        # only: this public checkout holds no installation (test_public_checkout_claims_no_local_installation).
        section = " ".join((PATTERN / "starter/agents/project-section.md").read_text(encoding="utf-8").split())
        self.assertNotIn(reentry, section)
        # The marker is the retained interface; wording changes keep it.
        self.assertTrue(raw.startswith("<!-- director-starter:2 -->\n"))
        self.assertTrue(raw.endswith("<!-- /director-starter:2 -->\n"))

    def test_flat_reuse_rules_do_not_survive_compaction_or_resume(self):
        # Wording only: reuse rules cannot excuse skipping the re-read or re-check.
        payload = PATTERN / "starter/payload"
        read = lambda name: " ".join((payload / name).read_text(encoding="utf-8").split())
        block = " ".join((PATTERN / "starter/agents/block.md").read_text(encoding="utf-8").split())
        operations, worker, badge = read("OPERATIONS.md"), read("WORKER.md"), read("cards/badge.md")
        # Revision 3.3: the block's own test replaces the DIRECTOR and START clauses.
        self.assertIn("A run or read is fresh if your own, still shown and after the latest break", block)
        self.assertIn("begin every reply with 🎬 until the next break", block)
        self.assertIn("Reconcile each with current evidence", block)
        self.assertIn("Reuse an unchanged result within one uninterrupted conversation.", badge)
        self.assertIn("After every compaction or session resume; when an opt-out ends; and when startup bytes change", badge)
        self.assertIn("Reuse unchanged current-conversation facts; relevant changed startup bytes require recheck, "
                      "and so do facts from before a compaction or session resume.", operations)
        self.assertIn("reuse unchanged retained instructions. A compaction summary does not retain them; "
                      "after compaction or session resume, read them again. Recover incomplete reads.", worker)

    def test_flat_roles_preserve_delegation_fallback_and_bounded_worker_default(self):
        read = lambda name: " ".join((PATTERN / "starter" / name).read_text(encoding="utf-8").split())
        block, worker = read("agents/block.md"), read("payload/WORKER.md")
        staffing, requests = read("payload/cards/staffing.md"), read("payload/cards/requests.md")
        # Standing block (duty 2): delegate first, answer discussion directly, gap-and-stop without subagents.
        self.assertIn("Delegate project investigations, reviews and changes to bounded subagents before doing the detailed work", block)
        self.assertIn("Answer discussion, simple lookups and acceptance judgments yourself", block)
        # Revision 3.4: the role-domain exception sits beside the direct-answer rule, in the block and on the card.
        domain = "a judgment, draft or rule in a roster role's domain goes to that role, even in chat."
        self.assertIn("acceptance judgments yourself; " + domain, block)
        self.assertIn("- Discussion, simple lookups and acceptance judgments: do them yourself. A " + domain[2:]
                      + " Accepting a return against the whole request stays yours.", staffing)
        self.assertIn("If subagents are unavailable or prohibited, report the gap and stop that work instead of doing it", block)
        self.assertIn("| staff or brief work, set tier and effort, or change a role | cards/staffing.md |", block)
        # Staffing card: role choice from the roster, the executor's own reads, and a scope that permits them.
        self.assertIn('Take the roster role whose "use when" fits; a general worker never silently replaces a maintained role', staffing)
        # Recorded behaviour (staffer reads the selection/authority package): a route prohibition in a role file reaches selection.
        self.assertIn("Before dispatch, when the row or the project section names a role file, read its selection and authority part", staffing)
        self.assertIn("Its executor reads the rest completely before acting; you need not", staffing)
        self.assertIn("Before dispatch read only the selection and authority part of the role file its row names.", block)
        self.assertIn("the role ID, its role file and the instructions it must read; its scope must permit those reads", staffing)
        self.assertIn("**Applicable knowledge:** the selector tags or query context", staffing)
        self.assertIn("Settle missing or conflicting role limits with the owner before that dispatch", staffing)
        self.assertNotIn("A reply that fulfills the intended discussion needs no delegation", block)
        self.assertIn("Answer discussion directly", requests)
        self.assertIn("Narrow validated state operations are ordinary Director duties", requests)
        self.assertIn("Delegate useful independent subsets within your authorized assignment unless its explicit limits prohibit them", worker)
        self.assertNotIn("only when authorized by the assignment", worker)
        self.assertIn("If the assignment blocks required startup or knowledge reads, return that conflict to the assigner before affected task work", worker)

    def test_flat_root_check_and_final_acceptance_match_the_flat_roles(self):
        block = " ".join((PATTERN / "starter/agents/block.md").read_text(encoding="utf-8").split())
        records = " ".join((PATTERN / "starter/payload/RECORDS.md").read_text().split())
        # Defaulted or explicitly selected, the user-facing session is the Project Director and runs the check.
        self.assertIn("Otherwise you are the Project Director, even if a tool started the session", block)
        self.assertIn("**🎬 and the check (Project Director only).** Before your first reply, even to a greeting", block)
        self.assertIn("never the check or 🎬; report to your parent, who keeps acceptance", block)
        self.assertIn("No check, no 🎬.", block)
        self.assertIn("The Project Director evaluates the complete submission and makes the final acceptance decision", records)
        self.assertIn("A worker or scoped child Director cannot self-accept for the Project Director", records)
        self.assertIn("Required human gates and independent verification still apply", records)
        self.assertNotIn("outcome owner does not close its own outcome", records)
        self.assertIn("Preserve an existing roster/cursor when project policy requires it; do not create one for the flat starter", records)

    def test_flat_complete_reads_keep_combined_bounds_and_recovery(self):
        read = lambda name: " ".join((PATTERN / "starter" / name).read_text(encoding="utf-8").split())
        worker, block, knowledge = read("payload/WORKER.md"), read("agents/block.md"), read("payload/cards/knowledge.md")
        # Full read rules: WORKER.md. Short form for every role: the block's Reading rule.
        self.assertIn("An explicit bounded role assignment selects `worker` or `director`", worker)
        self.assertIn("Batch independent reads only; wait for required instructions to return and read them before running dependent commands", worker)
        self.assertIn("individual and combined tool output bounded", worker)
        self.assertIn("read contiguous numbered ranges through EOF", worker)
        self.assertIn("total extent and returned range in the same read result", worker)
        self.assertIn("Recover every failed, missing or truncated portion", worker)
        self.assertIn("stop affected work if recovery fails", worker)
        self.assertIn("summaries, searches and unprinted results are not instruction reads", worker)
        self.assertIn("have a fresh complete read; wait for it before the command it governs", block)
        self.assertIn("Read a long file in bounded numbered ranges, every range", block)
        self.assertIn("keep combined output bounded", block)
        self.assertIn("If a cut-off read cannot be recovered, stop that work and say so", block)
        self.assertIn("every line to its shown total length", block)
        self.assertIn("Default to Project Director unless explicitly assigned a worker or scoped child Director role", block)
        self.assertLess(knowledge.index("Load the project's required canonical I/O instructions before querying knowledge"), knowledge.index("page `canonical_learning.py selectors`"))

    def test_flat_action_clarifications_retain_the_fail_closed_routes(self):
        read = lambda name: " ".join((PATTERN / "starter/payload" / name).read_text().split())
        updates, learning, api, operations = map(read, ("UPDATES.md", "LEARNING.md", "API.md", "OPERATIONS.md"))
        self.assertIn("answer greeting-only requests without network", updates)
        self.assertIn("supported background route or the next active project-work step", updates)
        self.assertIn("at most once per rolling 24 hours", updates)
        self.assertIn("Always supply `--root /project/.director` before the command", updates)
        self.assertIn("subject to its existing daily window", updates)
        self.assertIn("Do not reinstall, reset the cache or promote acceptance", updates)
        self.assertIn("Never select them as knowledge, even if previously accepted", learning)
        self.assertIn("Do not infer a type from wording or edit old notes", learning)
        self.assertIn("never retry through an old loaded instance", api)
        self.assertIn("This also applies to init", api)
        self.assertIn("The bundled helper accepts config schema 1", api)
        self.assertIn("Existing trackers use their own verified adapter", api)
        self.assertIn("Do not use this option to bypass required configuration, initialize a backend or certify an unconfigured template", operations)

    def test_flat_staffing_keeps_strong_default_with_occasional_lighter_tier(self):
        # Instruction wording only; actual host tier/effort selection is unverified.
        read = lambda name: " ".join((PATTERN / "starter" / name).read_text(encoding="utf-8").split())
        staffing, block = read("payload/cards/staffing.md"), read("agents/block.md")
        tier = staffing.split("## Tier and effort", 1)[1].split("## The brief", 1)[0]
        self.assertIn("No model name, vendor or price is ever a default", tier)
        self.assertIn("Default: the strong tier at high effort, chosen at dispatch", tier)
        self.assertIn("Occasionally, as a suggestion and never a quota or cost target", tier)
        self.assertIn("for small, well-specified, easily checked work that you are very confident a lighter tier can do, choose a lighter tier at high effort (extra-high if a little less confident) or the strong tier at medium", tier)
        self.assertIn("Ambiguous, consequential or hard-to-check work stays on the strong tier", tier)
        self.assertIn("Map these words to the host's nearest real controls; never invent one", tier)
        self.assertIn("Your evaluation and any required independent review apply unchanged at every tier", tier)
        self.assertIn("Record each dispatch's requested tier and effort, what the tool selected, what was effective (or \"unknown\"), and a one-line reason", tier)
        self.assertIn("Default: the strong tier at high effort.", block)
        self.assertIn("Checks are never silently dropped or expanded", staffing)

    def test_flat_sitrep_checks_due_each_turn_and_suggests_a_shape(self):
        # Instruction wording only; actual SitRep cadence and uptake are unverified.
        read = lambda name: " ".join((PATTERN / "starter/payload" / name).read_text(encoding="utf-8").split())
        director = read("cards/supervision.md")
        heading = "While delegated work is outstanding, proactively send a labeled **📋 SitRep**"
        self.assertEqual(director.count(heading), 1)
        start = director.index(heading)
        sitrep = director[start:director.index("Answer status questions briefly", start)]
        self.assertIn("about every five minutes from actual dispatch (or the agreed interval)", sitrep)
        self.assertIn("On every turn, including worker returns and notifications, check whether one is due, using host timestamps or a clock check, and note each SitRep's time", sitrep)
        self.assertIn("Cover every held stream, including quiet, stalled or returned-but-unevaluated work, with actual handles/observations, results, blockers, steering and next proof", sitrep)
        self.assertIn('A suggested shape: **Done** · **In progress** (who, what, actual status, next step) · **Waiting on you** (❓ questions, 🖐️ user-only actions, or "nothing") · **Next**', sitrep)
        self.assertNotIn("(owner, actual status)", sitrep)
        intro = "For a full SitRep, for example (a table where it renders well; the same columns as lines also work):"
        self.assertIn(intro, sitrep)
        example = sitrep[sitrep.index(intro):]
        for part in ("| Who | Doing | Status | Next step |", "**📋 SitRep**", "**Done:**", "**Waiting on you:**", "**Next:**"):
            self.assertIn(part, example)
        # Raw text: blank lines keep the copied example rendering as a table.
        raw = (PATTERN / "starter/payload/cards/supervision.md").read_text(encoding="utf-8")
        raw_example = raw[raw.index("For a full SitRep, for example"):raw.index("Answer status questions briefly")]
        self.assertIn("\n\n| Who | Doing | Status | Next step |", raw_example)
        self.assertIn("|\n\n**Waiting on you:**", raw_example)
        rows = [line.split("|")[1:-1] for line in raw_example.splitlines() if line.startswith("| ") and "Next step" not in line]
        self.assertTrue(rows)
        for cells in rows:
            self.assertNotIn(cells[-1].strip(), ("", "—", "-"), "Every example row names a next step")
        self.assertIn("When nothing changed since the last SitRep, give one line per held stream, not the full shape", sitrep)
        self.assertIn("Reserve 📋 for that report heading; between due reports use ordinary prose, not another full block", sitrep)
        self.assertIn("Ordinary progress/status answers and notification replies do not reset or replace it", sitrep)
        self.assertIn("After compaction or session resume, if one is overdue or you cannot tell when the last one was sent, report once promptly and time the next from it", sitrep)
        self.assertIn("Without any time source, say so once and report at each user message or held-stream change instead", sitrep)
        self.assertIn("Stricter host progress updates stay concise and separate", sitrep)
        self.assertIn("supported waits must leave both cadences usable", sitrep)
        self.assertNotIn("report promptly if overdue or timing is unknown", director)
        block = " ".join((PATTERN / "starter/agents/block.md").read_text(encoding="utf-8").split())
        self.assertIn("While delegated work is out, send a 📋 SitRep on every stream about every five minutes from dispatch; check each turn, including worker returns and notifications, whether one is due.", block)
        self.assertIn("With work out, if a 📋 SitRep is overdue or its last time unknown, send one now and time the next from it.", block)

    def test_starter_manifest_records_revision_and_format_number(self):
        # Static manifest check only; the installer's receipt is checked in test_flat_starter.
        manifest = json.loads((PATTERN / "starter/manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["starter_revision"], "3.4")
        self.assertEqual(manifest["starter_version"], 3)

    def test_updates_run_through_each_projects_own_director(self):
        # Instruction wording / static only; actual update behavior is unverified.
        updates = " ".join((PATTERN / "starter/payload/UPDATES.md").read_text(encoding="utf-8").split())
        for phrase in (
            "This project's Director, or an agent it authorizes within this project, performs an update",
            "Update each installation from its own project, through that project's Director",
            "ask that project's Director (or the agent the user directs there) to update its Director Pattern in its own conversation",
            "Never patch another installation's files from outside, even by following this protocol",
            "An ordinary compatible update is bounded, well specified and checked by the required independent review",
            "choose a lighter capability tier at high effort, or the strong tier at medium effort, and record the choice",
            "Keep the required independent review",
            "Use the strong tier at high effort or above, with a recorded reason, for unresolved conflicts, migrations, unknown provenance or ambiguous project adaptations",
            "Keep the required independent review; by default it uses the strong tier at high effort",
            "Start a session in another project only when the user asked for that update, and carry the user's request with it",
            "If no documented staging route exists, report the gap; do not edit the template",
            "Record the incoming manifest's `starter_revision` in the update receipt, and name the previous and new `starter_revision` when reporting the update to the user",
            'When the installed receipt has none, report the previous one as "unrecorded"',
        ):
            self.assertIn(phrase, updates)
        self.assertNotIn("it need not already be a Director", updates)

    def test_director_is_a_partner_and_sets_dispatch_settings(self):
        # Instruction wording / static only; actual partner behavior and dispatch settings are unverified.
        read = lambda path: " ".join(path.read_text(encoding="utf-8").split())
        block = read(PATTERN / "starter/agents/block.md")
        requests = read(PATTERN / "starter/payload/cards/requests.md")
        updates = read(PATTERN / "starter/payload/cards/update-check.md")
        staffing = read(PATTERN / "starter/payload/cards/staffing.md")
        # Standing every turn: the partner rule, the mid-flight pause and explicit settings sit in the block,
        # ahead of the check paragraph, so no file read is needed to meet them.
        for phrase in (
            "As the user's partner, not a literal executor, map each request onto the project's established mechanism and owner",
            "if the literal request would bypass it, or a better route appears mid-flight, pause the conflicting work, say so, recommend that route as a ❓ decision and hold that work until the user chooses",
            "Set the host's tier and reasoning-effort controls explicitly on every dispatch. Default: the strong tier at high effort.",
            "tier, effort and a one-line reason",
        ):
            self.assertEqual(block.count(phrase), 1, phrase)
            self.assertLess(block.index(phrase), block.index("**🎬 and the check (Project Director only).**"), phrase)
        for phrase in (
            "You are the user's partner, not a literal executor",
            "map a request onto the project's established mechanism and owner",
            "When the literal request would bypass it, say so, propose the established route and recommend it",
            "Judge recommendations on merit, not on work already started",
            "pause conflicting work first, then recommend",
            "Mark that recommendation ❓ as a user decision",
            "Do not start or resume the bypassing or paused work until the user chooses",
        ):
            self.assertEqual(requests.count(phrase), 1, phrase)
        for phrase in (
            "Before planning any Director Pattern update, in this or another project, read [UPDATES](../UPDATES.md) completely",
            "an agent the user directs there",
        ):
            self.assertEqual(updates.count(phrase), 1, phrase)
        self.assertIn("discuss or plan a Director Pattern update anywhere | cards/update-check.md; before planning, all of UPDATES.md |", block)
        for phrase in (
            "This card is the explicit instruction to set capability and reasoning effort on every dispatch, including on hosts that reserve those controls for explicit instructions",
            "Hosts often fall back to the parent's settings, so leaving one out is not a choice",
            "Default: the strong tier at high effort, chosen at dispatch",
            "a one-line reason (size, how easily it is checked, consequence of error)",
            '"Inherited" or "not set" is acceptable only with the forcing host constraint',
            "An ordinary compatible update under `UPDATES.md` is one such case",
        ):
            self.assertIn(phrase, staffing)
        maintainer = read(PATTERN.parent / "AGENTS.md")
        self.assertIn("fix it in runtime text, not only in the rationale or design notes", maintainer)
        self.assertIn("Bump `starter_revision` in `pattern/starter/manifest.json` with each published starter payload change", maintainer)

    def test_v1_and_explicit_lean_keep_the_selected_package_route(self):
        legacy = (PATTERN / "README-v1.md").read_text()
        starter = (PATTERN / "starter/README.md").read_text()
        self.assertIn("Read this package's README-v1.md and follow INSTALL-v1.md", legacy)
        self.assertIn("Director Pattern from manifest.json", legacy)
        self.assertIn("[INSTALL-v1.md](INSTALL-v1.md)", legacy)
        self.assertIn("pattern/README-v1.md", legacy)
        self.assertIn("[legacy v1 guide](../INSTALL-v1.md#select-and-copy-only-the-payload)", starter)
        self.assertIn("executable installer provisions tracked mode only", starter)
        self.assertEqual(self.manifest(PATTERN)["engine_api_version"], 1)

    def test_legacy_boundary_is_phased_and_transition_names_the_actual_layout(self):
        project = " ".join((PATTERN / "PROJECT.md").read_text().split())
        self.assertIn("Before installation, layout changes or engine updates, read the complete [interface-1 boundary]", project)
        self.assertIn("configuration and state are project-owned", project)
        for name in ("README-v1.md", "INSTALL-v1.md", "engine/references/UPDATES.md", "engine/references/BOUNDARY.md"):
            with self.subTest(name=name):
                text = " ".join((PATTERN / name).read_text().split())
                self.assertIn("legacy pre-engine v1 layout", text)
                self.assertIn("starter 2/3", text)
                self.assertIn("incompatible store", text)
                self.assertNotIn("A flat installation needs", text)

    def test_supported_v1_uses_subagents_without_requiring_git_initialization(self):
        director = " ".join((PATTERN / "engine/DIRECTOR.md").read_text().split())
        direction = " ".join((PATTERN / "engine/DIRECTION.md").read_text().split())
        install = " ".join((PATTERN / "INSTALL-v1.md").read_text().split())
        self.assertIn("Use the available subagent route for substantial analysis and project changes", director)
        self.assertIn("Treat requested project investigations and reviews as delegated work, including those reported in a reply", director)
        self.assertIn("Use bounded subagents for substantial analysis and project changes", direction)
        self.assertNotIn("loaded request or available tool alone proves neither permission", director)
        self.assertNotIn("loaded delegation request or tool's existence proves neither permission", direction)
        self.assertIn("Git is recommended for review and recovery, not a prerequisite for useful subagents", direction)
        self.assertIn("preserve verified backups before writes", direction)
        self.assertIn("initialize Git only on the user's request", direction)
        self.assertIn("do not create separate worktrees or checkouts", direction)
        self.assertIn("Useful subagents may still work in the same project tree with bounded file ownership", install)

    def test_startup_incomplete_reads_cannot_be_acknowledged_as_loaded(self):
        # Instruction-path check only; a fresh-agent trial must observe behavior.
        text = " ".join((PATTERN / "engine/PATTERN.md").read_text(encoding="utf-8").split())
        self.assertRegex(text, r"failed, missing, or truncated result.*recover and read every missing portion before claiming")
        self.assertRegex(text, r"cannot be recovered, disclose the specific gap and stop affected action")
        self.assertRegex(text, r"acknowledgment reports reads, not permission to delegate.*Recorder availability.*checked setup")

    def test_updates_integrate_changed_hook_without_replacing_local_rules(self):
        # Hook is project-owned, outside the engine replacement; static contract only.
        for name in ("engine/references/UPDATES.md", "starter/payload/UPDATES.md"):
            with self.subTest(name=name):
                update = " ".join((PATTERN / name).read_text(encoding="utf-8").split())
                self.assertRegex(update, r"incoming startup hook changes.*existing host-loaded entrypoint")
                self.assertRegex(update, r"Back up and verify (the|each) startup file.*compare.*prior and incoming hook")
                self.assertRegex(update, r"Preserve all unrelated bytes and project-specific instructions.*Do not append a duplicate hook")
                self.assertRegex(update, r"ambiguous, retain the original and report the incomplete integration")
        # The legacy v1 guide keeps its November 1 wording; starter 3.2 replaces it below.
        legacy = " ".join((PATTERN / "engine/references/UPDATES.md").read_text(encoding="utf-8").split())
        self.assertIn("keep the role default and explicit request for bounded subagents in the actual host entrypoint (AGENTS.md or CLAUDE.md) as well", legacy)

    def test_starter_updates_keep_director_text_in_agents_and_claude_only_imports_it(self):
        # Wording only (November 9); no downstream project update is exercised here.
        update = " ".join((PATTERN / "starter/payload/UPDATES.md").read_text(encoding="utf-8").split())
        self.assertIn("Keep the role default, the explicit request for bounded subagents and the marked block in "
                      "AGENTS.md, or in the hook source the project's check selects, even when other rules live in a "
                      "shared file. When the host loads CLAUDE.md and expands its imports into loaded text, make "
                      "CLAUDE.md only import AGENTS.md (for example `@AGENTS.md`) and move its other content into "
                      "AGENTS.md; never keep a second copy of the Director paragraph in CLAUDE.md. Where the host does "
                      "not expand imports, keep the role default and the bounded-subagent request in CLAUDE.md and "
                      "report that gap.", update)
        self.assertIn("Back up and verify each startup file the update changes, both AGENTS.md and CLAUDE.md, "
                      "compare the identifiable marked block", update)
        self.assertIn("Report, rather than move, content whose ownership is unclear or that applies to only one host.",
                      update)
        self.assertNotIn("(AGENTS.md or CLAUDE.md) as well", update)
        # Guarding CLAUDE.md in a check stays a supported example; it writes no Director text.
        operations = (PATTERN / "starter/payload/OPERATIONS.md").read_text(encoding="utf-8")
        self.assertIn("--guard CLAUDE.md", operations)

    def test_project_owned_index_and_selected_definitions_are_reachable_in_isolated_payload(self):
        # Installation fixture: target context is generated, never upstream payload.
        # This proves file/link reachability only, not any agent's read sequence.
        manifest = self.manifest(PATTERN)
        self.assertNotIn("ROLE_INDEX.md", manifest["base_files"] + manifest["tracked_files"])
        with tempfile.TemporaryDirectory() as temporary:
            installed = Path(temporary) / ".director"
            for name in manifest["base_files"]:
                target = installed / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(PATTERN / name, target)
            index = installed / "ROLE_INDEX.md"
            definitions = ["engine/DIRECTOR.md", "engine/REQUEST_MANAGER.md", "engine/RECORDER.md", "engine/ANALYSIS.md"]
            index.write_text("# Fixture index\n" + "\n".join(f"[Fixture entry]({name})" for name in definitions), encoding="utf-8")
            bootstrap = installed / "PATTERN.md"
            bootstrap.write_text(bootstrap.read_text().replace(
                "<installation fills the single project-owned index locator>",
                "[Fixture canonical index](ROLE_INDEX.md)"), encoding="utf-8")
            self.assertIn("ROLE_INDEX.md", set(markdown_links(bootstrap)))
            self.assertEqual(set(markdown_links(index)), set(definitions))
            # A recurring responsibility is a separate maintained file registered
            # in that same index, rather than another live role table in startup.
            (installed / "roles").mkdir()
            (installed / "roles/reader.md").write_text("# Fixture reader\nRead [worker boundaries](../engine/WORKER.md).\n", encoding="utf-8")
            index.write_text(index.read_text() + "\n[Fixture reader](roles/reader.md)\n", encoding="utf-8")
            self.assertIn("roles/reader.md", set(markdown_links(index)))
            self.check_links(installed)

    def test_manifest_partitions_replaceable_engine_from_project_owned_seeds(self):
        manifest = self.manifest(PATTERN)
        self.assertEqual(manifest["engine_api_version"], 1)
        owned = [set(manifest[key]) for key in ("engine_files", "project_seed_files", "entrypoint_files")]
        self.assertEqual(set.union(*owned), set(manifest["base_files"] + manifest["tracked_files"]))
        for i, paths in enumerate(owned):
            for other in owned[i + 1:]:
                self.assertFalse(paths & other)
        self.assertTrue(all(p.startswith("engine/") for p in owned[0]))
        self.assertTrue(all(not p.startswith("engine/") for p in owned[1] | owned[2]))
        self.assertLessEqual({"PATTERN.md", "PROJECT.md", ".gitignore", "IDENTITY_POOL.txt"}, owned[1])
        self.assertFalse(any(p.startswith(("requests/", "sources/", "receipts/")) or p == "config.json" for p in set.union(*owned)))

    def test_engine_replacement_preserves_custom_project_and_both_helper_roots(self):
        # Actual CLI roots, state continuity, and custom reference reachability;
        # this is not a claim about an agent reading the files.
        manifest = self.manifest(PATTERN)
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            root = project / ".director"
            for name in manifest["base_files"] + manifest["tracked_files"]:
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(PATTERN / name, root / name)
            (root / "roles").mkdir()
            (root / "roles/custom.md").write_text("# Fixture specialist\nRead [worker](../engine/WORKER.md) and [policy](../policy.md).\n")
            (root / "policy.md").write_text("Fixture authority: no external release.\n")
            (root / "ROLE_INDEX.md").write_text("# Fixture index\n[Specialist](roles/custom.md)\n")
            (root / "PATTERN.md").write_text((root / "PATTERN.md").read_text().replace(
                "<installation fills the single project-owned index locator>", "[Roles](ROLE_INDEX.md)"))
            (root / "IDENTITY_POOL.txt").write_text("custom-project-pool\n")
            launcher = [sys.executable, str(root / "tools/requests.py")]
            direct = [sys.executable, str(root / "engine/tools/requests.py")]
            first = json.loads(subprocess.run(launcher + ["init"], capture_output=True, text=True, check=True).stdout)
            before = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file() and not p.is_relative_to(root / "engine")}
            shutil.rmtree(root / "engine")
            shutil.copytree(PATTERN / "engine", root / "engine")
            after = {str(p.relative_to(root)): p.read_bytes() for p in root.rglob("*") if p.is_file() and not p.is_relative_to(root / "engine")}
            self.assertEqual(before, after)
            again = json.loads(subprocess.run(direct + ["init"], capture_output=True, text=True, check=True).stdout)
            self.assertEqual(first, again)
            subprocess.run(direct + ["validate"], capture_output=True, check=True)
            self.assertFalse((root / "engine/config.json").exists())
            self.check_links(root)
            for script in (root / "tools/update_check.py", root / "engine/tools/update_check.py"):
                subprocess.run([sys.executable, str(script), "set-policy", "off", "--authorization", "fixture"], capture_output=True, check=True)
                self.assertEqual(json.loads((root / "update-policy.json").read_text())["mode"], "off")
                self.assertFalse((root / "engine/update-policy.json").exists())
            (root / "receipts").mkdir()
            (root / "receipts/source.json").write_text(json.dumps({"source": {"url": "https://github.com/bladnman/director_pattern", "sha": "a" * 40, "published": True}}))
            # Read the real receipt through the implementation using project-root-relative paths.
            import importlib.util
            spec = importlib.util.spec_from_file_location("fixture_update", root / "engine/tools/update_check.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            self.assertEqual(module.installed_source(root, ".director/receipts/source.json"), ("a" * 40, None))

    def test_identity_pool_is_static_unique_and_skips_reserved_markers(self):
        manifest = self.manifest(PATTERN)
        self.assertIn("IDENTITY_POOL.txt", manifest["base_files"])
        markers = [line.strip() for line in (PATTERN / "IDENTITY_POOL.txt").read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertTrue(markers)
        bare = [marker.replace("️", "") for marker in markers]
        self.assertEqual(len(bare), len(set(bare)), "Pool markers must be distinct")
        for reserved in ("🎬", "📋", "❓", "🖐"):
            self.assertNotIn(reserved, bare, reserved)

    def test_declared_payloads_have_only_internal_markdown_dependencies(self):
        with tempfile.TemporaryDirectory() as temporary:
            isolated = Path(temporary) / "pattern"
            shutil.copytree(PATTERN, isolated)
            manifest = self.manifest(isolated)
            for mode, extra in (("base", []), ("tracked", manifest["tracked_files"])):
                with self.subTest(mode=mode):
                    payload = Path(temporary) / mode / ".director"
                    for name in manifest["base_files"] + extra:
                        target = payload / name
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(isolated / name, target)
                    self.check_links(payload)

    @unittest.skipUnless(shutil.which("git"), "git is required for ignore checks")
    def test_installed_payload_commits_state_and_ignores_only_machine_local_files(self):
        manifest = self.manifest(PATTERN)
        self.assertIn(".gitignore", manifest["base_files"])
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            git = ["git", "-c", f"core.excludesFile={os.devnull}"]
            subprocess.run(git + ["init", "-q"], cwd=project, check=True)
            installed = project / ".director"
            for name in manifest["base_files"] + manifest["tracked_files"]:
                (installed / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(PATTERN / name, installed / name)
            helper = [sys.executable, str(installed / "tools/requests.py")]
            subprocess.run(helper + ["init"], capture_output=True, check=True)
            (project / "raw.txt").write_text("Committed by default")
            event_id = subprocess.run(helper + ["event-id", "create"], capture_output=True, text=True, check=True).stdout.strip()
            subprocess.run(helper + ["create", "--raw-file", str(project / "raw.txt"), "--title", "Shared", "--event-id", event_id], capture_output=True, check=True)
            for scratch in (".request-txn/intent.json", ".request-stage-abc/bundle", ".request-complete-abc/file", "backups/2026-10-21/PATTERN.md", "receipts/2026-10-21-setup.md", ".update-check.json", ".update-check.lock", ".update-check-fixture.tmp", "update-policy.json"):
                (installed / scratch).parent.mkdir(parents=True, exist_ok=True)
                (installed / scratch).write_text("fixture")

            def listed(*flags):
                out = subprocess.run(git + ["ls-files", "--others", "--exclude-standard", *flags], cwd=project, capture_output=True, text=True, check=True).stdout
                return set(out.split())

            ignored, kept = listed("--ignored"), listed()
            self.assertEqual(ignored, {".director/.requests.lock", ".director/.request-txn/intent.json", ".director/.request-stage-abc/bundle",
                                       ".director/.request-complete-abc/file", ".director/backups/2026-10-21/PATTERN.md",
                                       ".director/.update-check.json", ".director/.update-check.lock", ".director/.update-check-fixture.tmp"})
            for name in manifest["base_files"] + manifest["tracked_files"] + ["config.json", "receipts/2026-10-21-setup.md", "update-policy.json"]:
                self.assertIn(f".director/{name}", kept, name)
            self.assertTrue(any(p.startswith(".director/requests/pending/") for p in kept), kept)
            self.assertTrue(any(p.startswith(".director/sources/") for p in kept), kept)


if __name__ == "__main__":
    unittest.main()
