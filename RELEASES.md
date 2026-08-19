# KING AI Verified Releases

This repository is the unified public release hub for downloadable KING AI products.

A product is **Current / Verified** only after its registered private source authority has produced the required artifacts and the release gate has verified package integrity, checksums/signatures where applicable and installation/startup behavior. A commit, build attempt or partially uploaded Release is not release truth.

## Multi-product release convention

Because multiple products share this repository, **do not use GitHub repository-global `releases/latest` as product truth**.

Each downloadable product uses:

- a product-prefixed immutable release tag;
- a product-specific current-release document;
- a product-specific latest-channel pointer.

Examples:

| Product | Public tag pattern | Current truth | Stable channel |
|---|---|---|---|
| KINGAI OPS | `kingai-ops-vX.Y.Z` | `releases/KINGAI-OPS-CURRENT.md` | `releases/kingai-ops-latest.txt` |
| KINGAI OS | `kingai-os-vX.Y.Z` | `releases/KINGAI-OS-CURRENT.md` | `releases/kingai-os-latest.txt` |
| KINGAI Security | `kingai-security-vX.Y.Z` | `releases/KINGAI-SECURITY-CURRENT.md` | `releases/kingai-security-latest.txt` |
| KINGAI Office | `kingai-office-vX.Y.Z` | `releases/KINGAI-OFFICE-CURRENT.md` | `releases/kingai-office-latest.txt` |
| KINGAIBOT | `kingaibot-vX.Y.Z` | `releases/KINGAIBOT-CURRENT.md` | `releases/kingaibot-latest.txt` |

A channel/truth file is created or updated **only after the corresponding release pipeline has reread and verified the uploaded assets**. Missing channel files mean there is no unified-hub verified current release yet; never invent one manually.

## Release source authorities

| Product | Private source authority |
|---|---|
| KINGAIBOT | `kingaiwork/kingibot` |
| KINGAI OS | `kingaiwork/kingaioscode` |
| KINGAI OPS | `kingaiwork/kingai-ops` |
| KINGAI Security | `kingaiwork/KINGAI-Security` |
| KINGAI Office | `kingaiwork/office-` |

Other web-first products are delivered through their official product surfaces unless a downloadable release is explicitly registered.

## Verification contract

Minimum downloadable-software publication gate:

**registered private authority → tests → build → source-free/customer-safe artifact as applicable → checksum/signature → installation/startup smoke → immutable product-prefixed release → reread/verify remote assets → product current truth/channel**

The public hub never exposes private build configuration, signing secrets, deployment credentials or proprietary source.

## Legacy release repositories

Older product-specific public repositories may retain historical Releases and links while repository consolidation is completed. Archiving those repositories preserves history; it does not make them current source or release authorities.

Existing installations using a historical product-specific release URL may continue to use those immutable assets. New release pipelines must converge on the product-scoped channels in this repository.
