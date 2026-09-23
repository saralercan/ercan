---
name: developer-resource-discovery
description: Discover task-appropriate free-tier developer services, public APIs, self-hosted alternatives and Agent Skills from reviewed catalogs, then verify the actual candidate before recommending or adopting it. Use when the user asks for free/low-cost infrastructure, an API for a feature, a self-hosted replacement, or new agent/skill capabilities.
---

# Developer Resource Discovery

This is a JIT discovery capability owned by `@UpstreamIntelligence`. It expands recall without turning curated lists into trusted dependencies.

## Discovery lanes

- FreeTierServices -> `ripienaar/free-for-dev` as a discovery index.
- PublicAPIs -> `public-apis/public-apis` as a discovery index.
- SelfHostedAlternatives -> `awesome-selfhosted/awesome-selfhosted` + its machine-readable data companion as discovery indexes.
- AgentSkillDiscovery -> `hesreallyhim/awesome-claude-code` as a discovery index only.
- OfficialSkillReference -> `anthropics/skills` as an official Anthropic implementation/example source; the open Agent Skills specification remains the canonical format authority.

## Owner mapping

- Discovery/funnel/dedupe -> `@UpstreamIntelligence`
- Architecture/fit -> task-domain specialist
- Security/license/ops review -> existing security capability + `upstream-adoption-audit`
- Cost/quota/provider constraints -> `@Orchestrator` + task-domain owner
- Final adoption -> project/platform owner + independent QA

## Procedure

1. Define the actual requirement: capability, traffic/usage shape, data sensitivity, hosting preference, region, auth, SLA, budget and lock-in tolerance.
2. Search the smallest relevant discovery lane first.
3. Build a shortlist; do not recommend an entry merely because the catalog lists it.
4. Resolve each shortlisted item to its canonical official site/repository/docs.
5. Re-verify current pricing/free-tier limits, API auth, rate limits, maintenance, license, security posture, privacy/data residency and production terms from current primary sources.
6. Compare managed vs self-hosted operational burden where both are viable.
7. Prefer existing Ercan OS adopted capabilities when they already satisfy the requirement.
8. Promote only the smallest useful unit: reference, JIT provider, project dependency or infrastructure decision.
9. Record material durable decisions in the upstream catalog/current overlay/ledger.
10. Never claim a free tier, API feature or self-hosted project is current solely from a curated list snapshot.

## Source-specific rules

### free-for-dev
Use only to discover candidate SaaS/PaaS/IaaS/developer free tiers. Its own list policy excludes trial-only offers and aims at durable free tiers, but provider terms remain volatile and must be checked on the provider's current official pricing/docs before selection. Because the reviewed repository exposes no root LICENSE file, do not copy or redistribute substantial list content into Ercan OS.

### public-apis
Use category/Auth/HTTPS/CORS fields to shortlist APIs. Before production use, verify the API's actual official docs, auth model, HTTPS, CORS behavior, quota, license/terms, data quality, uptime and deprecation state. A public API is not automatically free, stable, safe or suitable for commercial use.

### awesome-selfhosted
Use as a broad discovery index for free-software network services and web applications. Project-level licenses vary and self-hosting introduces patching, backups, observability, secrets, abuse prevention and availability responsibilities. Never select self-hosting only to avoid a subscription without comparing operational cost and security burden.

### awesome-claude-code
Discovery only. The reviewed list is CC BY-NC-ND 4.0, so do not copy/adapt its curated content into Ercan OS. Follow links to the original candidate repository and audit that upstream independently.

### anthropics/skills
Official Anthropic examples/implementation reference. Do not treat the whole repository as uniformly open-source: the README states many skills are Apache-2.0 while document skills are source-available with different terms. Check the exact subdirectory license before reuse. Use current `agentskills.io` / canonical Agent Skills specification for format authority; use Anthropic's repo for examples and production-inspired patterns.

## Selection output

Return:
- requirement and constraints
- source(s) searched
- shortlisted candidates
- current primary-source verification
- managed vs self-hosted tradeoff when relevant
- security/license/privacy/ops cautions
- decision: ADOPT / ADOPT_WHEN_NEEDED / ADOPT_PATTERN_ONLY / WATCHLIST / REJECT
- exact Ercan OS/project integration point
- final state: VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED
