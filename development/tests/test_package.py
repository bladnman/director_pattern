"""Check package isolation and declared payload links, not agent installation behavior."""
import json
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
        guidance = {"README.md", "INSTALL.md"}
        contracts = {p.relative_to(PATTERN).as_posix() for p in PATTERN.rglob("*.md")} - guidance
        self.assertLessEqual(contracts, set(manifest["base_files"]), "Lean installs must be self-contained")
        install = (PATTERN / "INSTALL.md").read_text(encoding="utf-8")
        hook = re.search(r"<!-- director-pattern:start -->(.*?)<!-- director-pattern:end -->", install, re.S)
        assert hook is not None, "INSTALL must carry the marked startup hook"
        named = set(re.findall(r"\b[A-Z_]+\.md\b", hook.group(1)))
        self.assertEqual(named, {"PATTERN.md"}, "The common hook routes through the bootstrap, not selected role duties")
        self.assertLessEqual(named, set(manifest["base_files"]), "Startup hook names only installed files")

    def test_common_bootstrap_does_not_load_director_policies(self):
        # Structural contract boundary; does not measure size or imitate role behavior.
        common = set(markdown_links(PATTERN / "PATTERN.md"))
        self.assertIn("WORKER.md", common)
        self.assertTrue(common.isdisjoint({"DIRECTION.md", "DIRECTOR.md", "REQUEST_MANAGER.md", "STATE.md", "MODELS.md"}))
        for definition in ("DIRECTOR.md", "REQUEST_MANAGER.md"):
            self.assertIn("DIRECTION.md", set(markdown_links(PATTERN / definition)))
        self.assertNotIn("DIRECTION.md", set(markdown_links(PATTERN / "WORKER.md")))

    def test_repository_and_installation_hooks_share_the_same_startup_barrier(self):
        # Static entrypoint parity only: no assertion here proves a host obeys it.
        marker = r"<!-- director-pattern:start -->(.*?)<!-- director-pattern:end -->"
        install = (PATTERN / "INSTALL.md").read_text(encoding="utf-8")
        authoring = (PATTERN.parent / "AGENTS.md").read_text(encoding="utf-8")
        install_hook = re.search(marker, install, re.S)
        authoring_hook = re.search(marker, authoring, re.S)
        self.assertIsNotNone(install_hook)
        self.assertIsNotNone(authoring_hook)
        normalize = lambda value: " ".join(value.split())
        common = normalize(install_hook.group(1))
        # The source repository alone adds its optional-local-installation guard.
        self.assertIn(common, normalize(authoring_hook.group(1)))

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
            definitions = ["DIRECTOR.md", "REQUEST_MANAGER.md", "RECORDER.md", "ANALYSIS.md"]
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
            (installed / "roles/reader.md").write_text("# Fixture reader\nRead [worker boundaries](../WORKER.md).\n", encoding="utf-8")
            index.write_text(index.read_text() + "\n[Fixture reader](roles/reader.md)\n", encoding="utf-8")
            self.assertIn("roles/reader.md", set(markdown_links(index)))
            self.check_links(installed)

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
