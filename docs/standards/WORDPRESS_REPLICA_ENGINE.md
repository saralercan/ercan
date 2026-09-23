# Ercan OS — WordPress Replica Engine

Status: active  
Date: 2026-09-23

## Purpose

Define the production contract for turning an authorized visual reference — screenshot, mockup, Figma design, HTML prototype, or reference-led specification — into a real WordPress implementation with measurable visual fidelity, CMS editability, responsive behavior, migration safety and independent QA.

This capability is JIT. It does **not** add a new stable routing identity. The user-facing alias `@WordPressReplica` resolves to the qualified stable-owner pod defined in `.agents/skills/wordpress-replica/SKILL.md`.

## Core principle

A screenshot is a reference, not the website.

A valid WordPress replica must reconstruct the system behind the reference:
- layout
- typography
- spacing
- imagery/crops
- components
- interactions
- responsive behavior
- content model
- editor controls
- WordPress runtime contracts

Using the reference image as a full-page background, shipping a static HTML shell with no realistic editability path, or scaling a fixed desktop canvas down to mobile fails this standard.

## Routing

Default route:
`@Orchestrator -> @ScreenshotToCode -> @WordPressExpert + @FrontendSystem -> @RealAsset -> @PixelMatch -> @AccessibilityQA + @BrowserQA -> @ProductionQA`

Add:
- `@WebPerformance` for material performance-sensitive production work.
- `@TechnicalSEO + @WordPressSEO` for existing indexed sites, migrations or URL/metadata changes.
- hosting/deployment specialist only when deployment is actually in scope.

## Modes

### NEW_THEME
Create an installable theme from the approved reference.

### MIGRATION_REPLICA
Redesign an existing WordPress property while preserving production contracts and SEO/content continuity.

## Architecture requirements

Choose the narrowest compatible WordPress architecture:
- block theme
- hybrid/classic theme
- child theme
- existing-theme refactor
- custom componentized theme

Prefer native WordPress capabilities over unnecessary dependencies. Do not add Elementor/ACF/page-builder dependencies unless existing architecture or explicit requirements justify them.

## CMS requirements

Repeated content should be modeled, not pasted:
- projects/case studies
- journal/news
- services
- industries/categories
- navigation
- shared CTA/contact/global settings

Content modeling must remain proportional to the project. Do not create unnecessary CPT/meta complexity for one-off copy.

## Reference fidelity

“1:1” is a QA target, not an unsupported promise.

Agreement should define reference viewports. At each viewport:
1. render the implementation in a real browser
2. capture output
3. compare to reference
4. correct material drift
5. repeat until the accepted threshold is reached

When the input contains only one viewport, derive missing breakpoints from the same design system and mark those responsive states as inferred rather than source-exact.

## Migration invariants

Unless scope explicitly changes them, preserve:
- URLs/slugs
- canonical/noindex
- hreflang/locales
- structured data truth
- menus
- published content
- media provenance
- forms/lead routes
- analytics/tracking
- account/auth flows
- existing integrations

A public URL change requires an explicit redirect/mapping decision.

## Rights and provenance

Visual structure may be studied from authorized/public references, but source extraction does not transfer rights to third-party photography, logos, fonts, copy or proprietary assets. Use project-owned, user-provided, licensed or otherwise authorized assets.

## Verification

A theme ZIP alone is not verification.

Material work should produce evidence for the applicable subset:
- PHP/static validation
- WordPress/theme validation
- lint/build
- critical browser routes
- console/network errors
- mobile/tablet/desktop
- visual/reference comparison
- accessibility
- links/forms
- SEO/indexability
- performance
- staging/post-deploy smoke
- rollback point

## Required failure handling

Return `PARTIAL`, `BLOCKED` or `NOT VERIFIED` rather than hiding:
- missing source assets
- inaccessible existing WordPress content
- unavailable premium plugin/theme dependencies
- unknown custom backend contracts
- untested deployment/runtime
- unresolved reference mismatch

## Anti-patterns

Fail the implementation if it relies on:
- screenshot-as-background reproduction
- fixed 1440px desktop canvas scaled for mobile
- hard-coded dynamic project/article lists that should be editable
- duplicate content types without migration rationale
- silent URL changes
- hidden placeholder images presented as final assets
- “pixel perfect” claim without rendered comparison
- production-ready claim from ZIP/syntax validation alone
