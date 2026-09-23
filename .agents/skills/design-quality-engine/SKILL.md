---
name: design-quality-engine
description: Build and review high-quality product interfaces using distinctive visual direction, platform-aware motion, accessibility, responsive adaptation, design-system discipline, shadcn/ui composition and evidence-led critique. Use for premium UI implementation, interface polish, responsive adaptation, interaction/motion work, accessibility review or final design QA.
---

# Design Quality Engine

This JIT capability strengthens the existing Ercan OS web/design pod without creating new stable routing identities. For deeper UX research, information architecture, interaction-design or formal accessibility-evaluation work, also load `.agents/skills/digital-specialist-agent-pack/SKILL.md` + `docs/standards/DIGITAL_SPECIALIST_AGENTS.md`.

## Stable-owner mapping

- visual direction / distinctive frontend design -> `@FrontendSystem + @BrandSystemArchitect`
- component composition / shadcn -> `@FrontendSystem`
- generative UI presentation/review -> `@FrontendSystem + @AccessibilityQA + @BrowserQA`
- accessibility -> `@AccessibilityQA`
- responsive/adaptive UI -> `@FrontendSystem + @BrowserQA`
- motion / interaction -> `@FrontendSystem + @WebPerformance + @AccessibilityQA`
- design review -> independent `@BrandComplianceQA + @AccessibilityQA + @BrowserQA`
- platform-specific Apple/Android behavior -> `platform-design-intelligence`
- design-system/token changes -> `@DesignTokenArchitect + @ComponentWorkshopQA`

## Ten lanes

### 1. Distinctive frontend direction
Reviewed upstream: `anthropics/skills` → `frontend-design` (Apache-2.0).

Use to avoid generic template output. Ground visual choices in the product, audience, content and brand. Define a compact visual system before implementation: palette, typography, layout logic, spacing/radius/material language and one memorable design idea.

Do not copy a house style from the upstream. Project brand and explicit references win.

### 2. Apple-style interaction and motion
Reviewed upstream: `emilkowalski/skills` → `apple-design` (MIT).

Use for responsive touch/drag/sheet/popover interactions, interruptible motion, velocity handoff, spatial continuity and refined feedback.

Treat Apple-style behavior as a design reference, not a requirement. For actual Apple platform work, current official Apple HIG remains authority.

### 3. Surface depth / shadows
Reviewed upstream: `MengTo/Skills` → `beautiful-shadows` (MIT).

Use as a pattern reference for layered neutral elevation and subtle surface depth. Do not paste one fixed shadow recipe across every product. Shadows must follow the active token system, theme, contrast, density and visual direction.

### 4. Accessibility
Reviewed upstream: `addyosmani/web-quality-skills` → `accessibility` (MIT).

Use WCAG 2.2-oriented evidence-led review. Automated tooling is a detector, not certification. Pair with keyboard/focus/semantic review and rendered accessibility-tree/runtime evidence where available.

### 5. Design review
Reviewed upstream: `Superfuture/design-review`.

Use its strongest pattern: ranked findings with evidence, severity and concrete fixes across hierarchy, typography, spacing, color/contrast, motion, states, responsiveness, accessibility, content and brand consistency.

Do **not** adopt its telemetry ping or license-gated Pro service into Ercan OS. README says MIT, but no repository license file was observed during review; use pattern-only unless licensing is clarified.

### 6. Design engineering polish
Reviewed upstream: `emilkowalski/skills` → `emil-design-eng` (MIT).

Use for micro-interaction quality, animation decisions, component polish and invisible interaction details. Motion is justified by state/relationship/feedback, not decoration alone.

### 7. shadcn/ui composition
Canonical upstream: `shadcn-ui/ui` → `skills/shadcn/SKILL.md` (MIT).

For projects with `components.json`, inspect actual project context before changing components. Prefer existing components/variants, semantic tokens and documented composition. Use the project's package runner and current shadcn CLI/docs; do not guess component APIs from memory.

Do not force shadcn into projects that use another established component system.

### 8. Responsive / adaptive design
Reviewed upstream: `pbakaus/impeccable` → `adapt` reference (Apache-2.0).

Adaptation means rethinking layout, interaction and information priority for the target context, not scaling pixels. Verify narrow/wide screens, touch/pointer/keyboard, orientation and content stress. Use content-driven breakpoints where appropriate.

### 9. Holistic interface review
Reviewed upstream: `jakubkrehel/skills` → `better-interface` (MIT).

Use the orchestration pattern: consolidate accessibility, layout, writing, typography, color and UI-polish findings into one ranked report. Findings require evidence, not taste. Prefer one root-cause finding over repeated symptoms.

### 10. Interaction design
Reviewed upstream: `wshobson/agents` → `plugins/ui-design/skills/interaction-design/SKILL.md` (MIT).

Use for purposeful microinteractions, motion, feedback, loading states, transitions, gestures and interaction-state polish. Combine it with:
- `emilkowalski/skills` motion/interaction patterns;
- `pbakaus/impeccable` interaction, animation and adaptive references;
- Ercan OS platform-design and accessibility contracts.

Do not import fixed timing/easing values as universal tokens; project interaction language, platform conventions, performance and reduced-motion requirements remain authoritative.

Key rules:
- immediate feedback for user actions;
- no functionality dependent only on hover;
- interactions remain keyboard/touch accessible;
- motion is interruptible where the interaction can be interrupted;
- state changes remain legible with reduced motion;
- gestures are verified, not inferred from screenshots.

## Generative UI handoff

When a project uses `vercel-labs/json-render`, the Web Builder pack owns the schema/catalog/action boundary. Design Quality reviews the generated surfaces against the same brand, interaction, accessibility, responsive and rendered-evidence standards as hand-authored UI. Do not treat schema-valid output as visually or behaviorally verified.

## Operating flow

`brief/reference -> project/brand constraints -> design thesis -> token/component strategy -> implementation -> responsive/adaptive pass -> interaction/motion pass -> accessibility pass -> rendered design review -> browser/visual QA -> completion`

## Design thesis

Before a material UI build, resolve:
- primary product/audience/job
- visual direction and what makes it specific
- typography roles
- spacing/density rhythm
- palette/material/depth rules
- component language
- interaction/motion language
- responsive/adaptive behavior
- accessibility floor

Avoid generic AI defaults unless the brief explicitly asks for them.

## Review contract

A material UI review must:
1. resolve scope;
2. inspect actual rendered states when visual/runtime judgment matters;
3. inspect source/tokens for implementation claims;
4. cover default, hover/focus/active/disabled, loading/empty/error and representative responsive states where relevant;
5. rank findings by user impact;
6. consolidate repeated root causes;
7. distinguish hard accessibility/runtime defects from subjective visual preference;
8. propose fixes in the project's existing stack/design system;
9. re-verify after implementation.

## Hard rules

- Project brand/reference requirements outrank generic aesthetic preferences.
- No upstream style guide is a universal visual identity.
- Do not declare WCAG compliance from Lighthouse/axe alone.
- Do not use motion to hide slow interaction or broken state.
- Do not apply Apple/shadcn/Tailwind-specific rules to an incompatible stack.
- Do not alter the design system through arbitrary local values when a shared token/component owns the behavior.
- Do not accept mobile screenshots as proof that touch gestures work.
- Do not claim design quality from source inspection alone when rendered evidence is available.
- Prefer platform/native primitives and existing project components before custom reconstruction.
- Preserve performance and reduced-motion behavior when adding polish.

## Completion evidence

Record:
- resolved design scope and references;
- design-system/brand source of truth;
- implemented lanes;
- responsive viewports and input modes checked;
- accessibility checks and manual review;
- interaction/motion verification;
- rendered screenshots/visual evidence;
- browser/runtime errors;
- remaining subjective tradeoffs;
- final state: VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED.
