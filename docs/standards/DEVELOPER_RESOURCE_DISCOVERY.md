# Ercan OS — Developer Resource Discovery

Status: active
Date: 2026-09-24

## Purpose

Give Ercan OS high-recall discovery for developer services, APIs, self-hosted alternatives and Agent Skills without mistaking curated lists for current provider truth or approved dependencies.

Execution skill: `.agents/skills/developer-resource-discovery/SKILL.md`.

## Reviewed discovery sources

| Source | Role | Decision | Key boundary |
|---|---|---|---|
| `ripienaar/free-for-dev` | free-tier SaaS/PaaS/IaaS discovery | DISCOVERY_SOURCE | provider pricing/terms must be rechecked; no root LICENSE observed |
| `public-apis/public-apis` | public API discovery | DISCOVERY_SOURCE | API's own docs/terms/auth/quota remain authority; repo MIT |
| `awesome-selfhosted/awesome-selfhosted` | self-hosted software discovery | DISCOVERY_SOURCE | list CC BY-SA 3.0; each project license/ops burden differs |
| `hesreallyhim/awesome-claude-code` | Claude/agent tooling discovery | DISCOVERY_SOURCE_ONLY | CC BY-NC-ND 4.0; do not adapt/copy catalog content |
| `anthropics/skills` | official Anthropic Agent Skills examples/implementation patterns | ADOPT_WHEN_NEEDED / OFFICIAL_REFERENCE | mixed licensing; exact sub-skill terms must be checked |

The canonical Agent Skills format/specification is not replaced by `anthropics/skills`; Ercan OS continues to use the current open Agent Skills specification as format authority.

## Decision model

### Free managed service
Evaluate current free-tier duration, hard/soft quotas, overage behavior, card requirement, production eligibility, data region, privacy, auth, SLA, export/lock-in and upgrade path.

### Public API
Evaluate canonical provider, auth, HTTPS, CORS where relevant, rate limits, data licensing, freshness/quality, commercial-use terms, stability/deprecation, privacy and fallback strategy.

### Self-hosted alternative
Evaluate license, maintenance health, deployment footprint, database/storage, backups, upgrades/migrations, secret management, observability, anti-abuse, outbound email, security advisories, HA/SLA need and total operational cost.

### Agent Skill/tool
Evaluate canonical owner, host compatibility, scripts/install hooks, shell/network access, credentials, prompt/instruction trust, license, maintenance, overlap with existing Ercan OS skill and regression requirements.

## Routing

`request -> developer-resource-discovery -> shortlist -> canonical primary-source verification -> upstream-adoption-audit if material -> task-domain owner -> QA -> decision record`

No new stable routing identity is created. `@UpstreamIntelligence` owns discovery; existing platform/domain owners own production adoption.

## Non-negotiable rules

- Stars are discovery signals, not trust or quality scores.
- "Free" is a volatile provider fact, never a durable promise copied from a catalog.
- A public API list entry does not establish commercial rights or production reliability.
- A self-hosted product is not automatically cheaper once operations/security are counted.
- A curated skill list may point to useful upstreams but never grants them Ercan OS authority.
- Never install a broad skill/tool bundle merely because it is official or popular; select the smallest relevant unit.
- Exact licensing is checked at the candidate/subdirectory level before copying code or instructions.
