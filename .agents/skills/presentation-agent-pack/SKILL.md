---
name: presentation-agent-pack
description: Route Ercan OS presentation work through a research, narrative, visual-design, editable-PPTX build and independent visual-QA pipeline. Use for PowerPoint, slide deck, pitch deck, proposal deck, report deck, academic presentation, speaker deck, presentation PDF/PNG export, or when the user asks to run all relevant agents for presentation work.
---

# Presentation Agent Pack

Load `docs/standards/PRESENTATION_ENGINE.md`, root `AGENTS.md`, `docs/standards/AGENT_REGISTRY.md`, the active project adapter, task-relevant brand standards and source material.

This is a JIT capability pack. It does **not** create duplicate permanent routing identities. It composes existing Ercan OS specialists with presentation-specific capability roles and replaceable upstream engines.

## Presentation capability roles

Use only the roles that materially contribute:

- `PresentationResearcher` — verifies claims, sources, numbers, dates and evidence; separates sourced facts from assumptions.
- `DeckStrategist` — defines audience, objective, decision/action, slide count, narrative arc and information hierarchy.
- `NarrativeEditor` — turns research into concise slide-level messages, titles, bullets, callouts and speaker-note structure.
- `SlideArtDirector` — owns composition, typography, grid, visual rhythm, layout variation, brand fit and slide-to-slide coherence.
- `AssetCurator` — selects authoritative project/user assets and records provenance; do not leave irrelevant placeholders.
- `DataVizPlanner` — maps real data to appropriate charts/tables/diagrams and prevents decorative or misleading charts.
- `PPTXEngineer` — builds or converts the deck into editable PowerPoint-compatible output and keeps the requested aspect ratio.
- `DeckReviewer` — independently reviews rendered slides for clipping, overlap, contrast, density, consistency, factual drift and visual quality.

Map these JIT roles onto existing Ercan OS owners where relevant: `@Orchestrator` for routing/synthesis, `@BrandSystemArchitect`/`@BrandBehavior`/`@DesignTokenArchitect` for brand systems, `@RealAsset` for authoritative assets, `@BrandComplianceQA` for brand verification and `@ProductionQA` for independent final verification. Add `@UpstreamIntelligence` only when a current tool/capability gap or explicit GitHub research is material.

## Reviewed upstream engines

### Primary editable-PPTX engine — `icip-cas/PPTAgent`
Use when the deliverable must be a polished, editable `.pptx` and visual review is required. Its current skill workflow explicitly separates slide authoring, rendering, per-slide review, deck review and finalization. Treat its CLI/runtime as a replaceable engine; Ercan OS owns research, brand, safety and completion decisions.

### Alternate template/API/export engine — `presenton/presenton` + `presenton/skills`
Use when existing PPTX templates, editable PPTX export, PDF/PNG parity, design/template search, shareable preview or API-based generation materially helps. Prefer user/project brand direction over generic built-in templates.

### Direct PPTX authoring/editing engine — `iOfficeAI/OfficeCLI`
Use when Ercan OS must create, inspect, revise or repair native PowerPoint structures directly, especially existing decks, templates, masters, notes, charts, shapes or iterative render→inspect→fix loops. Its reviewed PPTX skill enforces presentation-distance readability, explicit type hierarchy, editable native elements and visual delivery gates. Apache-2.0 licensed. Treat the installed CLI/version help as runtime authority for command syntax; never curl/execute remote install scripts automatically without an explicit runtime need and normal tool/security review.

### Bespoke visual-design engine — `SlideSpeak/slide-design-skill`
Use as an art-direction/layout engine when the user cares strongly about a distinctive on-brand visual system derived from a brief, brand URL, reference site or moodboard. It renders deterministic 1920×1080 HTML with charts, tables and imagery and is MIT licensed. It is not the default final PPTX authoring engine: when editable PowerPoint is required, pair its visual grammar/output plan with `PPTAgent`, `OfficeCLI` or another verified editable builder and run the normal Ercan OS render/review loop.

### Raster-first visual engine — `ningzimu/codex-ppt-skill`
Use only when highly visual full-slide image generation is intentionally preferred over native editability, or as a concept/reference workflow for style matching and slide-image generation. MIT licensed. Its default deck is image-based, so it must **not** be selected as the sole engine when editable text/shapes/charts are a requirement. Any later image-to-editable conversion is a separate lossy/QA-sensitive step and must be verified independently.

### Academic/scientific pattern engine — `Y-Research-SBU/SlideGen`
Use JIT for research-paper/scientific decks where figure/table/equation mapping and academic slide arrangement are material. It is a pattern/reference engine, not an automatic default for business or brand decks.

### Pattern-only / watchlist — `Westlake-AGI-Lab/Auto-Slides`
Useful for multi-agent academic presentation concepts, but its GitHub license metadata is `NOASSERTION`; do not copy or vendor code into Ercan OS without a separate license/provenance review. Concepts may be studied and reimplemented independently.

Do not adopt repositories with no usable license or materially stale maintenance merely because they advertise multi-agent presentations.

## Default flow

`brief/source intake → PresentationResearcher → DeckStrategist → NarrativeEditor → SlideArtDirector/AssetCurator/DataVizPlanner → PPTXEngineer → render every slide → DeckReviewer → correction loop → final export → independent QA → VERIFIED/PARTIAL/BLOCKED/NOT VERIFIED`

For reference-led decks:
`reference/template intake → extract design grammar, not copyrighted content → authoritative assets → narrative mapping → build → rendered comparison → correction loop → independent QA`.

For academic/scientific decks:
`paper/source parse → claim/evidence map → outline → figure/table/equation assignment → slide drafting → citations/notes as required → build → visual + factual review`.

## Quality rules

- The user states the goal once; Orchestrator resolves the smallest sufficient presentation pod.
- Never invent metrics, customer logos, case-study claims, citations, company facts or financial results.
- Every material factual claim must be traceable to user-provided material or a current reliable source when research is requested.
- One slide should normally communicate one primary idea. Avoid paragraph walls and tiny text.
- Titles should state the slide's message, not merely its topic, when the content supports that conclusion.
- Use visual hierarchy and whitespace before adding decoration.
- Vary layouts deliberately while preserving a coherent design system.
- Use real charts only for real data; do not fabricate trend lines or unlabeled numbers.
- Preserve editability for text, shapes and charts when the selected engine supports it.
- Preserve requested aspect ratio and safe slide margins.
- User/project templates, logos, fonts and brand rules outrank upstream defaults.
- Do not copy third-party presentation text, imagery or templates beyond rights/license/permission.
- If a user provides a reference deck, reproduce design language and structure only to the extent permitted; do not silently republish protected content.
- Speaker notes are generated only when requested or materially useful.

## Mandatory visual QA

A `.pptx` file existing on disk is not verification. For material delivery:

1. Render every slide to images or equivalent visual output.
2. Inspect every slide for clipping, overlap, broken assets, unreadable type, bad crops, inconsistent alignment and accidental overflow.
3. Check cross-slide coherence: title placement, margins, numbering, typography, colors, imagery treatment and density.
4. Review charts/tables against source data and labels.
5. Rebuild after source changes and re-review affected slides; shared-theme changes invalidate all visual reviews.
6. Run an independent final pass separate from the builder role.

## Completion gate

Mark `VERIFIED` only when:
- requested slide count/format/aspect ratio are satisfied;
- factual/source checks are complete for material claims;
- brand/project constraints are preserved;
- every slide has current rendered visual-review evidence;
- the final exported deck matches the reviewed source/render state;
- no known clipping/overlap/broken assets remain;
- independent QA has passed.

Use `PARTIAL` when a usable deck exists but a requested export, source, asset, template or review step remains incomplete. Use `BLOCKED` when required access/assets/runtime are unavailable. Never imply an upstream engine executed if it was not actually available and run.