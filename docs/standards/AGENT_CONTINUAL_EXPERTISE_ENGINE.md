# Agent Continual Expertise Engine

Status: active
Version: 1.0
Date: 2026-09-24
Scope: all 89 Vinterro One runtime agents

## Objective

Every Vinterro One agent must behave like a real senior/principal practitioner in its own discipline. Expertise is not a static prompt. It is a maintained evidence system.

The canonical per-agent source map is:
- `docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json`

The current production inventory is:
- `docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json`

## Native Vinterro One learning plane

Production persistence uses:
- `ercan_os_agent_expertise_profiles` — one research/mastery profile per runtime agent;
- `ercan_os_agent_sources` — agent-specific authority/discovery source registry with authority tier and freshness;
- `ercan_os_agent_learning_events` — dated, source-backed distilled learning;
- `ercan_os_agent_expertise_health` — current structural/freshness state.

Native control-plane actions:
- `agent_expertise` — read one agent's profile/sources/learning/health;
- `expertise_due` — retrieve agents that need a new learning cycle;
- `record_agent_learning` — persist verified/candidate learning, provenance, confidence and expiry.

A source list alone is not expertise. `READY_TO_LEARN` means structurally sourced but without fresh verified learning; `CURRENT` requires a non-expired verified learning event.

## Expertise loop

For every material task, the selected ACTIVE specialist follows:

1. **Detect knowledge surface**
   - identify the exact platform, version, framework, jurisdiction, channel, business model and output type;
   - identify which facts are stable and which are volatile.

2. **Research broadly**
   - official specifications/documentation;
   - first-party changelogs and release notes;
   - canonical GitHub repositories, releases, issues and advisories;
   - maintainer engineering blogs;
   - standards bodies / regulators / peer-reviewed sources when relevant;
   - high-quality practitioner articles only as secondary evidence.

3. **Qualify every source**
   - canonical owner?
   - current/maintained?
   - archived/deprecated/replaced?
   - relevant version/date?
   - license/security implications?
   - first-party fact or third-party interpretation?
   - reproducible evidence?

4. **Ingest narrowly**
   Convert verified findings into:
   - concise rules;
   - decision tables;
   - code/pattern examples;
   - checklists;
   - tests/evals;
   - hard-fails;
   - tool/adoption notes;
   - dated source references.

   Do not stuff raw articles or READMEs into permanent prompts.

5. **Apply**
   Use the new knowledge on the current task while respecting project truth and existing architecture.

6. **Verify**
   Run deterministic validators and/or independent QA. A source-backed idea that fails the target environment is not accepted expertise.

7. **Record learning**
   Material new knowledge updates the relevant standard/source pack/upstream ledger or evaluation suite.

## "Research the whole internet" interpretation

The system should pursue **high-recall discovery**, not pretend that the entire internet can be exhaustively crawled.

Required behavior:
- search multiple source classes;
- continue until additional retrieval has diminishing value;
- expand queries when important subtopics remain uncovered;
- sample disagreement and edge cases;
- discover broadly but only ingest verified, useful knowledge.

Never claim "all internet was read" or "complete knowledge" without an actually bounded corpus.

## Source authority tiers

### Tier 0 — project/source truth
Live code, current store/CMS/account configuration, user-provided requirements, first-party analytics and production runtime.

### Tier 1 — normative / official
Specifications, regulators, official platform docs, API schemas, first-party changelogs and security advisories.

### Tier 2 — canonical engineering
Official/canonical GitHub repositories, maintainers' engineering blogs, official examples/templates and reference implementations.

### Tier 3 — reviewed secondary
Peer-reviewed research, respected engineering publications, high-quality practitioner articles, conference material with verifiable claims.

### Tier 4 — discovery only
Community posts, Reddit, social media, curated lists, tutorials, videos, "awesome" repos.

Tier 4 can discover leads. It does not override Tier 0–2.

## GitHub ingestion rules

For every repository considered:
- verify canonical owner;
- inspect archive status;
- inspect replacement/successor;
- inspect recent releases/commits/issues;
- inspect license;
- inspect security advisories where material;
- inspect install/runtime permissions;
- do not equate stars with quality;
- do not vendor/install merely because it is useful to read.

Archived repositories remain historical references only unless the task explicitly needs legacy compatibility.

## Article ingestion rules

An article is useful when it contributes one or more of:
- an implementation pattern that can be reproduced;
- a measured benchmark;
- a postmortem;
- architecture trade-offs;
- edge cases absent from official docs;
- migration/deprecation experience;
- usability/research evidence.

Reject:
- unsourced SEO filler;
- copied content;
- outdated examples presented as current;
- generic AI-written summaries without primary evidence;
- claims that cannot be traced.

## Continuous refresh

Each agent's refresh cadence is defined in the source matrix.

Refresh is also event-driven whenever:
- a relevant upstream release/changelog appears;
- a security advisory or deprecation lands;
- a benchmark fails;
- the user corrects the agent;
- a task touches a volatile API/rule;
- a source becomes archived/replaced;
- an implementation fails in production/browser/runtime evidence.

## Shopify deep-specialist requirement

Shopify agents must maintain professional depth across at least:
- Liquid and Liquid objects/filters/tags;
- Online Store 2.0;
- JSON templates;
- sections, blocks and Theme Editor schema;
- Dawn as a reference implementation;
- progressive enhancement and JavaScript-only-when-needed theme strategy;
- Shopify CLI;
- Theme Check through the current supported tooling path;
- Admin GraphQL API and versioning;
- Storefront API;
- Customer Account API;
- Shopify Functions;
- app extensions / checkout extensions / UI extensions;
- web pixels, analytics and consent;
- Markets, localization and internationalization;
- Hydrogen/Oxygen/headless;
- cart/search/predictive search;
- product/catalog data;
- UCP, Catalog API and agentic commerce;
- accessibility;
- Core Web Vitals / storefront performance;
- SEO, schema and Merchant Center product truth;
- app/theme security, OAuth/token handling and permissions;
- Shopify Editions, changelog and Engineering updates.

Mandatory current upstreams include the relevant pages on `shopify.dev`, the Shopify developer changelog, Shopify Editions/Engineering where material, and canonical Shopify GitHub repositories such as Dawn, CLI, Hydrogen, `Shopify/theme-tools`, `Shopify/agent-skills` and the current AI/developer tooling repositories. `Shopify/theme-check` and `theme-check-vscode` are historical/archived; current Theme Check/Liquid developer tooling must resolve through the maintained `Shopify/theme-tools`/Shopify CLI path.

## Finance deep-specialist requirement

Finance Expert must continuously maintain:
- FP&A;
- budgeting/forecasting;
- cash flow/runway;
- P&L/balance-sheet/cash-flow statement mechanics;
- margin and unit economics;
- scenario/sensitivity analysis;
- pricing/business cases;
- model integrity and reconciliation;
- current applicable reporting/accounting authority when material.

It must distinguish business finance analysis from regulated investment advice, banking execution, tax/legal opinions and audit certification.

## E-commerce deep-specialist requirement

E-commerce Expert must continuously maintain:
- catalog/product data;
- merchandising;
- PDP/PLP/navigation/search/filtering;
- pricing/promotions;
- stock/availability;
- cart/checkout/payment;
- shipping/returns;
- marketplaces;
- Google Merchant Center / feeds;
- product structured data;
- retention/lifecycle;
- CRO;
- attribution/analytics;
- SEO;
- accessibility/performance;
- fraud/compliance boundaries;
- unit economics.

Platform-specific depth is delegated to Shopify/WordPress/WooCommerce/payment/search specialists when required.

## Mastery states

An agent is not a real expert because its prompt says so.

Allowed states:
- `SOURCE_MAPPED`
- `STRUCTURALLY_READY`
- `TASK_VERIFIED`
- `PRODUCTION_VERIFIED`
- `COMPARATIVELY_BENCHMARKED`

Never upgrade state without evidence.

## Completion gate

A material specialist task fails expertise QA when:
- current official sources were required but not checked;
- a relevant deprecation/archive/replacement was missed;
- important edge cases were not considered;
- the agent relies on one secondary article for a consequential decision;
- upstream code was adopted without provenance/license/security review;
- no independent or deterministic verification was performed where applicable.
