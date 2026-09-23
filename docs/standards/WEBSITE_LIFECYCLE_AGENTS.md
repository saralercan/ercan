# Ercan OS — Website Lifecycle Agents

Status: active
Date: 2026-09-24

## Purpose

Create a dedicated lifecycle layer for designing, redesigning and continuously updating websites while preserving business behavior, source ownership, accessibility, search visibility and release quality.

Execution skill:
`.agents/skills/website-lifecycle-agent-pack/SKILL.md`.

Stable routing identities remain **52**.

## JIT user-facing agents

| Agent | Role | Stable owners |
|---|---|---|
| `@WebsiteRefreshArchitect` | current-site audit, update/redesign architecture, scope/risk/rollback | WebArchitecture + FrontendSystem |
| `@LiveUIContextAgent` | rendered element/visual feedback -> exact source context/change packet | FrontendSystem + ScreenshotToCode + BrowserQA |
| `@ModernWebRefactorAgent` | modern HTML/CSS/JS/browser API modernization | FrontendSystem + WebPerformance + AccessibilityQA |
| `@RuntimeInspectorAgent` | console/network/performance/accessibility/runtime diagnosis | BrowserQA + WebPerformance + AccessibilityQA |
| `@MigrationGuardian` | URL/content/SEO/integration parity through moves/redesigns | WebArchitecture + TechnicalSEO + platform specialist |
| `@ReleaseGuardian` | test planning, browser/visual/a11y/perf/post-deploy protection | BrowserQA + AccessibilityQA + WebPerformance + VisualRegression |

These are routing aliases/capability roles, not new stable identities.

## Internet research conclusions

### Modern Web Guidance
Google Chrome's current Modern Web Guidance project supplies agent-oriented, token-efficient guidance for current web APIs, performance, accessibility, CSS/layout, forms and responsible fallbacks.

Decision:
`ADOPT_WHEN_NEEDED / OFFICIAL_GUIDANCE / Apache-2.0 / preview`.

It improves implementation currency but does not replace real browser or accessibility testing.

### Chrome DevTools for agents
Current official Chrome DevTools for agents exposes live browser inspection/control through MCP/CLI, including network, console, screenshots and performance traces.

Decision:
`ADOPT_WHEN_NEEDED / RUNTIME_INSPECTION / Apache-2.0`.

Security note: a connected agent can see browser content and effectively act through the browser. Dedicated test sessions are preferred.

### React Grab
Current `aidenybai/react-grab` maps a selected React UI element to its component stack/source location and can provide browser MCP access.

Decision:
`ADOPT_WHEN_NEEDED / LIVE_UI_CONTEXT / MIT`.

Use in development-compatible React projects; remove/disable production instrumentation unless explicitly intended.

### Design Mode
Current `SandeepBaskaran/design-mode` is an MIT Chrome/Firefox visual editor that tracks live page edits and can hand structured changes to coding agents through cloud/local/self-hosted MCP modes.

Decision:
`ADOPT_WHEN_NEEDED / LIVE_UI_FEEDBACK / MIT`.

Cloud relay mode is a data-boundary decision; prefer local/self-hosted for sensitive projects where practical.

### Onlook
Already present in Ercan OS as a visual editing reference.

Decision remains:
`ADOPT_PATTERN_ONLY`.

Use visual/code roundtrip ideas without making Onlook a global dependency.

### stagewise
Current canonical `stagewise-io/stagewise` is an agentic browser/IDE environment with AGPLv3 licensing.

Decision:
`ADOPT_PATTERN_ONLY / AGPLv3`.

Useful product/workflow reference for browser-context editing; do not copy/integrate code into incompatible proprietary distributions without license review.

### Playwright Test Agents
Current official Playwright includes:
- planner;
- generator;
- healer.

Decision:
`ADOPT / OFFICIAL_WEB_TEST_AGENT_PATTERN`.

The planner creates human-readable test plans, generator creates executable tests, and healer replays failures and proposes fixes. Ercan OS keeps independent acceptance rules so healed tests cannot redefine correct behavior.

### Google Search Central site moves
Current Google guidance emphasizes:
- test the new site;
- create old->new URL mapping;
- use permanent server-side redirects for permanent moves;
- update canonicals/hreflang/internal links/sitemaps;
- monitor Search Console and analytics;
- avoid combining multiple major migration changes when avoidable.

Decision:
`AUTHORITATIVE_MIGRATION_REFERENCE`.

### Accessibility
WCAG 2.2 remains the stable W3C Recommendation; WCAG-EM 2.0 is the current evaluation methodology note. WCAG 3 remains a working draft and does not replace the production conformance target.

## Website update lifecycle

`inventory -> classify update mode -> protect business/search contracts -> define design/modernization plan -> implement minimal source changes -> runtime inspect -> regression test -> staging -> release -> production smoke -> monitor`

## Update classification

### PATCH
Small isolated fix.
Examples: spacing, button alignment, typo, one responsive defect.

### REFRESH
Visual/system improvements without replacing core information architecture/business logic.

### REDESIGN
Material component/layout/interaction changes with retained product/content purpose.

### REBUILD
Substantial implementation replacement.

### MIGRATION
CMS/framework/domain/URL/content-model or hosting transition.

The chosen class determines test/migration depth.

## Source/runtime evidence

For material changes, evidence should include the relevant subset:
- source diff;
- route/component mapping;
- before/after screenshots;
- browser console/network evidence;
- accessibility tree/keyboard behavior;
- Playwright tests/traces;
- visual diff;
- performance trace/Lighthouse;
- URL/indexability/link checks;
- deployment URL;
- post-release smoke;
- rollback reference.

## Modern web rule

Set a browser-support/Baseline target at the project level.

Native browser features should be preferred when:
- they meet product requirements;
- target browser compatibility is acceptable;
- accessibility behavior is sound;
- they reduce unnecessary JS/dependencies.

Do not use limited-availability features without deliberate fallback/progressive enhancement.

## Release risk matrix

Low:
- isolated visual/content patch;
- no URL/data/auth/payment change.

Medium:
- shared component;
- major template;
- navigation;
- form behavior;
- localization;
- performance-critical asset.

High:
- domain/URL move;
- CMS migration;
- auth/account;
- checkout/order/payment;
- analytics/conversion tracking;
- robots/canonical/hreflang;
- broad design-system change;
- production data/integration changes.

High-risk changes require explicit staging/post-release evidence and rollback planning.

## Completion

`VERIFIED` means:
- the deployed/target runtime matches the intended update;
- critical behavior and visual states are checked;
- no unacknowledged high-severity regression remains.

A source commit alone is not completion.
