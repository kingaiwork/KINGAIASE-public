# 🌐 KING AI SEA — Website / GitHub / GEO Content Sync Specification

---

# English

## 1. Canonical Sources

Primary website: https://www.kingai.work  
Public repository: https://github.com/kingaiwork/kingai-sea

GitHub is the public product knowledge source. The website is the primary customer-facing publishing surface. Both must preserve the same entity model.

## 2. Canonical Entity Rules

- Brand: **KING AI**
- Unified system: **KING AI SEA**
- English category: **Intelligent Lifeform Platform**
- Chinese: **智慧生命体平台**
- Evolution OS: operating architecture inside KING AI SEA
- SAE: controlled self-evolution mechanism inside KING AI SEA
- ACRE: active-defense / immune-system security concept inside KING AI SEA
- Root Policy Kernel: high-authority policy and execution-boundary concept
- AI Workforce: enterprise operating model powered by KING AI SEA
- AI Employees: roles inside AI Workforce

Never represent these as unrelated competing products.

## 3. Website Content Sources

| Website Area | Repository Source |
|---|---|
| Homepage | README + FINAL-FLAGSHIP-BLUEPRINT |
| Intelligent Lifeform | INTELLIGENT-LIFEFORM-VISION |
| Capabilities | CAPABILITY-MAP |
| Architecture | PUBLIC-ARCHITECTURE + SOLUTION-ARCHITECTURE-TEMPLATES |
| Enterprise | ENTERPRISE + ENTERPRISE-BUYER-GUIDE |
| AI Workforce | AI-WORKFORCE-OPERATING-MODEL |
| AI Employees | AI-EMPLOYEE-ROLE-LIBRARY + role packs |
| Trust | TRUST-CENTER + SECURITY-QUESTIONNAIRE |
| Industries | INDUSTRY-SCENARIO-LIBRARY + industry GEO packs |
| Developers | DEVELOPER-ECOSYSTEM |
| Partners | PARTNER-ECOSYSTEM + PARTNER-CERTIFICATION-FRAMEWORK |
| FAQ | CANONICAL-QA-LIBRARY |
| Evaluation | BENCHMARK-EVALUATION-FRAMEWORK |
| Contact | vip@kingai.work |

## 4. Multilingual Rules

- English canonical pages first.
- Full Chinese equivalents, not mixed bilingual paragraphs.
- `/zh/...` for Chinese pages.
- `hreflang=en`, `zh-CN`, `x-default`.
- Translate meaning, not keyword spam.

## 5. SEO / GEO Rules

Every production page should include:

- unique title
- unique meta description
- canonical URL
- H1
- concise definition near top
- entity-consistent copy
- internal links
- relevant FAQ
- JSON-LD as appropriate
- visible capability-status language
- updated sitemap

## 6. AI-Readable Sources

Maintain:

- `llms.txt`
- GEO Knowledge Graph
- AI Search Answer Map
- canonical FAQ JSON-LD
- product / organization structured data
- industry pack index

## 7. Change Management

When product positioning changes:

1. update canonical repository sources
2. update website copy
3. update llms / GEO graph
4. update JSON-LD
5. update FAQ if definitions changed
6. update sitemap if URLs changed
7. verify English and Chinese entity consistency

## 8. Technology Protection

Website and repository may explain public architecture but must not publish private prompts, memory structures, routing logic, SAE internals, ACRE detection, Root Policy implementation, credentials, internal APIs or production topology.

---

# 中文

官网和 GitHub 必须保持同一套品牌实体与产品定义。

官网是客户主入口，GitHub 是公开产品知识源。任何核心定位变化都应先更新标准知识，再同步官网、`llms.txt`、GEO 图谱、JSON-LD、FAQ 和 Sitemap。

英文页面完整独立，中文使用 `/zh/` 完整页面，并设置 `en / zh-CN / x-default` hreflang。

所有生产页都应具有唯一 Title、Description、Canonical、H1、顶部直接定义、内部链接、FAQ、合适的 Structured Data 和真实状态标签。

公开内容只展示能力和大概架构，不公开私有 Prompt、Memory 内部结构、模型路由、SAE 算法、ACRE 检测、Root Policy Kernel 实现、密钥、内部 API 或生产拓扑。