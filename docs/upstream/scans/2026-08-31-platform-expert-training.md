# Upstream Intelligence Scan — 2026-08-31 platform expert training

Status: reviewed discovery/adoption record

Scope: official GitHub and platform documentation suitable for training production-grade Shopify, WordPress and Wix specialist agents in Ercan OS. No third-party community code was installed or executed and no production credentials were used.

## Shopify

### `Shopify/Shopify-AI-Toolkit` — ADOPT_WHEN_NEEDED / CANONICAL AGENT TRAINING SOURCE
Official Shopify AI Toolkit provides platform skills, current documentation/schema search, GraphQL/Liquid/extension validation and Shopify CLI integration for AI coding tools. Its skill inventory spans onboarding, Admin API, Liquid, Functions, Hydrogen, customer/custom data, partner/app review/payments and Polaris/extension surfaces.

Decision: use as the primary JIT Shopify agent-training/reference source, not as a globally injected bundle. Ercan OS platform rules and independent QA remain authoritative.

Privacy note: upstream toolkit skills/hooks may report skill/model/client telemetry and, when supplied by the host, verbatim prompt/session identifiers. Inspect current telemetry and apply Ercan OS privacy/opt-out policy before execution. Never pass secrets or private customer data unnecessarily.

Evidence:
- https://github.com/Shopify/Shopify-AI-Toolkit
- https://shopify.dev/docs/apps/build/ai-toolkit

### Shopify Dev MCP — ADOPT_WHEN_NEEDED / CANONICAL DEVELOPER CONTEXT
Official local MCP surface for Shopify developer docs, API schemas and code validation. Use JIT when it materially improves implementation correctness. It does not replace store/runtime/browser QA.

Evidence: https://shopify.dev/docs/apps/build/ai-toolkit

### Shopify platform status rules
- GraphQL Admin API is the primary Admin API for new apps/integrations; REST Admin API is legacy.
- Theme Check is canonical Liquid/JSON static validation and includes performance/best-practice checks.
- Current Shopify agentic-commerce surfaces include managed `agents.md`, WebMCP and Storefront MCP; use only supported contracts and re-check current docs at runtime.

Evidence:
- https://shopify.dev/docs/api/admin-rest
- https://shopify.dev/docs/storefronts/themes/tools/theme-check
- https://shopify.dev/docs/api/web-mcp
- https://shopify.dev/docs/apps/build/storefront-mcp

## WordPress

### `WordPress/agent-skills` — ADOPT_WHEN_NEEDED / CANONICAL AGENT TRAINING SOURCE
Official WordPress organization repository for AI coding-assistant skills. It explicitly targets modern WordPress development and addresses common model failures such as outdated pre-Gutenberg patterns, missing security checks, bad block deprecations and ignoring existing repo tooling.

Current skill corpus covers routing/triage, block development, block themes, patterns, plugin development, REST, Interactivity API, Abilities API, Abilities audit/verification, WP-CLI/ops, performance, PHPStan, Playground, WPDS, plugin-directory guidance and Blueprints.

Decision: primary JIT WordPress expert curriculum/reference. Prefer relevant skills only; do not globally install the entire corpus by default.

Evidence:
- https://github.com/WordPress/agent-skills
- https://github.com/WordPress/agent-skills/tree/trunk/skills

### WordPress modern agent architecture — ADOPT / CANONICAL DIRECTION
Use current WordPress core/developer docs plus `WordPress/mcp-adapter` for Abilities API → MCP integration. Treat permissions, input/output schemas and action annotations as explicit review fields.

Evidence:
- https://github.com/WordPress/mcp-adapter
- https://developer.wordpress.org/

## Wix

### `wix/skills` — ADOPT_WHEN_NEEDED / OFFICIAL EXPERIMENTAL TRAINING SOURCE
Official Wix organization repository provides Agent Skills for Wix apps, auth, design system, docs lookup, headless, vibe/headless browser integrations, Wix business-solution management and replatforming. It includes Codex plugin support and is actively maintained.

The repository is explicitly marked EXPERIMENTAL. Decision: use as official JIT training/automation assistance, but verify output against current `dev.wix.com` docs and actual project behavior before production use. Do not treat skill instructions as immutable Wix API contracts.

Evidence:
- https://github.com/wix/skills
- https://github.com/wix/skills/tree/main/skills

### Unified Wix CLI — ADOPT / CANONICAL DIRECTION
The current Wix CLI is the unified path for creating/developing/deploying Wix apps and Wix-managed headless projects and replaces the deprecated Wix CLI for Apps for new work. Existing projects must be inspected to determine whether they are current or legacy before commands are chosen.

Current CLI app extensions include dashboard, backend and site extension families. Some extensions are not fully registered by preview alone and require a release/app version.

Evidence:
- https://dev.wix.com/docs/wix-cli
- https://dev.wix.com/docs/build-apps/develop-your-app/develop-an-app-with-the-cli/about-the-wix-cli
- https://dev.wix.com/docs/build-apps/develop-your-app/develop-an-app-with-the-cli/supported-extensions/about-extensions-in-the-wix-cli

### Wix development-path triage — ADOPT AS REQUIRED ROUTING STEP
Before implementation, classify ordinary site/Git-integrated site, Wix-managed app, self-managed app, Wix-managed headless, self-managed headless or migration/replatform task. Extension and hosting capabilities differ by path.

Evidence: https://dev.wix.com/docs/overview/platform-overview/development-paths

## Ercan OS changes justified by this scan

- add stable identities `@ShopifyExpert`, `@WordPressExpert`, `@WixExpert`;
- add shared `PLATFORM_EXPERT_TRAINING.md` curriculum;
- add `PLATFORM_EXPERT_CERTIFICATION.md` production evals;
- route Shopify/WordPress/Wix work through the matching expert rather than a generic platform engineer alone;
- use official platform skill corpora JIT and minimally;
- preserve privacy/security boundaries around external skill telemetry;
- require current official docs/schema/changelog verification at execution time;
- keep hosting/deployment specialists separate from CMS/platform expertise;
- do not run all three platform experts unless the task genuinely spans platforms.

## Final decisions

- `Shopify/Shopify-AI-Toolkit` — **ADOPT_WHEN_NEEDED / CANONICAL AGENT TRAINING SOURCE**.
- Shopify Dev MCP — **ADOPT_WHEN_NEEDED / CANONICAL DEVELOPER CONTEXT**.
- `WordPress/agent-skills` — **ADOPT_WHEN_NEEDED / CANONICAL AGENT TRAINING SOURCE**.
- `WordPress/mcp-adapter` — existing **ADOPT / CANONICAL** decision strengthened for expert curriculum.
- `wix/skills` — **ADOPT_WHEN_NEEDED / OFFICIAL EXPERIMENTAL TRAINING SOURCE**.
- unified Wix CLI/current development-path docs — **ADOPT / CANONICAL DIRECTION**.
- legacy Shopify REST Admin and legacy Wix CLI patterns — **LEGACY / COMPATIBILITY ONLY**, not default training targets.