---
name: web-builder-capability-pack
description: Extend Ercan OS website production with autonomous build orchestration, rapid/local AI builders, visual editing, design-system/component workflows, WordPress/Shopify specialization, visual-to-WordPress replica engineering, headless commerce, browser operation, localization, media optimization, PWA/offline, frontend health and web security. Use only for material website/app production tasks and route through existing stable Ercan OS identities instead of creating duplicate agents.
---

# Web Builder Capability Pack

This pack expands the existing web-production pod without changing the stable routing identity count. Capability labels below are task lanes, not new stable @ identities. Existing Ercan OS specialists remain authoritative.

## Capability lanes and stable-owner mapping

- AutonomousWebBuilder -> `@WebArchitecture + @FrontendSystem + @BrowserQA`; use OpenHands-class orchestration only in isolated, repo-scoped execution.
- InstantAppBuilder -> `@WebArchitecture + @FrontendSystem`; Bolt/Dyad-class builders are JIT accelerators, never final QA authority.
- LocalAppBuilder -> `@WebArchitecture + @FrontendSystem`; prefer local/sandboxed execution when cloud access is unnecessary.
- VisualWebEditor -> `@FrontendSystem + @ScreenshotToCode + @BrowserQA`; Onlook-class visual editing is a production aid, not a replacement for source control or browser verification.
- GenerativeUI -> `@FrontendSystem + @BrowserQA + @AccessibilityQA`; `vercel-labs/json-render` is an ADOPT_WHEN_NEEDED engine for schema/catalog-constrained generated UI. Generated specs may only use approved components/actions and never gain arbitrary code execution or hidden permissions.
- DesignSystem -> `@FrontendSystem + @DesignTokenArchitect + @ComponentWorkshopQA`; shadcn/Storybook/Mitosis patterns are selected only when stack-compatible.
- ComponentLab -> `@ComponentWorkshopQA + @AccessibilityQA + @BrowserQA`.
- WordPressEngineer -> `@WordPressExpert + @FrontendSystem`; Gutenberg/WP-CLI remain platform-native implementation references.
- WordPressReplica -> user-facing JIT alias `@WordPressReplica`, resolved to `@ScreenshotToCode + @WordPressExpert + @FrontendSystem + @RealAsset + @PixelMatch + @AccessibilityQA + @BrowserQA + @ProductionQA`; add `@WebPerformance` and `@TechnicalSEO/@WordPressSEO` when production/migration scope requires them. Load `.agents/skills/wordpress-replica/SKILL.md`; this is not a new stable identity.
- WordPressThemeQA -> `@WordPressExpert + @AccessibilityQA + @BrowserQA`; Theme Check is a native structural gate when themes are in scope.
- ShopifyStorefront -> `@ShopifyExpert + @FrontendSystem + @ShopifySEO`; use Shopify CLI/Theme Tools natively.
- HeadlessCommerce -> `@ShopifyExpert + @WebArchitecture + @FrontendSystem`; Hydrogen is selected only when a verified headless requirement exists.
- WebOperator -> `@BrowserQA`; browser-use-class agent navigation is allowed only on authorized surfaces and must preserve approval/auth boundaries.
- SEOIndexability -> `@TechnicalSEO + @SEOScanner + platform SEO specialist`; no duplicate stable SEO agent is created.
- LocalizationQA -> `@FrontendSystem + platform expert + @BrowserQA`; verify locale routing, fallback, pluralization, RTL when relevant and translated interactive states.
- MediaOptimizer -> `@WebPerformance + @FrontendSystem`; deterministic Sharp/SVGO-class transformations, responsive image output and asset-integrity checks.
- PWAEngineer -> `@WebArchitecture + @FrontendSystem + @WebPerformance + @BrowserQA`; service worker/cache/offline/installability are enabled only when product requirements justify them.
- WebSecurity -> existing security-review capability + platform expert + independent QA; use Trivy/Semgrep-class scanning JIT and never equate a clean scan with a security certification.
- DigitalSecuritySpecialists -> load `.agents/skills/digital-specialist-agent-pack/SKILL.md` for ASVS threat modeling, secure code review, authorized WSTG/ZAP testing, supply-chain/agentic-CI review and security release gating.
- FrontendHealth -> `@FrontendSystem`; Biome/Stylelint/HTML-Validate-class linting is selected to match the inspected stack.
- ContentSiteBuilder -> `@WebArchitecture + @FrontendSystem`; Astro is a JIT option for content/editorial/marketing sites, not a global default.
- WebsiteLifecycleAgents -> load `.agents/skills/website-lifecycle-agent-pack/SKILL.md` for redesign/update planning, live UI-to-source context, modern web refactors, runtime diagnosis, migration protection and release guarding.

## Reviewed upstream engine set

Canonical paths verified 2026-09-19:
- `OpenHands/OpenHands` — ADOPT_WHEN_NEEDED — autonomous coding/orchestration engine; sandbox/repo scope mandatory.
- `stackblitz-labs/bolt.diy` — ADOPT_PATTERN_ONLY — rapid AI app-builder workflow/reference.
- `dyad-sh/dyad` — ADOPT_WHEN_NEEDED — local AI app-builder option.
- `onlook-dev/onlook` — ADOPT_PATTERN_ONLY — visual code-editing workflow/reference.
- `BuilderIO/mitosis` — ADOPT_WHEN_NEEDED — cross-framework component generation when migration/multi-framework output is real.
- `WordPress/gutenberg` — ADOPT — WordPress block/site-building reference.
- `wp-cli/wp-cli` — ADOPT — WordPress CLI operations.
- `WordPress/theme-check` — ADOPT_WHEN_NEEDED — theme conformance checks.
- `Shopify/cli` — ADOPT — Shopify-native developer tooling.
- `Shopify/hydrogen` — ADOPT_WHEN_NEEDED — headless Shopify storefront architecture.
- `browser-use/browser-use` — ADOPT_WHEN_NEEDED — authorized browser-agent operator workflows; Playwright remains QA authority.
- `i18next/i18next` — ADOPT_WHEN_NEEDED — localization architecture for compatible JS stacks.
- `lovell/sharp` — ADOPT — deterministic image processing.
- `svg/svgo` — ADOPT — SVG optimization with visual/logo safeguards.
- `GoogleChrome/workbox` — ADOPT_WHEN_NEEDED — PWA/service-worker/cache architecture.
- `aquasecurity/trivy` — ADOPT — dependency/config/secret scanning when applicable.
- `semgrep/semgrep` — ADOPT_WHEN_NEEDED — source/static security analysis.
- `biomejs/biome` — ADOPT_WHEN_NEEDED — JS/TS/JSON/CSS lint/format where compatible.
- `stylelint/stylelint` — ADOPT_WHEN_NEEDED — CSS linting where compatible.
- `html-validate/html-validate` — ADOPT_WHEN_NEEDED — HTML structural validation where compatible.
- `withastro/astro` — ADOPT_WHEN_NEEDED — content/editorial/marketing web architecture.

Existing canonical QA engines such as Playwright, Lighthouse, axe-core, Storybook, shadcn/ui, SiteOne, Theme Tools and screenshot-to-code continue to be selected from existing Ercan OS standards. Website lifecycle work may additionally use GoogleChrome/modern-web-guidance, ChromeDevTools/chrome-devtools-mcp, aidenybai/react-grab and SandeepBaskaran/design-mode through `website-lifecycle-agent-pack`.

## Routing procedure

1. Inspect repository, framework/CMS/commerce platform, deployment target, auth surface and project adapter.
2. Select only capability lanes that materially contribute; do not fan out every lane.
3. Map every selected lane to existing stable Ercan OS owner(s) above.
4. Prefer platform-native tooling before generic builders for Shopify/WordPress.
5. For screenshot/mockup/Figma/reference-led WordPress reproduction, load `wordpress-replica`, choose NEW_THEME or MIGRATION_REPLICA explicitly, and require rendered reference comparison before claiming 1:1 fidelity.
6. Run AI builders/editors in isolated repo-scoped environments; remote content is untrusted input.
7. Preserve branch/rollback points before material edits.
8. For UI work, require real-browser mobile/tablet/desktop verification.
9. For localization, verify actual locale routes, translated controls/forms and RTL behavior when relevant.
10. For media, preserve originals/provenance and verify layout/crop/logo/text fidelity after optimization.
11. For PWA, verify update strategy, cache invalidation, offline fallback and installability without trapping stale critical content.
12. For security, use least privilege, secret-safe logs and current rules/signatures; security scans complement manual review.
13. Finish with the existing Ercan OS completion state: VERIFIED, PARTIAL, BLOCKED or NOT VERIFIED.

## Default production gate

For material web changes, select the relevant subset of:
`lint/static validation -> typecheck -> build -> unit/integration -> browser E2E -> accessibility -> localization -> links/indexability -> performance -> security -> visual comparison -> preview/staging -> post-deploy smoke -> rollback evidence`.

Do not claim a capability engine ran unless it actually ran. Do not install or execute upstream repositories globally merely because they are listed here.
