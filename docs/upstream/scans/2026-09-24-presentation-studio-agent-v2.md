# Presentation Studio Agent v2 — Specialist Expansion Scan

Date: 2026-09-24
Parent skill: `.agents/skills/presentation-agent-pack/SKILL.md`
Parent standard: `docs/standards/PRESENTATION_ENGINE.md`

## Decision

Keep the existing Presentation Agent Pack and upgrade it into an expert JIT **Presentation Studio** rather than creating a second permanent presentation agent.

User-facing entry alias: `@Presentation`.

Stable routing identity count remains 52. Presentation roles are JIT capabilities mapped onto existing Orchestrator, editorial, brand, graphic-design, accessibility, asset, data/domain and ProductionQA owners.

## New specialist lanes

Strategy / audience:
- PresentationDirector
- AudienceIntentAnalyst
- EvidenceArchitect
- StoryArchitect
- ExecutiveDeckStrategist
- InvestorPitchStrategist
- SalesDeckStrategist
- ProposalDeckStrategist
- AcademicDeckStrategist
- TrainingDeckStrategist
- KeynoteDeckStrategist

Content / delivery:
- SlideCopyEditor
- SpeakerNotesWriter
- AppendixArchitect
- LeaveBehindEditor
- LocalizationDeckEditor
- PresenterCoach

Visual / information design:
- PresentationDesignSystemDirector
- TypographyDirector
- LayoutComposer
- VisualAssetDirector
- DiagramArchitect
- DataVizDesigner
- TableEditor

Build / QA:
- TemplateMasterEngineer
- MotionTransitionDesigner
- GoogleSlidesEngineer
- CanvaPresentationProvider
- GammaPresentationProvider
- AccessibilityDeckReviewer
- CompatibilityReviewer
- DeckRedTeamCritic

Existing PresentationResearcher, DeckStrategist, NarrativeEditor, SlideArtDirector, AssetCurator, DataVizPlanner, PPTXEngineer and DeckReviewer remain active.

## New source-first contract

Material decks should have a rebuildable slide manifest before build. Each slide records:
- audience job;
- primary message;
- evidence/source;
- visual type;
- layout archetype;
- data/assets;
- speaker-note intent;
- editability requirement;
- accessibility metadata needs.

This reduces drift between research, narrative, design and PPTX generation and makes updates/regeneration safer.

## Reviewed 2026 upstream additions

### PoplarPoplar/presentation-skill_-PPTskill — ADOPT_PATTERN_ONLY/JIT
- MIT.
- Source-first editable PPTX workflow based on structured outline/data artifacts.
- Encodes slide design as constraints/variant grammar and explicitly checks density/design-taste failure modes.
- Particularly useful as a pattern for board, investor-update, report, policy, clinical and data-heavy decks.

### hunkim/slide-skill — ADOPT_PATTERN_ONLY_JUDGMENT
- MIT.
- Strong presentation judgment layer: significance, structure, simplicity and one primary point per slide.
- Use the one-point principle as a strong default, not a rigid law for board/dashboard slides that require tightly related metrics together.

### office-kit/pptx — WATCH / ADOPT_JIT_LIVE_PREVIEW
- TypeScript/ESM create/read/edit PPTX with live browser preview and editable export.
- Current upstream reports 0.x/pre-1.0 status; API may break in minor versions.
- Pin exact versions and task-locally validate before production promotion.

### Current OpenAI/JetBrains PptxGenJS slide discipline — ADOPT_PATTERN/JIT
- Direct editable PPTX authoring.
- Strong patterns: explicit theme fonts, native PowerPoint charts for standard charts, SVG fallback for complex diagrams, crop/contain helpers, rendered slide review, overlap/out-of-bounds checks and font-substitution detection.
- Preserve a source JS/TS artifact when using direct programmatic authoring so decks remain rebuildable.

### OpenAI report/slide automation pattern — ADOPT_PATTERN
- Data-rich decks should treat charts/diagrams/figures as durable assets with their own source and mini-brief before slide placement.
- Slide composition should be a sequence of claims supported by figures rather than a dashboard dump.

### PracticalSwan/agent-skills pptx — REJECT_VENDOR / PROPRIETARY_REFERENCE_ONLY
- Current skill metadata reports a proprietary license.
- Do not vendor or treat it as an open reusable upstream.

### lgwanai/ppt-skill — WATCH / LICENSE_REVIEW_REQUIRED
- Interesting design-DNA extraction and reference-deck spec workflow.
- Do not promote until license/provenance and current runtime behavior are independently reviewed.

### wuchichiumike/editable-pptx — WATCH / LICENSE_REVIEW_REQUIRED
- Useful native editable PPTX/read/edit/render/XML ideas.
- Current scan did not establish a sufficiently clear license basis for vendoring; keep pattern-level until reviewed.

## Connected provider expansion

### Canva
When a connected Canva provider exists:
- may use brand kits;
- can generate presentation candidates from a structured brief/slide plan;
- produces an editable Canva design.

Ercan OS still owns research, facts, narrative, speaker-note plan and final brand/visual QA. A generated candidate is not automatically VERIFIED.

### Gamma
When a connected Gamma provider exists:
- may generate new presentations;
- may generate from a Gamma template;
- may export PPTX/PDF/PNG when requested;
- may expose deck/card/viewer engagement analytics for existing Gamma assets.

Gamma generation is an execution surface, not the presentation strategist. Exported PPTX still requires compatibility/visual QA.

### Google Slides
Use connected Google Slides/Drive when:
- a native Google Slides template/reference/prior-period deck must be followed;
- native Slides editing/copying is required.

Derive the design system from the source deck first; do not replace it with a generic theme.

## Accessibility authority — Microsoft PowerPoint

Current Microsoft accessibility guidance promotes:
- unique descriptive slide titles;
- intentional reading order;
- alt text for meaningful visuals;
- meaningful hyperlink text;
- sufficient contrast;
- color-independent communication;
- simple data tables when tables are unavoidable;
- captions/subtitles for media when applicable;
- body text around 18pt or larger as a general accessibility/readability recommendation, with larger sizes for room presentation.

Ercan OS treats these as a strong accessibility baseline while allowing a documented template/use-case exception where necessary.

## Speaker notes and leave-behind

Microsoft PowerPoint supports speaker notes that are visible to the presenter rather than the audience. Ercan OS uses notes for delivery detail, transitions, evidence cues and talking points instead of duplicating visible slide text.

If the same content also needs to function as a detailed reference document, generate/plan a separate leave-behind or appendix instead of shrinking document prose onto live slides.

## Motion / transitions

Animations and transitions are optional. Use only when they explain:
- sequence;
- causality;
- hierarchy;
- state change;
- staged reveal.

Do not use motion as a proxy for premium design. Motion is VERIFIED only when the selected native/runtime engine can inspect or replay the relevant structures.

## Output compatibility

The presentation studio distinguishes:
- native editable PowerPoint objects;
- generated SVG/raster assets;
- whole-slide raster output;
- provider-native Canva/Gamma/Google Slides content.

CompatibilityReviewer checks target format and editability expectations explicitly. Pixels alone cannot prove speaker notes, masters, animations, hyperlinks, reading order or chart editability.

## Regression watch

An open 2026 issue in the OpenAI skills repository reported certain generated PPTX files requiring PowerPoint repair. Treat this as a reason to keep open/render/round-trip validation mandatory, not as proof that every PptxGenJS/OpenAI-style deck is currently broken.

## Architecture outcome

The Presentation Studio is now an expert orchestrated capability:
`audience/decision -> research/evidence -> story -> slide manifest -> copy -> design system -> data/diagrams/assets -> build/provider -> notes/appendix -> render -> accessibility/compatibility -> red-team -> final reviewer`.

No new permanent agent identity is required.
