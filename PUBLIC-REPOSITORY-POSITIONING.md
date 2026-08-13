# KING AI Public Repository Positioning

This repository is the **public knowledge, discovery, technology, growth and partnership hub for KING AI**.

It is **not** the production website source repository and it is **not** the production runtime repository.

## What this repository is for

- Public product positioning
- Technical thought leadership
- Public architecture
- Research and intelligence publishing
- SEO and GEO
- AI-search discoverability
- Official project relationships
- Developer and enterprise education
- Trust and governance material
- Strategic partnerships
- Business development
- Investor-facing public information
- Media and ecosystem visibility

## What this repository is not for

This repository must not contain or mirror:

- Production website source code
- Private application source code
- Production database schemas that expose sensitive internals
- Credentials or secrets
- Private keys
- Stripe secrets
- Cloudflare production tokens
- Customer information
- Private endpoints
- Internal security controls that should remain private
- Production topology
- Root-policy implementation details

## Production boundary

The production website and runtime live in the private repository:

`kingaiwork/KINGAIASE`

Repository responsibilities:

```text
kingaiwork/KINGAIASE      PRIVATE
├── pages  → static website source for Cloudflare Pages
├── main   → Cloudflare Worker / API runtime
└── ops    → OpenClaw / Codex / VPS / AutoOps operations

kingaiwork/KINGAIASE-public      PUBLIC
└── product / technology / research / SEO / GEO / trust / partnerships / investor information
```

## Official public role

This public repository should help search engines, AI answer engines, developers, enterprises, researchers, partners and investors understand:

- What KING AI is
- What problems it is designed to solve
- How its public architecture is structured
- How KING AI approaches memory, intelligence, agents, governance and controlled execution
- Which official KING AI projects exist
- How the project ecosystem relates to the main KING AI platform
- How to evaluate KING AI for enterprise or strategic collaboration
- How to contact the KING AI team

## Official sources

- Website: https://www.kingai.work
- Official GitHub: https://github.com/kingaiwork
- Business & Partnership: vip@kingai.work

## Publication principle

**Private source, public knowledge.**

KING AI keeps production systems and sensitive implementation private while publishing enough verified product, technology, research and governance information for the global market to evaluate the platform responsibly.
