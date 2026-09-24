# Editorial & Writing Capability Pack — Upstream Scan

Date: 2026-09-24
Scope: writing agents/skills, blog/editorial workflows, copywriting, technical writing, prose linting, accessibility, SEO/AEO content and editorial quality systems.

## Decision

Create a JIT Editorial & Writing Capability Pack rather than adding permanent writer/editor identities. Separate authoring, editing, fact/citation checking and final review. Stable routing count remains 52.

## Agent/workflow references

### vercel/eve technical-writing — ADOPT_PATTERN_ONLY
A strong repo-grounded technical-writing workflow: new-page/edit/review/style paths, with source/tests/CLI/releases treated as truth. Valuable for documentation verification patterns, not a general editorial authority.

### gwagjiug/technical-writing — ADOPT_PATTERN_ONLY
Developer-facing technical-writing skill with document-type selection, structure principles, sentence style, review rubrics and templates. Useful decomposition/reference; project runtime remains authoritative.

### eigent-ai/agent-skills copywriting — ADOPT_PATTERN_ONLY
Marketing-copy workflow focused on product, audience, offer, channel, proof and objections. Frameworks such as AIDA/PAS/BAB are optional internal scaffolds, not output templates.

### shalintripathi/saas-marketing-agents content-marketing — ADOPT_PATTERN_ONLY
Useful editorial-operations patterns: blogs, whitepapers, case studies, newsletters, scripts, thought leadership, content briefs/calendars, SME workflow, inventories and governance. SaaS assumptions must not be generalized automatically.

### msimchowitz/writing-skills general-writing — ADOPT_PATTERN_ONLY
Strong “preserve meaning and personal voice” editing pattern and anti-generic-AI review. Do not use AI-tell heuristics to claim authorship detection.

### getburo/buro-free editor — ADOPT_PATTERN_ONLY
Useful separation of editing existing text from originating prose; developmental/structural/line-edit concepts support the independent editorial pipeline.

### richtabor/agent-skills red-pen — ADOPT_PATTERN_ONLY
Strict line/copy-edit review patterns for flab, vagueness and typography. Tone/style opinions remain subordinate to project voice.

### doeixd/writing-skill — WATCH/PATTERN_ONLY
Blog voice/flow/specificity and anti-generic-AI patterns. Very small adoption footprint; use ideas only, never production authority.

### Qiyao313/editorial-ai — ADOPT_PATTERN_ONLY
Source-grounded/fact-controlled long-form editorial decomposition. Useful for serious report/article workflow ideas, subject to source/license review before any code vendoring.

### Debanitrkl/technical-writing-automation — ADOPT_PATTERN_ONLY
Blog workflow, review-writing and SEO/AEO skill decomposition. Useful as a pattern for content pipeline/checklists; project-specific assumptions should not be copied wholesale.

## Prose/editorial tooling

### vale-cli/vale — ADOPT
- MIT, active.
- Markup-aware prose linter for team style/terminology.
- Project-owned YAML rules/styles make it suitable for brand/product terminology.
- Current package ecosystem includes Google and Microsoft-compatible style packages.
- Vale checks style consistency, not factual truth or general semantic correctness.

### textlint/textlint — ADOPT_WHEN_NEEDED
- Pluggable natural-language linter.
- Markdown/plain text built in; plugins support HTML and more.
- No default rules: project must deliberately choose rule packs.
- Strong fit for language-specific/custom content lint pipelines.

### retextjs/retext — ADOPT_WHEN_NEEDED
- MIT, Unified ecosystem.
- Natural-language syntax tree and plugin architecture.
- Useful plugins cover readability, spelling, equality and transformations.
- Plugin quality/maintenance must be reviewed individually.

### DavidAnson/markdownlint — ADOPT
- MIT.
- CommonMark/GFM-aware Markdown consistency and structural lint.
- Does not evaluate prose quality or factual claims.

### streetsidesoftware/cspell — ADOPT_WHEN_NEEDED
- MIT.
- Active spell/terminology checker, including code/docs dictionaries.
- Runtime support is versioned; current project Node compatibility must be checked.
- Project dictionaries can encode product/brand terminology.

### get-alex/alex — ADOPT_WHEN_NEEDED
- MIT.
- Flags potentially insensitive/inconsiderate phrasing across text/Markdown/MDX/HTML.
- Advisory only; context and literal/quoted terms matter.

### amperser/proselint — OPTIONAL/PATTERN
- BSD.
- English prose usage/style suggestions.
- Use only for English and only when it adds value beyond project Vale/retext rules.

### lycheeverse/lychee — EXISTING ADOPT
- Link integrity for Markdown/HTML and related formats.
- Valid link response does not verify the claim behind the link.

## Editorial authority layer

### Google Search Central
Current guidance emphasizes helpful, reliable, people-first content. Search language belongs naturally in prominent page locations, but content created primarily to manipulate rankings is not aligned with Search guidance. Generative AI can assist research/structure/content work, but large-scale unoriginal AI/scraped/synonymized pages can violate scaled-content-abuse policy.

### Google Technical Writing
Strong general technical-writing authority for audience definition, consistent terminology, active voice where useful, specific nouns/verbs, focused sentences/paragraphs, list structure and self-editing.

### Microsoft Writing Style Guide
Strong reference for technology/product writing, terminology consistency, concise user-centered copy, global/localization-aware phrasing and documentation voice.

### Mailchimp Content Style Guide
Strong reference for separating stable voice from situational tone; useful patterns for structured content, web accessibility, social copy and newsletters. Its public guide is brand-specific, so rules should be adapted rather than copied blindly.

### W3C/WAI
Authority for accessible web-content practices: unique/informative titles, semantic headings, meaningful link text, useful alternatives, clear instructions and clear/concise language.

## Routing design

User-facing aliases:
- @Writing
- @Editor
- @BlogEditor
- @Copywriter
- @TechnicalWriter
- @UXWriter
- @SEOContentEditor

JIT roles:
EditorialStrategist, ResearchWriter, BlogWriter, LongformWriter, TechnicalWriter, WebsiteCopywriter, ProductCopywriter, EcommerceContentEditor, UXWriter, SEOContentEditor, AEOContentEditor, BrandVoiceEditor, DevelopmentalEditor, StructuralEditor, LineEditor, CopyEditor, Proofreader, FactChecker, CitationEditor, OriginalityEditor, AccessibilityContentEditor, LocalizationEditor, StructuredContentEditor, NewsletterEditor, SocialCopyEditor, ScriptWriter, CaseStudyWriter, ThoughtLeadershipWriter, CorporateCommsEditor, EditorialReviewer.

These map to existing stable/JIT owners and do not add permanent routing identities.

## Hard boundaries

- No fabricated facts, citations, customer outcomes or quotations.
- No mass low-value SEO page generation or scraped/synonymized content farming.
- No claim that style/prose linters verify truth.
- No blind auto-fix of inclusive-language/style suggestions.
- No close imitation/copying of third-party protected prose.
- No writer self-certification for consequential publication artifacts.
