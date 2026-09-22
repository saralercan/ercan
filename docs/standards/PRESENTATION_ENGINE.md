# Ercan OS — Presentation Engine

Status: active
Date: 2026-09-23

Purpose: govern creation, revision, export and QA of presentations, PowerPoint decks, pitch decks, proposal decks, report decks and academic/scientific slide decks in Ercan OS.

JIT skill: `.agents/skills/presentation-agent-pack/SKILL.md`
Upstream review: `docs/upstream/scans/2026-09-23-presentation-agent-scan.md`
Regression eval: `docs/evals/PRESENTATION_ENGINE_REGRESSION.md`

## Architecture rule

Presentation repositories are replaceable upstream engines, not policy authorities and not new permanent Ercan OS identities. Ercan OS keeps the existing stable routing surface and composes presentation-specific JIT roles around the existing Orchestrator, brand, asset and QA specialists.

Default presentation capability roles:
- `PresentationResearcher`
- `DeckStrategist`
- `NarrativeEditor`
- `SlideArtDirector`
- `AssetCurator`
- `DataVizPlanner`
- `PPTXEngineer`
- `DeckReviewer`

These roles are capabilities inside the presentation pack, not additional global `@` identities.

## Reviewed upstream set

### `icip-cas/PPTAgent` — ADOPT_JIT_PRIMARY
- Purpose: reflective/agentic editable PowerPoint generation with render-and-review workflow.
- License: MIT.
- GitHub state reviewed 2026-09-23: active, not archived; 5k+ stars; recent push on 2026-09-21.
- Relevant strengths: editable PPTX delivery, host-authored slide sources, slide rendering, slide-level visual review, deck-level review, finalization gate, Codex/agent skill support.
- Ercan OS use: primary engine when a high-quality editable `.pptx` is the requested artifact and a compatible runtime is available.

### `presenton/presenton` + `presenton/skills` — ADOPT_JIT_ALTERNATE
- Purpose: open-source AI presentation generation with templates/designs, editable PPTX and API/export workflows.
- License: Apache-2.0 for both reviewed repositories.
- GitHub state reviewed 2026-09-23: active, not archived; `presenton/presenton` 10k+ stars and pushed 2026-09-22; the skill repository provides an agent-facing export/validation workflow.
- Relevant strengths: prompt/document/template-driven creation, existing PPTX-template support, PPTX/PDF/PNG export, design search, icon/image handling, shareable preview and HTML validation.
- Ercan OS use: alternate engine for template-led generation, API/export workflows or multi-format parity.

### `Y-Research-SBU/SlideGen` — ADOPT_PATTERN_ONLY / ACADEMIC_JIT
- Purpose: collaborative multimodal scientific slide generation.
- License: MIT.
- GitHub state reviewed 2026-09-23: active, not archived; pushed 2026-06-01.
- Relevant strengths: outliner, figure/table mapper, equation formulizer, arranger and refiner pattern for scientific decks.
- Ercan OS use: academic/scientific planning pattern when papers, figures, tables and equations dominate the deck. Do not make it the default business-deck engine.

### `Westlake-AGI-Lab/Auto-Slides` — WATCHLIST / PATTERN_ONLY
- Purpose: interactive multi-agent academic presentation generation.
- GitHub license metadata at review time: `NOASSERTION` / no clear SPDX license.
- Relevant strengths: multi-agent academic planning/customization concepts.
- Ercan OS use: study workflow ideas only. Do not vendor, copy or execute as a production dependency until license/provenance is explicitly cleared.

### `rsrohan99/presenter` — REJECT_CODE_ADOPTION / IDEA_REFERENCE_ONLY
- Purpose: multi-agent presentation, diagrams, scripts, narration and video.
- Review reason: no detected repository license and last push materially older than the selected production engines.
- Ercan OS use: concepts such as speaker scripts, diagrams and video/narration may inform independent implementation; do not import code as a production dependency without license clearance.

## Engine selection

Use `PPTAgent` when:
- editable `.pptx` is the primary deliverable;
- visual fidelity and explicit render/review/finalize gates matter;
- a compatible local/runtime environment exists.

Use `Presenton` when:
- existing PPTX templates or design-template search are useful;
- PPTX + PDF + PNG parity is requested;
- API-based generation/export or shareable preview materially helps;
- the user wants a fast editable deck with template-led styling.

Use `SlideGen` patterns when:
- the source is a research paper or scientific manuscript;
- figures, tables and equations must be deliberately assigned to slides.

Do not choose an engine solely by star count. Capability fit, editability, maintenance, license, runtime, visual QA and source fidelity decide routing.

## Source and evidence contract

- User-provided source material is authoritative for user-specific facts.
- Current external research must be verified against reliable sources before being placed on slides.
- Preserve a source map for material statistics, quotations, market claims, dates, customer/case-study claims and financial figures.
- Do not create fake citations, fake benchmarks, fabricated customer logos or invented metrics.
- When content is uncertain, label uncertainty or omit the claim rather than visually presenting it as fact.

## Narrative contract

Before designing slides, resolve:
1. audience;
2. objective;
3. decision/action expected from the audience;
4. slide count and presentation duration when relevant;
5. narrative arc;
6. key evidence;
7. requested language and tone;
8. aspect ratio and output formats;
9. brand/template/reference constraints.

Prefer message-led titles over generic section labels when supported by evidence. Keep one primary idea per slide unless a comparison or matrix intentionally requires more.

## Visual design contract

- Use the project's visual identity before generic upstream templates.
- Preserve consistent grid, margins, type scale, spacing, color system and image treatment.
- Layout variation is required when it improves storytelling; random variation is not.
- Avoid generic AI-template artifacts: excessive gradients, decorative blobs, icon spam, dense card grids, tiny text and irrelevant stock imagery.
- Use whitespace and composition to create hierarchy.
- Maintain presentation-distance readability.
- Images must be cropped intentionally and retain subject integrity.
- Logos and protected assets must not be distorted.

## Data visualization contract

- Charts represent real supplied or verified data only.
- Label units, time periods and comparison bases clearly.
- Avoid truncated axes or visual encodings that materially mislead.
- Prefer a table when precise lookup matters; prefer a chart when pattern/comparison matters.
- Preserve editable native charts when the selected pipeline supports them.

## PPTX/export contract

- Respect requested aspect ratio (`16:9` default only when the user has not specified another format).
- Preserve text editability where technically possible.
- Avoid rasterizing entire slides merely to make them look correct unless the user explicitly accepts non-editable output.
- Export requested formats from the same approved source state when possible.
- Do not claim compatibility without opening/rendering the final artifact through a compatible validation path.

## Visual QA contract

For every material deck:
1. render all slides;
2. inspect every slide;
3. correct clipping, overlap, bad crops, broken assets, tiny text, low contrast, inconsistent alignment, accidental overflow and malformed charts;
4. verify cross-slide consistency;
5. verify final export matches reviewed source state;
6. run independent deck review after builder corrections.

A successful build process is not equivalent to visual QA.

## Reference/template use

When a user supplies a reference presentation, screenshot, template or brand deck:
- extract grid, spacing, type hierarchy, color behavior, image treatment and recurring composition patterns;
- reuse user-owned/authorized assets when available;
- do not silently copy third-party protected text/images/templates beyond permission/license;
- compare rendered output with the reference direction before final acceptance.

## Routing examples

### Vinterro Digital pitch/proposal deck
`@Orchestrator → DeckStrategist/NarrativeEditor → @BrandSystemArchitect/@BrandBehavior → SlideArtDirector/@RealAsset → PPTXEngineer → DeckReviewer → @BrandComplianceQA/@ProductionQA`.

### Research-paper presentation
`@Orchestrator → PresentationResearcher → DeckStrategist → SlideGen-style figure/table/equation mapping → NarrativeEditor → SlideArtDirector → PPTXEngineer → DeckReviewer`.

### Existing corporate PPTX template
`@Orchestrator → template/brand inspection → DeckStrategist/NarrativeEditor → Presenton or PPTAgent according to runtime/template fit → rendered visual review → independent QA`.

## Completion states

`VERIFIED` — final artifact and requested exports exist; material facts/sources are checked; every slide has current visual-review evidence; project/brand constraints are preserved; independent QA passes.

`PARTIAL` — usable presentation exists but a requested export, asset, source, template fidelity check or QA step remains incomplete.

`BLOCKED` — a required source, template, asset, runtime, permission or compatible export path is unavailable.

`NOT VERIFIED` — output has not passed the required factual/visual/export verification.
