# MCP 2026-07-28: Why Stateless, Routable and Durable Tool Infrastructure Matters for AI Agents

**KING AI Intelligence Brief**  
**Published:** August 12, 2026  
**Topics:** Model Context Protocol · MCP · AI Agents · Agent Infrastructure · Tool Use · Enterprise AI · Security · Long-Running Tasks

> **Concise answer:** The July 28, 2026 MCP specification is important because it moves the protocol toward ordinary scalable web infrastructure: stateless self-contained requests, header-based routing, cacheable discovery results, stronger authorization rules, and modular extensions for long-running work and richer interaction. For production AI agents, this reduces transport-level session complexity while making governance, scaling and durable workflows easier to design explicitly.

---

# English

## Executive Summary

The Model Context Protocol (MCP) released a major specification update on July 28, 2026. The most consequential change is a **stateless protocol core**: MCP no longer requires the previous initialize/initialized handshake or protocol-level session identifier for normal request processing. Each request can carry the information needed to be processed independently, which makes MCP servers easier to place behind conventional load balancers, gateways, rate limiters and web application firewalls.

The release also introduces or formalizes several production-oriented capabilities: **Multi Round-Trip Requests (MRTR)** for mid-call user input and approval patterns, **header-based routing**, **cache hints for list results**, authorization hardening, a formal extension framework, the **Tasks extension** for asynchronous long-running work, and a formal deprecation policy.

The deeper significance is architectural. Agent systems increasingly need two things at the same time:

1. simple, horizontally scalable protocol infrastructure; and
2. explicit state, durable task handles, approval boundaries and observability at the application/workflow layer.

The new MCP design separates those concerns more cleanly.

## What Changed in MCP 2026-07-28?

### 1. The protocol core becomes stateless

The official MCP release notes state that the `initialize` / `initialized` exchange and the `Mcp-Session-Id` header are retired in the new specification. Requests are self-contained and carry protocol version, client identity and capabilities in request metadata.

A client can still call `server/discover` when it wants capability information in advance, but discovery is optional rather than a mandatory session-establishment step.

**Why this matters:** a request can be handled by any compatible server instance. Infrastructure no longer needs protocol-level sticky sessions simply to preserve an MCP transport session.

That aligns MCP more closely with the scaling characteristics of ordinary HTTP services.

### 2. Stateless transport does not mean stateless agents

This distinction is critical.

The MCP maintainers explicitly note that removing hidden transport sessions does **not** require the application itself to forget state. If an operation needs continuity across calls, an application can return an explicit state or task handle and pass that handle through subsequent requests.

This is an important production design principle:

```text
Protocol transport state ≠ Agent/application state
```

A scalable protocol can remain stateless while the agent, mission, user context or durable workflow remains stateful in an explicit storage and coordination layer.

For long-lived intelligent systems, this separation is healthier than hiding business or agent state inside a network transport session.

### 3. Multi Round-Trip Requests support approval and missing-input flows

Earlier MCP designs included server-to-client requests that could depend on an open bidirectional connection. The new specification introduces **Multi Round-Trip Requests (MRTR)** for cases where a tool needs additional information during execution.

For example, a tool might need:

- a missing parameter;
- confirmation before spending money;
- approval before creating or deleting a resource;
- clarification before continuing an irreversible operation.

Instead of requiring a permanently open stream, a server can return an `input_required` result and the client can retry the original operation with the requested responses attached.

For enterprise agents, the important idea is not the wire format itself. It is that **human approval can remain a first-class step without forcing the transport layer to stay stateful**.

### 4. Gateways can route and govern MCP traffic more directly

The new Streamable HTTP rules include `Mcp-Method` and `Mcp-Name` headers.

That means infrastructure such as gateways, WAFs, policy engines and rate limiters can inspect the requested MCP operation without parsing every JSON body.

This can improve operational control around questions such as:

- Which tools may this client call?
- Which tool calls require stronger authentication?
- Which methods should be rate-limited?
- Which operations should receive additional logging or approval?
- Which workloads should be routed to specialized backends?

This does not automatically solve authorization or policy design, but it gives infrastructure teams a cleaner point at which to implement those controls.

### 5. Tool and resource discovery can be cached

Responses such as `tools/list`, `prompts/list`, `resources/list` and `resources/read` can now include cache hints and deterministic ordering.

For large agent ecosystems, repeated discovery can become expensive and can also disturb upstream prompt caching when tool catalogs change ordering unnecessarily.

Cache-aware catalogs help reduce redundant fetches and make tool/context discovery more predictable.

### 6. Authorization is being hardened

The July specification includes multiple authorization changes. Official release notes highlight issuer validation based on RFC 9207, binding credentials to the authorization server that issued them, and a migration direction away from Dynamic Client Registration toward Client ID Metadata Documents.

The broader lesson is that production agent interoperability cannot treat authorization as an afterthought.

A protocol that gives models access to tools, data and potentially consequential operations must make identity, consent and authorization explicit.

The MCP specification itself continues to emphasize user consent, data privacy, tool safety and application-level access controls.

### 7. Long-running work moves into an explicit extension

The **Tasks** capability is now an MCP extension rather than experimental core protocol behavior.

The current specification describes Tasks as a mechanism for asynchronous long-running operations with durable handles, polling and mid-flight input.

This is strategically important because not every agent action should behave like a synchronous function call.

Some missions may involve:

- background research;
- data processing;
- infrastructure deployment;
- multi-step business workflows;
- human review delays;
- external service waits;
- recovery and continuation after interruption.

An explicit long-running-task abstraction makes those execution patterns easier to model without overloading the synchronous request path.

## Why This Matters for Production AI Agents

The central shift is from thinking about MCP as merely a **tool connector** to treating it as one layer in a broader production agent architecture.

A mature agent platform increasingly separates:

```text
Agent identity / continuity
        ↓
Mission and workflow state
        ↓
Durable task execution
        ↓
Tool / data interoperability (MCP)
        ↓
Gateway / authorization / policy
        ↓
External systems
```

MCP standardizes an important part of the lower integration layer. It does not replace agent memory, mission orchestration, enterprise policy, workflow durability or evaluation.

That separation is healthy.

## MCP and A2A Are Complementary, Not Interchangeable

The current A2A specification defines a protocol for communication and collaboration between independent agent systems. Its goals include agent discovery, capability negotiation, collaborative task management and secure information exchange without requiring agents to expose their internal memory or tools.

MCP, by contrast, primarily standardizes how applications expose **tools, resources, prompts and contextual capabilities** to AI systems.

A practical mental model is:

```text
MCP → agent-to-tool / agent-to-context interoperability
A2A → agent-to-agent interoperability
```

Real systems may use both.

An enterprise agent could use MCP to access CRM, databases or operational tools, while using A2A to delegate a specialized task to an external agent maintained by another team or vendor.

This is one reason the agent ecosystem is beginning to look less like one universal protocol and more like a **protocol stack**.

## Enterprise Architecture Implications

### Horizontal scale becomes easier

Stateless protocol requests fit ordinary HTTP scaling patterns better than hidden transport sessions. Teams can more naturally use load balancing, serverless infrastructure, autoscaling and gateway policy.

### State must become explicit

Removing protocol sessions forces architects to decide where continuity actually belongs:

- agent identity store;
- mission database;
- durable workflow engine;
- task handle store;
- memory subsystem;
- human approval queue.

That is usually a better design than relying on connection state accidentally becoming business state.

### Governance can move closer to infrastructure

Header-visible operation metadata, stronger authorization guidance and explicit approval flows make it easier to place policy and audit controls around tool execution.

### Long-running tasks should be modeled differently from fast tool calls

A five-second lookup and a two-hour research workflow should not have identical execution semantics.

The emergence of task extensions, durable workflows and resumable execution across the agent ecosystem reinforces this point.

## KING AI SEA Perspective

**Important product-status clarification:** this article analyzes an external open standard. It does not claim that every MCP 2026-07-28 capability is already implemented or enabled in KING AI SEA.

For KING AI SEA's public architecture, the release reinforces several principles already present in the technology radar:

1. **Keep the intelligent-lifeform core separate from protocol transport.** KING AI SEA's identity, continuity and controlled evolution should not depend on one transport protocol.
2. **Treat MCP as an interoperability layer, not the intelligence itself.** Tools and context are capabilities connected to the lifeform; they are not the lifeform's identity.
3. **Make durable state explicit.** Long-running missions need persistent mission state, checkpoints or durable task handles independent of transient HTTP connections.
4. **Keep approvals and policy boundaries first-class.** Agent actions that affect money, production infrastructure, customer data or other consequential resources should support explicit governance.
5. **Remain protocol-plural.** MCP, A2A and future standards can occupy different layers of the ecosystem. KING AI SEA should preserve interoperability without binding its architecture to a single vendor or protocol.
6. **Evaluate interoperability as an operational capability.** A protocol integration is not complete merely because a tool call succeeds; reliability, permissions, observability, recovery and human handoff also matter.

These are public architecture principles, not disclosure of private KING AI SEA orchestration or security internals.

## What Teams Should Review Now

Organizations already using MCP should review whether their implementation depends on behaviors deprecated or changed by the July specification, particularly:

- protocol-level session identifiers;
- initialize/initialized assumptions;
- legacy HTTP+SSE transport;
- deprecated Roots, Sampling or Logging behavior;
- Dynamic Client Registration assumptions;
- gateway rules that currently parse JSON bodies instead of using operation headers;
- tool catalogs that do not take advantage of deterministic ordering or caching;
- long-running operations modeled as ordinary synchronous tool calls.

Migration should follow the official specification and SDK migration guidance rather than assumptions derived from older MCP versions.

## Primary Sources

- Model Context Protocol — 2026-07-28 release: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Model Context Protocol — 2026-07-28 specification: https://modelcontextprotocol.io/specification/2026-07-28
- A2A Protocol — current specification: https://a2a-protocol.org/latest/specification
- Google Developers — Developer's Guide to AI Agent Protocols: https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/

## Related KING AI SEA Knowledge

- [Global Agent Technology Radar 2026](../docs/GLOBAL-AGENT-TECHNOLOGY-RADAR-2026.md)
- [Interoperability](../docs/INTEROPERABILITY.md)
- [Integration Design Standard](../docs/INTEGRATION-DESIGN-STANDARD.md)
- [Governance, Observability & Evaluation](../docs/GOVERNANCE-OBSERVABILITY.md)
- [Trust Center](../docs/TRUST-CENTER.md)
- [Agentic Automation & Workflows](../docs/AUTOMATION-WORKFLOWS.md)

**Update status:** Current as of August 12, 2026. Protocol behavior should be rechecked against the official MCP specification before production migration.

---

# 中文

## 简明答案

2026 年 7 月 28 日发布的新一版 MCP 规范之所以重要，是因为它把 MCP 进一步推向了更接近普通 Web 基础设施的形态：**无状态、自包含请求、基于 Header 的路由、可缓存的能力发现、更严格的授权规范，以及用于长任务和复杂交互的扩展体系**。

对于生产级 AI Agent 来说，这意味着可以减少协议传输层的 Session 复杂度，同时把真正需要长期保存的状态、任务、审批和治理放到更明确的应用与 Workflow 层。

## 核心变化是什么？

### 1. MCP 核心协议转向无状态

官方 2026-07-28 Release 说明，新规范取消了原先正常请求处理所依赖的 `initialize / initialized` 握手和 `Mcp-Session-Id` 协议 Session。

每一个请求都可以携带协议版本、客户端身份和能力信息，自包含地被处理。

如果客户端希望提前了解服务器能力，可以调用新的 `server/discover`，但它不再是所有请求之前必须建立 Session 的步骤。

这意味着一个请求可以更自然地落到负载均衡器后面的任意兼容实例。

### 2. “协议无状态”不等于“Agent 没有状态”

这是这次升级里最值得理解的一点。

MCP 协议层不再保存隐藏 Session，并不代表应用、智能体或 Mission 必须忘记上下文。

如果某项任务需要跨调用保持状态，可以由应用显式生成 state handle、task handle 或业务标识，并在后续请求中继续携带。

因此应该区分：

```text
协议传输状态 ≠ Agent / 应用状态
```

对于长期运行的智慧生命体系统来说，真正重要的身份、Mission、Memory、审批、任务进度，本来就不应该依赖一条临时网络连接是否还存在。

### 3. MRTR 让中途确认和补充信息可以在无状态协议中继续存在

新规范引入 Multi Round-Trip Requests（MRTR），用于工具执行过程中需要用户补充信息或进行确认的情况。

例如：

- 缺少参数；
- 支付前确认；
- 创建昂贵资源前审批；
- 删除数据前再次确认；
- 执行不可逆操作前要求人工授权。

服务器可以返回 `input_required`，客户端得到所需信息后，再带着回答重新提交原请求。

重要的不是具体字段，而是：**Human Approval 不再需要依赖长期保持的双向连接。**

### 4. Gateway、WAF 和 Policy Engine 更容易识别 MCP 操作

新 Streamable HTTP 请求会携带 `Mcp-Method` 和 `Mcp-Name` Header。

这样 Gateway、WAF、限流系统、审计系统和策略引擎就可以更容易回答：

- 某个客户端允许调用哪些 Tool？
- 哪些操作必须使用更强身份验证？
- 哪个 Tool 需要独立限流？
- 哪些操作必须进入人工审批？
- 哪些请求要进入更高等级审计？

它不能自动替企业设计治理制度，但提供了更干净的基础设施控制面。

### 5. Tool / Resource Catalog 可以缓存

`tools/list`、`prompts/list`、`resources/list` 和部分资源读取结果现在可以带缓存提示并保持确定性排序。

这对大规模 Agent 平台很重要，因为工具目录如果频繁重复请求，或者每次排列顺序不同，不仅浪费资源，也可能影响上游 Prompt Cache 的稳定性。

### 6. Authorization 进一步加强

7 月规范增加了多项 Authorization Hardening，包括基于 RFC 9207 的 issuer 校验、Credential 与签发 Authorization Server 绑定，以及从 Dynamic Client Registration 向 Client ID Metadata Documents 演进。

这说明一个越来越明确的行业事实：

> 当 Agent 可以调用真实工具、读取真实数据并执行真实操作时，Authorization 不是附加功能，而是核心基础设施。

MCP 官方规范本身也持续强调 User Consent、Data Privacy、Tool Safety 和应用层 Access Control。

### 7. 长任务被放到明确的 Tasks 扩展中

Tasks 现在成为 MCP Extension，用于异步、长期运行的操作，包括 Durable Handle、Polling 和任务执行途中补充输入。

这很重要，因为生产级智能体并不是所有事情都能在一次短请求里完成。

例如：

- 长时间研究；
- 数据批处理；
- 软件部署；
- 多步骤企业流程；
- 等待人工审核；
- 等待第三方系统；
- 故障后的恢复继续。

这些任务本来就应该和“几秒钟完成的 Tool Call”使用不同执行模型。

## 对生产级 AI Agent 意味着什么？

MCP 正从“工具连接协议”进一步成熟为现代 Agent 基础设施中的一个重要互联层。

一个更健康的生产架构通常会逐渐分成：

```text
Agent 身份 / 连续性
        ↓
Mission / Workflow 状态
        ↓
Durable Task Execution
        ↓
Tool / Data Interoperability（MCP）
        ↓
Gateway / Authorization / Policy
        ↓
外部业务系统
```

MCP 负责其中非常重要的一层，但它并不会替代 Agent Memory、Mission Orchestration、企业权限、Workflow Durability 或 Evaluation。

这种职责分离反而更加成熟。

## MCP 和 A2A 是互补关系，不是同一个东西

当前 A2A 规范解决的是**独立智能体系统之间的通信、发现、协作与任务管理**。

MCP 更主要解决的是 AI 系统如何标准化访问：

- Tools；
- Resources；
- Prompts；
- Context；
- External Capabilities。

可以用一个简单模型理解：

```text
MCP → Agent 与 Tool / Context 的互联
A2A → Agent 与 Agent 的互联
```

真实企业架构完全可能同时使用两者。

例如一个企业 Agent 通过 MCP 使用 CRM、数据库和内部工具，再通过 A2A 把一个专业任务委托给另一个独立 Agent。

未来 Agent 世界很可能不是“一种协议统治所有层”，而是逐渐形成**多层协议栈**。

## 企业架构层面的几个重要影响

### 横向扩展会更自然

Stateless Request 更适合普通 HTTP Load Balancer、Serverless、Autoscaling 和 Gateway 基础设施。

### 状态必须被显式设计

架构师需要明确决定长期状态到底放在哪里：

- Identity Store；
- Mission Database；
- Durable Workflow Engine；
- Task Handle Store；
- Memory System；
- Human Approval Queue。

这通常比把状态隐藏在 Transport Session 里更可靠。

### 治理更容易进入基础设施层

Header 可见的 Tool/Method 信息、强化的 Authorization 以及明确 Approval Flow，让 Policy、Audit、Rate Limit 和 Risk Control 更容易围绕真实 Tool Execution 建立。

### 长任务应该和短 Tool Call 使用不同模型

5 秒钟的数据查询和 2 小时的研究 Mission，不应该有完全相同的执行语义。

MCP Tasks、Durable Workflow、Checkpoint / Resume 等技术共同强化了这一趋势。

## KING AI SEA 视角

**产品状态说明：本文分析的是外部开放协议，不代表 KING AI SEA 已经实现或启用了 MCP 2026-07-28 的所有能力。**

这次升级进一步支持 KING AI SEA 公开架构中的几个原则：

1. **智慧生命体核心不能依赖某一种协议。** 身份、连续性和受控进化应该位于协议层之上。
2. **MCP 是互联层，不是智慧本身。** Tool 和 Context 是生命体可连接的外部能力，而不是生命体身份。
3. **Durable State 必须显式存在。** 长期 Mission 应通过持久任务状态、Checkpoint 或 Durable Handle 延续，而不是依赖临时 HTTP Connection。
4. **审批与策略边界应该是一等能力。** 涉及资金、生产系统、客户数据或不可逆操作时，应存在明确治理路径。
5. **保持 Protocol-Plural。** MCP、A2A 以及未来其他开放标准可以各自承担不同层次的互联职责。
6. **把互联质量当成运营能力评估。** Tool 能调用成功只是最低标准，还需要关注可靠性、权限、可观测、恢复和 Human Handoff。

这些属于公开架构原则，不涉及 KING AI SEA 私有 Orchestration、Memory 内核或安全实现细节。

## 已使用 MCP 的团队现在应该检查什么？

如果已有 MCP 部署，应重点核对是否依赖：

- 旧协议 Session ID；
- `initialize / initialized` 固定流程；
- Legacy HTTP+SSE Transport；
- 已弃用或进入弃用阶段的 Roots / Sampling / Logging；
- Dynamic Client Registration；
- 必须解析 JSON Body 才能进行 Gateway Policy 的规则；
- 无缓存策略的 Tool / Resource Catalog；
- 把长期任务当普通同步 Tool Call 的实现。

具体迁移应以官方最新规范和对应 SDK Migration Guide 为准。

## 一手来源

- Model Context Protocol — 2026-07-28 Release: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- Model Context Protocol — 2026-07-28 Specification: https://modelcontextprotocol.io/specification/2026-07-28
- A2A Protocol — Current Specification: https://a2a-protocol.org/latest/specification
- Google Developers — Developer's Guide to AI Agent Protocols: https://developers.googleblog.com/en/developers-guide-to-ai-agent-protocols/

## KING AI SEA 相关知识

- [2026 全球 Agent 技术雷达](../docs/GLOBAL-AGENT-TECHNOLOGY-RADAR-2026.md)
- [Interoperability](../docs/INTEROPERABILITY.md)
- [Integration Design Standard](../docs/INTEGRATION-DESIGN-STANDARD.md)
- [Governance, Observability & Evaluation](../docs/GOVERNANCE-OBSERVABILITY.md)
- [Trust Center](../docs/TRUST-CENTER.md)
- [Agentic Automation & Workflows](../docs/AUTOMATION-WORKFLOWS.md)

**更新状态：** 截至 2026 年 8 月 12 日。生产迁移前应重新核对 MCP 官方最新规范。