# Vinterro Digital — Creative Presentation Default (v1)

Status: **OPERATOR-APPROVED DEFAULT** · Adopted: 2026-10-26
Owner: `@Presentation` / Presentation Studio + `@VinterroDigital` for brand alignment.
Applies to: **all future presentations** requested through Vinterro One/ChatGPT/Codex, including client proposals, pitch decks, business/QA reports, executive decks, audit reports, project presentations and their PDF/HTML/print versions. This is a default creative visual language, **not** a command to reproduce one fixed deck layout or change content facts.

## Approved reference and priority

- Style exemplar: **SkiHub QA — Vinterro Creative v3**, delivered 2026-10-26 as `SkiHub_QA_Vinterro_Creative_2026-10-26.html`, `.pdf` and `_preview.png`.
- The exemplar established the operator's preference for colorful editorial direction, black/soft-white contrast, controlled mint/cobalt/coral accents, large message-led headlines, attractive but disciplined cards, status colors, evidence links, readable statistics and an explicit next-action roadmap.
- These are **approved visual-template tokens**, not a claim that every hexadecimal value was confirmed against live `vinterro.digital` brand code.
- Precedence: explicit user-selected reference/client brand/contractual template and the current verified brand system > this default. Adapt the default without losing its editorial craft. Truth, accessibility, source integrity and editable-format requirements always outrank decoration.
- Never assert that the actual SkiHub report, PDF or screenshot is accessible to a future runtime merely because the filename is recorded here. Recreate from the standards and retrieve exemplar only when available.

## Canonical design tokens

Machine-readable counterpart: `docs/standards/VINTERRO_PRESENTATION_CREATIVE_TOKENS.json`.

| Token | Hex | Purpose |
| --- | --- | --- |
| ink | `#111317` | Primary type, dark cover |
| navy | `#19222E` | Secondary dark surfaces |
| paper | `#FFFEFA` | Warm white reading canvas |
| cream | `#F7F5F0` | Ambient neutral background |
| mint | `#BFF8AE` | Primary creative accent / signal |
| blue | `#5C74EF` | Navigation / editorial contrast / focus |
| coral | `#F37C62` | High-priority accent, sparingly |
| pink | `#F7CBCA` | KPI/card pale fill |
| violet | `#AD9CFF` | Secondary editorial accent |
| ice | `#D6E5E5` | Quiet info/summary fill |
| lime | `#DDFF64` | Rare cover micro-accent |
| muted | `#6B7277` | Supporting labels (validate contrast) |
| hairline | `#DCDEDB` | Dividers / quiet structure |

Keep **ink/paper** as the base. Use 1–2 main accents per spread/slide, and alternate neutral and accent-led spreads for editorial rhythm; do not use every color on every slide. Semantic status colors must preserve their labels (e.g. Critical/Warning/Passed/Not tested) and be readable in grayscale.

## Visual grammar

1. **Cover:** dark, bold editorial hero with a genuinely meaningful title; strong high-contrast typography, generous whitespace and restrained blurred color geometry. Avoid giant empty blocks or fake imagery.
2. **Hierarchy:** single conclusion/message per slide; deck-level section label, overline, strong short title, then 1–3 supporting evidence blocks. Use readable number cards and large headlines only when they improve comprehension.
3. **Typography:** `Inter` or comparable clean sans; `Noto Sans` as a Turkish/multilingual fallback. Optional `Georgia` italic editorial emphasis for a *few* words. Tight heading tracking, natural body tracking, no illegibly tiny caps.
4. **Grid and space:** 8px base unit. Desktop report: typical section separation **40–64px**, content card gap 12–20px, card padding 22–32px. Slides: consistent safe margins around **5–7%** of slide width; vertical breathing space typically 24–48 equivalent pixels, adjusted to legibility and format. Never blindly force 40px on A4 or PPT slides.
5. **Layouts:** mix open editorial compositions, KPI overviews, evidence-heavy two-column structures, compact but readable QA tables, issue cards, risk/priority matrix, timeline/sprint roadmap and final actions. Avoid repeated identical AI-style card grids.
6. **Illustration/assets:** authentic owned/client imagery, substantiated charts and actual screenshots. Visuals should inform or reinforce content; no generic stock filler, fabricated UI data or decorative fake graphs.
7. **Reports/HTML:** optional compact left index/sidebar on desktop, readable stacked mobile layout, anchored sections, color-coded test filters when working interactivity is requested, and print-safe page breaks. No horizontal overflow.
8. **Slide decks:** 16:9 unless requested otherwise; native/editable PPTX elements, theme/master support, speaker notes when requested, linked evidence and source-backed charts. Interactive HTML-only affordances are not to be imitated as nonfunctional buttons in PPTX.
9. **Print/PDF:** preserve background colors only when readable in print, maintain visible page numbering and headings, control widow/orphan and split cards, test real exported pages.
10. **Tone:** world-class independent human art direction: minimal but energetic; premium yet not sterile. No emoji confetti, fake glass, excessive gradients, neon saturation, misleading AI-looking charts, repetitive buzzwords or template filler.

## Content rules by presentation type

- **QA/audit/report:** retain **every verified fact/test/bulgu**, IDs, statuses, severity, evidence URL, confidence/caveat, recommendation and owner/next step; do not beautify away failures or inaccessible tests.
- **Commercial proposal:** verified scope, deliverables, price, timing, assumptions and clear CTA; visual style must never alter commercial commitments.
- **Executive/strategy:** decision, metric context, risk, owner, timeline and action; prominent takeaways.
- **Investor/product:** actual evidence and data, no invented traction or metrics.
- **Research/training:** citations and method remain visible/traceable; presentational simplification must not distort data.
- **Client-specific deck:** apply verified customer brand first, adapt Vinterro structure/art direction around it.

## Default workflow and permanent agent checks

`@Presentation` must load this file together with the Presentation Engine and presentation-agent-pack **before** choosing styles or a generation provider:

1. Collect content/source truth and decide audience, format, purpose and locale; mark assumptions.
2. Build narrative + slide/report manifest with evidence and message hierarchy.
3. Use the tokens and visual grammar to create an **original** content-led layout; derive palette/master for current client.
4. Build editable output for PPTX/Slides if requested; provide PDF/HTML separately where appropriate.
5. Render **every** page/slide; inspect layout, typography, crop/overflow, data, links, status semantics, client branding and accessibility. Independently review; correct and rerender.
6. Confirm information completeness, tests/outcome truth, accurate exported content and brand/color consistency before calling it verified.

### Do not drift

A generic white corporate template, single monochrome deck, unrequested AI-style repeated tile layout, unsupported neon gradients or a raster-only PPTX fail the operator's default presentation style unless the brief/client brand explicitly calls for it. A beautiful cover with illegible body pages also fails. Never manufacture a PASS for tests not run.

## Regression scenarios

- Brief: "Make a QA report like the SkiHub creative report" => use colored KPI/priority cards, fully preserved verified findings, test status legend/filter (HTML), evidence and correction roadmap.
- Brief: "Prepare a client proposal" => inherit palette/editorial direction while retaining complete commercial terms and the client's brand.
- Brief: "Make an editable 10-slide PPTX" => preserve native editability, different content-driven layouts, readable text and rendered QA.
- Brief: "Use the client's provided brand template" => user-selected template takes precedence; Vinterro creative grammar must adapt and never override identity.
