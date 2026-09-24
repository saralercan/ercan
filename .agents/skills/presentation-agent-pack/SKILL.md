---
name: presentation-agent-pack
description: Route Ercan OS presentation work through an expert presentation-studio pipeline covering audience strategy, source research, story architecture, slide copy, visual systems, diagrams/data visualization, brand/template engineering, editable PPTX/Google Slides/Canva/Gamma provider routing, speaker notes, accessibility, compatibility and independent visual QA. Use for PowerPoint, slide deck, pitch deck, proposal deck, report deck, academic presentation, speaker deck, presentation PDF/PNG export, or when the user asks to run all relevant agents for presentation work.
---

# Presentation Agent Pack

Load `docs/standards/PRESENTATION_ENGINE.md`, root `AGENTS.md`, `docs/standards/AGENT_REGISTRY.md`, the active project adapter, task-relevant brand standards and source material.

This is a JIT capability pack. It does **not** create duplicate permanent routing identities or change the **21 Stable Core + 31 GitHub Specialist v3 Extension = 52 stable routing identities**. It composes existing Ercan OS specialists with presentation-specific capability roles and replaceable upstream engines.

## Presentation capability roles

Use only the roles that materially contribute:

- `PresentationDirector` — owns the end-to-end deck brief, audience, purpose, output mode, delivery constraints and specialist routing; user-facing entry alias is `@Presentation`.
- `AudienceIntentAnalyst` — resolves who will see the deck, what they already know, what decision/action is required and what objections or information gaps must be handled.
- `PresentationResearcher` — verifies claims, sources, numbers, dates and evidence; separates sourced facts from assumptions.
- `EvidenceArchitect` — creates claim→source and chart→data mappings so each material assertion/visual remains defensible.
- `DeckStrategist` — defines audience, objective, decision/action, slide count, narrative arc and information hierarchy.
- `StoryArchitect` — designs the through-line, section logic, tension/reveal/proof sequence and the reason each slide exists.
- `ExecutiveDeckStrategist` — executive/board/report decks: decisions, deltas, KPIs, risks, options, owners and next actions.
- `InvestorPitchStrategist` — investor/fundraising decks: opportunity, evidence, traction, economics, market, differentiation, GTM, team and ask without forcing a rigid template.
- `SalesDeckStrategist` — buyer-specific sales decks: buyer context, problem, value, proof, differentiation, objection handling and next step.
- `ProposalDeckStrategist` — client proposal decks: context/diagnosis, approach, scope, deliverables, timeline, commercial terms and next step using verified project/pricing truth.
- `AcademicDeckStrategist` — research/scientific decks: question, method, evidence, figures/tables, limitations and defensible conclusion.
- `TrainingDeckStrategist` — teaching/workshop decks: learning objectives, concept, demonstration, practice, check and recap.
- `KeynoteDeckStrategist` — keynote/story-led decks: memorable arc, visual pacing and speaker-led delivery rather than document density.
- `NarrativeEditor` — turns research into concise slide-level messages, titles, bullets, callouts and speaker-note structure.
- `SlideCopyEditor` — removes document prose, compresses slide copy, writes message-led titles and preserves meaning/source truth; load the Editorial & Writing Capability Pack for material copy work.
- `SpeakerNotesWriter` — creates presenter-only detail, source cues, transitions and talking points without duplicating the slide body.
- `AppendixArchitect` — moves necessary but non-core evidence, methodology, detailed tables and backup slides out of the main story while preserving findability.
- `LeaveBehindEditor` — creates or plans a denser handout/leave-behind when the audience needs reference detail beyond what belongs on presentation slides.
- `LocalizationDeckEditor` — adapts deck copy, examples, number/date formats and layout for target locales while preserving the same facts, brand and visual intent.
- `PresenterCoach` — prepares delivery flow, timing, likely questions, transitions and rehearsal notes when presentation delivery is in scope.
- `SlideArtDirector` — owns composition, typography, grid, visual rhythm, layout variation, brand fit and slide-to-slide coherence.
- `PresentationDesignSystemDirector` — derives/locks palette, typography, spacing, grids, recurring motifs, chart/diagram language and master-layout behavior for the deck.
- `TypographyDirector` — enforces presentation-distance readability, type hierarchy, line length, alignment and font substitution resilience.
- `LayoutComposer` — selects content-driven slide archetypes and prevents repetitive AI-card/grid layouts or dead whitespace.
- `DiagramArchitect` — converts systems, processes, timelines, comparisons, architecture and relationships into editable diagrams/flows where practical.
- `TableEditor` — turns dense tables into decision-friendly views, highlights material rows/columns and prevents tiny spreadsheet dumps.
- `AssetCurator` — selects authoritative project/user assets and records provenance; do not leave irrelevant placeholders.
- `VisualAssetDirector` — decides when to use real photography, product imagery, screenshots, icons, illustration, generated visuals or no image at all; preserves rights/provenance and avoids generic stock filler.
- `DataVizPlanner` — maps real data to appropriate charts/tables/diagrams and prevents decorative or misleading charts.
- `DataVizDesigner` — owns scales, labels, annotations, emphasis, color/encoding, data-story framing and chart editability/accessibility.
- `TemplateMasterEngineer` — preserves or builds masters/layouts/placeholders/theme behavior for reusable corporate/template-led decks.
- `MotionTransitionDesigner` — adds purposeful PowerPoint transitions/animations only when requested or materially useful and only through an engine/runtime that can verify them structurally; never uses motion as decorative default.
- `PPTXEngineer` — builds or converts the deck into editable PowerPoint-compatible output and keeps the requested aspect ratio.
- `GoogleSlidesEngineer` — uses a connected Google Slides/Drive workflow for native Slides templates, updates and reusable design-system fidelity when that surface is actually available.
- `CanvaPresentationProvider` — optional connected provider for brand-kit-led Canva presentation generation; provider output remains subject to Ercan OS content/brand/visual QA.
- `GammaPresentationProvider` — optional connected provider for rapid new presentations/templates/exports and engagement analytics; generation convenience does not replace deck strategy or QA.
- `AccessibilityDeckReviewer` — checks unique slide titles, reading order, alt text, color independence, contrast, hyperlink text and minimum readable type using current PowerPoint accessibility guidance.
- `CompatibilityReviewer` — checks fonts, missing assets, aspect ratio, export parity and target-viewer compatibility across requested PowerPoint/Keynote/Google Slides/PDF paths.
- `DeckRedTeamCritic` — independently attacks weak logic, unsupported claims, confusing slide purpose, generic layouts and unconvincing evidence before final approval.
- `DeckReviewer` — independently reviews rendered slides for clipping, overlap, contrast, density, consistency, factual drift and visual quality.

Map these JIT roles onto existing Ercan OS owners where relevant: `@Orchestrator` for routing/synthesis, `@BrandSystemArchitect`/`@BrandBehavior`/`@DesignTokenArchitect` for brand systems, `@RealAsset` for authoritative assets, `@BrandComplianceQA` for brand verification and `@ProductionQA` for independent final verification. Add `@UpstreamIntelligence` only when a current tool/capability gap or explicit GitHub research is material.

## Deck source-of-truth contract

For material decks, create a slide manifest before build. The implementation format may be JSON/YAML/Markdown, but each planned slide should resolve at least:

`slide_id | audience_job | primary_message | evidence/source | visual_type | layout_archetype | asset/data refs | speaker-note intent | editability requirement | accessibility title/alt needs`.

The manifest is the narrative/build source of truth. Builder-specific HTML/JS/XML/PPTX is generated from it. When source facts change, update the manifest/data artifact first and regenerate affected slides.

A deck should not become a handout by accident. If the audience needs dense reference detail, use speaker notes or a separate leave-behind/appendix when appropriate.

## Deck-type routing

- Investor/fundraising -> `InvestorPitchStrategist`.
- Sales/client pitch -> `SalesDeckStrategist`.
- Proposal/tender/commercial offer -> `ProposalDeckStrategist`.
- Board/executive/management report -> `ExecutiveDeckStrategist`.
- Academic/scientific/research -> `AcademicDeckStrategist`.
- Training/workshop/onboarding -> `TrainingDeckStrategist`.
- Keynote/conference/story-led -> `KeynoteDeckStrategist`.
- Portfolio/case-study/product launch -> `DeckStrategist + StoryArchitect + SlideArtDirector`, adding domain specialists as required.

Do not force every deck into the same canonical slide sequence.

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

### Source-traced native deck engine — `addsumtech/slides_maker`
Use when the deck must stay defensible against source material: papers, reports, repos, business documents or researched topics where numbers/figures must remain traceable. Its reviewed workflow emphasizes native editable PPTX, source fidelity, separate critic review and multi-canvas composition. Prefer it for high-stakes report, defense, executive and proposal decks when source-traceability and independent criticism are material.

### Round-trip PPTX ↔ HTML bridge — `solid-shuwen/shuttleslide`
Use for existing-deck conversion, inspection, web preview/editor workflows or repair where preserving editable PowerPoint structure through PPTX→HTML→PPTX matters. Its deterministic path preserves editable elements and formatting metadata; the optional AI generator is secondary. Use it as a bridge/conversion engine, not as a substitute for Ercan OS narrative/art-direction review.

### Image/PDF → editable PPT reconstruction — `ningzimu/image-to-editable-ppt-skill`
Use when the source is a slide image, PDF, screenshot or image-based PPTX and the user needs object-level editable PowerPoint. Reconstruct readable text as native text, simple geometry as PowerPoint shapes, and keep complex visuals as separate sourced assets when they cannot be meaningfully decomposed. This is a reconstruction capability, not a from-scratch deck authoring engine.

### Native Microsoft PowerPoint desktop control — `sbroenne/mcp-server-powerpoint`
Use only when a compatible Windows desktop with Microsoft PowerPoint is actually available and authorized. This MCP controls the live PowerPoint application through Microsoft Office interop, enabling true native templates/masters, SmartArt, animations, media, notes, accessibility operations and PowerPoint-rendered export-to-image verification. Prefer it for highest-fidelity repair/automation of an already-open or corporate-template deck. It is Windows-only and must never be assumed available on macOS/Linux/cloud runtimes.

### Browser-native PPTX editor/runtime — `sadmann7/pptx`
Use as a JIT browser editing/viewing capability when an Ercan OS surface needs to parse, render and edit real PowerPoint presentations in a React/browser UI. It provides accessible composable primitives, direct text/shape editing, selection, resize, undo/redo and PPTX save flows. This is an editor/runtime capability, not a presentation authoring or narrative agent; pair it with the presentation pod when in-browser human review/editing is required.

### Hosted fast-generation / narration provider — `2slides/mcp-2slides`
Use only as an optional external provider when fast theme-driven PowerPoint generation, reference-image style generation or AI voice narration materially helps and the user/runtime has authorized API access/credits. Treat outputs as drafts until Ercan OS source, brand and visual QA passes. Never expose or persist API keys in deck artifacts.

### Academic/scientific pattern engine — `Y-Research-SBU/SlideGen`
Use JIT for research-paper/scientific decks where figure/table/equation mapping and academic slide arrangement are material. It is a pattern/reference engine, not an automatic default for business or brand decks.

### Source-first constrained design — `PoplarPoplar/presentation-skill_-PPTskill`
Use as a reviewed MIT pattern/JIT reference for treating decks as source artifacts with explicit outline/data inputs, constrained slide variants and QA against density/design-taste failures. Strong fit for board, investor-update, policy/clinical/report and data-heavy decks. Ercan OS still owns narrative, facts and final QA.

### Presentation judgment layer — `hunkim/slide-skill`
Use as a lightweight MIT judgment reference for significance, structure, simplicity and “one primary point per slide.” Treat the one-point rule as a strong default, not an absolute law for board dashboards or tightly related metric clusters.

### Live-preview editable TypeScript engine — `office-kit/pptx`
Use JIT when a TypeScript/TSX authoring model with browser preview, editable PPTX export and agent-assisted visual iteration materially improves the workflow. Current upstream is pre-1.0, so pin versions and task-locally verify output/API behavior.

### PptxGenJS/OpenAI-style authoring discipline — PATTERN/JIT
PptxGenJS remains a strong direct editable-PPTX path. Current OpenAI/JetBrains slide-skill patterns add explicit theme fonts, crop/contain helpers, overflow/out-of-bounds checks, font-substitution detection, rendering and montage review. Keep the engine replaceable and always validate the exported file; never equate successful generation with openability or correctness.

### Optional connected providers — Canva / Gamma / Google Slides
Use Canva only when an authorized connected Canva surface/brand kit materially helps branded creation. Use Gamma only when an authorized connected Gamma surface materially helps rapid generation/template/export/analytics. Use Google Slides when a connected native Slides template/reference/update workflow is required. These providers are execution surfaces, not presentation-policy authorities, and their generated output must pass the same source, brand and visual review gates.

### Pattern-only / watchlist — `Westlake-AGI-Lab/Auto-Slides`
Useful for multi-agent academic presentation concepts, but its GitHub license metadata is `NOASSERTION`; do not copy or vendor code into Ercan OS without a separate license/provenance review. Concepts may be studied and reimplemented independently.

Do not adopt repositories with no usable license or materially stale maintenance merely because they advertise multi-agent presentations.

## Default flow

`brief/source intake → PresentationDirector/AudienceIntentAnalyst → PresentationResearcher/EvidenceArchitect → DeckStrategist/StoryArchitect + deck-type strategist → slide manifest → NarrativeEditor/SlideCopyEditor → PresentationDesignSystemDirector/SlideArtDirector/AssetCurator/DiagramArchitect/DataVizDesigner → TemplateMasterEngineer/PPTXEngineer or connected provider → speaker notes as needed → render every slide → Accessibility/Compatibility review → DeckRedTeamCritic → DeckReviewer → correction loop → final export → independent QA → VERIFIED/PARTIAL/BLOCKED/NOT VERIFIED`

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
- Speaker notes are generated when requested or materially useful; they hold delivery detail rather than duplicating slide body text.
- If the deck must also function as a leave-behind, explicitly design that artifact or appendix rather than shrinking handout prose onto live slides.
- Transitions/animations are optional communication tools. Use them to reveal sequence, causality, hierarchy or state change—not to make the deck feel “premium.”
- Every material slide needs a reason to exist: a decision, claim, explanation, comparison, proof point, transition or deliberate emotional beat.
- Prefer message-led titles (“Revenue concentration increased in Q3”) over topic labels (“Revenue”) when evidence supports the conclusion.
- Do not mechanically apply one-point-per-slide to board/dashboard slides where a small set of tightly related metrics must be viewed together; preserve a clear primary takeaway.
- Avoid repeating the same card grid/layout across the deck. Layout variation must follow content, not novelty.
- Use native editable charts/diagrams when practical; complex visuals may be SVG/raster assets but source/data must remain available for regeneration.
- Accessibility is a delivery requirement, not an optional polish pass, when the selected format supports it.

## Mandatory visual QA

A `.pptx` file existing on disk is not verification. For material delivery:

1. Render every slide to images or equivalent visual output.
2. Inspect every slide for clipping, overlap, broken assets, unreadable type, bad crops, inconsistent alignment and accidental overflow.
3. Check cross-slide coherence: title placement, margins, numbering, typography, colors, imagery treatment and density.
4. Review charts/tables against source data and labels.
5. Rebuild after source changes and re-review affected slides; shared-theme changes invalidate all visual reviews.
6. Run an independent final pass separate from the builder role.
7. When PowerPoint is the target, check accessibility-relevant title/reading-order/alt-text/contrast issues and font substitution where the runtime exposes those signals.
8. If speaker notes, animations, masters or hyperlinks are requested, verify those structures separately; rendered pixels alone cannot prove them.

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