---
name: weekly-seo-diagnostic
description: Run a recurring SEO/AEO/GEO diagnostic that compares current technical, ranking, backlink and AI-visibility evidence against prior snapshots, prioritizes only material new/regressed/resolved issues, and emits an evidence-backed action plan. Use for weekly SEO monitoring, Rerun/DataForSEO diagnostics, search visibility health checks or recurring SEO reports.
---

# Weekly SEO Diagnostic

This is a JIT capability under the existing SEO/AEO/GEO specialists. It does not create a new stable identity.

Primary reviewed provider stack:
- first-party measurement: Google Search Console / Bing Webmaster / analytics where available;
- external diagnostics: DataForSEO OnPage, Labs, SERP, Backlinks and optional AI Optimization;
- managed recurrence: Rerun when selected.

## Stable-owner mapping
- technical crawl/indexability -> `@TechnicalSEO + @SEOScanner`
- WordPress/Shopify implementation -> matching platform SEO specialist
- ranking/market deltas -> `@TechnicalSEO + @AEO_GEO`
- AI Overview / LLM visibility -> `@AEO_GEO`
- managed recurrence -> `managed-agent-deployment + rerun-api-bridge`
- independent verification -> task-relevant browser/search/platform QA

## Core principle

The report is **delta-first**, not score-first.

Every run classifies findings as:
- NEW
- REGRESSED
- IMPROVED
- RESOLVED
- PERSISTENT
- UNKNOWN / INSUFFICIENT FRESHNESS

Do not dump the same static issue list every week without explaining what changed.

## Measurement authority

Prefer first-party evidence for the site's actual search outcomes:
- Search Console clicks/impressions/query/page performance;
- Bing Webmaster data;
- analytics/conversions;
- index coverage / URL inspection where available.

Use DataForSEO for external crawl/search/backlink/market/AI visibility evidence.

Do not treat an external SEO score as a substitute for first-party performance.

## DataForSEO lanes

### 1. OnPage API — technical SEO
Use for:
- site crawl summary;
- status/indexability checks;
- duplicate title/description/content;
- redirect chains;
- links/resources;
- non-indexable pages;
- page timing;
- representative Lighthouse/performance checks;
- JavaScript/browser-rendering diagnostics when materially required.

Current DataForSEO OnPage API exposes customizable crawling and 60+ on-page checks. Features such as resource loading, JS execution, browser rendering and keyword density can add cost.

Do not enable every expensive crawl option by default.

### 2. DataForSEO Labs — ranking/search landscape
Use for:
- Ranked Keywords;
- ranking positions and URLs;
- competitor/domain intersections when relevant;
- keyword and domain opportunity analysis;
- AI Overview references via `item_types=["ai_overview_reference"]` when relevant.

Important freshness rule:
DataForSEO currently documents `Ranked Keywords` and several related Labs endpoints on a weekly refresh layer, while the underlying SERP database can have query/location refresh cycles ranging roughly 30–90 days.

Therefore:
- store `last_updated_time` / `previous_updated_time`;
- do not interpret every weekly delta as a fresh weekly Google movement;
- mark stale/unchanged provider timestamps as `INSUFFICIENT_FRESHNESS`;
- for high-priority volatile keywords, use a current live SERP spot-check instead.

### 3. SERP API — live verification
Use sparingly for:
- priority keyword spot-checks;
- local/device/location-specific current SERP verification;
- discrepancies between Labs and first-party evidence;
- SERP feature presence.

SERP results depend on explicit keyword, location, language, search engine and device. Preserve those parameters with evidence.

Do not live-check thousands of terms every week when Labs/first-party data is enough.

### 4. Backlinks API
Use for:
- backlink/referring-domain summary;
- new/lost backlinks/referring domains;
- material link-profile changes;
- selected spam/risk investigation when useful.

DataForSEO exposes bulk new/lost backlink endpoints with historical data. Its backlink index is continuously crawled but full index refresh can take substantially longer than one week.

Treat weekly new/lost link counts as diagnostic evidence, not a complete representation of the web.

### 5. AI Optimization / LLM Mentions
Optional.

Use when the project's search strategy explicitly includes AI-search/answer-engine visibility.

Track:
- brand/domain mentions;
- sources/citations where provided;
- prompt/query clusters;
- changes over time.

DataForSEO currently describes LLM Mentions data as continuously updated with a longer full-database refresh cycle. Avoid overstating short-window changes.

## Weekly run schema

### Input config
- canonical domain
- project/brand
- location(s)
- language(s)
- device(s)
- target keyword clusters
- priority landing/service/product pages
- competitor set
- technical crawl page cap
- optional AI visibility lane
- optional backlink lane
- DataForSEO weekly budget ceiling
- report destination

### Baseline
Store the prior successful run:
- URL issue fingerprint
- technical issue counts
- critical URL states
- ranked keyword snapshot + provider timestamps
- priority live SERP snapshot
- backlink deltas
- optional AI visibility snapshot
- first-party search KPIs
- run/provider costs

If there is no valid baseline, label the run BASELINE and do not invent trend direction.

## Issue fingerprinting

Create stable fingerprints from:
`issue_type + canonical_url + relevant_dimension`.

Examples:
- `non_indexable|https://example.com/page|noindex`
- `duplicate_title|/a|cluster_hash`
- `redirect_chain|/old|target_path`

This allows weekly dedupe and change tracking.

## Priority model

Prioritize using:
`severity × affected_scope × business_importance × confidence × freshness`.

Do not prioritize solely by vendor score.

### Critical examples
- important pages accidentally non-indexable;
- canonical to wrong domain/page;
- widespread 4xx/5xx;
- robots/sitemap regressions;
- broken hreflang affecting target locales;
- production templates losing titles/H1/schema;
- high-value page disappearing from first-party search evidence;
- severe performance/rendering regression affecting important pages.

### Lower-priority examples
- cosmetic metadata opportunities;
- one low-value page with minor warning;
- stale provider-only fluctuation without fresh corroboration.

## Cost governance

DataForSEO is usage-priced.

Rules:
- define a weekly budget ceiling before enabling recurrence;
- record per-run API cost from response fields/account evidence where available;
- avoid repeating full crawls when nothing changed and a lighter check is sufficient;
- use representative Lighthouse URLs rather than every URL by default;
- use live SERP only for priority terms;
- enable JS/browser rendering only where needed;
- stop/escalate before crossing the configured weekly ceiling;
- never quote cost from memory when an API/current pricing surface can provide it.

Sandbox/testing may be used before production calls where supported.

## Report output

### Executive summary
- overall state: HEALTHY / WATCH / ACTION_REQUIRED / DATA_INCOMPLETE
- 3–7 most important changes
- estimated business/search impact
- confidence/freshness caveats

### Changes
- NEW / REGRESSED
- RESOLVED / IMPROVED
- PERSISTENT critical
- rankings/visibility deltas
- backlink changes
- AI visibility changes when enabled

### Action queue
Each action includes:
- issue
- evidence
- affected URL/query
- owner
- recommended fix
- priority
- verification step
- whether implementation is safe to auto-fix or requires review

### Data quality
- provider timestamps
- first-party data availability
- failed endpoints
- incomplete crawl areas
- cost
- known stale datasets

## Auto-fix policy

Default is **diagnose and propose**, not autonomous SEO mutation.

May auto-create:
- issue/ticket/task;
- report;
- structured fix proposal;
- approved low-risk metadata patch in a separately authorized implementation workflow.

Do not automatically:
- rewrite many pages;
- change robots/noindex/canonicals;
- delete pages;
- alter redirect maps;
- publish schema/content;
- disavow links;
- submit broad indexing actions;
without the project-specific implementation/approval flow.

## Rerun deployment

When using the supplied Rerun template `weekly-seo-diagnostic-dataforseo`:
- treat the template as a managed workflow reference;
- exact template body was not directly retrievable in this review, so do not invent its internal steps;
- deploy through `managed-agent-deployment` + `rerun-api-bridge`;
- keep this Ercan OS skill/standard as the source of truth;
- use a project-specific workspace when client isolation matters;
- keep DataForSEO credentials outside templates/share links;
- schedule timezone explicitly;
- store snapshot/fingerprint state in a scoped database;
- run a safe initial baseline before weekly recurrence.

## Completion

A weekly diagnostic is VERIFIED only when:
- run executed on the intended domain/market;
- crawl/provider calls succeeded or failures are explicit;
- baseline comparison is valid;
- provider freshness timestamps are retained;
- first-party and external signals are not conflated;
- costs stay within the configured ceiling;
- critical findings have source evidence;
- report distinguishes observations from recommendations;
- no unauthorized SEO changes were applied.
