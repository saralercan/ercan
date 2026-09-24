# Shopify Expertise Refresh — 2026-09-24

Status: verified snapshot
Owner: @ShopifyExpert / Shopify runtime pod
Purpose: dated current-source findings that materially change Shopify implementation decisions.

## Verified primary / canonical sources

- Shopify developer docs: https://shopify.dev/docs
- Shopify developer changelog: https://shopify.dev/changelog
- Theme architecture: https://shopify.dev/docs/storefronts/themes/architecture
- Blocks: https://shopify.dev/docs/storefronts/themes/architecture/blocks
- Theme limits: https://shopify.dev/docs/storefronts/themes/architecture/limits
- Theme Store requirements: https://shopify.dev/docs/storefronts/themes/store/requirements
- Admin GraphQL latest: https://shopify.dev/docs/api/admin-graphql/latest
- Storefront events/actions changelog: https://shopify.dev/changelog/standard-storefront-events-and-actions
- Admin new-look changelog: https://shopify.dev/changelog/prepare-your-app-for-the-shopify-admins-new-look
- Dawn: https://github.com/Shopify/dawn
- Shopify CLI: https://github.com/Shopify/cli
- Hydrogen: https://github.com/Shopify/hydrogen

## Current findings

### Dawn reference baseline
Dawn is Shopify's first-party reference theme. The current repository advertises an HTML-first, server-rendered Liquid and progressive-enhancement approach with JavaScript only when needed. Dawn main can contain work ahead of the stable Theme Store release; production comparisons must distinguish main from stable.

Snapshot observed: Dawn theme version 16.0.0.

Operational rule:
- use Dawn as architecture/regression/reference evidence;
- do not blindly clone Dawn as the final merchant design;
- preserve merchant configurability, brand distinction and project-specific information architecture.

### Theme blocks are first-class
Current Shopify themes distinguish:
- reusable theme blocks in `/blocks`;
- section-local blocks;
- app blocks.

Theme blocks can nest. Snippets and blocks have different responsibilities: blocks expose merchant customization, snippets receive variables and provide reusable implementation.

Snapshot limits observed:
- up to 300 theme block files;
- theme block nesting depth up to 8;
- 25 sections per JSON template;
- 50 blocks per section.

Operational rule: choose section / theme block / section block / snippet / app block intentionally instead of repeating legacy section-only patterns.

### Theme Store QA is a real release gate
Current Theme Store requirements include Lighthouse benchmark thresholds and require actual content during tests.

Snapshot observed:
- average Lighthouse performance >= 60 across home/product/collection on mobile and desktop;
- average Lighthouse accessibility >= 90.

Operational rule: Shopify QA must include mobile/desktop performance, accessibility and key purchasing flows. A successful `theme check` alone is not release evidence.

### Admin GraphQL is version-aware
The current Admin GraphQL reference exposed 2026-07 as latest on 2026-09-24.

Operational rule:
- resolve the project's actual API version;
- validate queries/mutations against current schema;
- do not infer fields from model memory;
- treat REST Admin as legacy unless an inspected existing integration still requires it.

### Standard storefront events and actions
Shopify announced standard storefront events/actions on 2026-06-17. Themes can emit standard commerce events; apps/agents can use Shopify actions for storefront behaviors.

Operational rule: before inventing custom theme/app cross-theme event plumbing, inspect the current standard storefront event/action surface and use it when it fits.

### Shopify admin visual refresh
Shopify announced a new admin look rolling out from 2026-09-15. UI extensions adopt new styles automatically; custom App Home interfaces need deliberate Polaris 2.0 migration evaluation.

Operational rule: app-admin UI work must verify the current Polaris/admin surface rather than using stale screenshots or styling assumptions.

## Required Shopify research loop

For every material Shopify task:

1. Inspect the actual store/theme/app and API version.
2. Read the matching current `shopify.dev` surface.
3. Check the developer changelog for the affected surface.
4. Inspect the matching canonical Shopify repository/release when code/tool behavior matters.
5. Search issues/advisories for edge cases when relevant.
6. Use maintainer engineering articles and high-quality secondary sources only after primary evidence.
7. Implement through the native Shopify surface.
8. Run native validation.
9. Run browser/runtime/performance/accessibility QA as applicable.
10. Record material new learning with date/provenance/expiry.

Do not treat this snapshot as permanently current. It expires into task-time revalidation.
