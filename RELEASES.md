# KING AI Verified Releases

This file is the public release index for the KING AI ecosystem.

A product may be listed as **Current** only after its private source authority has produced the required artifacts and the release gate has verified the applicable package, checksum/signature and smoke test. A repository commit, build attempt or roadmap statement is not a verified release.

## Release families

| Product | Private source authority | Public release status |
|---|---|---|
| KINGAIBOT | private KINGAIBOT source authority | Use product-linked verified assets only |
| KINGAI OS | private KINGAI OS source authority | Use product-linked verified assets only |
| KINGAI OPS | private KINGAI OPS source authority | Use product-linked verified assets only |
| KINGAI Security | private KINGAI Security source authority | Use product-linked verified assets only |
| KINGAI Office | private KINGAI Office source authority | Use product-linked verified assets only |

Other web-first products are distributed through their official product surfaces unless a downloadable release is explicitly published.

## Verification contract

For downloadable software, the minimum publication gate is:

**registered private authority → tests → build → immutable artifact → SHA-256 or stronger verification → signature where supported → installation/startup smoke → release record → public index**

The public hub does not expose private build configuration, signing secrets, deployment credentials or proprietary source.

## Legacy release repositories

Older product-specific public repositories may still contain historical links or assets during consolidation. Their presence does not make them the current source authority. The current public KING AI navigation and release index lives in `kingaiwork/KINGAIASE-public`.
