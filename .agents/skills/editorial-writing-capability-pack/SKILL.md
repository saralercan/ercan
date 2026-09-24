---
name: editorial-writing-capability-pack
description: Route material writing, editing, blog, article, website copy, technical writing, UX/microcopy, SEO/AEO content, product/ecommerce copy, newsletter, social copy, scripts, case studies, thought leadership, fact-checking, citations, proofreading, accessibility and localization through a source-grounded editorial pipeline. Use for creating, rewriting, editing, reviewing, optimizing or publishing text where accuracy, brand voice, readability, search visibility or editorial quality matters.
---

# Editorial & Writing Capability Pack

Load `docs/standards/EDITORIAL_WRITING_ENGINE.md`, root `AGENTS.md`, `docs/standards/AGENT_REGISTRY.md`, the active project adapter, approved brand/voice sources and task-relevant SEO/social/platform standards.

This is a JIT capability pack. It does **not** add stable routing identities or change the 21 Stable Core + 31 GitHub Specialist v3 Extension = 52 accounting.

User-facing aliases such as `@Writing`, `@Editor`, `@BlogEditor` and `@Copywriter` resolve to the smallest sufficient editorial pod.

## Editorial roles and stable-owner mapping

Use only roles that materially contribute:

- `EditorialStrategist` -> `@Orchestrator + @BrandBehavior` plus channel/search owner as needed; audience, objective, editorial brief, content type, evidence requirements and approval path.
- `ResearchWriter` -> `@Orchestrator + @UpstreamIntelligence` when current/public research is required; source map before factual drafting.
- `BlogWriter` -> `@BrandBehavior + @TechnicalSEO/@AEO_GEO` when discovery is material; articles, guides, editorial posts and evergreen blog content.
- `LongformWriter` -> `@BrandBehavior + @ProductionQA`; reports, essays, whitepapers, deep guides and narrative business content.
- `TechnicalWriter` -> active domain/platform specialist + `@ProductionQA`; documentation, tutorials, README, API/use guides, troubleshooting, release notes and SOP-style technical content.
- `WebsiteCopywriter` -> `@BrandBehavior + @FrontendSystem` with `@TechnicalSEO`/CRO owner as needed; homepage, landing, service, about, pricing, CTA and conversion copy.
- `ProductCopywriter` -> `@BrandBehavior` + platform/product owner; benefit-led product/service descriptions grounded in verified attributes.
- `EcommerceContentEditor` -> `@ShopifyExpert` or active commerce owner + `@ShopifySEO/@TechnicalSEO`; titles, descriptions, collections, taxonomy and merchandising copy.
- `UXWriter` -> `@FrontendSystem + @AccessibilityQA + @BrandBehavior`; labels, buttons, forms, errors, empty states, onboarding, consent and system microcopy.
- `SEOContentEditor` -> `@TechnicalSEO + @ContentOpportunityAgent`; search intent, topical completeness, titles/headings/internal links and query language without keyword stuffing.
- `AEOContentEditor` -> `@AEO_GEO + @SchemaEntityArchitect`; answerability, entity clarity, concise evidence-led passages and AI/search discoverability without synthetic query-spam.
- `BrandVoiceEditor` -> `@BrandBehavior + @BrandComplianceQA`; voice, tone, vocabulary, message hierarchy and project-specific do/don't enforcement.
- `DevelopmentalEditor` -> `@Orchestrator + @ProductionQA`; thesis, audience fit, missing sections, sequencing, evidence gaps and major cuts/additions.
- `StructuralEditor` -> `@ProductionQA`; hierarchy, section order, headings, paragraph flow and scanability without line-level polishing theater.
- `LineEditor` -> `@BrandBehavior + @ProductionQA`; sentence rhythm, clarity, specificity, concision and human prose while preserving meaning.
- `CopyEditor` -> `@ProductionQA`; grammar, usage, terminology, consistency, capitalization, punctuation, numbers and house-style conformance.
- `Proofreader` -> independent final `@ProductionQA`; typos, duplicated/missing words, punctuation/formatting defects and last-pass mechanical errors.
- `FactChecker` -> `@Orchestrator` plus task-domain specialist; verify material claims, dates, names, numbers, product behavior and quoted assertions against sources.
- `CitationEditor` -> `@Orchestrator + @ProductionQA`; source-to-claim mapping, citation completeness, quotation limits and link/source integrity.
- `OriginalityEditor` -> `@ProductionQA + @BrandComplianceQA`; prevent stitched/synonymized/derivative copy, preserve original contribution and flag close imitation.
- `AccessibilityContentEditor` -> `@AccessibilityQA`; plain language, heading structure, descriptive links, alt-text quality, instructions and cognitive readability.
- `LocalizationEditor` -> active locale/platform owner + `@BrandBehavior`; translation-ready source, locale adaptation, terminology consistency and cultural neutrality where required.
- `StructuredContentEditor` -> `@FrontendSystem` or CMS/platform owner + `@ProductionQA`; Markdown/MDX/CMS fields/frontmatter/reusable content models and semantic structure.
- `NewsletterEditor` -> `@BrandBehavior + @SocialStrategy` or email owner; newsletter structure, subject/preheader/body/CTA and channel-appropriate cadence/voice.
- `SocialCopyEditor` -> `@SocialStrategy + @BrandBehavior`; platform-native captions, hooks, threads, short-form copy and reuse without blind cross-posting.
- `ScriptWriter` -> `@SocialStrategy + @BrandBehavior`; video/podcast/reel/voiceover scripts with spoken-language rhythm and production cues.
- `CaseStudyWriter` -> `@BrandBehavior + @ProductionQA`; problem/intervention/evidence/outcome narratives using only verified customer/project facts.
- `ThoughtLeadershipWriter` -> `@BrandBehavior + ResearchWriter`; point-of-view content with explicit evidence and no fabricated expertise.
- `CorporateCommsEditor` -> `@BrandBehavior + @ProductionQA`; announcements, statements and internal/external company communications.
- `ContentRefreshEditor` -> `@TechnicalSEO + @SEOScanner + @BrandBehavior`; updates stale/decaying articles/pages while preserving working intent, source truth and useful existing value.
- `HeadlineTitleEditor` -> `@BrandBehavior` plus `@TechnicalSEO` when search-facing; accurate titles, headlines, subject-like hooks and metadata without clickbait drift.
- `ReadabilityEditor` -> `@BrandBehavior + @AccessibilityQA`; plain language, paragraph load, information density, scanability and comprehension without flattening necessary technical detail.
- `ContentRepurposingEditor` -> `@ContentRecycling + @BrandBehavior`; turns validated source content into platform-native derivatives without inventing new facts.
- `DocumentationEditor` -> active domain/platform specialist + `@ProductionQA`; restructures documentation around reader goals, prerequisites, procedures, examples, verification and failure modes.
- `HelpCenterWriter` -> active product/platform owner + `@AccessibilityQA`; help-center and knowledge-base articles optimized for task completion, searchability and support deflection without hiding limitations.
- `FAQEditor` -> `@BrandBehavior + @AEO_GEO` when discovery matters; selects real user questions, removes duplicate/contrived questions and writes direct evidence-grounded answers.
- `EmailCopywriter` -> `@BrandBehavior + @ProductionQA`; lifecycle, transactional-content, campaign and announcement copy. Sending/auth/consent/deliverability remain separate systems.
- `AdCopywriter` -> `@AdsCreativeStrategist + @BrandBehavior`; ad headlines/body/CTA variants grounded in the verified offer and platform constraints; no fabricated scarcity or outcomes.
- `OutreachCopyEditor` -> `@BrandBehavior + @Orchestrator`; research-led B2B/outreach messages and follow-ups. Recipient research, sending approval and mailbox actions remain separate workflows.
- `ProposalWriter` -> `@BrandBehavior + @Orchestrator + @ProductionQA`; proposals, scopes, capability statements and commercial narratives grounded in verified pricing/deliverables.
- `PressReleaseWriter` -> `@BrandBehavior + @ProductionQA`; press releases/media statements with clear news value, attributable facts and no invented quotes.
- `InterviewTranscriptEditor` -> `@ProductionQA + @BrandBehavior`; cleans interviews/transcripts for readability while preserving speaker meaning and clearly marking substantive edits/omissions when needed.
- `StyleGuideEditor` -> `@BrandBehavior + @BrandComplianceQA`; creates/maintains project house style, terminology, voice examples, forbidden phrases and editorial conventions from approved sources.
- `TerminologyEditor` -> `@BrandBehavior + task-domain specialist`; canonical terms, capitalization, spelling, product/API names and glossary consistency; can emit Vale/CSpell dictionaries when useful.
- `EditorialCalendarStrategist` -> `@Orchestrator + @SocialStrategy + @TechnicalSEO` as relevant; topic portfolio, cadence, pillar/cluster balance, refresh-vs-new decisions and evidence requirements without content-farm volume goals.
- `EditorialReviewer` -> independent `@ProductionQA + @BrandComplianceQA`; checks brief, truth, structure, voice, usefulness, accessibility/search constraints and readiness after writing/editing passes.

## Default editorial workflow

`brief -> source intake/research -> outline -> draft -> developmental/structural edit -> fact/citation check -> brand/search/channel edit -> line/copy edit -> accessibility/localization checks as needed -> proofread -> independent EditorialReviewer -> publish-ready state`.

Do not run every role on trivial text. Do not let the primary writer self-certify material work.

## Source and truth contract

- User-provided/project-approved source material is authoritative for user-specific facts.
- Current or time-sensitive claims require current reliable sources when research is in scope.
- Never invent statistics, customer results, quotes, dates, credentials, product behavior, case-study outcomes or citations.
- Distinguish verified facts, attributed claims, estimates and editorial opinion.
- Preserve a source map for material long-form/report/blog claims when factual defensibility matters.
- Quotation and paraphrase must respect source/copyright limits; do not stitch third-party prose into synthetic original-looking content.
- If evidence is missing, narrow, qualify or remove the claim rather than writing around the gap.

## Writing quality contract

- Lead with the reader's need, outcome or main point; avoid throat-clearing.
- Prefer specific nouns and strong verbs over vague abstractions.
- Keep paragraphs purposeful and scannable; one primary idea per paragraph is a strong default.
- Use active voice when it improves clarity, not as an absolute rule.
- Remove filler, grandiose claims, repetitive summaries, generic AI transitions and visible framework scaffolding.
- Preserve the author's/project's distinctive voice; editing must not flatten every piece into the same polished generic style.
- Marketing frameworks such as AIDA/PAS/BAB may guide structure, but should not be visible as formulaic prose.
- Technical content must preserve commands, API names, version facts and trade-offs.
- UX copy must make the action/state/error understandable without relying on visual position alone.

## Search / AI discovery contract

Google Search's current guidance remains authority:
- create helpful, reliable, people-first content;
- use relevant search language naturally in prominent places;
- do not generate large volumes of low-value pages for ranking manipulation;
- generative AI may assist research/structure/drafting, but scaled unoriginal content without user value is not acceptable.

SEO/AEO optimization is a refinement pass over useful content, not the purpose of the content itself.

## Accessibility contract

For web content, follow current W3C/WAI principles:
- informative unique titles;
- meaningful semantic headings;
- descriptive link text instead of vague “click here” wording;
- useful text alternatives where images convey information;
- clear instructions;
- concise, understandable language;
- do not rely only on visual direction/position to convey meaning.

## Localization contract

- Write source text that can be translated cleanly: consistent terminology, fewer idioms, controlled ambiguity and clear referents.
- Localization may adapt examples, units, tone and cultural references when the project requires it.
- Never mix machine-translated fragments with approved terminology without review.
- Preserve brand terms/product names exactly when project sources require them.

## Editorial tooling

Select only when compatible with the project:
- `vale-cli/vale` — ADOPT — MIT; house-style/terminology prose linting across markup, configurable with project-owned rules and available Google/Microsoft packages.
- `textlint/textlint` — ADOPT_WHEN_NEEDED — MIT; pluggable natural-language linting for Markdown/plain text and supported formats.
- `retextjs/retext` — ADOPT_WHEN_NEEDED — MIT; AST/CST-based natural-language transforms, readability/spelling/equality plugins.
- `DavidAnson/markdownlint` — ADOPT — MIT; Markdown/CommonMark consistency and structural lint.
- `streetsidesoftware/cspell` — ADOPT_WHEN_NEEDED — MIT; spelling/terminology dictionaries for code/docs; follow current supported runtime line.
- `get-alex/alex` — ADOPT_WHEN_NEEDED — MIT; considerate/inclusive-language warnings, advisory rather than automatic truth.
- `amperser/proselint` — ADOPT_PATTERN_OR_OPTIONAL — BSD; English prose suggestions; use only when language fit and maintenance/runtime fit are acceptable.
- `lycheeverse/lychee` — existing link-integrity reference for checking published Markdown/HTML links.
- `doeixd/writing-skill` — PATTERN_ONLY — blog voice/flow/anti-generic-AI editing patterns; low adoption, never an authority.
- `vercel/eve:technical-writing` — PATTERN_ONLY — source/test/CLI-grounded technical documentation workflow.
- `eigent-ai/agent-skills:copywriting` and comparable marketing skill packs — PATTERN_ONLY — conversion-copy decomposition; project brand/product truth overrides formulas.
- `shalintripathi/saas-marketing-agents:content-marketing` — PATTERN_ONLY — editorial operations/content-calendar/SME workflow ideas.
- `Qiyao313/editorial-ai` — PATTERN_ONLY — source-grounded serious long-form editorial workflow ideas.

## Authority references

Use current official guidance as applicable:
- Google Search Central — people-first, reliable content, generative-AI and spam/scaled-content policies.
- Google Technical Writing — audience, clarity, concision, active voice, paragraph/list structure and self-editing.
- Microsoft Writing Style Guide — technical/product terminology, concise user-centered writing and localization-aware style.
- Mailchimp Content Style Guide — voice/tone separation, structured content, web/newsletter/social writing patterns.
- W3C/WAI — accessible web writing and semantic content structure.

Project-owned brand/style rules outrank generic style-guide preferences when they do not conflict with accuracy, safety or accessibility.

## Completion gate

A material editorial artifact is `VERIFIED` only when:
- requested content/format is complete;
- material factual claims are sourced or traceable as required;
- writer and independent reviewer are separated for consequential work;
- brand/channel/search rules actually used are identified;
- no fabricated evidence/citations remain;
- accessibility/locale/Markdown/link gates relevant to the artifact pass;
- final proofread/review is based on the current final text, not an earlier draft.

Otherwise report `PARTIAL`, `BLOCKED` or `NOT VERIFIED`.
