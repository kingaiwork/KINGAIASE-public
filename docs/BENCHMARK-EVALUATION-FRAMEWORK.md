# 📊 KING AI SEA — Benchmark & Evaluation Framework

> Measure outcomes, not marketing claims.

---

# English

## 1. Evaluation Dimensions

### Understanding
- intent recognition
- constraint recognition
- missing-information detection
- correct clarification / escalation behavior

### Knowledge
- source relevance
- groundedness
- freshness where required
- uncertainty handling

### Planning
- step quality
- dependency handling
- realistic sequencing
- approval checkpoints

### Execution
- task completion
- correct tool usage
- permission compliance
- idempotency / duplicate-action avoidance where relevant

### Collaboration
- role handoff
- human handoff
- context transfer
- cross-functional coordination

### Trust
- refusal of unauthorized action
- approval enforcement
- audit completeness
- override responsiveness

### Reliability
- recovery from tool errors
- resilience to partial data
- long-running mission continuity
- retry behavior

### Business Value
- cycle time
- throughput
- rework
- conversion / retention influence where applicable
- user satisfaction
- cost per successful outcome

## 2. Test Sets

Use representative test sets:

- expected routine tasks
- difficult edge cases
- ambiguous requests
- adversarial / out-of-scope requests
- missing-data cases
- permission-boundary cases
- integration-failure cases
- long-running workflows

## 3. Scorecard

A recommended scorecard uses five ratings:

**Critical Fail / Needs Work / Acceptable / Strong / Excellent**

Do not publish benchmark percentages unless tests, dataset, date, environment and methodology can be disclosed accurately.

## 4. Release Gates

A role or mission moves toward production only when:

- critical failures are resolved
- permission tests pass
- human takeover works
- expected task quality is acceptable
- observability is sufficient
- business owner accepts residual limitations

## 5. Continuous Evaluation

Production evaluation should monitor drift, new failure patterns, changing data sources, cost changes and business KPI changes. Findings may feed controlled improvement proposals.

---

# 中文

Benchmark 和 Evaluation 必须衡量真实结果，而不是宣传口号。

核心维度包括：

- **理解** — 意图、约束、缺失信息、正确升级。
- **知识** — 来源相关性、可追溯、时效和不确定性处理。
- **规划** — 步骤、依赖、顺序、审批点。
- **执行** — 成功完成、工具使用、权限遵守、避免重复动作。
- **协作** — AI 角色交接、人类交接、上下文传递、跨部门协调。
- **信任** — 未授权动作拒绝、审批、审计、人类接管。
- **可靠性** — 工具错误、部分数据、长任务、恢复。
- **商业价值** — 周期、吞吐、返工、转化/留存影响、满意度和单次成功成本。

测试集必须包含正常、边缘、歧义、越界、缺数据、权限、故障和长任务。

禁止发布无法说明测试集、日期、环境和方法的 Benchmark 百分比。