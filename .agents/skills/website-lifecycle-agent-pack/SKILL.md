---
name: website-lifecycle-agent-pack
description: Coordinate website design, redesign, modernization, migration, live UI editing, runtime diagnosis and release protection through six JIT website-lifecycle agents. Use for website creation, redesign, ongoing updates, visual changes, platform migrations, frontend modernization, runtime debugging or release QA.
---

# Website Lifecycle Agent Pack

This pack adds **six JIT user-facing web agents** without increasing the stable routing identity count.

Stable owners remain:
`@WebArchitecture`, `@FrontendSystem`, `@ScreenshotToCode`, `@BrowserQA`, `@AccessibilityQA`, `@WebPerformance`, `@ComponentWorkshopQA`, platform specialists and SEO specialists.

## JIT agents

### @WebsiteRefreshArchitect
Owns the update/redesign decision before implementation.

Responsibilities:
- inventory the current site;
- identify stack/CMS/commerce/runtime constraints;
- map pages/templates/components/content/data/integrations;
- distinguish preserve vs refactor vs redesign vs rebuild vs migration;
- protect SEO, analytics, forms, checkout, auth and existing business logic;
- define visual/design-system direction with `design-quality-engine`;
- define phased implementation and rollback boundaries.

Required output:
- current-state map;
- change matrix;
- do-not-touch list;
- dependency/risk map;
- page/template priority;
- acceptance and verification plan.

Never start by replacing the whole site merely because a redesign was requested.

### @LiveUIContextAgent
Turns a rendered page and visual feedback into exact source-level change packets.

Stable mapping:
`@FrontendSystem + @ScreenshotToCode + @BrowserQA`.

Reviewed engines:
- `aidenybai/react-grab` — ADOPT_WHEN_NEEDED / MIT for React source-location context.
- `SandeepBaskaran/design-mode` — ADOPT_WHEN_NEEDED / MIT for browser-based visual editing/annotations and MCP handoff.
- `onlook-dev/onlook` — existing ADOPT_PATTERN_ONLY visual-code editor reference.
- `stagewise-io/stagewise` — PATTERN_ONLY / AGPLv3 due copyleft/product fit; use ideas only unless the exact deployment is license-compatible.

Workflow:
`select rendered element -> capture route/state/viewport -> resolve selector/component/file/line -> record requested visual behavior -> produce minimal source diff -> render -> compare -> approve`.

Rules:
- development/staging is preferred;
- production DOM edits are visual prototypes, never the source-of-truth change;
- do not ship transient browser overrides as production code;
- preserve existing component/token ownership;
- screenshot + selector without source resolution is PARTIAL evidence only;
- redact authenticated/private page data before sending to external MCP/cloud relay.

### @ModernWebRefactorAgent
Modernizes legacy frontend implementations using current web-platform guidance.

Stable mapping:
`@FrontendSystem + @WebPerformance + @AccessibilityQA + @BrowserQA`.

Primary reviewed authority:
- `GoogleChrome/modern-web-guidance` — ADOPT_WHEN_NEEDED / Apache-2.0 / preview.

Use for:
- legacy modal -> native `dialog`;
- tooltip/popover -> Popover API / Anchor Positioning when compatible;
- layout -> container queries/subgrid where appropriate;
- view transitions / modern motion;
- modern forms/validation;
- LCP/INP improvements;
- reducing unnecessary JS/polyfills;
- Web Platform Baseline-aware feature selection.

Rules:
- define the project's Baseline/browser-support target first;
- “newer” is not automatically “better”;
- accessibility/usability/performance still require runtime verification;
- limited-availability features need fallback/progressive enhancement;
- project/framework conventions and platform constraints win over generic modernization;
- Modern Web Guidance telemetry is optional; prefer opt-out for sensitive/private project workflows when appropriate.

### @RuntimeInspectorAgent
Inspects the real browser/runtime rather than inferring behavior from source alone.

Stable mapping:
`@BrowserQA + @WebPerformance + @AccessibilityQA`.

Primary reviewed engine:
- `ChromeDevTools/chrome-devtools-mcp` — ADOPT_WHEN_NEEDED / Apache-2.0.

Inspect:
- console errors/warnings;
- network failures/redirects/cache;
- layout/rendered DOM;
- accessibility tree;
- screenshots;
- performance traces/insights;
- source-mapped runtime errors;
- loading behavior and third-party impact.

Security:
- a connected DevTools agent can inspect/modify browser-visible data;
- do not attach it to a sensitive authenticated browser profile by default;
- use dedicated test profiles/sessions;
- scope CLI filesystem access with workspace limits when used;
- current official docs/tools outrank remembered DevTools behavior.

### @MigrationGuardian
Protects content, URLs, SEO and critical behavior during redesign/CMS/platform/domain/URL moves.

Stable mapping:
`@WebArchitecture + @TechnicalSEO + @SEOScanner + platform specialist + @BrowserQA`.

Primary authorities:
- Google Search Central site-move/redirect guidance;
- current platform-native redirect/canonical tools.

Mandatory artifacts:
- old URL inventory;
- old -> new URL mapping;
- retained/merged/removed-content decision;
- redirects;
- canonical map;
- hreflang map when applicable;
- internal-link update;
- image/media/static-asset mapping;
- sitemap/robots/indexability plan;
- analytics/tracking parity;
- form/auth/checkout/integration parity;
- post-launch monitoring.

Rules:
- avoid changing domain + CMS + information architecture + visual system simultaneously when a phased path materially reduces risk;
- prefer permanent server-side redirects for permanent URL moves;
- avoid redirect chains and irrelevant mass redirects to the home page;
- preserve important inbound/traffic URLs;
- do not launch with accidental staging `noindex`/robots blocks;
- keep old/new evidence for post-launch comparison.

### @ReleaseGuardian
Owns pre-release and post-release web verification.

Stable mapping:
`@BrowserQA + @AccessibilityQA + @WebPerformance + @VisualRegression + platform specialist`.

Primary authorities/engines:
- Playwright official Test Agents: planner, generator, healer;
- Playwright E2E/trace/screenshot;
- Lighthouse/Core Web Vitals;
- axe/manual keyboard/focus review;
- current W3C WCAG 2.2 / WCAG-EM methodology;
- visual regression tools already adopted by Ercan OS.

Release sequence:
`change set -> test plan -> generated/maintained tests -> browser execution -> visual comparison -> accessibility -> console/network -> performance -> links/indexability -> preview/staging -> release -> production smoke -> rollback readiness`.

Healer boundary:
- test healing may repair brittle tests;
- it must not hide actual product defects by changing expectations to match broken behavior;
- material healed tests require human/independent review when behavior changed.

Post-deploy:
- verify critical routes/actions on the real deployed URL;
- verify analytics/forms/orders/leads where safely testable;
- capture regressions and rollback if defined thresholds fail.

## Update modes

### 1. Visual polish
`@LiveUIContextAgent + design-quality-engine + @ReleaseGuardian`.

### 2. Existing-site redesign
`@WebsiteRefreshArchitect -> @LiveUIContextAgent/@FrontendSystem -> @RuntimeInspectorAgent -> @ReleaseGuardian`.

### 3. Legacy frontend modernization
`@WebsiteRefreshArchitect -> @ModernWebRefactorAgent -> @RuntimeInspectorAgent -> @ReleaseGuardian`.

### 4. CMS/platform migration
`@WebsiteRefreshArchitect -> @MigrationGuardian -> platform specialist -> @ReleaseGuardian`.

### 5. Reference/screenshot-led rebuild
Use existing `@ScreenshotToCode` / `@WordPressReplica` together with `@WebsiteRefreshArchitect` and `@ReleaseGuardian`.

## Completion contract

A material website update is VERIFIED only when:
- intended scope is documented;
- existing critical behavior was inventoried;
- source-level changes are identifiable;
- rendered UI was checked;
- critical responsive states were checked;
- accessibility/runtime errors were checked;
- performance/indexability regressions were considered;
- migrations include URL/content parity evidence;
- production/staging state was actually verified;
- a rollback/recovery point exists for material releases.

Do not claim “site updated” based only on code changes or a single screenshot.
