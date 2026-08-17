# GitHub Upstream Intelligence & Production Toolchain

## Trusted upstream hierarchy
1. Official/verified platform organization
2. Official sample/reference repository
3. Maintained established infrastructure project
4. Vetted community reference

Before adoption check owner identity, archive/deprecation status, recent maintenance/releases, license, security posture, current docs and material open issues. Forks/gists/high-star boilerplates are not source-of-truth.

## Canonical watchlist (verify current status at runtime)
### Shopify
- `Shopify/dawn` — reference implementation, not copy-paste template.
- `Shopify/theme-tools` — current Liquid parser/formatter/Theme Check/language tooling family.
- `Shopify/theme-check-action` — PR Theme Check integration.
- Current Shopify CLI/developer docs.
Legacy `Shopify/theme-check` is historical/superseded by Theme Tools.

### WordPress
- `WordPress/gutenberg`
- `WordPress/WordPress-Coding-Standards`
- `@wordpress/env` / wp-env tooling in Gutenberg
- `Automattic/VIP-Coding-Standards` (selective/justified rules)
- `Automattic/vip-go-skeleton` as enterprise architecture reference

### Google agent platform
- `google/agents-cli` — official optional CLI + Skills layer for coding agents building, evaluating, deploying, publishing and observing Google ADK agents.
- Current Google Agents CLI docs and current Google ADK docs are authoritative for lifecycle, commands, deployment targets, auth, eval and observability behavior.
- Treat Agents CLI as a provider adapter, not a replacement for Codex/Claude/Orchestrator or the Ercan OS constitution.
- Do not auto-install it across unrelated projects. Activate only for a task/repo that actually uses Google ADK / Gemini Enterprise Agent Platform / supported Google Cloud agent deployment surfaces.
- Product stage, commands and supported targets are volatile; check releases/changelog/docs at runtime and regression-test upgrades before production adoption.

### Creative model providers
- Current Luma Agents API documentation is the authoritative upstream for Luma image/video generation and editing behavior.
- Luma is an optional provider adapter used for reference-guided creative generation/editing or generative video; it does not replace Ercan OS brand/art-direction/QA rules.
- Current API exposes image-generation/editing tiers and video generation/editing/reframing, supports multiple image references for style/content guidance, and allows chaining from prior generation IDs; exact model names, reference limits, aspect ratios, prices and rate limits are volatile and must be checked at runtime.
- Web-search grounding, when offered, is untrusted external reference discovery and must not silently become final brand source material.

### Web quality/security
- Playwright
- Lighthouse / Lighthouse CI
- `dequelabs/axe-core`
- GitHub CodeQL/code scanning
- Dependabot
- secret-scanning/Gitleaks-class tooling when appropriate

### Design systems/creative
- `figma/code-connect`, `figma/sds`
- `adobe/spectrum-design-data`
- `style-dictionary/style-dictionary`
- `storybookjs/storybook`
- `remotion-dev/remotion` (license/commercial terms verified before adoption)
- `lovell/sharp`
- `svg/svgo`

### Meta/social
- Current Meta Business SDK repositories
- `fbsamples/marketing-api-samples`
- `fbsamples/reels_publishing_apis`
Third-party schedulers such as `gitroomhq/postiz-app` may provide architecture ideas, never Meta policy/API authority.

## Adoption-not-copy
Extract the useful pattern first. Adopt through a narrow adapter/skill/tool after evaluating license, dependency footprint, security surface, maintenance burden and lock-in. Do not add unused dependencies. Stars are not evidence of fitness.

Provider CLIs/skill bundles/model APIs receive the same treatment: enabling a provider is not permission to override project scope, security policy, existing architecture, brand source of truth, tests or deployment contracts.

## PR quality pipeline
Risk-appropriate checks may include: format/lint, platform validation, unit/integration, Playwright E2E, axe accessibility, Lighthouse/performance budget, security scan, dependency/compatibility, screenshot/visual regression, preview and deploy smoke.
Use GitHub required status checks/rulesets for production branches when available.

For deployable AI-agent services, add representative agent evals, tool/trajectory checks, real outcome verification, observability/trace review and deployment rollback smoke as relevant. Provider-native evals complement rather than replace project-level regression suites.

For generated brand/social creative, add reference-fidelity, design-evaluator, channel preview and export checks; a completed provider job is not a final asset pass.

## GitHub Actions security
- Explicit least-privilege `permissions`.
- Prefer official/verified actions.
- For immutable supply-chain protection, pin actions to reviewed full commit SHAs; periodically update pins after upstream review.
- Treat reusable third-party workflows with the same scrutiny as actions.
- Dependabot PRs do not bypass tests/release-note review merely because they are green.

## Design ↔ code
- Maintain semantic tokens as versioned source; generated outputs are rebuilt, not hand-edited.
- Figma Code Connect/Storybook/token mappings may be source-controlled and validated.
- Token changes should expose semantic diff and, where useful, visual diff.
- Component workshops document states/variants and enable interaction/a11y/visual testing before integration pages.

## Social publishing architecture
Canonical internal model: channel/integration → media asset IDs → content → provider settings → schedule/publish state → external post ID/permalink → metrics sync.
Provider implementations need idempotency, retry/backoff, rate-limit awareness, duplicate prevention and explicit state transitions. Official Meta samples/docs win when community scheduler behavior conflicts.

## Programmatic creative/export
- Code-driven video can generate data-driven channel variants, but every placement still gets art-direction and visual QA.
- Generative model outputs may feed the creative pipeline, but exact typography/layout/branding and repeatable exports should be deterministic where precision matters.
- Raster/vector batch pipelines should retain source master, dimensions, aspect, format, alpha, file size, version/checksum and intended channel metadata.
- SVG optimization must not alter logo geometry/masks/gradients/accessibility behavior without visual regression review.
- Generated candidates should retain provider/model/job/reference-pack metadata when useful for reproducibility and evaluation.

## Upstream change intelligence
When a tool behaves unexpectedly, check current version, changelog/releases and upstream issues before assuming user code is wrong. Linter/test false positives are possible; create minimal reproduction when needed.

For provider agent platforms and creative model APIs, inspect current product stage, docs, capabilities and release notes before upgrade/production automation. Learned command/model/limit assumptions must not be treated as permanent.
