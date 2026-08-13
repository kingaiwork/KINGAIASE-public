# KING AI Public Architecture

## English

This document describes the public architecture of the KING AI intelligent-agent system without exposing proprietary production internals.

## Architecture at a glance

```text
Users / Teams / Enterprises / Developers
                │
                ▼
┌───────────────────────────────────────────────┐
│ Experience & Identity                        │
│ Web · Account · Personal · Enterprise · API  │
└───────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────┐
│ KING AI SEA — Persistent Intelligence Core   │
│ Memory · Knowledge · Missions · Planning     │
│ Verified Intelligence · Agent Coordination   │
└───────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────┐
│ Governance & Trust                            │
│ Policy · Permissions · Approval · Risk       │
│ Audit · Human Override · Controlled Evolution│
└───────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────┐
│ KINGAIBOT — Controlled Execution             │
│ Tools · APIs · MCP · A2A · Workflows         │
│ Services · Devices                           │
└───────────────────────────────────────────────┘
                │
                ▼
┌───────────────────────────────────────────────┐
│ KINGAI OS / Computing                         │
│ Server · Desktop · IoT / Edge                │
└───────────────────────────────────────────────┘
```

## 1. Experience & identity

This is where people and organizations interact with KING AI.

Public product directions include:

- Web and account experiences
- Personal Intelligence
- Enterprise Intelligence
- AI Workforce / AI Employee experiences
- Developer/API access
- Website AI and App AI

The evolving Auth Lite direction is designed to provide a low-friction no-payment account foundation with human verification, verified email and secure sessions before broader commercial account features are introduced.

## 2. Persistent intelligence core

KING AI SEA is the conceptual mother system for:

- useful long-term continuity
- memory and knowledge organization
- goal and mission understanding
- planning and task decomposition
- verified intelligence
- specialized agent coordination
- observation and feedback
- controlled improvement

The goal is not permanent unrestricted autonomy. The goal is persistent intelligence under explicit authority.

## 3. Governance & trust

Governance is a cross-cutting requirement rather than an optional add-on.

Public principles include:

- least privilege
- explicit execution boundaries
- approval for high-impact actions
- auditability
- human override
- fail-closed behavior for dangerous or uncertain operations
- reversible deployment and update patterns
- controlled evolution rather than unrestricted self-modification

Related public concepts:

- Root Policy Kernel
- ACRE active-defense / immune-system direction
- SAE controlled evolution direction
- owner-defined action ladder

## 4. Controlled execution

KINGAIBOT is the execution-oriented project intended to bridge intelligence and authorized digital action.

Its public v1.2.0 engineering foundation documents:

- durable tasks and restart recovery
- `allow / ask / deny` execution policy
- sandboxed filesystem capabilities
- restricted shell behavior
- HTTPS protections
- separate identities for administrative and agent protocols
- MCP and A2A interoperability
- audit integrity
- safe update and rollback patterns
- controlled evolution proposals

KINGAIBOT remains under active development and should not be represented as a fully mature universal execution platform.

## 5. AI-native computing

KINGAI OS is the system-level computing direction for:

- Server
- Desktop
- IoT / Edge

Public principles include local-first operation, model neutrality, cloud neutrality, least privilege, secure updates, privacy-aware memory and replaceable execution engines.

Current public status: **D4 Developer Foundation / Pre-Alpha**.

## 6. Global delivery & survival architecture

KING AI public services are designed around the principle that public availability should not depend synchronously on one private AI host.

High-level delivery direction:

```text
Private / heavy intelligence work
        │
        ▼
Verified public data / approved artifacts
        │
        ▼
Global edge delivery and cache
        │
        ▼
Web / API / account / public intelligence
```

Public delivery may use Cloudflare technologies for static delivery, serverless APIs, data storage, bot protection, caching and asynchronous workloads where appropriate. Specific production bindings, IDs, credentials and sensitive operational topology are not public documentation.

## 7. Research & knowledge layer

The public repository is itself part of the architecture:

- KING AI Intelligence
- technology radar
- enterprise frameworks
- AI Workforce role library
- industry scenario library
- trust and governance documents
- SEO/GEO and AI-search sources
- machine-readable public facts

This allows search engines, AI systems, enterprises and developers to understand the system from canonical public sources without exposing production code.

## 8. Model and framework neutrality

KING AI is designed so that the identity of the system is not tied to one LLM, model provider, cloud platform, agent framework or execution engine.

Models and third-party technologies are treated as replaceable resources, integrations or research signals. Public references to third-party technologies do not automatically mean a feature is currently integrated or production-ready.

## Public/private boundary

Public architecture documents may explain:

- product relationships
- capabilities
- high-level components
- user and enterprise workflows
- governance models
- commercial packaging
- integration patterns

They do not publish production secrets, customer data, proprietary internal orchestration or security-sensitive operational detail.

---

# 中文

## KING AI 公开系统架构

KING AI 的公开架构可以概括为五层：

```text
体验与身份
    ↓
KING AI SEA 持续智慧核心
    ↓
治理与信任
    ↓
KINGAIBOT 受控执行
    ↓
KINGAI OS / Server / Desktop / Edge
```

### 体验与身份层
覆盖网站、账户、个人智慧、企业智慧、AI Workforce、开发者/API 和 Website/App AI。Auth Lite 当前作为无支付注册、真人验证、邮箱验证和安全 Session 的轻量身份基础进行部署验证。

### 持续智慧核心
由 KING AI SEA 统一承担长期连续性、记忆、知识、Mission、规划、可信情报、Agent 协同、观察反馈和受控改进方向。

### 治理与信任
坚持最小权限、明确执行边界、高风险审批、审计、人工接管、危险操作 Fail-Closed、可回滚和受控进化。

### KINGAIBOT 执行层
负责把上层智慧转化为授权数字行动。公开 v1.2.0 已展示持久任务、allow/ask/deny、沙箱、MCP/A2A、审计、更新与回滚等工程基础，但仍属于持续开发项目。

### KINGAI OS 计算层
面向 Server、Desktop、IoT / Edge，强调本地优先、模型中立、云中立、安全默认、隐私与可替换执行引擎。当前为 D4 Developer Foundation / Pre-Alpha。

### 全球交付与生存架构
公开服务的原则是：即使某个私有 AI 节点暂时不可用，网站、账户、API、可信缓存和公共信息仍应尽可能保持独立可用。Cloudflare 等边缘基础设施承担全球交付、缓存、数据与防机器人能力，但生产 ID、密钥和敏感拓扑不进入公共仓。
