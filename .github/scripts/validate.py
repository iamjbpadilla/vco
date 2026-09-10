#!/usr/bin/env python3
"""
VCO 0.1.0 deterministic validator.

Runs with Python 3 standard library only. No dependencies to install.

Usage:
    python3 .github/scripts/validate.py               # manifest / state + version + terminology
    python3 .github/scripts/validate.py --structure   # normative file tree check
    python3 .github/scripts/validate.py --links       # internal markdown link check
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ALLOWED_PROFILES = {"web", "pwa", "mobile", "saas", "api", "internal-tool"}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:-[a-zA-Z0-9.]+)?(?:\+[a-zA-Z0-9.]+)?$")

# Normative file tree (from VCO 0.1 plan). Directories are listed with a trailing slash.
NORMATIVE = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "AGENTS.md",
    "SKILL.md",
    "assets/logo.png",
    ".github/workflows/ci.yml",
    ".github/scripts/validate.py",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    "rules/core.md",
    "rules/verity.md",
    "rules/scope.md",
    "rules/architecture.md",
    "rules/design.md",
    "rules/security.md",
    "rules/testing.md",
    "rules/deployment.md",
    "skills/plan/SKILL.md",
    "skills/build/SKILL.md",
    "skills/test/SKILL.md",
    "skills/review/SKILL.md",
    "skills/audit/SKILL.md",
    "skills/ship/SKILL.md",
    "templates/AGENTS.md",
    "templates/PROJECT_STATE.md",
    "templates/SCOPE.md",
    "templates/REQUIREMENTS.md",
    "templates/TASKS.md",
    "templates/CHANGE_REQUEST.md",
    "templates/ADR.md",
    "profiles/web.md",
    "profiles/pwa.md",
    "profiles/mobile.md",
    "profiles/saas.md",
    "profiles/api.md",
    "profiles/internal-tool.md",
    "docs/philosophy.md",
    "docs/architecture.md",
    "docs/workflow.md",
    "docs/agent-compatibility.md",
    "docs/getting-started.md",
    "packages/cli/README.md",
    # Dogfood layer (required by spec §34 for the VCO project itself)
    ".vco/manifest.json",
    ".vco/state.json",
    ".vco/decisions/",
    ".vco/context/",
    ".vco/verification/",
    "PROJECT_STATE.md",
    "SCOPE.md",
    "REQUIREMENTS.md",
    "TASKS.md",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def validate_manifest() -> None:
    manifest_path = ROOT / ".vco" / "manifest.json"
    if not manifest_path.exists():
        fail(".vco/manifest.json not found")

    with manifest_path.open() as f:
        try:
            manifest = json.load(f)
        except json.JSONDecodeError as exc:
            fail(f"manifest.json is not valid JSON: {exc}")

    if not isinstance(manifest.get("vco"), dict):
        fail("manifest.json: 'vco' must be an object")
    version = manifest["vco"].get("version")
    if not version:
        fail("manifest.json: missing vco.version")
    if not SEMVER_RE.match(version):
        fail(f"manifest.json: vco.version '{version}' is not a valid semantic version")

    project = manifest.get("project")
    if not isinstance(project, dict):
        fail("manifest.json: 'project' must be an object")
    name = project.get("name")
    if not name or not isinstance(name, str):
        fail("manifest.json: missing or empty project.name")
    profile = project.get("profile")
    if profile not in ALLOWED_PROFILES:
        fail(f"manifest.json: project.profile '{profile}' not in {ALLOWED_PROFILES}")

    author = manifest.get("author")
    if not isinstance(author, dict):
        fail("manifest.json: 'author' must be an object")
    author_name = author.get("name")
    if not author_name or not isinstance(author_name, str):
        fail("manifest.json: missing or empty author.name")

    state_path = ROOT / ".vco" / "state.json"
    if not state_path.exists():
        fail(".vco/state.json not found")
    with state_path.open() as f:
        try:
            json.load(f)
        except json.JSONDecodeError as exc:
            fail(f"state.json is not valid JSON: {exc}")

    # Consistency checks
    for path in [ROOT / "README.md", ROOT / "CHANGELOG.md"]:
        text = path.read_text()
        if version not in text:
            fail(f"{path.name} does not contain version {version}")

    print("PASS: manifest, state, and version consistency")


def validate_structure() -> None:
    missing = []
    for relative in NORMATIVE:
        absolute = ROOT / relative
        if relative.endswith("/"):
            if not absolute.is_dir():
                missing.append(relative)
        else:
            if not absolute.is_file():
                missing.append(relative)

    if missing:
        fail("Missing normative files/directories:\n  " + "\n  ".join(missing))

    # Check for unexpected top-level files/directories not in the plan
    allowed_root = {
        ".git",
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "AGENTS.md",
        "SKILL.md",
        "assets",
        ".github",
        ".vco",
        "rules",
        "skills",
        "templates",
        "profiles",
        "docs",
        "packages",
        "PROJECT_STATE.md",
        "SCOPE.md",
        "REQUIREMENTS.md",
        "TASKS.md",
    }
    extra = [p.name for p in ROOT.iterdir() if p.name not in allowed_root]
    if extra:
        fail(f"Unexpected top-level entries: {extra}")

    print("PASS: required file tree present, no unexpected top-level entries")


def _extract_links(text: str) -> list[str]:
    """Extract relative markdown links (not URLs or anchors)."""
    links = set()
    # [text](path)
    for match in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", text):
        target = match[1]
        # skip anchors, web URLs, and mailto
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if target.startswith("/"):
            target = target[1:]  # absolute-from-root path
        links.add(target)
    return list(links)


def validate_links() -> None:
    broken = []
    for md in ROOT.rglob("*.md"):
        if md.name == "CHANGELOG.md":  # external URLs and releases; not checked
            continue
        text = md.read_text()
        for link in _extract_links(text):
            if link.startswith("../"):
                target = md.parent / link
            else:
                target = md.parent / link
            # Resolve relative paths to the repo root
            try:
                resolved = target.resolve()
            except OSError:
                broken.append((md.relative_to(ROOT), link))
                continue
            if not resolved.exists():
                broken.append((md.relative_to(ROOT), link))

    if broken:
        msg = "\n  ".join(f"{src} -> {link}" for src, link in broken)
        fail(f"Broken internal markdown links:\n  {msg}")

    print("PASS: internal markdown links verified")


def main() -> None:
    parser = argparse.ArgumentParser(description="VCO 0.1.0 validator")
    parser.add_argument("--structure", action="store_true", help="check normative file tree")
    parser.add_argument("--links", action="store_true", help="check internal markdown links")
    args = parser.parse_args()

    if args.structure:
        validate_structure()
    elif args.links:
        validate_links()
    else:
        validate_manifest()


if __name__ == "__main__":
    main()
