# KINGAI Repository Agent Contract

This is an active KINGAI repository. Before any deployment, GPT, Codex, OpenClaw or other automation MUST read the canonical platform policy in `kingaiwork/KINGAIASE`:

1. `AGENTS.md`
2. `config/repository-registry.json`
3. `config/repository-operating-model.json`
4. `config/infrastructure-policy.json`
5. `config/free-resource-vps-plan.json`
6. `config/runtime-resource-state.json`
7. `docs/INFRASTRUCTURE-FREE-FIRST.md`

Repository-local code remains authoritative for this product/surface; cross-product infrastructure policy remains authoritative in `KINGAIASE`.

Mandatory deployment rules: free/unlimited static first; hard-capped free second; guarded metered-free resources only below policy thresholds; 60% warning/optimization, 70% eligible background migration to registered VPS, 80% VPS-first for eligible dynamic work, 90% edge-preservation mode. Paid overage/upgrade/model fallback is forbidden without explicit owner authorization.

VPS application traffic must enter only through Cloudflare Tunnel. Direct public VPS application/database/cache/OpenClaw/admin ports are forbidden. The only permitted direct public ingress profile is SSH TCP/58888. Legacy/frozen repositories must never be used as deployment authority.

A commit is not deployment evidence: build/test, deploy, smoke the real endpoint/runtime, and record evidence.
