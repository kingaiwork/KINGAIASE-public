#!/usr/bin/env python3
"""Block accidental personal identity disclosures in the company public repository.

Only scans publishable text; it does not inspect commit history or binary EXIF.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SUFFIXES = {".md", ".txt", ".json", ".html", ".svg", ".xml", ".yml", ".yaml",
            ".js", ".mjs", ".cjs", ".ts", ".tsx", ".astro", ".css"}
EXCLUDE = {Path("scripts/privacy_guard.py")}
IDENTITY = re.compile("jack[._ -]*" + "hao" + "|" + "郝" + "才子", re.I)
REGISTRATION_DETAIL = re.compile(
    r"(?i)(?:\bWyoming\b|\bSheridan\s*,?\s*WY\b|2026-002120886|"
    r"30\s+N\s+Gould\s+St|怀俄明州|州实体编号|注册地址)"
)
FORMATION_CONTEXT = re.compile(
    r"(?i)(?:Nov(?:ember)?\s+1,?\s+2026|2026-11-01)"
)
CORPORATE_CONTEXT = re.compile(r"(?i)\b(?:LLC|Entity ID|formed|formation)\b|成立日期|注册")
PERSONAL_EMAIL = re.compile(
    r"\b[A-Za-z0-9_.+%-]+@(?:gmail|hotmail|outlook|yahoo|icloud|qq|163)\.(?:com|cn)\b",
    re.I,
)
PUBLIC_RATES = re.compile(
    r"(?i)(?:US\$|USD\s*|\$)\s*\d[\d,]*(?:\.\d{1,2})?\s*(?:/|per |a year|monthly|yearly|annual|每月|每年)?"
)
# Explicit standalone public amounts only; code examples showing regular expressions
# and technical numeric notation must not be classified as customer pricing.
PRICE_LINE = re.compile(
    r"(?i)(?:annual fee|implementation fee|pricing table|年费|实施费|起售价|企业版年费)"
)

findings: list[str] = []
checked = 0
for path in sorted(ROOT.rglob("*")):
    if not path.is_file() or ".git" in path.parts:
        continue
    rel = path.relative_to(ROOT)
    if rel in EXCLUDE or path.suffix.lower() not in SUFFIXES:
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    checked += 1
    for line_num, line in enumerate(content.splitlines(), start=1):
        kinds = []
        if IDENTITY.search(line):
            kinds.append("private-identity")
        if PERSONAL_EMAIL.search(line):
            kinds.append("personal-mailbox")
        if REGISTRATION_DETAIL.search(line) or (FORMATION_CONTEXT.search(line) and CORPORATE_CONTEXT.search(line)):
            kinds.append("unnecessary-company-registration-detail")
        if PRICE_LINE.search(line) and PUBLIC_RATES.search(line):
            kinds.append("published-commercial-amount")
        if kinds:
            # Never print the matching value or source line into public CI logs.
            findings.append(f"{rel}:{line_num}: {','.join(kinds)}")

for finding in findings:
    print(f"FAIL {finding}", file=sys.stderr)
if findings:
    print(f"Privacy policy failed: {len(findings)} finding(s).", file=sys.stderr)
    raise SystemExit(1)
print(f"PASS privacy guard: {checked} text files scanned")
