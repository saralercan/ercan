---
name: continual-expertise-engine
description: Maintain source-backed, current, principal-level expertise for all 89 Vinterro One runtime agents. Use when improving agents, refreshing knowledge, researching current platform/domain practice, or when a selected specialist needs current authoritative evidence.
---

# Continual Expertise Engine

Load:
- `docs/standards/AGENT_CONTINUAL_EXPERTISE_ENGINE.md`
- `docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json`
- `docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json`
- task-relevant domain standards only.

## Core loop

For each selected ACTIVE specialist:

1. Read its source/expertise profile.
2. Identify volatile facts, APIs, rules, tooling, standards and professional practices.
3. Discover broadly across current public web, canonical GitHub, standards, primary research and high-quality engineering/practitioner sources.
4. Verify first-party/spec/canonical evidence before ingesting a claim.
5. Detect archives, successors, deprecations, version drift and conflicting guidance.
6. Convert accepted knowledge into concise durable learning: rules, checklists, tests, examples, migration notes or evals.
7. Re-verify in the target environment when executable evidence exists.
8. Record verified learning in Vinterro One through `record_agent_learning` when the native control plane is available.
9. Keep unrelated STANDBY agents inactive.

## Native Vinterro One actions

- `agent_expertise` — read one agent's profile, sources, recent learning and health.
- `expertise_due` — list agents that are missing/stale learning.
- `record_agent_learning` — store a verified/candidate learning with provenance and expiry.

## Source rules

- Tier 0 project/runtime truth overrides generic guidance.
- Tier 1 official/spec/regulator/platform sources are preferred.
- Tier 2 canonical maintained repositories are implementation authority.
- Tier 3 primary research/reviewed technical evidence supplements.
- Tier 4/5 community/social/tutorial content is discovery only until verified.
- Archived repositories never remain the current path when an official successor exists.

## Shopify

Shopify work must check current `shopify.dev`, the Shopify changelog and canonical Shopify repositories. The current Theme Check/Liquid developer tooling path includes `Shopify/theme-tools`; old archived Theme Check repositories are historical only. Use official Shopify agent-skills guidance as a current agent-development reference, but verify generated code with current Shopify tooling and the inspected theme/store.

## Completion

Do not claim an agent is current merely because it has a source list. `CURRENT` requires non-expired verified learning; `READY_TO_LEARN` means the source map is structurally ready but a fresh verified learning cycle has not yet been recorded.
