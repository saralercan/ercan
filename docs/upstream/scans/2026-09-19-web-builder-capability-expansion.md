# 2026-09-19 — Web Builder Capability Expansion

Status: REVIEWED / ADOPT NARROWLY
Repository: `saralercan/ercan`
Purpose: expand website-building capability without duplicating existing stable Ercan OS agent identities.

## Decision

Keep the stable routing surface at **21 Stable Core + 31 GitHub Specialist v3 Extension = 52 identities**. The new website-building areas are implemented as JIT capability lanes mapped onto existing stable specialists. This preserves the 2026-09-07 anti-duplication rule while materially expanding what the web pod can do.

## Canonical upstream verification

The following GitHub repositories were verified as public and non-archived on 2026-09-19 before inclusion:
- `OpenHands/OpenHands` (GitHub canonical redirect from historical owner path)
- `stackblitz-labs/bolt.diy`
- `dyad-sh/dyad`
- `onlook-dev/onlook`
- `BuilderIO/mitosis`
- `WordPress/gutenberg`
- `wp-cli/wp-cli`
- `WordPress/theme-check`
- `Shopify/cli`
- `Shopify/hydrogen`
- `browser-use/browser-use`
- `i18next/i18next`
- `lovell/sharp`
- `svg/svgo`
- `GoogleChrome/workbox`
- `aquasecurity/trivy`
- `semgrep/semgrep`
- `biomejs/biome`
- `stylelint/stylelint`
- `html-validate/html-validate`
- `withastro/astro`

## New capability lanes

Autonomous build orchestration, rapid/local AI app building, visual code editing, design-system/component lab, WordPress engineering/theme QA, Shopify storefront/headless commerce, authorized browser operation, SEO/indexability, localization QA, media optimization, PWA/offline, web security, frontend health and content-site architecture.

## Duplicate-role decisions

No new stable identity is created for DesignSystem, ComponentLab, WordPressEngineer, ShopifyStorefront or SEOIndexability because Ercan OS already has stable owners: `@FrontendSystem`, `@DesignTokenArchitect`, `@ComponentWorkshopQA`, `@WordPressExpert`, `@ShopifyExpert`, `@TechnicalSEO` and `@SEOScanner`.

AI builder/editor projects are engines/references, not policy authorities. Playwright/browser QA, platform-native validation, independent QA and Ercan OS safety/scope rules remain authoritative.

## Safety/operations

- Autonomous builders run repo-scoped and preferably sandboxed.
- Browser agents operate only on authorized surfaces and respect auth/approval boundaries.
- WordPress/Shopify changes prefer native tooling before generic automation.
- PWA/cache changes require rollback/update strategy.
- Security scanning uses current signatures/rules and is never treated as a complete security certification.
- Media optimization preserves originals and checks logo/text/crop integrity.
