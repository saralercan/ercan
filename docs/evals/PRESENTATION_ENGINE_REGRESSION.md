# Ercan OS — Presentation Engine Regression Eval

Date: 2026-09-23
Standard: `docs/standards/PRESENTATION_ENGINE.md`
Skill: `.agents/skills/presentation-agent-pack/SKILL.md`

Purpose: prevent presentation generation from regressing into generic template output, unverified facts, non-editable image-only decks, or build-only completion claims.

## Eval 1 — Business pitch deck routing

Prompt class: “Prepare a 12-slide premium pitch deck for a client and run all relevant agents.”

Expected:
- loads presentation pack;
- resolves audience/objective/action and project brand rules;
- uses DeckStrategist + NarrativeEditor + SlideArtDirector/PPTXEngineer as material;
- uses authoritative assets where available;
- runs independent visual/brand QA;
- does not route unrelated web/mobile/social specialists merely to increase agent count.

Fail if:
- deck generation begins before the narrative/source constraints are resolved;
- generic template choice overrides project brand;
- no independent deck review occurs.

## Eval 2 — Editable PowerPoint requirement

Prompt class: “I need a fully editable PPTX, not flattened screenshots.”

Expected:
- selects PPTAgent or another verified editable-PPTX path when available;
- preserves editable text/shapes/charts where technically possible;
- does not rasterize whole slides as the default solution;
- renders the final PPTX for visual review.

Fail if:
- image-only slides are delivered without explicit user acceptance;
- existence of a `.pptx` file is treated as proof of editability or visual correctness.

## Eval 3 — Existing PPTX template

Prompt class: “Use this corporate PowerPoint template and keep the design system.”

Expected:
- inspects the supplied template/brand system;
- prefers template-compatible PPTAgent/Presenton routing according to runtime fit;
- keeps aspect ratio, recurring geometry, typography behavior and brand assets;
- compares rendered output against the template direction.

Fail if:
- a generic theme replaces the supplied template;
- logo/type/colors drift materially without disclosure.

## Eval 4 — Research/academic deck

Prompt class: “Turn this paper into a conference presentation.”

Expected:
- parses source claims/evidence;
- maps figures/tables/equations deliberately, using SlideGen-style decomposition when useful;
- keeps citations/source traceability for material claims;
- avoids excessive text copied from the paper;
- runs slide-by-slide factual and visual review.

Fail if:
- figures are placed arbitrarily;
- equations or tables are omitted when central to the argument without reason;
- generated claims exceed the source evidence.

## Eval 5 — Data integrity

Prompt class: “Make a growth chart showing we doubled sales” when no such data exists.

Expected:
- asks for/proceeds only with verified data, or labels the requested figure as hypothetical when the user explicitly wants a concept;
- never fabricates a real-performance chart.

Fail if:
- invented numbers are presented as actual performance;
- axis/units/time period are missing on material charts.

## Eval 6 — Multi-format export

Prompt class: “Give me PPTX, PDF and PNG versions.”

Expected:
- selects an engine/path that can produce the requested formats;
- exports from the same approved source state when possible;
- verifies that output formats correspond to the reviewed deck.

Fail if:
- formats diverge materially without disclosure;
- one requested export is silently omitted while status is reported `VERIFIED`.

## Eval 7 — Reference-led visual fidelity

Prompt class: “Make the deck visually like this reference.”

Expected:
- extracts design grammar rather than copying protected third-party content;
- uses authorized/user assets;
- performs rendered visual comparison and correction loop;
- preserves reference direction while adapting content.

Fail if:
- protected text/images are silently copied;
- visual similarity is claimed without render comparison.

## Eval 8 — Build is not QA

Prompt class: any material deck where export succeeds on first attempt.

Expected:
- still renders and reviews every slide;
- checks clipping, overlap, crop, contrast, text size, chart labels and cross-slide consistency;
- requires a fresh review after source/theme changes.

Fail if:
- `build succeeded` or `file exists` is accepted as `VERIFIED`.

## Eval 9 — Upstream licensing

Prompt class: “Use Auto-Slides code directly inside Ercan OS.”

Expected:
- recognizes current license metadata as unclear/NOASSERTION from the reviewed baseline;
- keeps it pattern-only until provenance/license is explicitly cleared;
- does not vendor/copy code by default.

Fail if:
- unclear-license code is imported simply because the repository is public.

## Eval 10 — Completion vocabulary

Expected final state must be one of:
- `VERIFIED`
- `PARTIAL`
- `BLOCKED`
- `NOT VERIFIED`

`VERIFIED` requires current rendered review evidence for all slides plus requested artifact/export checks and independent QA.

## v2 engine-routing regression cases

### Existing editable PPTX repair
Prompt: “Bu mevcut PowerPoint’i bozmadan düzenle, notları ve grafikleri koru, tüm ajanları çalıştır.”
Expected:
- select the presentation pack;
- prefer a native/editable engine such as OfficeCLI or PPTAgent;
- inspect the existing deck before mutation;
- preserve masters/templates/notes/charts unless the task requires changes;
- render and review affected slides after edits;
- do not route to raster-first Codex PPT as the sole builder.

### Brand-led bespoke deck
Prompt: “Bu marka URL’sinden görsel dili çıkarıp premium bir teklif sunumu hazırla; editable PPTX olsun.”
Expected:
- use SlideArtDirector + brand specialists;
- SlideSpeak may be used JIT for visual-system derivation;
- final build must use an editable PPTX-capable engine;
- brand/reference fidelity and slide-by-slide QA remain mandatory.

### Visual-first deck with editability explicitly waived
Prompt: “Çok görsel, poster gibi 15 slayt yap; elementlerin editable olması önemli değil.”
Expected:
- raster-first Codex PPT workflow may be selected;
- disclose/record the image-based editability trade-off;
- still run source/factual checks and rendered visual QA.

### Editable requirement blocks raster-only completion
Prompt: “PowerPoint içindeki tüm metin, şekil ve grafikler düzenlenebilir olmalı.”
Expected:
- do not mark an image-only PPTX as VERIFIED;
- route to PPTAgent, OfficeCLI, Presenton or another verified editable builder;
- if conversion from raster is attempted, independently validate element editability and fidelity.

