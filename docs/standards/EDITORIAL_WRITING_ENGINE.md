# Ercan OS — Editorial & Writing Engine

Status: active
Date: 2026-09-24
Skill: `.agents/skills/editorial-writing-capability-pack/SKILL.md`
Regression eval: `docs/evals/EDITORIAL_WRITING_ENGINE_REGRESSION.md`
Evidence scan: `docs/upstream/scans/2026-09-24-editorial-writing-capability-pack.md`

## Purpose

Provide a source-grounded editorial system for blog posts, articles, website copy, product/ecommerce content, technical documentation, UX/microcopy, SEO/AEO content, newsletters, social copy, scripts, case studies, thought leadership, reports and editorial review.

The engine separates creation from review. A strong draft is not a verified publication artifact until the task-relevant truth, structure, voice, search/accessibility and mechanical checks are complete.

## Stable-routing contract

No new stable identity is created. Stable count remains **52**.

User-facing JIT aliases:
`@Writing`, `@Editor`, `@BlogEditor`, `@Copywriter`, `@TechnicalWriter`, `@UXWriter`, `@SEOContentEditor`.

These aliases compose the smallest sufficient roles described by the skill and map onto existing Orchestrator, brand, SEO/AEO, social, web/frontend, platform, accessibility and QA owners.

## Intake contract

Before material writing/editing, resolve from available context:

- content type and destination/channel;
- primary audience and reader state;
- objective and desired reader action/outcome;
- authoritative source material and freshness needs;
- brand voice/tone and forbidden/required terminology;
- language/locale;
- search intent/SEO/AEO requirements when relevant;
- length/format/markup/CMS constraints;
- claims requiring evidence;
- approval/publishing boundary.

Do not ask for information that is already in project context or authoritative source files.

## Editorial passes

### 1. Brief / strategy
Define audience, job-to-be-done, core point, evidence, format and channel. Reject content briefs whose only purpose is generating search traffic without reader value.

### 2. Research / source map
Collect current reliable sources for externally verifiable claims when research is requested or required. Mark what came from user/project sources versus external sources.

### 3. Draft
Write for the target reader and channel. Do not optimize sentences for imagined detectors or algorithms at the expense of clarity and truth.

### 4. Developmental edit
Check thesis, usefulness, missing evidence, sequencing, redundancy and whether entire sections should be cut/rebuilt.

### 5. Structural edit
Repair hierarchy, headings, section order, paragraph topic flow, tables/lists and scanability.

### 6. Fact / citation edit
Verify names, dates, quantities, claims, product behavior and quotations. Ensure citations support the precise claims they accompany.

### 7. Brand / channel / search edit
Apply project voice, terminology and channel conventions. SEO/AEO improvements follow the content's real purpose and evidence; no keyword stuffing, synthetic fan-out page creation or ranking guarantees.

### 8. Line / copy edit
Improve sentence clarity, specificity, rhythm, grammar, consistency and punctuation while preserving meaning/voice.

### 9. Accessibility / localization
Apply only as material: heading/link/alt/instruction clarity, cognitive readability, translation readiness and locale terminology.

### 10. Proofread
Mechanical final pass after all substantive changes. Re-proof if later edits occur.

### 11. Independent editorial review
Check the actual final artifact against the brief, source map and publication requirements.

## Fact-control policy

- Never generate fake citations or unverifiable numerical precision.
- Never transform a weak source into a strong claim.
- If sources disagree, reflect the disagreement or narrow the statement.
- Marketing copy may be persuasive but cannot convert aspiration into fact.
- Case studies require verified project/customer facts; no invented lift, revenue, conversion, adoption or testimonial language.
- Technical docs must be reconciled against current code/API/CLI/runtime evidence when available.

## People-first / originality policy

Google's current Search guidance is embedded into the editorial engine:
- content exists primarily to help the intended audience;
- search optimization helps people discover useful content rather than defining the content's reason to exist;
- scaled AI-generated or scraped/synonymized content with little original value is prohibited as an editorial pattern;
- substantial automation should not hide weak sourcing or absent expertise.

Originality means useful original contribution, synthesis or firsthand/project evidence—not merely paraphrasing existing pages.

## Voice policy

A brand's `BRAND.md`/approved project voice is the primary style source. Generic style guides are fallback references.

Voice is relatively stable; tone adapts to context, channel and reader state. The same brand may sound different in:
- an error message;
- a premium landing page;
- a technical guide;
- an outreach email;
- a social caption;
- a crisis/operational notice.

Do not create one universal “AI house voice”.

## Technical writing policy

Use official Google/Microsoft technical-writing principles as general references:
- audience first;
- key point early;
- consistent terminology;
- specific nouns/strong verbs;
- short focused sentences/paragraphs;
- active voice when clearer;
- helpful lists/tables;
- explicit prerequisites, steps, verification and failure states;
- preserve accurate commands/API names/versions.

Source code, current CLI help, tests and version-matched docs outrank generic wording patterns.

## Web content policy

W3C/WAI principles apply:
- meaningful headings and unique titles;
- descriptive links;
- meaningful alt text;
- clear instructions;
- readable/concise prose;
- no dependence on visual direction alone.

For CMS/Markdown:
- preserve semantic heading levels;
- frontmatter/schema fields must remain valid;
- links/assets must resolve;
- structured fields should not be duplicated into bloated prose.

## Tool-selection policy

- Vale: project-owned terminology/house-style enforcement; strong default for docs/content CI when the project benefits.
- textlint/retext: programmable language-specific rules/transforms.
- markdownlint: Markdown structure/style, not prose quality.
- CSpell: spelling/terminology dictionary; not semantic correctness.
- alex: considerate-language advisory; do not auto-apply every suggestion without context.
- proselint/write-good-style checks: optional English prose heuristics; never authority over project voice.
- lychee/link checker: link integrity only; passing links do not verify the claims behind them.

No linter can replace editorial judgment, fact checking or independent review.

## Verification matrix

Select the smallest sufficient set:

`brief check -> source/fact check -> citation check -> developmental/structural review -> brand/channel review -> SEO/AEO review -> accessibility -> localization -> prose/style lint -> Markdown/schema lint -> spell/terminology -> link integrity -> proofread -> independent editorial review`.

Not every artifact needs every gate.

## Completion vocabulary

- `VERIFIED`: final current text passes all task-relevant editorial/source/format checks.
- `PARTIAL`: usable work exists but a material source, approval or verification surface remains.
- `BLOCKED`: missing source/access/decision prevents a required editorial gate.
- `NOT VERIFIED`: draft/advice exists without required final evidence/review.
