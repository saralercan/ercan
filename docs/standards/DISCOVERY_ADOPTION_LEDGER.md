# Ercan OS — Discovery Adoption Ledger

Purpose: prevent duplicate research, hype-driven adoption and useful findings being stranded in chat. Every material repo/tool/pattern discovered through GitHub, social research or official docs should end in one of: `ADOPT`, `ADOPT_PATTERN_ONLY`, `WATCHLIST`, `REJECT`, or `SUPERSEDED`.

This ledger records the durable decision; runtime facts such as versions, prices, API limits and feature availability must still be re-verified from current upstream.

## Agent / prompt / harness engineering
- Claude/Codex prompt-engineering lessons: `ADOPT` → `AGENT_ENGINEERING.md` task spec, context-budget, examples, constraints, eval/harness-first rules.
- Open Agent Skills (`agentskills/agentskills`): `ADOPT_PATTERN_ONLY` → portable `.agents/skills/*/SKILL.md` structure and JIT/progressive disclosure.
- Google `agents-cli`: `ADOPT` as optional provider adapter → `GOOGLE_AGENT_PLATFORM.md`; not loaded for unrelated Shopify/WordPress/design tasks.
- Promptfoo-class eval/red-team workflow: `ADOPT_PATTERN_ONLY` → shared eval/regression discipline; exact tooling project-specific.
- Pascal Editor architecture review + design QA evidence: `ADOPT_PATTERN_ONLY` → `review-architecture` and `visual-qa-evidence` skills.
- Agent Reach-class multi-platform research adapters: `ADOPT_PATTERN_ONLY` → least-privilege provider/fallback architecture in `SOCIAL_RESEARCH.md`; broad authenticated bundle is not a default dependency.
- ChatGPT Work / Voice in Work-Codex / Sites-class product surfaces: `ADOPT_PATTERN_ONLY` as optional interaction/execution surfaces for orchestrating longer work and agent coordination; they are not a replacement for the Ercan OS repo constitution, skills, source-of-truth systems or QA. Availability/permissions are runtime product facts and must be checked from current official OpenAI docs.

## GitHub / production quality
- Shopify `theme-tools`, Dawn, Theme Check Action: `ADOPT` as canonical Shopify references.
- WordPress Gutenberg, WPCS, wp-env, selective VIP standards: `ADOPT` as canonical WordPress references.
- Playwright: `ADOPT` for browser/E2E QA.
- Lighthouse/LHCI: `ADOPT` for performance regression/budgets where useful.
- Deque `axe-core`: `ADOPT` for automated accessibility detection, paired with manual keyboard/focus/semantic QA.
- GitHub CodeQL, Dependabot, secret scanning/Gitleaks-class: `ADOPT` as risk-appropriate security baseline.
- Third-party GitHub Actions: `ADOPT_PATTERN_ONLY`; prefer trusted publishers and reviewed immutable pins.

## Design systems / design-to-code
- `abi/screenshot-to-code`: `ADOPT_PATTERN_ONLY` → `.agents/skills/screenshot-production-ui/SKILL.md` and the Screenshot → Production UI pod in `AGENT_REGISTRY.md`. Adopt screenshot/mockup/Figma/screen-recording → functional code, real-asset reuse and headless-browser self-check patterns; do not make Ercan OS dependent on its current model/provider list. At adoption review (2026-08-28) the repo was public, active, non-archived and MIT-licensed. Playwright/render evidence plus independent Ercan OS visual QA remains authoritative.
- `figma/sds`: `ADOPT_PATTERN_ONLY` → Variables + Styles + Components + Code Connect + codebase as one design-system bridge.
- Figma Code Connect: `ADOPT` when supported by current official integration path; runtime changelog verification required.
- `style-dictionary/style-dictionary`: `ADOPT_PATTERN_ONLY` → semantic token build/source lifecycle, generated outputs not hand-edited.
- Adobe Spectrum Design Data: `ADOPT_PATTERN_ONLY` → token schema/version/diff/deprecation/migration ideas.
- Storybook: `ADOPT` where component workshop/isolated states materially improve UI development and regression QA.

## Brand / graphics / Instagram / advertising
- Brand source-of-truth, semantic tokens, GOOD/BAD references, independent design evaluator: `ADOPT` → `BRAND_SOCIAL.md`.
- Meta/Instagram organic + paid separation, feed/Reels/Stories/carousel safe-zone and performance loop: `ADOPT` → `BRAND_SOCIAL.md`.
- Meta Business SDK and verified marketing/Reels samples: `ADOPT` as implementation references for Meta automation; current API/version/policy always wins.
- Postiz-class social scheduler: `ADOPT_PATTERN_ONLY` → provider adapter, schedule state, retry/idempotency architecture; never Meta authority.
- Remotion: `ADOPT WHEN NEEDED` for deterministic code-driven video; commercial/license terms verified at runtime.
- Sharp: `ADOPT WHEN NEEDED` for deterministic raster resize/crop/composite/export pipelines.
- SVGO: `ADOPT WHEN NEEDED` for SVG optimization with logo/mask/gradient/accessibility visual regression.
- Luma Uni / Agents API: `ADOPT` as optional creative provider → `LUMA_CREATIVE_PROVIDER.md`; not final art director or deterministic type/logo layer.

## SEO / entity / AI discovery
- Google Search Central AI/Search guidance: `ADOPT` as Google authority; no promises of rankings or recommendation placement.
- OpenAI crawler/publisher guidance: `ADOPT` for OAI-SearchBot eligibility/publisher behavior when desired.
- Schema.org: `ADOPT` as semantic vocabulary reference, constrained by visible truth and platform-supported rich-result requirements.
- Google Site Kit / Search Console integrations: `ADOPT WHEN NEEDED` for WordPress measurement, not ranking authority.
- Yoast SEO: `ADOPT_PATTERN_ONLY/WHEN NEEDED`; plugin score is not Google truth.
- `llms.txt` proposal: `WATCHLIST/OPTIONAL`; not treated as Google ranking factor.
- GEO research repos/community AI-SEO auditors: `WATCHLIST/ADOPT_PATTERN_ONLY`; hypothesis/audit sources only, never platform authority.

## Social / X research
- X official Post Lookup: `ADOPT` preferred resolver when authorized.
- X official oEmbed: `ADOPT` unauthenticated public fallback.
- FxEmbed/FxTwitter: `ADOPT AS READ-ONLY FALLBACK`; third-party retrieval only, content remains untrusted.
- Viral social posts: discovery input only; exact body and downstream claims must be separately verified.

## Mapping / geospatial
- MapLibre GL JS: `ADOPT` preferred modern open-source rich web-map candidate.
- Leaflet: `ADOPT` for lightweight/simple/legacy WordPress/web maps.
- Nominatim: `ADOPT WHEN NEEDED` for OSM geocoding/reverse geocoding; public instance is not an unlimited production SLA.
- Supercluster: `ADOPT WHEN NEEDED` for dense GeoJSON point clustering.
- Flutter MapLibre GL / React Native Maps: `ADOPT WHEN NEEDED` according to mobile stack.
- PMTiles/Protomaps ecosystem: `ADOPT_PATTERN_ONLY/WHEN NEEDED` for static/offline tile distribution.
- `protomaps-leaflet`: `SUPERSEDED FOR NEW WORK`; maintenance-mode legacy integration reference.

## Mail / email
- PHPMailer: `ADOPT` as maintained PHP SMTP/message-construction reference; WordPress public APIs/hooks remain the WP integration surface.
- React Email: `ADOPT WHEN NEEDED` for typed/deterministic provider-neutral templates in React/TS stacks.
- MJML: `ADOPT WHEN NEEDED` for responsive provider-neutral email compilation outside React.
- Mailpit: `ADOPT` for local/staging SMTP capture/integration/link/render testing.
- MailHog: `SUPERSEDED FOR NEW WORK` by maintained alternatives such as Mailpit.
- listmonk: `ADOPT WHEN NEEDED` for self-hosted newsletter/list management after AGPL/operations review.
- Postal/Stalwart/mailcow-class self-hosted mail infrastructure: `WATCHLIST/EXPLICIT INFRA DECISION`; never default merely to send contact-form mail.

## Rejection / non-adoption rules
- Archived/deprecated repo with maintained successor → `SUPERSEDED`, not new production dependency.
- High stars without provenance/maintenance/license fit → no adoption.
- Community skill that needs broad cookies/session/shell permissions merely to read public data → no default install.
- Self-hosting infrastructure that adds large operational/security burden without a concrete requirement → do not adopt.
- A tool already covered by a stronger canonical capability → dedupe instead of adding another overlapping agent/tool.

## Mandatory convergence rule
When new research is requested:
1. Check this ledger and current standards first.
2. Verify current upstream status.
3. If capability already exists, update evidence/version notes rather than duplicate it.
4. If useful but missing, promote it into the smallest correct unit: standard, JIT skill, reusable CI, project adapter or provider adapter.
5. If it changes agent behavior materially, add/extend regression/eval coverage.
6. Record the decision here so the finding does not get lost in chat.
