# Ercan OS — Weekly SEO Diagnostic

Status: active
Date: 2026-09-24

## Purpose

Define a recurring SEO/AEO/GEO health diagnostic that reports meaningful changes rather than repeating static audit noise.

Execution skill: `.agents/skills/weekly-seo-diagnostic/SKILL.md`.

Stable routing identities remain **52**.

## Provider model

### First-party
Use Search Console/Bing/analytics/index diagnostics where available for actual site search outcomes.

### DataForSEO
Reviewed external diagnostic provider for:
- OnPage crawl;
- DataForSEO Labs;
- SERP;
- Backlinks;
- optional AI Optimization / LLM Mentions.

### Rerun
Optional managed recurrence/execution surface through `managed-agent-deployment` and `rerun-api-bridge`.

## Weekly architecture

`baseline -> current crawl/data pull -> normalize -> issue fingerprint -> compare -> freshness/confidence gate -> prioritize -> report -> approved implementation -> verification -> save snapshot`

## DataForSEO freshness contract

Current official DataForSEO documentation states:
- Labs `Ranked Keywords` and selected related endpoints have weekly refresh cycles;
- underlying SERP database refresh depends on query/location and can range from roughly 30–90 days;
- Backlinks index is crawled continuously, while a full index refresh can take up to roughly 90 days;
- LLM Mentions database is continuously updated with a longer full refresh cycle.

Therefore a weekly schedule is an **observation cadence**, not proof that every source dataset is freshly regenerated every seven days.

Every stored metric should carry:
- provider;
- endpoint;
- location/language/device;
- retrieval time;
- provider data timestamp when available;
- freshness status.

## Technical SEO lane

Use OnPage API to detect material regressions in:
- HTTP/crawl health;
- indexability;
- canonical/redirect behavior;
- metadata/heading/template health;
- duplicate content/tags;
- internal links/resources;
- representative browser-rendering/Lighthouse metrics.

A crawl score is diagnostic only.

## Search performance lane

Use first-party Search Console as preferred actual performance evidence when available.

Use Labs/Live SERP for:
- ranking landscape;
- competitor/search-result context;
- external verification;
- priority live spot checks.

Do not claim causality from simple ranking correlation.

## Backlink lane

Monitor new/lost links/referring domains where useful.

Do not:
- treat every lost link as a crisis;
- label links toxic from a single vendor metric;
- auto-disavow.

## AI visibility lane

Optional.

May track:
- AI Overview references;
- LLM/answer-engine mentions;
- cited sources;
- query/prompt clusters.

Treat it as an observation layer, not a stable ranking score.

## Delta categories

Each report must classify:
- NEW;
- REGRESSED;
- IMPROVED;
- RESOLVED;
- PERSISTENT;
- DATA_INCOMPLETE / INSUFFICIENT_FRESHNESS.

## Prioritization

Use:
`severity × scope × business importance × confidence × freshness`.

First-party conversion/search impact can raise business importance.

## Cost control

Before enabling weekly production:
- define maximum crawl pages;
- define priority live SERP set;
- define optional lanes;
- define weekly spend ceiling;
- record actual cost.

Paid API expansion requires explicit approval when it would exceed the configured ceiling.

## Rerun state

Recommended Rerun state storage:
- private database for project/run details;
- workspace-shared database only for genuinely shared non-sensitive operational data;
- separate Rerun workspace for separate client tenant boundaries.

Do not store DataForSEO credentials in report rows/templates.

## Report retention

Keep enough snapshots for trend analysis, but avoid indefinite raw payload accumulation without purpose.

Prefer storing:
- normalized metrics;
- fingerprints;
- selected evidence;
- source timestamps;
- run/cost metadata.

Raw large crawl payloads may be retained only where debugging/audit value justifies them.

## Implementation boundary

The weekly diagnostic produces recommendations/tasks.

Actual fixes route through:
- platform specialist;
- technical SEO;
- design/performance/accessibility if impacted;
- independent release verification.

## Completion contract

The recurring system is VERIFIED only after:
- a baseline run;
- at least one comparison run or a clearly labeled baseline-only state;
- schedule/timezone verified;
- costs measured;
- report delivered;
- state persisted;
- provider failures/freshness represented honestly;
- no unauthorized production mutations.
