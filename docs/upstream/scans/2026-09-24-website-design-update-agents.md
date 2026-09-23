# Upstream Scan — Website Design & Update Agents

Date: 2026-09-24

## Goal

Identify current tools/agent patterns that materially improve website design, redesign and ongoing update workflows without duplicating existing Ercan OS web specialists.

## Official/high-authority findings

### GoogleChrome/modern-web-guidance
Current official Google Chrome project, supported by Chrome/Edge/community.
Purpose:
- inject current web-platform guidance into coding agents;
- reduce legacy/ad-hoc JS patterns;
- cover modern CSS/layout, UI/forms, accessibility, performance and browser APIs;
- local semantic search/retrieval workflow.

License: Apache-2.0.
Status: preview.
Telemetry: anonymous install/retrieval/search usage is documented; opt-out supported.

Decision:
`ADOPT_WHEN_NEEDED / OFFICIAL_GUIDANCE`.

### ChromeDevTools/chrome-devtools-mcp
Current official Chrome DevTools for agents.
Capabilities:
- live Chrome automation;
- network/console inspection;
- screenshots;
- performance traces/insights;
- CLI and MCP;
- source/runtime debugging.

License: Apache-2.0.

Decision:
`ADOPT_WHEN_NEEDED / RUNTIME_INSPECTION`.

Security:
browser-visible data is exposed to the agent; use dedicated/scoped sessions and workspace filesystem bounds.

### Microsoft Playwright Test Agents
Current official Playwright docs expose:
- planner;
- generator;
- healer.

Decision:
`ADOPT / TEST_AGENT_PATTERN`.

Strong fit for release regression, but Ercan OS retains independent expected-behavior authority.

### Google Search Central site moves
Current official guidance requires:
- prepare/test new site;
- map old URLs;
- permanent redirects for permanent moves;
- update canonicals/hreflang/internal links;
- submit/monitor sitemaps/Search Console;
- monitor analytics;
- avoid unnecessary compounded migration changes.

Decision:
`AUTHORITATIVE_MIGRATION_REFERENCE`.

### W3C
Current production reference:
- WCAG 2.2 Recommendation;
- WCAG-EM 2.0 evaluation methodology.

WCAG 3 is currently a Working Draft.

Decision:
production accessibility claims remain on WCAG 2.2/current applicable standards.

## Community/open-source findings

### aidenybai/react-grab
Current project maps selected React UI elements to source/component stack and supports agent/browser workflows.

License: MIT.

Decision:
`ADOPT_WHEN_NEEDED / LIVE_UI_CONTEXT`.

### SandeepBaskaran/design-mode
Current browser visual editor with tracked changes and cloud/local/self-hosted MCP modes.

License: MIT.

Decision:
`ADOPT_WHEN_NEEDED / LIVE_UI_FEEDBACK`.

Cloud relay requires privacy review for sensitive projects.

### onlook-dev/onlook
Already reviewed by Ercan OS.
Current open-source visual-first editor supports DOM/code roundtrip, checkpoints and browser-based visual editing.

License: Apache-2.0.

Decision remains:
`ADOPT_PATTERN_ONLY`.

### stagewise-io/stagewise
Current agentic IDE/browser-context product.

License: AGPLv3.

Decision:
`ADOPT_PATTERN_ONLY` unless exact product/deployment license fit is separately approved.

### iklymchuk/autonomous-qa-agent
Interesting pattern: BFS crawl, AI flow inference, Playwright execution, axe, screenshots/diffs and severity reporting.

No root LICENSE was observed in this review.

Decision:
`PATTERN_ONLY / DO_NOT_COPY`.
Official Playwright agents are preferred where they cover the requirement.

## Architecture decision

Create one JIT `website-lifecycle-agent-pack` with six user-facing roles:
- @WebsiteRefreshArchitect
- @LiveUIContextAgent
- @ModernWebRefactorAgent
- @RuntimeInspectorAgent
- @MigrationGuardian
- @ReleaseGuardian

Map them onto existing stable web/SEO/platform specialists.

No stable identity count change.
