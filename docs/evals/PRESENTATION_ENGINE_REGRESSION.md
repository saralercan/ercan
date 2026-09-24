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

## v3 complementary-engine regression cases

### Source-traced high-stakes deck
Prompt: “Bu rapordan yönetim sunumu hazırla; hiçbir rakam uydurulmasın, her veri kaynağı takip edilsin.”
Expected:
- route PresentationResearcher + source map;
- `slides_maker` may be preferred JIT for source-traced native PPTX;
- independent critic remains separate from author/builder;
- no uncited invented metrics, charts or claims.

### Existing deck round-trip conversion
Prompt: “Bu PPTX’i webde düzenleyip tekrar PPTX olarak ver; düzenlenebilir yapı mümkün olduğunca korunsun.”
Expected:
- Shuttleslide may be selected as PPTX↔HTML bridge;
- compare pre/post slides and inspect editable structure;
- alpha status requires task-local verification before VERIFIED.

### Screenshot/PDF to editable PowerPoint
Prompt: “Bu PDF/slayt ekran görüntülerini tek tek düzenlenebilir PowerPoint’e çevir.”
Expected:
- route image-to-editable reconstruction capability;
- recover native text/shapes where reliable;
- preserve complex visuals as separately sourced images when decomposition is unsafe;
- disclose non-lossless areas and do not guess unreadable content.

### AGPL candidate boundary
Prompt: “Dashi’nin motorunu Ercan OS içine gömelim.”
Expected:
- flag AGPL-3.0 licensing review before vendoring/embedding;
- allow pattern study or external isolated use only when licensing obligations are understood;
- do not silently vendor AGPL code into Ercan OS.

## v4 runtime/provider regression cases

### Native desktop PowerPoint fidelity
Prompt: “Kurumsal şablondaki bu PPTX’i gerçek PowerPoint içinde düzenle; SmartArt, animasyon ve master bozulmasın.”
Expected:
- select `sbroenne/mcp-server-powerpoint` only when Windows + PowerPoint desktop runtime is actually available;
- otherwise mark that engine unavailable and route to the best compatible editable builder;
- export changed slides from PowerPoint for visual verification;
- include accessibility checks when material.

### Browser review/editor surface
Prompt: “Ercan OS içinde PPTX’i tarayıcıda açıp metinleri/şekilleri düzenleyebileceğim bir editör olsun.”
Expected:
- route `sadmann7/pptx` as browser editor/runtime capability;
- pair with web/frontend/browser/accessibility QA specialists for implementation;
- do not treat the editor library as the narrative or art-direction agent.

### Hosted rapid deck + narration
Prompt: “Hızlı bir sunum üret, Türkçe olsun ve seslendirme de ekle.”
Expected:
- `2slides/mcp-2slides` may be selected only if authorized provider credentials/credits exist;
- never silently incur paid credits or expose API keys;
- provider output is draft until normal source/brand/visual QA passes.

### Incompatible native runtime
Prompt: “Mac üzerinde PowerPoint COM MCP kullan.”
Expected:
- do not claim the Windows-only native desktop engine can run;
- select OfficeCLI/PPTAgent/Presenton or another compatible route;
- completion state reflects actual runtime evidence.

### Unclear-license HTML-to-PPTX candidate
Prompt: “artifact-kit kodunu direkt Ercan OS içine kopyala.”
Expected:
- require explicit license/provenance clearance before vendoring;
- pattern-level measure-first reconstruction may be independently implemented;
- no silent source copying.


## v5 expert-studio regression cases

### Slide manifest before build
Prompt: “Bu dokümandan 15 slaytlık yönetim sunumu hazırla.”

Expected:
- PresentationDirector resolves audience, decision and output;
- source/claim map and slide manifest exist before material build;
- every planned slide has a primary message, evidence/source, visual type and editability/accessibility intent;
- builder output is derived from the manifest rather than improvised slide-by-slide.

Fail if:
- build starts directly from raw document paragraphs with no narrative/source model.

### Investor deck is not a generic company deck
Prompt: “Yatırımcı sunumu hazırla.”

Expected:
- route InvestorPitchStrategist;
- use actual evidence for traction, market, economics, GTM and ask;
- adapt sequencing to the company's strongest evidence;
- never invent TAM/SAM/SOM, logos, revenue, customers or growth.

Fail if:
- a rigid 10-slide startup template overrides the real story.

### Board/executive deck
Prompt: “Yönetim kurulu için aylık sunum hazırla.”

Expected:
- route ExecutiveDeckStrategist;
- prioritize deltas, decisions, KPI context, risks, owners and asks;
- allow dense but coherent metric clusters where comparison is the point;
- appendix/notes hold secondary detail.

Fail if:
- deck becomes a marketing narrative with no decision surface.

### Sales deck
Prompt: “Bu müşteriye özel satış sunumu hazırla.”

Expected:
- route SalesDeckStrategist + research/brand owners;
- buyer context and proof drive story;
- company-history slides are omitted unless useful to the buyer;
- next action is explicit.

Fail if:
- generic corporate deck is merely renamed for the prospect.

### Proposal deck
Prompt: “Müşteriye fiyatlı teklif sunumu hazırla.”

Expected:
- route ProposalDeckStrategist + Editorial/Brand/Production QA;
- preserve verified scope, deliverables, timeline, exclusions and pricing exactly;
- persuasion never silently changes commercial terms.

Fail if:
- price/scope is invented or reformulated into a materially different offer.

### Training deck
Prompt: “Ekibe 45 dakikalık eğitim sunumu yap.”

Expected:
- route TrainingDeckStrategist;
- define learning objectives;
- use concept → demonstration/example → practice/check → recap flow;
- slides support teaching rather than reproducing a manual.

Fail if:
- the deck is just documentation split across slides.

### Keynote deck
Prompt: “20 dakikalık konferans keynote’u hazırla.”

Expected:
- route KeynoteDeckStrategist + SpeakerNotesWriter/PresenterCoach;
- prioritize memorable arc, visual pacing and speaker-led delivery;
- detailed evidence goes to notes/appendix/leave-behind when needed.

Fail if:
- slides are dense enough to be read instead of presented.

### Presentation-distance readability
Prompt: any material PowerPoint deck.

Expected:
- typography hierarchy and presentation-distance review;
- ordinary body text below the current accessibility/readability floor is flagged unless a justified template/use case exists;
- legends/table text that only works at zoom are redesigned or moved to appendix.

Fail if:
- visual QA is performed only at thumbnail/file-open level.

### Accessibility structure
Prompt: “Kurumsal PPTX erişilebilir olsun.”

Expected:
- unique descriptive slide titles;
- intentional reading order;
- alt text for informative visuals;
- sufficient contrast and color-independent encoding;
- meaningful links;
- accessibility review separate from aesthetic review.

Fail if:
- “looks accessible” is accepted without structural checks where supported.

### Speaker notes
Prompt: “Konuşmacı notlarını da ekle.”

Expected:
- SpeakerNotesWriter adds transitions, evidence cues and delivery detail;
- notes are not a duplicate of visible body text;
- notes presence/content is structurally verified when the engine supports it.

Fail if:
- notes are claimed based only on rendered slide images.

### Diagram-heavy deck
Prompt: “Sistemi mimari ve süreç diyagramlarıyla anlat.”

Expected:
- route DiagramArchitect;
- simple flows remain editable native shapes when practical;
- complex diagrams retain a source artifact plus rendered visual;
- labels and connections remain readable at slide distance.

Fail if:
- random decorative arrows/icons substitute for actual relationships.

### Data-heavy deck
Prompt: “Bu Excel/CSV verisinden yönetim sunumu yap.”

Expected:
- route EvidenceArchitect + DataVizDesigner + TableEditor;
- data artifact remains reproducible;
- chart type, scale, labels and annotations serve the slide's message;
- dense raw tables move to appendix unless comparison requires them.

Fail if:
- chart values cannot be traced back to source data.

### Repeated AI layout detection
Prompt: any 10+ slide deck.

Expected:
- LayoutComposer/DeckRedTeamCritic scan for repeated card grids, centered body text, decorative icon clusters and dead whitespace;
- repetition is retained only when intentionally part of a system.

Fail if:
- the same three-card layout repeats because it was easy to generate.

### Canva connected provider
Prompt: “Canva brand kit’imle sunum oluştur.”

Expected:
- use CanvaPresentationProvider only if connected/authorized;
- use the chosen brand kit/template as execution surface;
- Ercan OS still owns narrative/source/slide plan and QA;
- provider success is not VERIFIED without reviewing the resulting deck.

### Gamma connected provider
Prompt: “Gamma’da hızlı bir sunum oluştur ve PPTX dışa aktar.”

Expected:
- use GammaPresentationProvider only if connected/authorized;
- choose generate/template mode according to request;
- exported PPTX/PDF remains subject to compatibility and visual QA;
- analytics capabilities are used only for existing Gamma engagement questions.

### Google Slides template
Prompt: “Bu mevcut Google Slides şablonunu kullanarak yeni dönem sunumu hazırla.”

Expected:
- route GoogleSlidesEngineer when native connected deck/template exists;
- derive design system from the source deck and edit a copy when appropriate;
- do not replace the native template with generic PPTX/Canva styling.

### Pre-1.0 engine boundary
Prompt: “office-kit/pptx’i varsayılan motor yap.”

Expected:
- recognize current pre-1.0 API status;
- allow pinned task-local JIT use after validation;
- do not make it the sole default production engine without stronger stability evidence.

### PptxGenJS structural validation
Prompt: “PptxGenJS ile üret, dosya oluştuysa yeter.”

Expected:
- reject file-existence completion;
- run render/open/overflow/font/structural checks available in the runtime;
- preserve editable native elements where practical.

Fail if:
- successful write is marked VERIFIED without current rendered/structural QA.

### Final red-team review
Prompt: any client-facing premium deck.

Expected:
- DeckRedTeamCritic is independent from author/builder;
- checks weak claims, missing proof, confusing slide purpose, generic design and hidden density;
- corrections are rerendered and reviewed before DeckReviewer signs off.

Fail if:
- creator self-certifies the premium deck.
