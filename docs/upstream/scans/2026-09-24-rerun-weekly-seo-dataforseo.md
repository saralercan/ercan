# Provider/Template Scan — Rerun Weekly SEO Diagnostic + DataForSEO

Date: 2026-09-24
Input URL: https://rerun.build/templates/weekly-seo-diagnostic-dataforseo

## Retrieval status

The exact supplied Rerun template page was not directly retrievable through the current web fetch/search path during review. Therefore no unseen template steps, prompts, connector scopes or pricing are asserted.

The slug is used only as discovery input. Ercan OS independently verified the DataForSEO primitives appropriate for a weekly SEO diagnostic.

## DataForSEO — reviewed official capabilities

### OnPage API
Official docs describe a customizable site crawler with:
- summary/issues;
- pages/resources/links;
- duplicate tags/content;
- redirect chains;
- non-indexable pages;
- page timing;
- optional JavaScript/browser rendering;
- Lighthouse integration.

Some options add cost.

Decision: `ADOPT_WHEN_NEEDED / EXTERNAL_SEO_DIAGNOSTIC_PROVIDER`.

### DataForSEO Labs
Official docs expose Google Ranked Keywords and related domain/keyword intelligence.

Current update-cycle guidance states:
- Ranked Keywords and several related endpoints use a weekly update layer;
- the underlying SERP database refresh cycle varies by query/location and can range roughly 30–90 days.

Decision:
weekly reporting must retain provider freshness timestamps and must not equate report cadence with source-data freshness.

### SERP API
Official docs expose location/language/device-specific live and standard SERP collection.

Decision:
use for priority verification/spot checks, not blanket weekly polling of the whole keyword universe.

### Backlinks API
Official docs expose summary/history/backlinks plus bulk new/lost backlink/referring-domain endpoints.

Current update guidance states continuous crawling with a longer full-index refresh cycle.

Decision:
weekly new/lost is useful diagnostic evidence but not a complete real-time web graph.

### AI visibility
DataForSEO currently exposes:
- AI Overview references through Ranked Keywords `item_types=["ai_overview_reference"]`;
- LLM Mentions via AI Optimization API.

Decision:
optional AEO/GEO lane with explicit provider timestamp/freshness caveats.

## Cost

DataForSEO APIs are usage-priced. Official docs expose cost fields and current pricing surfaces; OnPage JS/browser modes can add cost. Sandbox/API Playground can be used for testing, although API Playground itself can issue charged production calls depending on surface.

Decision:
weekly Ercan OS workflows require a configured budget ceiling and actual per-run cost recording.

## Architecture decision

Create one JIT `weekly-seo-diagnostic` capability under existing SEO/AEO/GEO specialists.

Preferred evidence order:
1. first-party search/index/analytics evidence;
2. DataForSEO technical/external market evidence;
3. Rerun as optional recurrence/orchestration runtime.

Do not create a new stable SEO agent and do not allow the report engine to autonomously mutate production SEO settings.
