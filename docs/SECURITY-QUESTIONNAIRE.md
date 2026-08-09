# 🛡️ KING AI SEA — Enterprise Security Questionnaire

> Public due-diligence questionnaire. It is designed to evaluate trust and control without exposing sensitive security implementation.

---

# English

## A. Identity & Access

1. How are users and service identities authenticated?
2. Can roles and permissions be scoped by team, environment and mission?
3. Is least privilege supported?
4. Can privileged actions require explicit approval?
5. Can access be revoked quickly?

## B. Data & Knowledge

6. What data categories may be connected?
7. Can data sources be isolated by tenant / environment?
8. Can customers control what knowledge is accessible?
9. Are retention and deletion policies configurable by deployment scope?
10. Can sensitive sources be excluded from AI missions?

## C. Actions & Approvals

11. Are read, draft, recommend and execute permissions separable?
12. Can high-risk actions require human approval?
13. Is there an escalation path when confidence or policy conditions require review?
14. Can actions be disabled by tool, role, workflow or environment?
15. Is human override supported?

## D. Audit & Observability

16. Are mission and action histories observable?
17. Can administrators review approvals and failures?
18. Can execution state be monitored?
19. Can evaluation results be recorded?
20. Can incidents be traced to role, mission and approved integration context?

## E. Deployment & Isolation

21. Which deployment models are supported by project scope?
22. Can customer-controlled/private environments be used?
23. Can development, staging and production be separated?
24. Can integration credentials be isolated by environment?
25. Can network exposure be minimized?

## F. Secrets & Credentials

26. Are credentials excluded from public code and documentation?
27. Are secrets scoped to the minimum required integration?
28. Can credentials be rotated and revoked?
29. Can privileged integrations require additional controls?
30. Are sensitive credentials prevented from appearing in public logs or documentation?

## G. Agent / AI Risk Controls

31. Are AI roles assigned explicit missions and scopes?
32. Can tool access be restricted per role?
33. Can risky autonomous loops be bounded by checkpoints?
34. Are unsupported actions rejected or escalated?
35. Are model/tool failures treated separately from business authorization?

## H. Incident & Continuity

36. Is there a process to pause affected automation?
37. Can a human take over an active mission?
38. Are recovery and rollback procedures defined by deployment?
39. Are high-impact incidents reviewed before re-enabling automation?
40. Can recurring issues feed evaluation and controlled improvement?

## I. Governance

41. Who owns AI policy decisions?
42. Who approves high-risk integrations?
43. How are changes to mission scope controlled?
44. How are new roles and permissions reviewed?
45. What evidence is retained for enterprise governance reviews?

## J. Public Technology Boundary

Security review should verify outcomes, controls and evidence. It should **not** require publishing exploitable internal detection logic, privileged policy-engine implementation, secret topology or credentials.

---

# 中文

本安全问卷覆盖十类企业尽调问题：

1. **身份与访问** — 登录、角色、最小权限、特权审批、撤销。
2. **数据与知识** — 数据来源、隔离、访问范围、保留/删除、敏感源排除。
3. **行动与审批** — 读/写/建议/执行分离、高风险审批、升级、人类接管。
4. **审计与可观测** — Mission 历史、审批、失败、执行状态、评估与追踪。
5. **部署与隔离** — Cloud/VPS/Private/Hybrid、开发/测试/生产隔离、网络最小暴露。
6. **密钥与凭据** — 不进入公开仓库、最小范围、轮换撤销、高权限加强控制。
7. **AI 风险控制** — 角色 Mission、工具范围、检查点、拒绝/升级、授权与模型故障分离。
8. **事件与连续性** — 暂停自动化、人类接管、恢复、复盘、受控改进。
9. **企业治理** — 谁制定策略、谁批准高风险集成、如何变更权限、保留什么治理证据。
10. **核心技术保护** — 安全审核验证控制和证据，不公开可被利用的检测逻辑、特权策略引擎、敏感拓扑或密钥。