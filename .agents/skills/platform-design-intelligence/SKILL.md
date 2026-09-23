---
name: platform-design-intelligence
description: Apply platform-specific interface guidance for Web, Android and Apple platforms while preserving Ercan OS design-system, accessibility and QA authority. Use when creating or reviewing interfaces where platform conventions materially affect navigation, components, interaction, accessibility or responsive/adaptive behavior.
---

# Platform Design Intelligence

This JIT capability adapts `ehmo/platform-design-skills` as a platform-convention reference. It does not replace official platform guidance or Ercan OS design/QA contracts.

## Stable-owner mapping
- Web -> `@FrontendSystem + @AccessibilityQA + @BrowserQA`
- Android -> `@MobileArchitect + @MobileQA` plus implementation-stack specialist
- iOS/iPadOS/macOS/watchOS/tvOS/visionOS -> `@MobileArchitect + @MobileQA` plus platform-native implementation specialist where available
- Shared design system -> `@DesignTokenArchitect + @BrandSystemArchitect + @BrandComplianceQA`
- Performance-sensitive UI -> `@WebPerformance` or platform performance owner as appropriate

## Reviewed upstream
- `ehmo/platform-design-skills` — MIT.
- Covers 450+ distilled rules across Apple HIG, Material Design 3, WCAG 2.2 and MDN-oriented web guidance.
- ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED because distilled rules can lag current normative guidance.

## Authority order
1. User/project product requirements and accessibility obligations.
2. Current official platform guidance: Apple HIG / Android & Material / W3C WCAG / MDN as applicable.
3. Ercan OS brand/design-system standards.
4. Reviewed community skill summaries such as this upstream.

## Procedure
1. Detect target platform(s), form factor(s), input method(s) and accessibility needs.
2. Load only the relevant platform slice; do not mix mobile/web conventions indiscriminately.
3. Identify conflicts between brand expression and platform-native usability.
4. Preserve platform-native navigation, focus, gestures, semantics, sizing and interaction expectations unless the product has a justified alternative.
5. Verify responsive/adaptive states and input modalities actually used.
6. For web, combine with `web-builder-capability-pack`, `design-quality-engine`, accessibility and browser QA where material.
7. For mobile, combine with `mobile-app-specialist` and release/QA lanes only when required.
8. Re-check volatile platform conventions against current official sources before production claims.

## Hard rules
- Do not claim HIG/Material/WCAG compliance from a community checklist alone.
- Accessibility automation never replaces manual keyboard/focus/screen-reader-relevant reasoning where applicable.
- Platform conventions do not override explicit product requirements without surfacing the tradeoff.
- Cross-platform consistency means coherent product behavior, not pixel-identical UI everywhere.
- Apple-style web motion references from `design-quality-engine` never override current Apple HIG or project-specific interaction requirements.

## Completion evidence
Target platforms, official/current authority checked where material, applied conventions, intentional deviations, accessibility/adaptive verification and final state.
