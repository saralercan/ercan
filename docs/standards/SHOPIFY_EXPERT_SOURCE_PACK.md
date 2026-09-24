# Shopify Expert Source Pack

Status: active
Snapshot verified: 2026-09-24
Owner: Shopify Agent / Shopify Theme Developer / E-commerce Expert Agent
Freshness SLA: 7 days for material work

## Authority order

### Tier 1 — Shopify official
- Shopify Dev Docs: https://shopify.dev/docs
- Developer changelog: https://shopify.dev/changelog
- API release notes: https://shopify.dev/release-notes
- Theme best practices: https://shopify.dev/docs/storefronts/themes/best-practices
- Theme performance: https://shopify.dev/docs/storefronts/themes/best-practices/performance
- Theme accessibility: https://shopify.dev/docs/storefronts/themes/best-practices/accessibility
- Theme design: https://shopify.dev/docs/storefronts/themes/best-practices/design
- Storefront MCP / agentic commerce: https://shopify.dev/docs/apps/build/storefront-mcp
- Agents / UCP / catalog: https://shopify.dev/docs/agents
- WebMCP: https://shopify.dev/docs/api/web-mcp

### Tier 1 — Shopify canonical repositories
- https://github.com/Shopify/agent-skills
- https://github.com/Shopify/dawn
- https://github.com/Shopify/cli
- https://github.com/Shopify/hydrogen
- official Theme Check sources/rules
- current official API schemas exposed by Shopify tooling/skills

## Current 2026 snapshot

Verify again at task time. As of 2026-09-24:
- API version `2026-07` is the latest stable Shopify API release snapshot.
- Shopify's official agent-skills repository provides portable skills for Admin GraphQL, Storefront GraphQL, Customer Account, Partner API, Payments Apps, Functions, Hydrogen, Liquid/themes, Polaris extension surfaces, POS, custom data and general developer-documentation search.
- The official skills pair documentation search with schema/component validation; this is preferred over coding from memory.
- Dawn remains an HTML-first, JavaScript-only-as-needed reference theme, not a template to copy blindly.
- Themes should minimize JavaScript and prefer native browser/Liquid/CSS capabilities.
- Performance work must distinguish Liquid/server TTFB from browser work and use measured evidence.
- Theme Inspector is the native Liquid profiling route when render cost is suspect.
- LCP/CLS/INP are required storefront performance signals; do not lazy-load the LCP image.
- Standard storefront events/actions provide a common interaction layer across Liquid themes.
- Storefront MCP/UCP and WebMCP are material to agentic commerce and must be considered for AI-shopping work.
- Liquid `block` / `partial` composition is a July 2026 developer-preview surface unless current docs say otherwise.
- `useBuyerJourneyIntercept` / related checkout blocking patterns are deprecated in 2026-07; current validation should route to Shopify Functions where appropriate.

## Expert competency map

### Merchant/store architecture
- store plans/capabilities and merchant constraints
- markets/localization
- products/variants/collections
- metafields/metaobjects/custom data
- navigation/search/filtering
- inventory/fulfillment/shipping/returns
- discounts/pricing/promo presentation
- customer accounts and B2B when relevant

### Theme engineering
- Liquid
- JSON templates
- sections/blocks/snippets
- schema/settings
- app blocks/theme extensions
- localization
- semantic HTML
- CSS
- minimal JS
- standard storefront events/actions
- accessibility
- performance
- SEO/product structured data
- merchant configurability

### Apps/APIs
- GraphQL Admin API
- API versioning/migrations
- scopes/auth/security
- webhooks
- Functions
- Admin UI / checkout / customer account / POS extension surfaces
- custom distribution vs public apps
- Partner API
- Payments Apps when in scope

### Headless
- Storefront GraphQL
- Hydrogen
- React Router/runtime version fit
- caching/data-loading
- Oxygen/deployment when applicable
- headless SEO/performance/accessibility

### Agentic commerce
- Storefront MCP
- UCP catalog
- Global vs single-store catalog scope
- WebMCP
- tools/actions/events
- agent profiles/capabilities
- cart/checkout safety
- human confirmation for consequential writes

### Toolchain
- Shopify CLI
- Theme Check
- Theme Inspector
- official agent-skills
- browser QA
- accessibility checks
- Lighthouse/CWV
- GraphQL/schema validation

## Material-task gates

Before changing a Shopify production surface:
1. inspect store/theme/app reality;
2. identify API/theme/runtime versions;
3. refresh relevant official docs/changelog;
4. check current deprecations;
5. use the official schema/tool validation available;
6. measure performance before optimization;
7. preserve merchant editability;
8. run browser/mobile/accessibility/performance checks;
9. verify analytics/SEO when affected;
10. keep production publish/catalog/pricing/inventory/payment/destructive changes behind policy/Human Approval.

## Knowledge-ingestion examples

Accept:
- a current official API migration requirement;
- a new Theme Check rule;
- a stable storefront event/action;
- a measured Liquid performance failure pattern;
- a new supported MCP/UCP capability.

Do not ingest as authority:
- random theme snippets;
- stale Stack Overflow answers;
- Reddit claims without primary verification;
- star count;
- a vendor marketing article describing Shopify behavior without Shopify evidence.

## Regression cases

- stale API version used without checking latest stable -> fail
- deprecated checkout interception recommended -> fail
- heavy JS framework added when Liquid/CSS/native action suffices -> fail
- LCP image lazy-loaded -> fail
- Theme Check not run for material theme change -> fail
- merchant configurability broken -> fail
- unverified product/price/stock invented -> fail
- preview Liquid feature used without compatibility guard -> fail
- Dawn copied as a brand design rather than used as implementation reference -> fail
- agentic-commerce task ignores Storefront MCP/UCP/WebMCP surfaces -> fail
