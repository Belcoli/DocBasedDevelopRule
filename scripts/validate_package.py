#!/usr/bin/env python3
"""Optional maintainer checks. No third-party dependency; not a skill runtime."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

PLUGIN = "document-first-development"
MARKETPLACE = "document-first-development-marketplace"
EXCLUDED = {".git", ".validation-local", "dist", "__pycache__"}
LOCAL_LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
MACHINE_PATH = re.compile(r"(?<![\w])[A-Za-z]:[\\/]|/(?:Users|home)/[^/\s]+/")


def within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def source_files(root: Path) -> list[Path]:
    return [
        path
        for path in root.rglob("*")
        if path.is_file()
        and not any(part in EXCLUDED for part in path.relative_to(root).parts)
    ]


def anchors(text: str) -> set[str]:
    result: set[str] = set()
    counts: dict[str, int] = {}
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        if fenced:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        title = re.sub(r"<[^>]+>", "", match.group(1)).replace("`", "")
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        count = counts.get(slug, 0)
        result.add(slug if count == 0 else f"{slug}-{count}")
        counts[slug] = count + 1
    return result


def relative_entry(root: Path, value: object, errors: list[str], label: str) -> Path | None:
    if not isinstance(value, str) or not value.startswith("./"):
        errors.append(f"{label}: expected ./-relative path")
        return None
    parts = value.replace("\\", "/").split("/")
    candidate = root / value
    if ".." in parts or not within(candidate, root):
        errors.append(f"{label}: path escapes its root")
        return None
    if not candidate.exists():
        errors.append(f"{label}: missing target")
        return None
    return candidate


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    errors: list[str] = []
    counts = {"markdown": 0, "local_links": 0}
    plugin_root = root / "plugins" / PLUGIN
    manifest_file = plugin_root / ".codex-plugin" / "plugin.json"
    catalog_file = root / ".agents" / "plugins" / "marketplace.json"

    def read_json(path: Path) -> dict:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(value, dict):
                raise ValueError("expected an object")
            return value
        except (OSError, ValueError) as exc:
            errors.append(f"{path.relative_to(root)}: invalid JSON ({type(exc).__name__})")
            return {}

    manifest = read_json(manifest_file)
    catalog = read_json(catalog_file)
    if manifest.get("name") != PLUGIN:
        errors.append("plugin identity mismatch")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?", str(manifest.get("version", ""))):
        errors.append("plugin version must be explicit")
    if not manifest.get("description"):
        errors.append("plugin description is missing")
    for field in ("mcpServers", "apps", "hooks", "dependencies"):
        if manifest.get(field):
            errors.append(f"unexpected runtime dependency: {field}")
    skills_root = relative_entry(plugin_root, manifest.get("skills"), errors, "skills")
    skill_files = list(skills_root.glob("*/SKILL.md")) if skills_root else []
    if len(skill_files) != 1:
        errors.append("expected exactly one skill entry")
    for skill_file in skill_files:
        text = skill_file.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not match:
            errors.append("skill frontmatter is missing")
            continue
        fields = {}
        for line in match.group(1).splitlines():
            key, sep, value = line.partition(":")
            if sep:
                fields[key.strip()] = value.strip().strip('"')
        if fields.get("name") != PLUGIN or skill_file.parent.name != PLUGIN:
            errors.append("skill identity mismatch")
        if not fields.get("description"):
            errors.append("skill description is missing")
        if len(text.splitlines()) > 120:
            errors.append("skill entry grew beyond this package's concise-entry budget")

    if catalog.get("name") != MARKETPLACE:
        errors.append("marketplace identity mismatch")
    entries = catalog.get("plugins")
    if not isinstance(entries, list) or len(entries) != 1:
        errors.append("expected exactly one marketplace entry")
        entries = []
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("invalid marketplace entry")
            continue
        if entry.get("name") != PLUGIN:
            errors.append("marketplace plugin identity mismatch")
        source = entry.get("source", {})
        if not isinstance(source, dict) or source.get("source") != "local":
            errors.append("expected repository-local plugin source")
            continue
        target = relative_entry(root, source.get("path"), errors, "marketplace source")
        if target and target.resolve() != plugin_root.resolve():
            errors.append("marketplace source does not point to this plugin")
        policy = entry.get("policy", {})
        if not isinstance(policy, dict):
            errors.append("marketplace policy must be an object")
            policy = {}
        if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
            errors.append("marketplace policy mismatch")
        if not entry.get("category"):
            errors.append("marketplace category is missing")

    for path in source_files(root):
        if not within(path, root):
            errors.append(f"{path.relative_to(root)}: source escapes repository")
            continue
        if path.suffix.lower() not in {".md", ".json", ".yaml", ".yml"}:
            continue
        text = path.read_text(encoding="utf-8")
        if MACHINE_PATH.search(text):
            errors.append(f"{path.relative_to(root)}: host-specific absolute path")
        if path.suffix.lower() != ".md":
            continue
        counts["markdown"] += 1
        for match in LOCAL_LINK.finditer(text):
            raw = match.group(1).strip()
            if "{{" in raw:
                continue
            raw = raw.split(' "', 1)[0].strip("<>")
            parsed = urlsplit(raw)
            if parsed.scheme or parsed.netloc:
                continue
            counts["local_links"] += 1
            target = (path.parent / unquote(parsed.path)) if parsed.path else path
            boundary = plugin_root if within(path, plugin_root) else root
            if not within(target, boundary):
                errors.append(f"{path.relative_to(root)}: reference escapes allowed root: {raw}")
            elif not target.is_file():
                errors.append(f"{path.relative_to(root)}: missing local reference: {raw}")
            elif parsed.fragment and target.suffix.lower() == ".md":
                if unquote(parsed.fragment) not in anchors(target.read_text(encoding="utf-8")):
                    errors.append(f"{path.relative_to(root)}: missing heading: {raw}")
    return errors, counts


def self_test(root: Path) -> None:
    scratch = root / ".validation-local"
    scratch.mkdir(exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix="validator-", dir=scratch)).resolve()
    if temp.parent != scratch.resolve():
        raise RuntimeError("Unexpected temporary directory")
    try:
        for original in source_files(root):
            target = temp / original.relative_to(root)
            if not within(target, temp):
                raise RuntimeError("Copy target escapes temporary directory")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(original, target)
        baseline, _ = validate(temp)
        if baseline:
            raise AssertionError(f"Baseline failed: {baseline}")
        plugin_root = temp / "plugins" / PLUGIN
        skill = plugin_root / "skills" / PLUGIN / "SKILL.md"
        manifest = plugin_root / ".codex-plugin" / "plugin.json"
        catalog = temp / ".agents" / "plugins" / "marketplace.json"
        cases = []

        data = json.loads(manifest.read_text(encoding="utf-8"))
        data["skills"] = "./../outside"
        cases.append(("reject escaped skill directory", manifest, json.dumps(data), "path escapes"))
        data = json.loads(catalog.read_text(encoding="utf-8"))
        data["plugins"][0]["source"]["path"] = "./../outside"
        cases.append(("reject escaped marketplace source", catalog, json.dumps(data), "path escapes"))
        data = json.loads(catalog.read_text(encoding="utf-8"))
        data["plugins"][0]["policy"] = None
        cases.append(("reject non-object marketplace policy", catalog, json.dumps(data), "marketplace policy must be an object"))
        original_skill = skill.read_text(encoding="utf-8")
        cases.append(("reject missing resource", skill, original_skill + "\n[x](missing.md)\n", "missing local reference"))
        cases.append(("reject runtime reference to repository docs", skill, original_skill + "\n[x](../../../../docs/design.md)\n", "reference escapes"))
        cases.append(("reject invalid skill identity", skill, original_skill.replace("name: " + PLUGIN, "name: different", 1), "skill identity"))
        machine_example = "Q" + chr(58) + chr(92) + "host-bound"
        cases.append(("reject host path in instructions", skill, original_skill + "\n" + machine_example + "\n", "host-specific"))
        for name, path, changed, expected in cases:
            before = path.read_text(encoding="utf-8")
            try:
                path.write_text(changed, encoding="utf-8")
                errors, _ = validate(temp)
                if not any(expected in item for item in errors):
                    raise AssertionError(f"{name}: failure was not detected")
                print(f"PASS: {name}")
            finally:
                path.write_text(before, encoding="utf-8")
        restored, _ = validate(temp)
        if restored:
            raise AssertionError(f"Restored baseline failed: {restored}")
        print(f"PASS: {len(cases)} negative cases and restored baseline")
    finally:
        # This exact newly-created directory is the only recursive delete target.
        if temp.resolve().parent != scratch.resolve():
            raise RuntimeError("Refusing cleanup outside verification scratch")
        shutil.rmtree(temp)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    errors, counts = validate(args.root)
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    print(f"PASS: {counts['markdown']} Markdown files, {counts['local_links']} local references; package identity and containment valid")
    if args.self_test:
        self_test(args.root.resolve())
    return 0


if __name__ == "__main__":
    sys.exit(main())
