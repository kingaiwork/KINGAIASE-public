# 🌍 KING AI SEA — Global Deployment Guide

# English

## Deployment Patterns
- Managed Cloud
- Dedicated VPS
- Private Server
- Private Cloud / VPC
- Hybrid
- Customer-Controlled Environment
- Edge/local components where project scope supports them

## Design Dimensions
1. data residency
2. latency
3. integration locality
4. network exposure
5. identity provider
6. secrets ownership
7. observability ownership
8. backup/recovery
9. regional support
10. regulatory/customer policy constraints

## Environment Model
Recommended separation: Development → Test → Staging → Production, adjusted to project size.

## Globalization
Support architecture should plan for language, timezone, locale, regional policy, data boundaries and human escalation coverage.

## Public Rule
Do not claim a region, certification or compliance status until actually supported and verified.

# 中文
部署形态：Managed Cloud、Dedicated VPS、Private Server、Private Cloud/VPC、Hybrid、客户控制环境，以及项目允许时的本地/边缘组件。

设计必须考虑数据驻留、延迟、集成位置、网络暴露、身份、密钥所有权、可观测、备份恢复、区域支持和客户/监管政策。

建议区分开发、测试、预生产和生产环境。

全球化还要考虑语言、时区、Locale、区域规则、数据边界和人工升级覆盖。任何地区、认证或合规能力只有实际验证后才能公开声称。