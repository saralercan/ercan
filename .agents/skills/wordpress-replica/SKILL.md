---
name: wordpress-replica
description: Convert an authorized screenshot, mockup, Figma design, HTML prototype, or reference-led visual specification into a real, editable, production-grade WordPress theme or WordPress redesign. Use for 1:1 visual reproduction, visual-to-WordPress, theme reconstruction, or migration/redesign work where fidelity, CMS editability, responsive behavior, SEO preservation, and browser/visual QA all matter.
---

# WordPress Replica

`WordPressReplica` is a JIT capability lane, not a new stable Ercan OS routing identity. Users may invoke it as `@WordPressReplica`; Orchestrator resolves it to the qualified pod below without increasing the stable agent count.

## Stable-owner composition

Default qualified pod:
- `@ScreenshotToCode` — reference decomposition and first functional UI implementation.
- `@WordPressExpert` — WordPress-native theme/block/CPT/taxonomy/admin architecture.
- `@FrontendSystem` — reusable components, tokens, responsive contracts and shared frontend structure.
- `@RealAsset` — authoritative asset reuse and provenance control when reference assets exist.
- `@PixelMatch` — rendered reference-vs-output geometry/typography/spacing/crop correction.
- `@AccessibilityQA` — automated + manual keyboard/focus/semantic checks.
- `@BrowserQA` — real-browser functional/runtime validation.
- `@WebPerformance` — performance regression and Core Web Vitals-oriented review when production scope requires it.
- `@ProductionQA` — independent final verification for material reference-led work.

Add `@TechnicalSEO` / `@WordPressSEO` when an existing indexed WordPress site is being redesigned or migrated.

## Trigger intents

Use this skill for requests such as:
- “Bunu 1:1 WordPress temasına dönüştür.”
- “Bu mockup'ı WordPress yap.”
- “Bu screenshot'ı gerçek yönetilebilir tema yap.”
- “Figma tasarımını WordPress'e çevir.”
- “Bu sitenin tasarımını benim WordPress siteme uygula.”
- “Desktop aynı kalsın, mobilini üret.”
- “Codex'in yarım bıraktığı WordPress temasını tamamla.”
- “Mevcut WordPress içeriğini koruyup tasarımı bununla değiştir.”

## Operating modes

### NEW_THEME
Build a new installable WordPress theme from the approved visual reference.

Required output when artifact delivery is in scope:
- installable theme directory
- installable `.zip`
- `style.css`, theme metadata and required templates
- responsive frontend implementation
- editable WordPress content architecture
- preview evidence
- QA notes

### MIGRATION_REPLICA
Apply the target visual system to an existing WordPress property while preserving its content and production contracts.

Preserve unless explicitly approved otherwise:
- public URLs/slugs
- redirect mappings
- canonical relationships
- hreflang/locale relationships
- structured data truth
- menus
- post/page/CPT content
- media provenance
- forms and lead routes
- analytics/tracking contracts
- authentication/account surfaces
- existing SEO equity

Do not replace an existing production architecture with a fresh demo theme merely because it is easier.

## Input hierarchy

Prefer inputs in this order when available:
1. authoritative project source files / existing WordPress theme
2. editable Figma or design-system source
3. user-supplied mockup/screenshot
4. user-supplied HTML prototype
5. authorized/public reference site for structural study

A reference image is design evidence, not executable code.

## Hard implementation rules

1. Never fake fidelity by setting the supplied screenshot as a full-page background.
2. Build actual HTML/CSS/JS/PHP or WordPress block/theme structures.
3. Text, images, projects, posts, menus and repeatable sections must be CMS-editable where editing is reasonably expected.
4. Prefer WordPress-native primitives: block themes, `theme.json`, patterns, Gutenberg, native menus, CPT/taxonomy, Customizer/settings, REST/Interactivity API, or WP-CLI as appropriate.
5. Add ACF, Elementor or other page builders only when the inspected project or user requirement justifies them.
6. Desktop composition must not be implemented as a fixed canvas that merely scales down.
7. Mobile/tablet behavior must be intentionally derived and verified; no hover-only critical interaction.
8. Preserve semantic heading order, keyboard access, focus visibility and `prefers-reduced-motion` behavior.
9. Treat third-party logos, photography, copy, fonts and proprietary assets as separate rights/provenance concerns. Reuse only authorized assets.
10. Avoid global CSS/JS hacks that cannot be maintained from the theme architecture.
11. Do not claim “1:1” as VERIFIED without rendered reference-comparison evidence at the agreed viewports.
12. Do not claim production readiness from a valid ZIP alone; runtime/browser checks are still required.

## Theme architecture decision

Before implementation, choose one and record why:
- block theme
- classic/hybrid theme
- child theme
- existing-theme refactor
- componentized custom theme

Decision factors:
- existing production theme
- Gutenberg usage
- Theme Editor requirements
- plugin dependencies
- PHP/WordPress compatibility
- deployment/hosting limits
- editor experience
- migration risk

## Visual fidelity loop

For every agreed viewport:
`reference -> implementation -> browser render -> screenshot -> compare -> correct -> repeat`

Correct at minimum:
- container width and grid
- geometry/alignment
- typography family/weight/line-height/tracking
- spacing/rhythm
- crop/object position
- colors
- borders/radii
- shadows/blur/glass
- sticky/fixed behavior
- interaction states
- responsive breakpoints

Use deterministic overlay/diff evidence when tooling permits. First render is never final evidence.

## WordPress editability contract

When a visual section contains repeatable data, map it to an appropriate content model rather than hard-coding content.

Examples:
- projects/case studies -> CPT + taxonomy/meta as appropriate
- journal/news -> Posts or dedicated CPT
- service families -> pages/CPT/taxonomy according to information architecture
- navigation -> registered WordPress menus/navigation blocks
- reusable global settings -> theme settings/options/`theme.json` as appropriate
- hero/CTA copy -> block/editor/settings source suitable for the project

Avoid over-modeling: simple one-off copy does not need a custom database schema.

## SEO and migration gate

For MIGRATION_REPLICA, verify:
- current URL inventory or mapped route set
- canonicals/noindex
- titles/meta/H1 structure
- sitemap participation
- hreflang when applicable
- structured data against visible content
- redirect requirements
- internal-link targets
- analytics/tagging continuity

Any changed public URL needs an explicit mapping decision.

## Default QA gate

Select the risk-appropriate subset:
`php/static validation -> lint -> build/assets -> WordPress/theme validation -> browser E2E -> console/network -> accessibility -> mobile/tablet/desktop -> visual comparison -> links/forms -> SEO/indexability -> performance -> preview/staging -> post-deploy smoke -> rollback evidence`

Minimum reference-led completion evidence:
- valid/installable theme artifact when requested
- no PHP fatal error on tested surface
- no critical browser-console error on tested surface
- no unintended horizontal overflow at tested mobile viewport
- keyboard/focus smoke passed
- rendered visual comparison completed
- editability path checked for the primary dynamic sections

## Completion states

- `VERIFIED` — implementation and required rendered/browser/reference checks passed.
- `PARTIAL` — usable implementation exists but one or more required QA/migration gates remain.
- `BLOCKED` — external dependency, inaccessible production source, permissions, or required environment prevents completion.
- `NOT VERIFIED` — artifact/code exists without sufficient runtime/reference evidence.

Load `docs/standards/WORDPRESS_REPLICA_ENGINE.md` and `docs/evals/WORDPRESS_REPLICA_REGRESSION.md` for material tasks.
