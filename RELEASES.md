# KING AI Verified Releases

**Unified public release policy**  
Main system: https://www.kingai.work/  
Business: vip@kingai.work

## English

This repository is the unified public reference point for current customer-facing release information across downloadable KING AI products.

A product is **Current / Verified** only after its private production authority has produced the required customer artifact and the release gate has verified the relevant integrity and startup/install behavior. A commit, build attempt, roadmap statement, draft release or partially uploaded asset is not release truth.

### Product-scoped release truth

Multiple products share this public hub, so repository-global `releases/latest` must not be treated as the current version of every KING AI product.

Downloadable products use product-scoped release references such as:

| Product | Tag pattern | Current truth | Stable channel |
|---|---|---|---|
| KINGAI OPS | `kingai-ops-vX.Y.Z` | `releases/KINGAI-OPS-CURRENT.md` | `releases/kingai-ops-latest.txt` |
| KINGAI OS | `kingai-os-vX.Y.Z` | `releases/KINGAI-OS-CURRENT.md` | `releases/kingai-os-latest.txt` |
| KINGAI Security | `kingai-security-vX.Y.Z` | `releases/KINGAI-SECURITY-CURRENT.md` | `releases/kingai-security-latest.txt` |
| KINGAI Office | `kingai-office-vX.Y.Z` | `releases/KINGAI-OFFICE-CURRENT.md` | `releases/kingai-office-latest.txt` |
| KINGAIBOT | `kingaibot-vX.Y.Z` | `releases/KINGAIBOT-CURRENT.md` | `releases/kingaibot-latest.txt` |

A current-truth or channel file is created or updated only after the corresponding release process has verified the remotely published assets. If the product-scoped truth file does not exist, do not invent a current version.

### What users should trust

For downloadable software, prefer this order:

1. product-specific current-truth document in this hub;
2. immutable product-prefixed release tag referenced by that document;
3. official product website release/download guidance;
4. historical legacy repository assets only when explicitly needed for an older installation.

### What users should not infer

- A GitHub commit is not automatically a customer release.
- A CI build is not automatically a verified release.
- A legacy public repository is not automatically a current release authority.
- A future roadmap feature is not automatically present in a downloadable build.

### Verification contract

The public release model is:

**private production authority → tests → build → customer-safe artifact → integrity verification → installation/startup smoke where applicable → immutable product tag → reread/verify published assets → product-scoped current truth.**

Private build paths, signing secrets, deployment credentials, infrastructure topology, internal source and security implementation remain private.

### Web-first products

Products delivered primarily through their official web experience should be treated as web-first unless an explicit downloadable release is published here.

### Legacy release repositories

Older product-specific public repositories can retain historical assets or references during consolidation, but their default branches should redirect users toward this unified hub and the official current product experience. Historical immutable assets may remain useful for existing installations without making the old repository the current authority.

---

# 中文

本仓是 KING AI 可下载产品当前公开发布信息的统一参考入口。

一个版本只有在私有生产权威仓完成构建，并通过必要的完整性、安装/启动等验证以后，才能称为 **Current / Verified**。普通 commit、构建尝试、路线图、草稿 Release 或只上传了一部分文件，都不能代表正式发布。

### 产品级发布真相

因为多个产品共用一个公开中心，不能直接把整个仓的 `releases/latest` 当成所有产品的“最新版”。每个可下载产品必须使用自己的产品前缀 Tag、CURRENT 文件和 latest channel。

### 用户应该相信什么

优先顺序：

1. 本仓中的产品级 CURRENT 文件；
2. CURRENT 文件指向的不可变产品 Tag；
3. 官方产品网站；
4. 只有在需要旧版本时才使用 legacy 仓中的历史资产。

### 不应该推断什么

Git commit 不等于发布；CI 构建不等于正式版本；旧公开仓不等于当前发布权威；路线图也不等于当前安装包已经包含。

公开发布中心不会公开私有构建路径、签名密钥、部署凭据、基础设施拓扑、内部源码或安全实现。
