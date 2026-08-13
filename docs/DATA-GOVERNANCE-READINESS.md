# 🗂️ KING AI SEA — Data Governance & Readiness

# English

## Data Readiness Questions
- What sources are authoritative?
- Who owns each source?
- Which sources are current?
- Which data can be used for reading, reasoning, drafting or action?
- Which data is sensitive or restricted?
- What retention/deletion requirements apply?
- What data must remain isolated by team, customer, region or environment?

## Source Classes
1. Public knowledge
2. Internal general knowledge
3. Customer/account data
4. Operational data
5. Financial data
6. Employee/HR data
7. Security-sensitive data
8. Regulated/special-category data

## Connection Rules
Every source should define:
- owner
- purpose
- access method
- read/write mode
- role access
- mission access
- environment
- freshness expectations
- audit needs
- deletion/offboarding process

## Stateful-Agent Residency Map
For persistent agents, do not treat "region" as one inherited setting. Record storage, processing, retention, external transfer and owner separately for:

1. agent identity and conversation state
2. long-term memory and files
3. embeddings, vector stores and retrieval indexes
4. workflow/checkpoint state
5. model inference
6. tools, MCP servers and external SaaS/API calls
7. telemetry, traces, evaluations and audit logs
8. human-approval and operations channels

### Minimum Residency Matrix
For each layer define:
- data classification
- storage location
- processing location
- retention/deletion rule
- encryption/secret ownership
- external subprocessors or services
- cross-region/cross-boundary transfer conditions
- mission(s) allowed to use it
- accountable owner

**Rule:** no layer automatically inherits another layer's region or retention assumptions.

## Quality Readiness
Assess completeness, duplicates, contradictory records, stale content, missing ownership, weak naming, unstructured documents and unsupported legacy sources.

## Validation
Residency and data-boundary claims should be tested through representative missions, tool calls, workflow recovery, telemetry inspection and deletion tests—not only documented in diagrams.

## AI Principle
More data is not automatically better. The objective is **approved, relevant, current and governed context**.

# 中文

数据就绪必须回答：权威来源是谁、谁负责、是否最新、能否用于读取/推理/草稿/行动、哪些敏感、保留多久、哪些必须按团队/客户/区域/环境隔离。

每个数据源都应定义：负责人、用途、访问方式、读写模式、角色范围、Mission 范围、环境、时效、审计和退出/删除流程。

## 持续型 Agent 的数据驻留地图

不要把“Region”当成所有数据自动继承的单一设置。以下各层必须分别记录 Storage、Processing、Retention、External Transfer 与 Owner：

1. Agent Identity / Conversation State
2. Long-term Memory / Files
3. Embedding / Vector Store / Retrieval Index
4. Workflow / Checkpoint State
5. Model Inference
6. Tools / MCP / External SaaS & API
7. Telemetry / Trace / Evaluation / Audit
8. Human Approval / Operations Channel

每一层至少定义：数据分类、存储位置、处理位置、保留/删除、加密和密钥所有权、外部服务/子处理者、跨区域条件、允许使用它的 Mission 和责任人。

**规则：任何一层都不能自动继承另一层的 Region 或 Retention 假设。**

重点检查缺失、重复、冲突、过期、无负责人、命名混乱、非结构化文档和老旧系统。

数据驻留与边界不只写在架构图里，还应该通过代表性 Mission、Tool Call、Workflow Recovery、Telemetry Inspection 和删除测试进行验证。

KING AI SEA 的原则不是“接入越多数据越好”，而是**授权、相关、及时、受治理的上下文越好**。
