"""Check package isolation and declared payload links, not agent installation behavior."""
import json
import ast
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
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

    def test_source_hook_reaches_flat_package_or_preserves_absent_private_installation(self):
        # Filesystem/reference wiring for both public-clone states, not model behavior.
        authoring = (PATTERN.parent / "AGENTS.md").read_text(encoding="utf-8")
        marker = r"<!-- director-starter:2 -->(.*?)<!-- /director-starter:2 -->"
        hook = re.search(marker, authoring, re.S)
        self.assertIsNotNone(hook)
        branches = re.fullmatch(r"\s*When `([^`]+)` exists in this checkout:\n(.*?)\nOtherwise:\n(.*?)\s*", hook.group(1), re.S)
        self.assertIsNotNone(branches)
        locator, present, absent = branches.groups()
        # Keep the actual starter's role/delegation instructions in the guarded branch.
        tree = ast.parse((PATTERN / "starter/install.py").read_text())
        bridge = next(ast.literal_eval(node.value) for node in tree.body
                      if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "BRIDGE" for t in node.targets))
        installed_hook = re.search(marker, bridge, re.S)
        self.assertIsNotNone(installed_hook)
        normalize = lambda value: " ".join(value.split())
        self.assertEqual(normalize(present), normalize(installed_hook.group(1)))
        manifest = json.loads((PATTERN / "starter/manifest.json").read_text())
        for adopted in (False, True):
            with self.subTest(adopted=adopted), tempfile.TemporaryDirectory() as temporary:
                checkout = Path(temporary)
                (checkout / "AGENTS.md").write_text(authoring)
                if adopted:
                    for name in manifest["payload"]:
                        target = checkout / ".director" / name
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(PATTERN / "starter/payload" / name, target)
                selected = present if (checkout / locator).is_file() else absent
                reads = re.findall(r"Read\s+`([^`]+)`", selected)
                if adopted:
                    self.assertEqual(reads, [locator])
                    self.assertTrue(all((checkout / path).is_file() for path in reads))
                    # Reach real selected foundations without a hidden v1 engine/index.
                    for name in ("START.md", "DIRECTOR.md", "WORKER.md"):
                        document = checkout / ".director" / name
                        for link in markdown_links(document):
                            self.assertTrue((document.parent / link).exists(), link)
                    self.assertFalse((checkout / ".director/engine").exists())
                else:
                    self.assertEqual(reads, [])
                    self.assertFalse((checkout / ".director").exists())
                    self.assertIn("repository maintainer rules above", selected)
                    self.assertIn("assigns no Director role", selected)
                    self.assertIn("# Maintaining this repository", authoring.split("<!-- director-starter:2 -->", 1)[0])

    def test_loaded_hook_explicitly_requests_director_delegation_with_host_precedence(self):
        # Guards the host-loaded entrypoint itself; it cannot prove host permission.
        install = (PATTERN / "INSTALL-v1.md").read_text(encoding="utf-8")
        hook = re.search(r"<!-- director-pattern:start -->(.*?)<!-- director-pattern:end -->", install, re.S)
        self.assertIsNotNone(hook)
        text = " ".join(hook.group(1).split())
        self.assertRegex(text, r"selected Director role.*delegate substantial analysis and project changes.*bounded subagents")
        self.assertIn("higher-priority host instructions", text)

    def test_startup_incomplete_reads_cannot_be_acknowledged_as_loaded(self):
        # Instruction-path check only; a fresh-agent trial must observe behavior.
        text = " ".join((PATTERN / "engine/PATTERN.md").read_text(encoding="utf-8").split())
        self.assertRegex(text, r"failed, missing, or truncated result.*recover and read every missing portion before claiming")
        self.assertRegex(text, r"cannot be recovered, disclose the specific gap and stop affected action")
        self.assertRegex(text, r"acknowledgment reports reads, not permission to delegate.*Recorder availability.*checked setup")

    def test_updates_integrate_changed_hook_without_replacing_local_rules(self):
        # Hook is project-owned, outside the engine replacement; static contract only.
        update = " ".join((PATTERN / "engine/references/UPDATES.md").read_text(encoding="utf-8").split())
        self.assertRegex(update, r"incoming startup hook changes.*existing host-loaded entrypoint")
        self.assertRegex(update, r"Back up and verify the startup file.*compare.*prior and incoming hook")
        self.assertRegex(update, r"Preserve all unrelated bytes and project-specific instructions.*Do not append a duplicate hook")
        self.assertRegex(update, r"ambiguous, retain the original and report the incomplete integration")

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
