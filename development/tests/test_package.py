"""Check package isolation and declared payload links, not agent installation behavior."""
import json
from pathlib import Path, PurePosixPath
import re
import shutil
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
        self.assertTrue({"PATTERN.md", "DIRECTOR.md", "REQUEST_MANAGER.md", "ROLES.md"} <= named, named)
        self.assertLessEqual(named, set(manifest["base_files"]), "Startup hook names only installed files")

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


if __name__ == "__main__":
    unittest.main()
