# Upstream Scan — Developer Resource Discovery Sources

Date: 2026-09-24

## ripienaar/free-for-dev
Observed: curated developer-focused SaaS/PaaS/IaaS free tiers. Repository policy states entries should be genuine free tiers rather than ordinary short trials and, when time-bucketed, last at least a year. No root LICENSE file was observed in the reviewed repository.
Decision: DISCOVERY_SOURCE.
Use: candidate discovery only; re-check provider official pricing/terms/limits before recommendation or production use.

## public-apis/public-apis
Observed: broad public API catalog grouped by domain with Auth, HTTPS and CORS metadata; contribution tooling validates the catalog format.
License observed: MIT.
Decision: DISCOVERY_SOURCE.
Use: shortlist APIs, then verify the API's own official docs, current auth/quota/terms/data licensing/maintenance.

## awesome-selfhosted/awesome-selfhosted
Observed: broad catalog of free-software network services and web applications intended for self-hosting; current README links to active dead-link/unmaintained-project checks and a recommended HTML version. The catalog is already represented in Ercan OS upstream discovery.
License observed for list: CC BY-SA 3.0.
Decision: DISCOVERY_SOURCE / EXISTING.
Use: recursive discovery only; every listed project's own license/security/ops status must be audited.

## hesreallyhim/awesome-claude-code
Observed: curated Claude Code ecosystem list spanning documentation, tools, hooks, skills, orchestration, memory, observability, testing and related resources.
License observed: CC BY-NC-ND 4.0.
Decision: DISCOVERY_SOURCE_ONLY.
Use: follow links to original upstreams and audit them; do not copy/adapt the curated catalog into Ercan OS.

## anthropics/skills
Observed: official Anthropic skill examples/implementation patterns, template and links to the Agent Skills standard. README states many skills are open source (Apache-2.0) while document creation/editing skills are source-available rather than open source.
Decision: ADOPT_WHEN_NEEDED / OFFICIAL_REFERENCE.
Use: high-priority reference for Anthropic skill implementation patterns, but inspect exact subdirectory terms before reuse. The current open Agent Skills specification remains Ercan OS format authority.

## Architecture decision
Create one `developer-resource-discovery` JIT skill under `@UpstreamIntelligence` rather than five stable agents or dependencies. Extend existing discovery funnels and durable catalog/ledger/current overlay. No upstream code is installed or executed by this integration.
