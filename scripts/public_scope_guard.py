#!/usr/bin/env python3
"""Ensure the public repository is focused on business, products and solutions."""
from pathlib import Path
import json
import sys

root = Path(__file__).resolve().parent.parent
required = {"README.md", "BUSINESS.md", "PRODUCTS.md", "SOLUTIONS.md",
            "llms.txt", "public-project-facts.json", "customer-knowledge.json"}
removed_topics = {
    "INVESTORS.md", "DILIGENCE.md", "MARKET.md",
    "COMMERCIAL-PACKAGING.md", "RELATED-PROJECTS.md",
    "FOUNDER-PROJECTS.md", "PUBLIC-PORTFOLIO.md",
    "REPOSITORY-CONSOLIDATION.md", "KINGAI_SYSTEM.md",
}
missing = sorted(path for path in required if not (root / path).is_file())
unexpected = sorted(path for path in removed_topics if (root / path).exists())

facts = json.loads((root / "public-project-facts.json").read_text(encoding="utf-8"))
knowledge = json.loads((root / "customer-knowledge.json").read_text(encoding="utf-8"))
assert facts.get("presentation_scope") == "business-products-solutions"
assert facts.get("business_areas") and facts.get("products") and facts.get("solution_areas")
assert not facts.get("related_projects") and not facts.get("internal_foundations")
assert knowledge.get("presentation_scope") == "business-products-solutions"
assert all(str(row.get("source_path", "")) in {p for p in required if p.endswith(".md")}
           for row in knowledge.get("entries", []))
readme = (root / "README.md").read_text(encoding="utf-8")
for doc in ("BUSINESS.md", "PRODUCTS.md", "SOLUTIONS.md"):
    assert f"]({doc})" in readme, f"README missing {doc} link"
if missing or unexpected:
    for path in missing:
        print(f"FAIL required-public-document {path}", file=sys.stderr)
    for path in unexpected:
        print(f"FAIL out-of-scope-document {path}", file=sys.stderr)
    raise SystemExit(1)
print("PASS business / products / solutions public-scope guard")
