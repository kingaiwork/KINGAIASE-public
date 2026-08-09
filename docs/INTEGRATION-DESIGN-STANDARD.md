# 🔌 KING AI SEA — Integration Design Standard

# English

## Integration Card
Every integration should document:
- system name
- owner
- business purpose
- authentication method category
- environment
- allowed operations
- prohibited operations
- accessible data classes
- AI roles allowed
- missions allowed
- approval rules
- rate/cost constraints
- failure behavior
- audit/log expectations
- credential rotation/offboarding

## Permission Modes
- Read-only
- Draft-only
- Limited write
- Approved action
- Privileged restricted

## Failure Design
Define behavior for timeout, partial result, stale data, permission denial, schema change, vendor outage and duplicate action risk.

## Public Boundary
Public docs may name integration categories and high-level capability. Credentials, private endpoints, network topology and privileged implementation remain private.

# 中文
每个集成都应有 Integration Card：系统、负责人、业务用途、认证类别、环境、允许/禁止操作、数据类别、可使用岗位、可使用 Mission、审批、成本/速率、失败行为、审计、凭据轮换和退出。

权限可分：只读、只草稿、有限写入、审批动作、特权受限。

必须设计超时、部分结果、过期数据、权限拒绝、Schema 变化、供应商故障和重复执行风险。