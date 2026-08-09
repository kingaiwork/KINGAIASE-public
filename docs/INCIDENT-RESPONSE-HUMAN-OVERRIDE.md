# 🚨 KING AI SEA — Incident Response & Human Override

# English

## Incident Classes
- quality failure
- integration failure
- permission violation attempt
- unexpected action
- data-quality issue
- security signal
- excessive cost/looping
- service outage
- customer-impacting error

## Immediate Controls
1. pause affected mission
2. disable affected tool/role if required
3. preserve evidence
4. route to human owner
5. communicate impact
6. recover/rollback where applicable
7. validate before re-enable

## Human Override
Production deployments should provide a practical way for authorized humans to stop, pause, narrow or take over AI-driven work.

## Post-Incident
Record timeline, trigger, impact, affected permissions, recovery, root cause category, controls changed, evaluation test added and whether controlled evolution proposals are appropriate.

# 中文
事件类型包括质量失败、集成故障、权限越界尝试、异常动作、数据问题、安全信号、成本/循环失控、服务中断和客户影响错误。

立即控制：暂停 Mission → 必要时禁用工具/岗位 → 保存证据 → 人工负责人接管 → 沟通影响 → 恢复/回滚 → 验证后重启。

生产环境必须允许授权人类随时停止、暂停、缩小范围或接管 AI 工作。

事后记录时间线、触发原因、影响、权限、恢复、根因类别、控制变化、增加的测试以及是否需要受控进化提案。