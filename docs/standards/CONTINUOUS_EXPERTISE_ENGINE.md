# Continuous Expertise Engine — Vinterro One

Status: active
Version: 1.0
Date: 2026-09-24
Runtime scope: 89 active agents

## Purpose

Vinterro One agents do not rely on frozen model memory as their definition of expertise. Each runtime agent maintains a continuously refreshed, source-backed specialist profile.

The system is deliberately **high-recall but bounded**. “Search the whole internet” is interpreted operationally as: search broadly enough to cover the authoritative and technically relevant source space, then adopt only verified, applicable knowledge. No system can literally read the entire public internet, and no agent may claim that it did.

## Canonical artifacts

- Runtime inventory: `VINTERRO_RUNTIME_AGENT_MANIFEST.json`
- Per-agent source authority: `AGENT_SOURCE_AUTHORITY_89.json`
- Agency quality bar: `AGENCY_EXCELLENCE_STANDARD.md`
- Portable routing: `PORTABLE_AGENT_RUNTIME.md`
- Shopify deep pack: `SHOPIFY_EXPERT_SOURCE_PACK.md`
- JIT skill: `.agents/skills/continuous-expertise/SKILL.md`

## Research ladder

For every material task, use the smallest relevant slice of this authority order:

1. Project/company/store/source-of-truth data.
2. Current official specifications, platform docs and product documentation.
3. Official changelogs, release notes and deprecation notices.
4. Canonical maintained repositories, schemas, code references and official examples.
5. Standards bodies, security advisories, regulatory/primary scientific sources.
6. Measured runtime evidence from the actual system.
7. Maintainer discussions/issues when official docs are incomplete.
8. High-quality engineering/editorial/industry articles as secondary context.
9. Community/social material only for discovery and hypothesis generation.

Popularity, search rank, virality and star count are never authority.

## Deep-research procedure

A specialist entering a material task must:

1. Identify the exact surface/version/runtime/project.
2. Load its entry from `AGENT_SOURCE_AUTHORITY_89.json`.
3. Determine whether the existing source knowledge is inside its freshness SLA.
4. Search current primary sources and relevant canonical repositories.
5. Read the surrounding source context; do not learn from snippets/titles alone.
6. Extract atomic claims/patterns with URL/repo, date/version and applicability.
7. Resolve contradictions:
   - current official docs beat old official docs;
   - executable schema/runtime evidence beats prose assumptions;
   - project truth beats generic examples;
   - security/regulatory authority beats community guidance.
8. Classify each finding:
   - `CURRENT_PATTERN`
   - `EXPERIMENTAL/PREVIEW`
   - `DEPRECATED`
   - `PROJECT_SPECIFIC`
   - `UNVERIFIED`
9. Use verified findings in the task.
10. Fold reusable knowledge into the role source pack/eval when it changes how future tasks should be done.
11. Add a regression/eval case when a newly learned failure mode is material.
12. Never say knowledge was “internalized” unless the relevant source pack/manifest/eval actually changed.

## Freshness SLAs

Default maximum age before a material task requires a refresh:

- security/advisories, social/ads APIs, local events/facts: **3 days**
- Shopify/e-commerce/search/finance/agent-runtime/DevOps/Supabase/Firebase: **7 days**
- WordPress, web engineering, content/design/brand: **14 days**
- accessibility standards / slower standards surfaces: **30 days**

A task can demand a shorter SLA.

## Knowledge ingestion contract

Ingest a finding only when it is:
- materially useful;
- source-backed;
- current and applicable;
- non-duplicative;
- license/rights compatible where code/assets are involved.

Store:
- source URL/repository;
- source type;
- publication/release/verification date;
- platform/API/runtime version;
- concise claim/pattern;
- applicability;
- confidence;
- deprecation/preview state;
- associated benchmark or regression test when material.

Never copy entire external documents into prompts or the repository. Store concise operational rules and point back to the source.

## Progressive disclosure

Do not inject all 89 agents' research into every task.

- Orchestrator selects the ACTIVE pod.
- Only ACTIVE agents load their source-authority entries.
- Only task-relevant sections of source packs are loaded.
- STANDBY agents receive no task context unless activated.
- A new need triggers `STANDBY -> ACTIVE` and a targeted source refresh.

This preserves quality without context pollution.

## Expertise state

Allowed labels:

- `SOURCE_MAPPED` — authoritative source map exists.
- `FRESHLY_RESEARCHED` — required authority refresh executed inside SLA.
- `TASK_VERIFIED` — a real task passed its domain checks.
- `PRODUCTION_VERIFIED` — live or production-equivalent evidence passed.
- `COMPARATIVE_BENCHMARKED` — reproducible external comparison exists.

Do not infer `PRODUCTION_VERIFIED` from health=100 or from the presence of instructions.

## Evaluation

Every agent must have:
- at least one authority route;
- at least one deep-scan topic;
- a freshness SLA;
- an ingestion rule;
- a hard rule preventing fabricated research/validation;
- a runtime adapter path.

Specialists with volatile APIs should additionally maintain version/deprecation regression cases.

## Continuous improvement

When a task, incident, failed QA check, platform change or newly discovered authoritative source reveals a better practice:
1. fix the task;
2. update the agent's reusable source rule;
3. update/create the eval;
4. mark the old rule deprecated if relevant;
5. propagate only to agents whose scope materially overlaps.

The goal is compounding verified expertise, not uncontrolled prompt growth.
