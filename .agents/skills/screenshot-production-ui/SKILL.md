---
name: screenshot-production-ui
description: Convert a screenshot, mockup, Figma reference or screen recording into a production-ready UI through reference analysis, real-asset reuse, browser rendering, iterative visual comparison, UX enhancement and independent QA. Use when the user asks to reproduce, closely match, adapt or improve a visual reference. The first generated render is never final evidence.
---

# Screenshot → Production UI

Follow root `AGENTS.md`, `AGENT_REGISTRY.md`, the matching project adapter and relevant platform/design standards. Pair with `visual-qa-evidence` for acceptance and `agent-eval-regression` when a repeated fidelity failure or routing failure is being fixed.

This skill adopts the useful production pattern from `abi/screenshot-to-code` without making Ercan OS depend on that repository or on any single model/provider. The upstream is a reference implementation, not the constitution or final QA authority.

## Activation

Use this skill when the task contains one or more of these intents:
- reproduce this screenshot / make it like this reference
- convert a screenshot, mockup or Figma design to code
- adapt a Pinterest/Dribbble/reference design to an Ercan OS project
- match an existing page while preserving its visual language
- improve a generated UI that is visibly drifting from the supplied reference
- turn a screen recording into a functional prototype

Do not activate for ordinary copy edits, isolated CSS tweaks with no visual reference, or backend-only work.

## Specialist pod

The Orchestrator may instantiate these bounded specialist roles:

### `@ScreenshotToCode`
Owns reference decomposition and the first functional implementation. Extracts hierarchy, layout, grid, spacing, typography, imagery, crop, overlays, surfaces, glass/blur, radii and responsive intent. Produces the smallest viable code target for the actual project stack.

### `@RealAsset`
Owns asset fidelity. Reuses user-supplied or project-authoritative logos, photos, icons and artwork when available. Rejects unrelated placeholder imagery in final output and records provenance for substituted assets.

### `@PixelMatch`
Owns reference-vs-render comparison. Measures and corrects visible drift in geometry, spacing, type scale/line height, alignment, crop, colors, opacity, borders, shadows, blur, positioning and responsive behavior.

### `@UXEnhancement`
Owns improvement after baseline fidelity is established. Adds motion, hover, transitions, scroll behavior, interaction states and premium UX only when they preserve the reference's composition and project brand rules.

### `@ProductionQA`
Independent verifier. Checks browser behavior, console/network errors, mobile/tablet/desktop viewports, accessibility smoke, performance regression risk, broken assets/links, SEO/metadata where relevant and final visual evidence. Implementation roles do not self-certify.

## Required inputs
- authoritative visual reference(s)
- target route/screen/component and project context
- target stack/platform if already known
- project-authoritative assets and copy when available
- do-not-touch constraints
- acceptance criteria or best observable approximation when not explicitly provided

## Production loop

1. **Reference intake**
   - Identify which reference is authoritative.
   - Record target viewport/aspect ratio where known.
   - Separate content truth from visual style; do not copy third-party factual content into a client project unless intended.

2. **Visual decomposition**
   - Extract page regions, composition, grid, container widths, spacing rhythm, typography hierarchy, surface treatments, asset crops, interaction clues and responsive assumptions.
   - Identify high-salience anchors whose mismatch would make the page feel wrong at first glance.

3. **Asset resolution**
   - Prefer user/project assets.
   - Reuse/extract real visual assets from the supplied reference only when legally and contextually appropriate.
   - If a replacement is required, choose one that preserves composition, brightness, focal placement and subject class; document the substitution.

4. **First functional implementation**
   - Produce working code in the project-native stack.
   - Preserve semantic structure, responsiveness and accessibility fundamentals while matching the reference.
   - Do not over-engineer platform integration before the visual baseline is correct.

5. **Browser render**
   - Render the actual implementation in a real browser (Playwright or equivalent) at the meaningful target viewport/state.
   - Capture implementation evidence.
   - The first render is a candidate, never final acceptance.

6. **Pixel-match loop**
   - Compare reference and render using `visual-qa-evidence`.
   - Prioritize P0/P1 drift first: wrong structure, wrong asset, major crop, broken hierarchy, viewport overflow, typography scale, spacing and dominant color/surface mismatch.
   - Apply corrections and re-render.
   - At least one render → compare → correction cycle is mandatory for screenshot/reference reproduction tasks unless the first render cannot be produced, in which case status is `BLOCKED`/`NOT VERIFIED`.
   - Continue until remaining differences are non-material or a concrete blocker is recorded.

7. **UX enhancement**
   - Only after fidelity is stable, add high-value interaction polish.
   - Avoid generic AI-template effects, excessive gradients/glass, random motion or decorative chrome not supported by the reference/brand.

8. **Platform adaptation**
   - Adapt the verified UI into the real target architecture: Shopify sections/snippets, WordPress/Gutenberg/plugin/theme, Next.js/React, Firebase-hosted app or static output.
   - Preserve Theme Editor/CMS/admin editability where the project requires it.
   - Do not let platform conversion reintroduce visual drift without another browser check.

9. **Production QA**
   - Run risk-appropriate lint/build/tests.
   - Inspect critical mobile/tablet/desktop viewports.
   - Inspect console/network failures and broken assets/links.
   - Run keyboard/focus/accessibility smoke where interactive.
   - Check performance regressions and CLS/LCP risk for material page changes.
   - Check SEO/meta/semantic structure when the task changes a public page.
   - Capture final visual evidence and completion state.

10. **Completion**
   - Final state is exactly one of `VERIFIED`, `PARTIAL`, `BLOCKED`, `NOT VERIFIED`.
   - Never claim "birebir", "pixel-perfect" or equivalent without rendered comparison evidence supporting that claim.

## Fidelity priorities

When trade-offs are required, preserve in this order unless the brief says otherwise:
1. page structure and dominant composition
2. correct brand/project assets and identity
3. hero/media crop and focal point
4. typography hierarchy and line breaks
5. container geometry, spacing and alignment
6. dominant color/surface/contrast system
7. component styling and interaction states
8. decorative micro-details

## Provider/tool policy

- `abi/screenshot-to-code` is `ADOPT_PATTERN_ONLY`: useful reference for screenshot/video → code, asset reuse and headless-browser self-checking.
- Do not hardcode its current model list or provider choices into Ercan OS.
- Playwright/browser rendering is preferred evidence where available.
- Model/image providers are swappable adapters. Provider output is not final QA.
- Never require broad credentials merely to reproduce a public visual reference.

## Acceptance checklist

A screenshot/reference implementation is not complete unless the relevant items pass:
- authoritative reference recorded
- real project assets used or substitutions documented
- working implementation rendered in a browser
- at least one explicit reference-vs-render correction cycle completed
- critical viewport states checked
- no major console/network/broken-asset failures
- no material overflow/clipping or wrong image crop
- accessibility/performance/SEO checks selected according to scope
- final screenshot/evidence retained
- independent QA result recorded

## Forbidden shortcuts

- declaring completion from code inspection alone
- treating the first generated render as final
- replacing supplied brand imagery with unrelated placeholders without disclosure
- hiding layout errors with oversized overlays/gradients/blur
- changing adjacent brand/content architecture simply to make matching easier
- adding fashionable glass/motion effects that contradict the reference
- claiming exact fidelity without comparable rendered evidence

## Regression cases

Minimum routing/fidelity regressions:
- positive activation: user provides screenshot and asks to reproduce it → skill must activate and browser comparison must be planned
- positive activation: user asks to adapt a Dribbble/Pinterest reference to a project → skill activates but project brand/content truth remains authoritative
- negative activation: user asks to change one button label with no visual-reference intent → skill should not activate
- forbidden behavior: implementation returns after first render without comparison/correction → fail
- forbidden behavior: final UI contains generic placeholder images despite authoritative supplied assets → fail
- completion oracle: final state may be `VERIFIED` only when rendered evidence exists for the target state
