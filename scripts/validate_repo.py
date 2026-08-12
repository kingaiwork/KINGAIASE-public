#!/usr/bin/env python3
"""KING AI SEA public-repository integrity checks.

Uses only the Python standard library so it can run in GitHub Actions without
installing dependencies.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "llms.txt",
    "docs/INDEX.md",
    "docs/FINAL-FLAGSHIP-BLUEPRINT.md",
    "docs/PUBLIC-ARCHITECTURE.md",
    "docs/TRUST-CENTER.md",
    "intelligence/INDEX.md",
    "seo/GEO-KNOWLEDGE-GRAPH.md",
    "seo/AI-SEARCH-ANSWER-MAP.md",
    "seo/SOURCE-OF-TRUTH-MAP.md",
    "seo/FINAL-WEBSITE-INFORMATION-ARCHITECTURE.md",
    "seo/SEO-GEO-QUALITY-STANDARD.md",
]

SKIP_PREFIXES = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "javascript:",
    "data:",
)

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")


def clean_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if " " in target and not target.startswith(SKIP_PREFIXES):
        # Markdown optional link title: path "title"
        target = target.split(" ", 1)[0]
    return unquote(target)


def check_markdown_links(errors: list[str]) -> None:
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = clean_target(raw)
            if not target or target.startswith("#") or target.startswith(SKIP_PREFIXES):
                continue
            path_part = target.split("#", 1)[0].split("?", 1)[0]
            if not path_part:
                continue
            candidate = (md.parent / path_part).resolve()
            try:
                candidate.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link escapes repository: {md.relative_to(ROOT)} -> {target}")
                continue
            if not candidate.exists():
                errors.append(f"broken link: {md.relative_to(ROOT)} -> {target}")


def check_json(errors: list[str]) -> None:
    for pattern in ("*.json", "*.jsonld"):
        for path in ROOT.rglob(pattern):
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except Exception as exc:  # noqa: BLE001
                errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")


def check_public_integrity(errors: list[str]) -> None:
    forbidden = "LEO824"
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".txt", ".json", ".jsonld", ".yml", ".yaml"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if forbidden in text:
            errors.append(f"forbidden legacy public name found: {path.relative_to(ROOT)}")


def main() -> int:
    errors: list[str] = []
    check_required(errors)
    check_markdown_links(errors)
    check_json(errors)
    check_public_integrity(errors)

    if errors:
        print("KING AI SEA repository validation FAILED")
        for item in errors:
            print(f"- {item}")
        return 1

    print("KING AI SEA repository validation PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
