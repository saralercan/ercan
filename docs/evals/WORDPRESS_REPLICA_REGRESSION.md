# WordPress Replica Regression

Status: active  
Date: 2026-09-23

Purpose: regression cases for `WordPressReplica` / `@WordPressReplica` JIT routing and production behavior.

## Pass conditions

A case passes only when routing, implementation constraints and completion claims all match the expected behavior. A code artifact without runtime/reference evidence must not be upgraded to `VERIFIED`.

## Case 1 — User mockup -> new theme

Input:
“Bu mockup'ı 1:1 WordPress temasına dönüştür.”

Expected:
- load `.agents/skills/wordpress-replica/SKILL.md`
- route `@ScreenshotToCode + @WordPressExpert + @FrontendSystem`
- include `@PixelMatch + @BrowserQA + @AccessibilityQA + @ProductionQA` for material delivery
- choose NEW_THEME
- implement actual theme structure
- create editable repeated content
- produce ZIP when artifact delivery is requested
- rendered comparison is required before claiming VERIFIED

Fail:
- screenshot used as page background
- static HTML presented as complete WordPress theme
- “1:1 verified” with no comparison evidence

## Case 2 — Desktop-only reference

Input:
“Desktop görseli burada. Aynısını yap, mobilini de hazırla.”

Expected:
- desktop reference treated as source evidence
- mobile/tablet states explicitly marked as derived/inferred
- responsive system is intentionally designed
- no hover-only critical control
- mobile overflow and browser checks performed before VERIFIED

Fail:
- fixed desktop canvas simply scaled down

## Case 3 — Existing WordPress redesign

Input:
“Mevcut sitemde bu tasarımı uygula ama SEO ve içerikler aynı kalsın.”

Expected:
- choose MIGRATION_REPLICA
- add `@TechnicalSEO + @WordPressSEO`
- inventory/retain URLs, canonicals, hreflang, content types, menus, forms and tracking as applicable
- record redirect decision for any changed URL
- do not replace production content with demo content

Fail:
- fresh theme demo silently replaces indexed site architecture
- public URLs change without mapping

## Case 4 — Figma -> editable WordPress

Input:
“Bu Figma tasarımını WordPress'e geçir; müşteri hero, projeler ve yazıları panelden değiştirsin.”

Expected:
- use Figma/design source as authoritative visual input
- choose suitable block/hybrid/custom theme architecture
- map repeatable projects/articles to WordPress content model
- preserve design tokens/components where possible
- verify editor path for primary dynamic sections

Fail:
- every section hard-coded into PHP templates with no realistic edit path

## Case 5 — Third-party reference website

Input:
“Şu public sitenin aynısını WordPress yap.”

Expected:
- clarify/observe authorized reference scope through existing project rights context when available
- structural study is allowed
- third-party proprietary assets/copy/fonts are not silently copied without authorization
- use approved/project assets or recorded substitutions
- browser/visual QA compares composition without falsely claiming ownership of source assets

Fail:
- scrape and redistribute third-party protected assets as if project-owned

## Case 6 — Codex/agent left incomplete theme

Input:
“Codex yarım bıraktı; tema açılıyor ama menü ve mobil bozuk. Tamamla.”

Expected:
- inspect existing repo/theme before rewriting
- preserve working architecture
- repair only required surfaces
- browser E2E on menu/mobile
- visual comparison if a reference exists
- no unnecessary full rebuild

Fail:
- discard the existing theme and generate unrelated starter theme

## Case 7 — ZIP-only evidence

Input:
“ZIP oluştu, bitti mi?”

Expected:
- ZIP integrity/syntax may support PARTIAL
- VERIFIED requires applicable WordPress runtime/browser/reference checks
- communicate missing verification directly

Fail:
- mark VERIFIED because archive exists

## Case 8 — Vinterro Digital 2026 fixture

Fixture:
The approved Vinterro Digital 2026 homepage mockup produced on 2026-09-23.

Expected:
- reconstruct hero, manifesto, selected work, capabilities, operating-system, industries, studio and journal sections as real components
- do not embed the full mockup screenshot as the page
- create project/journal editability paths
- responsive behavior derived for tablet/mobile
- package installable theme when requested
- compare rendered homepage against the reference viewport before VERIFIED

This fixture is the first canonical regression example for the capability.
