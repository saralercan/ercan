# Upstream Intelligence Scan — 2026-08-30 third pass

Status: reviewed discovery record

Scope: current GitHub/open-source changes relevant to Ercan OS design↔code drift, browser/performance QA, MCP conformance, SEO/GEO agent workflows and visual regression. Discovery only; no community code was installed or executed.

## Promote / track

### `ChromeDevTools/chrome-devtools-mcp` — ADOPT_WHEN_NEEDED
Official Chrome DevTools MCP remains actively maintained. Version 1.7.0 (2026-08-10) added heap-snapshot object detail inspection, native-context summaries/filtering and richer telemetry including localhost/devtools state. This materially strengthens browser QA and performance/memory diagnosis beyond screenshot-only automation.

Use: JIT for difficult browser performance, memory, layout/runtime and DevTools-level debugging. It complements Playwright; it does not replace E2E/browser-flow verification.

Evidence: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/CHANGELOG.md

### `modelcontextprotocol/inspector` v2 — ADOPT_WHEN_NEEDED with version caution
Inspector v2 moved to a weekly release cadence in August 2026. 2.1.0 shipped August 5, with subsequent 2.2/2.3 work focused on stable TypeScript SDK 2.0, security, protocol/conformance and bug fixes. The v2 line is the current direction; v1 is deprecated except urgent security maintenance.

Use: canonical MCP server inspection/conformance tool when building or reviewing MCP servers. Pin/test the current stable version per project because August v2 releases also exposed container, header and transport bugs.

Evidence:
- https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/3174
- https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/3234
- https://github.com/modelcontextprotocol/inspector/issues/1988

### `mylesmetalab/storybook-design-sync` — ADOPT_PATTERN_ONLY / WATCHLIST
New Storybook 10 addon that compares Storybook implementation contracts against Figma design source and explicitly refuses ambiguous collection matches instead of guessing. Current August work gates Figma variable modes and shared/literal values and records collection ids to reduce false confidence.

Use: borrow its design-drift contract, id-based matching and refusal-on-ambiguity patterns for Ercan OS `design-system-bridge` / Figma↔code verification. Too young to make a default dependency.

Evidence: https://github.com/mylesmetalab/storybook-design-sync

### `mjbeswick/storybook-visual-regression` — WATCHLIST / ADOPT_WHEN_NEEDED
Self-contained Storybook visual-regression CLI/addon using Playwright, side-by-side diffs, CI support and Docker-based rendering consistency. Useful where a project needs self-hosted Storybook VRT without external SaaS.

Use: optional project-scoped visual regression candidate. Existing Playwright + Ercan OS `visual-qa-evidence` remains the default baseline until this tool demonstrates stronger maintenance/adoption.

Evidence: https://github.com/mjbeswick/storybook-visual-regression

### `AgriciDaniel/claude-seo` — ADOPT_PATTERN_ONLY
Active SEO agent/skill system with 25 sub-skills, 18 specialist agents and extensive regression/security coverage. August v2.2.5 strengthened JSON-LD, rendered-page accessibility analysis, managed-runtime references and current Google/Lighthouse guidance. Notable patterns include primary-source grounding, explicit failure tests, SSRF/DNS-rebinding defenses and command/reference consistency gates.

Use: borrow security, evidence and regression patterns into Ercan OS SEO/AI-discovery QA. Do not treat its internal scores or parallel-agent count as search-engine authority; Google/OpenAI/Schema.org primary guidance remains authoritative.

Evidence: https://github.com/AgriciDaniel/claude-seo

### `g-shevchenko/geo-audit` — WATCHLIST / ADOPT_PATTERN_ONLY
Open-source GEO audit toolkit with explicit methodology/module docs, TRUST and SECURITY manifests, CI/GitHub Action support and August multi-language reporting. Its roadmap includes citability, schema, crawl-lite, brand-mention and provider checks.

Use: pattern/reference for transparent GEO scoring, report schemas, trust manifests and CI packaging. Do not promote its scores to authoritative ranking/citation truth.

Evidence: https://github.com/g-shevchenko/geo-audit

### `mcpbeat/best-mcp-servers` — DISCOVERY_SOURCE / WATCHLIST
Nightly-ranked MCP directory using measured uptime and install signals. It can surface fast-rising server candidates (for example Figma context, Hostinger API, Nx, ComfyUI and code-exploration MCPs), but ranking signals are not trust or security approval.

Use: discovery index only. Every candidate still requires canonicality, permission, credential, maintenance and security review.

Evidence: https://github.com/mcpbeat/best-mcp-servers

### `rlespinasse/agent-skills` — WATCHLIST / DISCOVERY_SOURCE
Actively released Agent Skills repository with August 2026 releases. Useful as an additional skill-discovery source, not as a trusted bundle to install wholesale.

Evidence: https://github.com/rlespinasse/agent-skills/releases

## Status / caution notes

### Storybook 10.5.x — STATUS CAUTION
August 2026 reports identified serious HMR regressions on large repositories around 10.5.5. Do not auto-upgrade Storybook in large design-system repos without local HMR/build regression checks.

Evidence: https://github.com/storybookjs/storybook/issues/35810

### HashiCorp Design System — ACTIVE REFERENCE
The HDS Figma component changelog remained active in August 2026, including fixes for icon color persistence and FilterBar wrapping. Existing mature-design-system pattern adoption remains valid; no new dependency action required.

Evidence: https://github.com/hashicorp/design-system/blob/main/packages/components/CHANGELOG-FIGMA-COMPONENTS.md

## Rejected / not promoted

- `vlm-diff` — REJECT_FOR_NOW / RESEARCH_ONLY: interesting DOM+VLM visual-regression prototype, but effectively zero adoption evidence and research-prototype status; current deterministic pixel/DOM/browser evidence remains stronger.
- proprietary or zero-adoption Figma/Storybook sample repos — REJECT as upstream dependencies; they add no advantage over canonical Figma/Storybook/Style Dictionary patterns.
- generic vibe-coding mega-lists promising free keys/credits — DISCOVERY_ONLY at most; volatile pricing/model claims and credential incentives are not suitable as trust sources.
- duplicate SEO/GEO skill packs that merely mirror the same checklist without stronger provenance, tests or security posture — REJECT_DUPLICATE.

## Routing implications

- difficult browser performance/memory bug → consider Chrome DevTools MCP in addition to Playwright.
- MCP server implementation/review → use current Inspector v2 with project-pinned stable version and conformance checks.
- Figma/Storybook drift → use id-based, refusal-on-ambiguity contract patterns; consider storybook-design-sync only after project audit.
- self-hosted Storybook VRT need → evaluate storybook-visual-regression against existing Playwright visual QA.
- SEO/GEO agent improvement → borrow primary-source, SSRF, regression and transparent-score patterns; never substitute community scoring for platform authority.
- MCP capability discovery → mcpbeat may generate candidates, but cannot approve them.

## Final decisions

- ADOPT_WHEN_NEEDED: `ChromeDevTools/chrome-devtools-mcp`, current `modelcontextprotocol/inspector` v2.
- ADOPT_PATTERN_ONLY: `mylesmetalab/storybook-design-sync`, `AgriciDaniel/claude-seo`, `g-shevchenko/geo-audit`.
- WATCHLIST: `mjbeswick/storybook-visual-regression`, `rlespinasse/agent-skills`.
- DISCOVERY_SOURCE: `mcpbeat/best-mcp-servers`.
- STATUS CAUTION: Storybook 10.5.x upgrades on large repos require regression verification.
