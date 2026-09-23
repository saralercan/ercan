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
- MCPServerDiscovery -> `punkpeye/awesome-mcp-servers` as a high-recall MCP discovery index; every server is independently audited before connection.
- LLMAppPatternDiscovery -> `Shubhamsaboo/awesome-llm-apps` as an agent/RAG/app pattern library; audit only the needed subproject.
- AgentSkillDiscovery -> `hesreallyhim/awesome-claude-code` plus `composio-community/awesome-codex-skills` as discovery indexes only; the latter requires per-skill license/security review.
- RootAwesomeDiscovery -> `sindresorhus/awesome` as the last-resort recursive index when narrower catalogs do not cover the requirement.
- PromptLeakResearch -> `x1xhlol/system-prompts-and-models-of-ai-tools` as defensive research reference only; do not copy, redistribute or operationalize leaked/proprietary prompt content.
- OfficialSkillReference -> `anthropics/skills` as an official Anthropic implementation/example source; the open Agent Skills specification remains the canonical format authority.
- CodingModelRouterWatchlist -> `Alishahryar1/free-claude-code` as a provider/router/fallback architecture reference only.

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

### awesome-mcp-servers
Use only to discover candidate MCP servers. Treat every MCP server as a separate software/credential/permission dependency. Resolve it to the original repository and review publisher identity, license, maintenance, install scripts, command execution, network egress, filesystem/database access, auth model and exposed tool surface before connection. Never grant production credentials merely because a server appears in the catalog.

### awesome-llm-apps
Use as a pattern/template library, not a trusted executable bundle. Audit the exact subproject, dependencies, external services, model/provider assumptions, data handling and domain risk before running or reusing it. High-stakes examples require domain-specific evidence and must not be promoted from demo code directly into production.

### awesome-codex-skills
The reviewed canonical repository is `composio-community/awesome-codex-skills`. Root license was not established; individual skills may carry distinct licenses. Resolve and audit the exact skill path, SKILL.md, scripts, allowed-tools, network/credential behavior and license. Do not bulk-install the catalog.

### sindresorhus/awesome
Use as a root recursive discovery index only after narrower Ercan OS sources fail to cover the requirement. Follow the relevant sub-list to the original project and audit the original project. Never recursively ingest the whole awesome ecosystem into task context.

### prompt-leak collections
Collections of exposed/leaked system prompts or model artifacts are not approved skill/prompt sources. They may inform defensive threat modeling for prompt extraction or prompt injection, but Ercan OS must not copy or operationalize leaked/proprietary content, infer vendor behavior from it as authoritative, or redistribute material without clear rights. Prefer official/current product documentation and observable public behavior.

### free-claude-code
Use only when the actual goal is coding-model/provider routing, fallback resilience or local proxy architecture. The repository is MIT, but provider integrations have independent authentication, terms, quotas, privacy and billing behavior. Review installer scripts, local listening interfaces, credential storage, proxy authentication and every selected provider's current official terms before any execution. Do not treat the README's aggregate free-token claim as a durable fact.

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
