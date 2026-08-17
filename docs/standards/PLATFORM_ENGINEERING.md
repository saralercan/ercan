# Platform Engineering — Shopify + WordPress

## Shared release principle
“Works” is not enough. Production changes must be platform-native, maintainable, upgrade-safe, testable and rollback-aware.

Risk-appropriate release chain:
`inspect/reproduce → identify source of truth → minimal patch → lint/schema → build → unit/integration → browser E2E → responsive/visual QA → console/network → a11y → performance/security → preview/staging → publish → post-deploy smoke`.

### Shared rules
- Never edit platform core or generated build outputs as the source fix.
- Prefer public APIs, hooks, extensions, blocks/sections and supported integration surfaces over DOM hacks/monkey patches.
- Temporary compatibility shims must be isolated, documented and regression-tested.
- Verify current platform versions/deprecations from official docs/upstream at runtime.
- No `DONE` without required gates passing.

## Shopify
### Architecture
- Native theme structure: assets, blocks, config, layout, locales, sections, snippets, templates.
- Reusable merchant-editable UI belongs in sections/blocks/snippets with schema; avoid monolithic `theme.liquid` or giant feature sections.
- Preserve Theme Editor selection/reorder/drag/drop behavior and `@app` support where relevant.
- App integrations prefer Theme App Extensions/app blocks/app embeds; supported checkout/customer-account/admin/POS extension points beat legacy injection.

### Liquid/code
- Do not guess Liquid tags/filters/objects. Validate against current Shopify docs/Theme Tools.
- `render` is isolated scope; pass dependencies explicitly.
- Use locale keys (`t`), platform money/localization, modern image helpers and responsive images.
- Avoid hot-loop product/variant/metafield over-iteration, excessive nesting and global JS/CSS.
- HTML/CSS first; JS only for necessary interaction.

### Tooling
- Current upstream is Shopify Theme Tools/Shopify CLI; legacy `Shopify/theme-check` is historical/superseded.
- Run Theme Check before release. Use development/unpublished theme preview rather than direct live editing.
- Store/theme/app config and API behavior are validated with current CLI/docs.
- Use Git as source of truth where possible; reconcile Theme Editor/admin changes before pushing.

### Performance
- No meaningful regression on home/product/collection/critical custom templates.
- LCP/hero media is not blindly lazy-loaded; below-fold media is a lazy-load candidate.
- Inspect actual Liquid bottlenecks when needed; keep bundles/assets scoped and lean.

### Storefront regression candidates
Header/nav, multi-level mobile/mega menu, search, collection filter/sort/pagination, variant-price-media-availability sync, quantity, add-to-cart, cart drawer/page update/remove, discount/free-shipping messaging, checkout handoff, customer/account, localization/currency, app blocks and Theme Editor interactions across critical viewports.

### Security/access
Least-privilege collaborator/staff/API scopes; never expose secrets/tokens in Liquid/frontend/logs/screenshots. Checkout/payment/customer-data changes receive higher risk gates.

## WordPress
### Architecture
- Never edit WordPress core.
- Persistent business functionality belongs in a plugin; presentation belongs in theme. Parent-theme customization should be update-safe (child theme/custom plugin/hooks as appropriate).
- Prefer actions, filters, REST API, Settings API, Block APIs and official extension mechanisms over third-party plugin source edits.
- Modern editor projects should consider `block.json`, `theme.json` and Interactivity API; preserve existing architecture when migration is not part of scope.

### Coding and security
- WordPress Coding Standards/PHPCS are baseline.
- Unique namespace/prefix/class naming; separate source/generated output.
- Validate → sanitize → authorize → nonce where applicable → execute → late/contextual escape.
- Nonce is not authorization; use capability checks.
- REST routes need intentional `permission_callback`.
- Use platform DB APIs or safe prepared queries; never raw SQL interpolation.
- Secrets do not enter frontend/localized script/log output.

### Assets/performance
- Enqueue APIs, dependency graph and scoped asset loading; avoid hardcoded script/link injection.
- Inspect N+1/query count, remote latency, autoload/options bloat, duplicate bundles and oversized DOM/assets.
- Cache is not a substitute for root-cause analysis.

### Plugin lifecycle
Activation, deactivation and uninstall have distinct semantics. Persistent user-owned data is not casually deleted on deactivation. Schema migrations are versioned/repeatable/failure-aware; cron, rewrites, custom tables/options have explicit lifecycle cleanup.

### Testing
- Reproducible `wp-env`/equivalent dev environment.
- PHP unit/integration tests where relevant.
- Playwright E2E for site load, navigation, forms, custom blocks, admin settings save, frontend output and project-critical flows.
- CI lint/build/activation/security checks.
- `WP_DEBUG`/dev logs should not contain unexpected fatal/warning/deprecation output before release.
- Core/plugin/theme upgrade compatibility smoke for critical projects.

### Enterprise-strength optional layer
When justified, augment WPCS with PHPCompatibilityWP, VariableAnalysis and selected VIP Coding Standards rules. Do not impose VIP-specific rules blindly on ordinary sites.

## Definition of high-confidence completion
No known critical bug; no fatal/console blocker; platform-native architecture; required static/build/tests green; critical E2E and responsive visual QA green; no material a11y/performance regression; security checks green; rollback point known. Zero-bug guarantees are never claimed.
