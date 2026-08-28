# Ercan OS — Codex Execution Profile

Status: active

This document defines how OpenAI Codex should execute Ercan OS tasks when working in this repository or in a project that inherits this control-plane contract. It supplements the root `AGENTS.md`; it does not replace project adapters, platform standards, safety rules, or independent QA.

## Core rule

Codex must treat repository knowledge as the source of truth and load only the task-relevant instructions. Start from root `AGENTS.md`, then the agent registry, the matching project adapter, and only the standards/skills needed for the current task.

## Qualified-agent routing

When the user says **“tüm ajanları çalıştır”**, **“ajanları çalıştır”**, **“use all agents”**, or equivalent, Codex must interpret the request as **automatic qualified-agent routing** and load `docs/standards/QUALIFIED_AGENT_ROUTING.md`.

Codex must not ask the user to enumerate specialists that can be inferred from the task. It must detect the project, decompose the goal into capability requirements, select the minimum sufficient set of qualified workstreams, order dependencies, run only materially useful roles, and include independent QA when the work requires verification.

Selection criteria are: project fit, task competence, tool/data fit, dependency fit, risk fit and verification fit. A specialist required by the task should be included even if the user did not name it. An unrelated specialist should not be included merely because the user said “all agents.” Codex must never claim that an unavailable or unexecuted specialist actually ran.

Examples:
- production speed task → platform specialist + Performance Engineer + browser/performance QA; do not add redesign/copy/SEO unless material
- screenshot-led rebuild → ScreenshotToCode + RealAsset + platform implementation + PixelMatch + ProductionQA; add UXEnhancement only when justified
- SEO remediation → SEO/Entity/Local/AI-discovery specialists according to scope + technical verification; do not add unrelated visual agents
- simple deterministic change → smallest competent implementation path + appropriate check, not a theatrical multi-agent workflow

## Screenshot → Production UI activation

When the task includes a screenshot, mockup, Figma frame, Pinterest/Dribbble reference, screen recording, or phrases such as “birebir uygula”, “bu tasarımı kullan”, “referanstaki gibi yap”, “screenshotı koda çevir”, or equivalent reference-led UI intent, Codex must load:

1. `.agents/skills/screenshot-production-ui/SKILL.md`
2. `.agents/skills/visual-qa-evidence/SKILL.md`
3. the matching `projects/<slug>/AGENTS.md` and `PROJECT.md`
4. task-relevant platform/design standards

Do not activate this pipeline for ordinary copy edits, backend-only work, or isolated CSS changes with no reference-fidelity requirement.

## Mandatory Codex execution loop

`inspect → reference decomposition → authoritative asset resolution → first functional implementation → real browser render → reference-vs-render comparison → correction → re-render → UX enhancement when appropriate → platform adaptation → production QA → final state`

The first generated implementation or first render is never final acceptance evidence.

For reference-led work, at least one explicit `render → compare → correction → re-render` cycle is mandatory whenever browser execution is available. If browser rendering is unavailable or blocked, Codex must not claim pixel-perfect fidelity and must finish as `PARTIAL`, `BLOCKED`, or `NOT VERIFIED` as appropriate.

## Codex specialist roles

Codex may execute these as bounded internal workstreams rather than pretending they are independent persistent processes:

- `@ScreenshotToCode` — decompose the reference and create the first working implementation in the project-native stack.
- `@RealAsset` — locate and preserve authoritative project/user assets; prevent unrelated placeholders from surviving into final output.
- `@PixelMatch` — compare browser evidence with the authoritative reference and correct material visual drift.
- `@UXEnhancement` — add interaction polish only after visual fidelity is stable and only when consistent with brand/reference intent.
- `@ProductionQA` — independently verify critical viewports, console/network errors, accessibility smoke, performance regression risk, broken assets/links, and relevant SEO/metadata.

Running “all agents” never means blindly spawning every role. The Orchestrator selects only the workstreams needed for the task.

## Visual fidelity priorities

When trade-offs are necessary, preserve this order unless the task says otherwise:

1. page structure and dominant composition
2. correct brand/project assets and identity
3. hero/media crop and focal point
4. typography hierarchy and line breaks
5. container geometry, spacing and alignment
6. dominant color/surface/contrast system
7. component styling and interaction states
8. decorative micro-details

## Asset rules

- Prefer user-supplied and project-authoritative assets.
- Do not replace a supplied logo, product image, person, venue, event image, or brand asset with a generic placeholder unless the task explicitly permits it.
- When a substitute image is necessary, preserve subject class, composition, focal placement, brightness and aspect/crop intent as closely as practical, and record the substitution.
- Do not fabricate factual visual content for real businesses, places, products or events when the reference requires real-world accuracy.

## Browser evidence

Use Playwright or an equivalent real-browser path whenever the project supports it. Inspect at least the task-relevant viewport and state; for material page changes include representative mobile, tablet and desktop checks.

Visual QA should cover, as applicable:

- viewport geometry and overflow
- layout regions and container widths
- spacing and alignment
- font family/size/weight/line-height and line breaks
- image crop/focal point
- colors, opacity, borders, blur and shadows
- sticky/fixed layers and z-index
- hover/focus/active states
- animation/scroll behavior
- console and network errors
- broken image/link states

If a project does not define an evidence location, store disposable local evidence under an ignored temporary/artifact path rather than polluting production assets.

## Platform adaptation

Build the correct visual baseline first, then adapt it into the actual platform architecture. Preserve native editability and conventions:

- Shopify: sections/snippets/blocks, Theme Editor compatibility, product/variant/cart integrity.
- WordPress: theme/plugin/block architecture, admin-editable content, no brittle page-source hacks.
- Next.js/React: component boundaries, routing, image/font handling, performance and accessibility.
- Firebase/static: deployment-safe paths, caching, routing and environment separation.

After platform adaptation, rerun browser/visual verification because platform conversion can reintroduce drift.

## Completion contract

Codex must end material reference-led UI work with exactly one evidence-based state:

- `VERIFIED` — implementation was rendered and required checks passed; remaining differences are non-material.
- `PARTIAL` — useful work is complete but one or more acceptance criteria remain unmet.
- `BLOCKED` — an external dependency, permission, missing asset, environment problem or other concrete blocker prevents completion.
- `NOT VERIFIED` — code/output exists but required runtime or visual evidence could not be obtained.

Forbidden completion behavior:

- claiming “birebir”, “pixel-perfect”, “tamamlandı” or equivalent from code inspection alone
- stopping after the first generated render
- hiding structural mismatch with overlays, gradients, blur or other cosmetic effects
- leaving unrelated placeholder imagery in a final reference-led implementation
- adding fashionable glass/motion effects that contradict the supplied reference or project identity
- changing unrelated content, architecture or business logic merely to simplify visual matching

## Upstream reference policy

`abi/screenshot-to-code` is adopted as `ADOPT_PATTERN_ONLY`. Codex may reuse the architectural ideas of screenshot/video-to-code, real-asset extraction/reuse, browser rendering and iterative self-correction, but Ercan OS must remain provider-neutral. Do not hardcode that repository’s transient model/provider list into the Ercan OS contract.

## Definition of done

For a screenshot/reference implementation, Codex should not return `VERIFIED` unless the relevant items are satisfied:

- authoritative reference identified
- project context and do-not-touch constraints respected
- real assets used or substitutions documented
- project-native working implementation produced
- implementation rendered in a real browser
- at least one explicit reference comparison and correction cycle completed
- critical responsive states inspected
- no material clipping/overflow/wrong crop
- no major console/network/broken-asset failures
- accessibility/performance/SEO checks applied according to scope
- final visual evidence retained or summarized
- independent QA decision recorded
