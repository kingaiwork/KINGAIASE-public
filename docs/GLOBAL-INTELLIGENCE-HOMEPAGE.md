# KING AI Global Intelligence Homepage

**Official website:** https://www.kingai.work  
**Official GitHub:** https://github.com/kingaiwork  
**Business & Partnership:** vip@kingai.work

## Purpose

The KING AI homepage is designed as a public global-intelligence entry point rather than a conventional AI marketing page. It combines clear product storytelling with a compact view of public security signals, country-level context, enterprise and personal digital-safety trends, agent-technology research, official KING AI projects, project activity, verification status and system availability.

The homepage itself remains a static Cloudflare Pages site. Dynamic data is supplied separately through the public KING AI API and cached Cloudflare data services.

## Data Modes

Every public data block must expose its operating mode.

### LIVE DATA

Used only when the system has a current, verified public snapshot.

### VERIFIED CACHE

Used when current upstream sources are temporarily unavailable but a previously verified snapshot remains within the permitted cache window.

### DEMO DATA

Used when no verified live or cached snapshot is available, including before the Cloudflare data plane has been fully provisioned.

Demo values are presentation-only. They are not statements about any real country, enterprise, person, vulnerability, campaign or incident. Demo data is never eligible for automated action and must never be written into real intelligence history.

## Public Homepage Modules

- Global overview
- Global security signals
- Country intelligence overview
- Enterprise security trends
- Personal digital-safety trends
- Agent technology radar
- Official KING AI projects
- Public project activity
- Verified-intelligence pipeline
- Today's intelligence brief
- KING AI public system status

## Official KING AI Projects

The homepage may surface public project metadata from the official `kingaiwork` GitHub account.

Current examples include:

- **KING AI SEA / KINGAIASE-public** — public architecture, knowledge, intelligence, enterprise and personal-intelligence material.
- **KINGAIBOT** — a separate execution-oriented agent runtime intended to become a controlled terminal execution layer for KING AI over time.
- **KINGAI OS** — a long-term AI-native operating-system project for server, desktop and edge environments.
- **KING AI Online Tools** — a public utility platform with 130+ browser tools.

Private repositories are excluded from public synchronization by default.

## Public Data Architecture

```text
GitHub / Public Sources / Research
              ↓
      Verification & Normalization
              ↓
      Cloudflare Data Plane
        D1 · KV · R2 · Queues
              ↓
        Public API Snapshot
              ↓
       Cloudflare Pages
              ↓
       www.kingai.work
```

The public static site should not query GitHub or large source networks directly from each visitor's browser. Expensive collection, normalization and enrichment happen outside the request path. The homepage consumes a compact cached public snapshot.

## Safety and Trust Boundary

- No private repository data is automatically public.
- No production secrets or credentials are present in the Pages site.
- Demo data is explicitly labeled.
- Low-confidence information may be held back rather than displayed as fact.
- Public data is not an instruction to agents or an authorization for automated action.
- Intelligence generation and production authority remain separate concerns.

## Long-Term Goal

KING AI aims to make complex changes easier to understand without turning uncertainty into false certainty. The homepage is designed to be useful even when the intelligent back end is unavailable: the site continues to load, the most recent verified cache may remain visible, and demo content provides an honest presentation fallback when no trustworthy live snapshot exists.
