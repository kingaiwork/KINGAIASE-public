# KINGAI System Synchronization

Architecture baseline: `2026-08-23 / current-v2`

This repository participates in the current KINGAI system defined by `kingaiwork/KINGAIASE`.

- GitHub is source/policy/automation authority.
- Cloudflare is the public edge for DNS, TLS, CDN/cache, WAF/security, static delivery, Workers and Tunnel ingress.
- Cloudflare D1 is the platform single-writer authority for central identity and bounded critical transactions.
- Registered VPS capacity carries PostgreSQL 17 + pgvector, private APIs, agents, heavy jobs and encrypted backups.
- VPS application/database/admin ports are never directly public; application ingress is Cloudflare Tunnel only.
- Zero-cost mode forbids automatic paid plans, overage, paid AI or resource purchase.
- Database failover is fenced single-writer only.

This public repository must not contain private provider-access metadata, Secret locations or credential values. Authorized operators use the private control-plane `AGENTS.md` for takeover procedures.

A commit is not deployment evidence; require real endpoint/runtime readback.
