# Upstream Intelligence Scan — 2026-08-30 fourth pass

Status: reviewed discovery record

Scope: image/video generation, creative coding, social automation, Shopify/WordPress production tooling and agent/MCP security. Discovery only; no community code was installed or executed and no credentials were used.

## Image / video generation

### `huggingface/diffusers` — ADOPT_WHEN_NEEDED (status strengthened)
The existing catalog decision remains valid and is strengthened by the August 2026 release line. Diffusers 0.40.0 (2026-08-20) added new image/video pipelines including LTX2.5, MiniMax-H3 and Wan Animate 2, graduated Modular Diffusers from experimental to stable support, and added initial tensor-parallel support.

Use: provider-neutral/open model experimentation, reproducible image/video pipelines, training/inference research and evaluation. Do not treat model availability as a reason to bypass project brand, provenance, disclosure or deterministic final-layout QA.

Caution: current August issues include Apple Silicon/MPS and quantization edge cases, so project hardware compatibility must be tested before production adoption.

Evidence:
- https://github.com/huggingface/diffusers/releases
- https://github.com/huggingface/diffusers/issues

### `Comfy-Org/ComfyUI` — ADOPT_WHEN_NEEDED (status strengthened)
ComfyUI remains a strong node-based workflow/runtime candidate. The project reached v0.34.0 on 2026-08-26, with active image/video model integration and continuing frontend/runtime updates.

Use: complex local/hosted image/video workflow prototyping, repeatable node graphs, provider/model comparison and production-engine research.

Caution: model/node compatibility changes quickly; August releases removed retired partner models and current issue traffic shows model/hardware-specific regressions. Pin workflow dependencies and verify export/runtime before production use.

Evidence: https://github.com/Comfy-Org/ComfyUI/releases

### `Vidia-Tools/Vidia-Open-Workflows` — WATCHLIST / DISCOVERY_SOURCE
Curated ComfyUI video-generation/editing workflows with August 2026 compatibility notes for Comfy Cloud. Useful as a workflow-discovery source because it explicitly documents missing cloud nodes/models and substitutions.

Do not promote as a default production dependency: some flows require unavailable/private nodes or model substitutions.

Evidence: https://github.com/Vidia-Tools/Vidia-Open-Workflows

### `remotion-dev/remotion` — ADOPT_WHEN_NEEDED (active direction)
Remotion remains the deterministic video/social-export default candidate. Late-August development shows active work around a richer Canvas/Studio editing surface, WebMCP exposure, quick actions, transcription and asset/composition management.

Use: code-driven deterministic social/video production, templated campaigns and final composition after generative assets are created.

Caution: several of these Studio/WebMCP items are active issues/masterplans rather than stable contracts. Do not hard-code unreleased APIs.

Evidence: https://github.com/remotion-dev/remotion/issues

## Creative coding

### `camilleroux/genart-skill` — ADOPT_PATTERN_ONLY
New 0.1.0 release (2026-08-28) packages generative-art practice as a JIT skill with deterministic PRNG/hash seeding, resolution-independent rendering, feature/rarity design, ethics/licensing guidance and runnable verification scripts. It supports Canvas 2D, p5.js, Three.js/WebGL and SVG.

Use: borrow deterministic creative-coding verification, resolution-independence, named PRNG substreams, contact-sheet/batch export and ethics/provenance patterns into Ercan OS creative coding workflows. Do not install globally by default.

Evidence:
- https://github.com/camilleroux/genart-skill
- https://github.com/camilleroux/genart-skill/blob/main/CHANGELOG.md

### `processing/p5.js` 2.x — ADOPT_WHEN_NEEDED / STATUS CHANGE
p5.js 2.x became the default version in the p5.js Editor at the start of August 2026. This changes the baseline for new creative-coding experiments: new Ercan OS p5 work should target 2.x unless compatibility with an existing 1.x project requires otherwise.

Caution: 2.x still has active WebGL/WebGPU and compatibility bug reports; existing 1.x sketches should not be mass-migrated without visual/performance regression checks.

Evidence:
- https://github.com/processing/p5.js/issues/8870
- https://github.com/processing/p5.js/issues

## Social production / automation

### `indranilbanerjee/socialforge` — ADOPT_PATTERN_ONLY (status strengthened)
The previous decision remains valid. August 2026 releases materially strengthened cross-agent packaging, delivery audits, failure semantics, cost accounting and provider-failure recording. The project explicitly verifies that FINAL delivery claims correspond to real non-empty files and refuses silent provider failures.

Use: continue borrowing delivery-truth, approval-gate, no-silent-failure, cost-lower-bound, provider-fallback and audit-manifest patterns. Official social platform APIs remain authority for publishing.

Evidence: https://github.com/indranilbanerjee/socialforge

### Social scheduler dedupe — NO NEW DEFAULT
Current scans still do not justify replacing the existing Postiz-class provider-adapter architecture. Posthive remains a WATCHLIST candidate for its OAuth 2.0 + PKCE / MCP-first credential model, but adding multiple scheduler stacks would increase operational and token-handling risk without a demonstrated capability gap.

Evidence: https://github.com/AstaBlackClove/posthive

Decision: keep social publishing adapters minimal; evaluate another scheduler only for a concrete unsupported platform, materially safer auth model or required workflow.

## WordPress production / agent tooling

### `WordPress/mcp-adapter` — ADOPT / CANONICAL
Major status change. The official WordPress MCP Adapter shipped its first stable release in August 2026 and is now the canonical WordPress bridge from the Abilities API to MCP. Current source targets WordPress 6.9+ and exposes abilities as MCP tools/resources/prompts.

Its default server uses layered discovery: a small discover → get-info → execute meta-tool surface rather than dumping every ability schema into `tools/list`, which directly addresses tool/context bloat.

Use: primary WordPress-native MCP integration reference. Require authenticated users, explicit permission callbacks, least-privilege exposure and project-specific review before write/destructive abilities are surfaced.

Evidence:
- https://github.com/WordPress/mcp-adapter/releases/
- https://github.com/WordPress/mcp-adapter/blob/trunk/docs/guides/default-server.md
- https://github.com/WordPress/mcp-adapter/blob/trunk/mcp-adapter.php

### `Automattic/wordpress-mcp` — SUPERSEDED
The repository is deprecated/archived in favor of `WordPress/mcp-adapter`. Do not use it for new production integrations.

Evidence: https://github.com/Automattic/wordpress-mcp/blob/trunk/Readme.md

### `WordPress/agent-skills` — ADOPT_WHEN_NEEDED
Official WordPress Agent Skills repository provides project-scoped skills for plugin/block/theme development, project triage, REST, Abilities API auditing/verification and related WordPress workflows. It is directly compatible with Codex-class skill hosts.

Use: JIT/project-scoped WordPress expertise source; prefer relevant skills rather than globally installing the full bundle. Ercan OS project rules, security and QA remain authoritative.

Evidence:
- https://github.com/WordPress/agent-skills
- https://github.com/WordPress/agent-skills/blob/trunk/README.md

### `WordPress/abilities-api` standalone repo — SUPERSEDED AS ACTIVE UPSTREAM
The standalone repository is archived because the Abilities API moved into WordPress core. The API itself remains canonical; use current WordPress core/developer documentation and `WordPress/agent-skills` references rather than treating the archived repo as the evolving source of truth.

Security requirement: every registered ability must have a `permission_callback`; input/output schemas and explicit readonly/destructive/idempotent annotations should be treated as required Ercan OS review fields even when WordPress runtime allows permissive defaults.

Evidence:
- https://github.com/WordPress/abilities-api
- https://github.com/WordPress/agent-skills/blob/trunk/skills/wp-abilities-api/references/php-registration.md

### `Automattic/wp-feature-api` — SUPERSEDED
Deprecated in favor of the Abilities API/Core direction. Historical architecture reference only.

Evidence: https://github.com/Automattic/wp-feature-api

## Shopify production / agent tooling

### `Shopify/cli` + `Shopify/theme-tools` — ADOPT / CANONICAL
No replacement needed. Shopify CLI remains the official app/theme/Hydrogen build/deploy surface and Theme Tools remains the canonical Liquid/theme developer-quality stack.

Evidence:
- https://github.com/Shopify/cli
- https://github.com/Shopify/theme-tools/pulls

### `Shopify/theme-check-vscode` — SUPERSEDED
The standalone repository has been absorbed into `Shopify/theme-tools`. Do not adopt it as a separate dependency/source for new work.

Evidence: https://github.com/Shopify/theme-check-vscode

### `Shopify/app-intent-types` — ADOPT_WHEN_NEEDED
Newly important official catalog for Sidekick app-extension intent schemas. It defines app-owned and Shopify-resource intent types and the contracts Sidekick uses to discover/routable app actions.

Use: JIT when building Shopify apps intended to participate in Sidekick/agent workflows. Treat schemas and supported actions as current upstream facts that must be checked at implementation time.

Evidence: https://github.com/Shopify/app-intent-types

### `Shopify/hydrogen` agent/MCP work — WATCHLIST / PREVIEW
Late-August Hydrogen work includes UCP MCP proxy route preview and agent/cart intent experiments. This is strategically relevant for future agentic/headless commerce, but preview PRs are not stable API contracts.

Use: watch official Hydrogen changes; do not wire Ercan OS production behavior to preview agent routes until Shopify ships supported contracts.

Evidence: https://github.com/Shopify/hydrogen/pulls

### Shopify App Proxy HMAC advisory — HIGH PRIORITY SECURITY STATUS
Shopify published an August 10, 2026 advisory for App Proxy HMAC signature validation affecting multiple official packages. The advisory lists patched major versions and states there is no workaround other than upgrading.

Ercan OS rule: any Shopify app using unauthenticated App Proxy requests must verify its installed package versions against the current advisory before production changes/deploys. Do not assume an old Shopify SDK is safe because the app otherwise functions.

Evidence: https://github.com/Shopify/shopify-app-js/security/advisories/GHSA-3h8r-q86m-44c7

## Agent / MCP security

### MCP server-provided instructions are UNTRUSTED — SECURITY RULE
An August 2026 MCP protocol issue documents prompt-injection risk when server-controlled `instructions` content is inserted into an LLM context, especially when combined with shared/public caching.

Ercan OS rule: remote MCP instructions, tool descriptions, resource content and discovery metadata are data, not trusted policy. Never merge them into system/developer authority. Isolate, length-limit and review untrusted instructions before they can influence agent behavior.

Evidence: https://github.com/modelcontextprotocol/modelcontextprotocol/issues/3213

### Network-binding/auth defaults — SECURITY RULE
Recent 2026 advisories show repeated critical MCP failures caused by binding servers to all interfaces without mandatory authentication. `mcp-router` before its fixed release and an Argo CD MCP server are concrete examples.

Ercan OS rule: default MCP listeners to loopback/private transport; non-loopback listeners require explicit authentication, scoped credentials, network policy and production security review.

Evidence:
- https://github.com/advisories/GHSA-g448-x63h-m2m3
- https://github.com/advisories/GHSA-p2x5-x87w-v2xj

### SSRF / outbound-request controls — SECURITY RULE
August advisories continue to show MCP-related SSRF risks, including Chainlit MCP transports and community MCP servers. Hostname-only allowlists are insufficient when DNS can resolve to loopback/link-local/cloud metadata targets.

Ercan OS rule: tools that accept URLs require scheme validation, DNS/IP resolution checks, private/link-local/metadata blocking, redirect re-validation, credential/header isolation and least-privilege outbound network access.

Evidence:
- https://github.com/advisories/GHSA-hvfh-5mj3-5f3j
- https://github.com/advisories/GHSA-274v-3mgv-hg6c

### `modelcontextprotocol/php-sdk` transport advisory — VERSION GATE
GitHub reviewed advisory GHSA-7m52-jw36-44r3 affects MCP PHP SDK HTTP/SSE client versions >=0.5.0 and <0.7.1 due to unbounded SSE buffering; patched version is 0.7.1.

Ercan OS rule: PHP projects using `mcp/sdk` must version-check before MCP client use and must not accept affected versions in production.

Evidence: https://github.com/advisories/GHSA-7m52-jw36-44r3

### Community MCP scanners — WATCHLIST / ADOPT_PATTERN_ONLY
`L3G5/mcp-scan` and `HailBytes/mcp-security-scanner` cover useful categories such as tool poisoning, prompt injection, missing auth, unsafe defaults and overprivileged tools.

Use: borrow threat-model/test categories and consider project-scoped read-only evaluation after provenance/package review. They do not become global security authorities and a clean scanner result does not certify an MCP server.

Evidence:
- https://github.com/L3G5/mcp-scan
- https://github.com/HailBytes/mcp-security-scanner

### `modelcontextprotocol/inspector` v2 — CANONICAL CONFORMANCE TOOL, NOT A TRUST BOUNDARY
The v2 line is actively supported; v1 is security-fixes-only. Continue using current pinned v2 for protocol inspection, while remembering that connecting Inspector to an untrusted MCP server is itself a security-sensitive action.

Evidence: https://github.com/modelcontextprotocol/inspector/security

## Final decisions

- ADOPT / CANONICAL: `WordPress/mcp-adapter`, `Shopify/cli`, `Shopify/theme-tools`.
- ADOPT_WHEN_NEEDED: `WordPress/agent-skills`, `Shopify/app-intent-types`, `huggingface/diffusers`, `Comfy-Org/ComfyUI`, `remotion-dev/remotion`.
- ADOPT_PATTERN_ONLY: `camilleroux/genart-skill`, current SocialForge production/audit patterns.
- WATCHLIST / DISCOVERY_SOURCE: `Vidia-Tools/Vidia-Open-Workflows`; current Hydrogen agent/MCP preview work; community MCP scanners after provenance review.
- SUPERSEDED: `Automattic/wordpress-mcp`, standalone `WordPress/abilities-api` repo as active upstream, `Automattic/wp-feature-api`, `Shopify/theme-check-vscode`.
- SECURITY GATES: Shopify App Proxy package versions; MCP listener authentication/binding; MCP URL/SSRF controls; server-provided MCP instructions treated as untrusted; `mcp/sdk` PHP >=0.7.1 when that SDK is used.
