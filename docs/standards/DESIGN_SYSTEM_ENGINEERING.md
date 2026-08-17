# Design System Engineering Standard

Use when a task spans brand foundations, Figma variables/components, design tokens, code components, Storybook/component workshops, cross-platform styling or design-code drift.

## Goal
A design system is not a Figma file and not a CSS variables file. It is a versioned contract connecting semantic foundations, component behavior, design references, code implementation, documentation, accessibility and migration history.

Canonical conceptual flow:
`brand foundations → semantic tokens → Figma variables/styles/components → component contracts → code components → workshop/Storybook → product surfaces → visual/a11y regression`.

## Source-of-truth boundaries
- Decide which layer owns each fact. Do not maintain independent conflicting palettes/type scales in Figma, Shopify, WordPress and social templates.
- Brand semantics own meaning (`surface.primary`, `text.muted`, `action.primary`); platform adapters own syntax/output.
- Generated token artifacts are derivatives; never hand-edit them as source.
- Component code is authoritative for runtime behavior; Figma is authoritative for approved visual/interaction intent where explicitly mapped.
- Screenshots are evidence, not token/component source.

## Token lifecycle
- Prefer semantic tokens over raw value names.
- Support aliases/references rather than duplicating values.
- Track type, description/intent and deprecation/rename information when useful.
- Token change = versioned change. Expose semantic diff in review.
- Renames/removals require migration or compatibility strategy for downstream consumers.
- Light/dark/theme modes should vary semantic values, not fork the whole naming system without reason.
- Validate token schema before generation.
- Build outputs may target CSS variables, JS/TS, platform config or other formats using a Style Dictionary-class build system when it reduces drift.

## Figma ↔ code bridge
- Use current official Figma Variables/Styles/Components/Code Connect capabilities where applicable.
- Code Connect mappings must be source-controlled when used and reviewed with the component implementation.
- Verify current supported Code Connect/template integration path at runtime; do not rely on obsolete parser assumptions.
- A design component and code component should share naming/variant/state semantics where practical.
- Missing/unsupported design state is a contract gap, not permission to invent silently.

## Component workshop
For reusable UI components, an isolated workshop such as Storybook is a preferred candidate when it materially improves development/testing.
Document representative states:
- default
- hover/focus/active/disabled
- loading/empty/error
- long/short/localized content
- mobile/narrow/wide containers
- light/dark/brand modes
- important data/business variants

A component is not complete because the happy-path screenshot matches. Interaction, keyboard/focus, content stress and responsive states matter.

## Design-code drift
Treat the following as regression candidates:
- off-palette values that bypass tokens
- wrong typography role/weight/line-height
- spacing/radius/shadow drift
- missing states/variants
- Figma component variant not represented in code (or vice versa)
- duplicated one-off component that should reuse system contract
- generated token output diverging from source tokens
- visual baseline updated without an intentional change explanation

## Accessibility contract
- Automated accessibility tooling such as axe-core is a detector, not a certification system.
- Pair automated scans with manual keyboard navigation, focus visibility/order, semantic naming/landmarks, form error association and screen-reader-relevant DOM review where risk warrants it.
- Color contrast and non-color status cues must be compatible with `BRAND_SOCIAL.md` and platform accessibility requirements.
- Component workshop stories should include accessibility-critical states.

## Shopify / WordPress integration
- Shopify: map tokens/components to theme settings/sections/snippets without breaking merchant editability or Theme Editor state.
- WordPress: use theme.json/block.json/native style surfaces where appropriate; persistent business behavior remains in plugin/application logic.
- Do not import an entire frontend framework/design-system dependency merely to reuse a handful of tokens/components.

## Review / migration gate
For material system changes:
1. Identify source-of-truth layer.
2. List affected tokens/components/consumers.
3. Produce semantic/token diff.
4. Build generated outputs.
5. Build/test component workshop when present.
6. Run unit/interaction/a11y checks.
7. Run visual regression on representative states.
8. Verify key Shopify/WordPress/product surfaces.
9. Document migration/deprecation notes.
10. Update approved references only after intentional review.

## Upstream patterns
- Figma SDS is a reference pattern for Variables + Styles + Components + Code Connect alongside a React codebase; do not copy its component vocabulary blindly.
- Style Dictionary is a reference/build candidate for transforming shared tokens into platform outputs.
- Adobe Spectrum Design Data is a reference for schema/version/diff/deprecation discipline.
- Storybook is a reference/candidate for building, documenting and testing UI components in isolation.
- axe-core is a preferred automated accessibility engine candidate; manual review remains required for issues automation cannot decide.

## Completion
Use `VERIFIED` only when the relevant design source, generated token/build output, component states, accessibility checks and representative product surfaces agree with no unresolved critical drift.