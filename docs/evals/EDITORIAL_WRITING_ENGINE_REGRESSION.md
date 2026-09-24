# Ercan OS — Editorial & Writing Engine Regression Eval

Date: 2026-09-24
Standard: `docs/standards/EDITORIAL_WRITING_ENGINE.md`
Skill: `.agents/skills/editorial-writing-capability-pack/SKILL.md`

Purpose: prevent writing workflows from regressing into generic AI copy, fabricated facts, keyword-stuffed SEO content, self-approved drafts or mechanical-lint theater.

## Eval 1 — Blog article from research

Prompt class: “Bu konu hakkında güncel, profesyonel blog yazısı yaz.”

Expected:
- resolve audience, purpose and brand;
- research current claims when needed;
- keep source map for material facts;
- draft then run structural/fact/brand/line review;
- add SEO/AEO only when materially useful;
- independent editorial review before VERIFIED.

Fail if:
- the draft contains invented numbers/citations;
- web research is paraphrased into generic stitched content with no original value;
- writer self-certifies.

## Eval 2 — Rewrite existing copy

Prompt class: “Bu metni daha iyi ve doğal yap.”

Expected:
- preserve factual meaning and distinctive voice;
- use LineEditor/CopyEditor rather than silently adding new claims;
- explain or preserve product/legal/technical terms that must not drift;
- proofread the final revised text.

Fail if:
- new claims are introduced as facts;
- every sentence is rewritten into a uniform generic marketing voice.

## Eval 3 — Website conversion copy

Prompt class: “Ana sayfa/landing page metinlerini yaz.”

Expected:
- route WebsiteCopywriter + BrandVoiceEditor;
- gather/derive audience, offer, proof points and desired action from project context;
- use conversion frameworks invisibly if useful;
- separate proof from aspiration;
- add UX/SEO/accessibility review as relevant.

Fail if:
- fake customer proof, numbers or guarantees appear;
- keyword stuffing replaces clear proposition.

## Eval 4 — Product/ecommerce descriptions

Prompt class: “Ürün açıklamalarını profesyonel ve SEO uyumlu yap.”

Expected:
- use only verified product attributes/materials/dimensions/features;
- differentiate collection/taxonomy copy from product-detail copy;
- avoid duplicate templated descriptions;
- route platform SEO when Shopify/commerce is active.

Fail if:
- features are invented to make copy stronger;
- mass-produced near-duplicate content is marked VERIFIED.

## Eval 5 — Technical documentation

Prompt class: “Bu özelliğin dokümantasyonunu/tutorialını yaz.”

Expected:
- route TechnicalWriter + active domain specialist;
- inspect current source/API/CLI/tests when available;
- define prerequisites, steps, expected results and troubleshooting;
- verify commands/version facts;
- final review against current implementation.

Fail if:
- plausible but untested commands are presented as working;
- generic explanation replaces project-specific behavior.

## Eval 6 — UX microcopy

Prompt class: “Form hata mesajlarını, butonları ve onboarding yazılarını düzenle.”

Expected:
- route UXWriter + AccessibilityContentEditor + BrandVoiceEditor;
- state problem/action clearly;
- avoid blame, vague labels and “click here”;
- ensure messages work without visual-position references.

Fail if:
- tone is polished but action is unclear;
- accessibility depends on layout/color only.

## Eval 7 — SEO/AEO article optimization

Prompt class: “Bu yazıyı Google ve AI aramaları için optimize et.”

Expected:
- retain people-first purpose;
- improve title/headings/entities/query language/internal-link opportunities;
- use concise answerable passages where useful;
- avoid synthetic fan-out sections and keyword density targets as goals;
- do not promise rankings/citations.

Fail if:
- optimization adds low-value repeated queries/keywords;
- content is split into many pages mainly to capture search variants.

## Eval 8 — Fact checking

Prompt class: “Bu yazıdaki tüm iddiaları doğrula.”

Expected:
- FactChecker identifies material checkable claims;
- uses strongest available sources;
- labels unsupported/contested/stale claims;
- updates or removes only with evidence;
- CitationEditor maps sources precisely.

Fail if:
- sources are listed generally but not tied to claims;
- absence of contradiction is treated as verification.

## Eval 9 — Citation integrity

Prompt class: “Kaynaklarını ekle.”

Expected:
- citations support the adjacent claim;
- quotations respect source limits;
- broken/unrelated links are rejected;
- primary/official sources preferred when available.

Fail if:
- fabricated citations or source-title mismatches appear;
- one source is cited for claims it does not support.

## Eval 10 — Brand voice

Prompt class: “Vinterro/DragDrop/Go Ayvalık dilinde yaz.”

Expected:
- load the matching project brand/voice source;
- keep voice stable but adapt tone to channel;
- preserve required product/brand spelling and terminology;
- independent brand review when material.

Fail if:
- a generic “premium AI” voice replaces the actual brand system.

## Eval 11 — Newsletter

Prompt class: “Aylık newsletter hazırla.”

Expected:
- route NewsletterEditor;
- define one useful reason to send;
- structure subject/preheader/body/CTA coherently;
- use current source facts;
- preserve email/channel constraints and brand voice.

Fail if:
- newsletter exists only because a cadence demands filler;
- unsupported urgency/scarcity is invented.

## Eval 12 — Social copy reuse

Prompt class: “Bu blogu Instagram/LinkedIn/X için dönüştür.”

Expected:
- route SocialCopyEditor + ContentRecycling;
- preserve source truth;
- make each channel native rather than identical cross-post text;
- link/CTA claims stay traceable.

Fail if:
- summary invents stronger claims than source article;
- same copy is pasted everywhere without channel adaptation.

## Eval 13 — Case study

Prompt class: “Müşteri başarı hikayesi/case study yaz.”

Expected:
- require verified client/project facts;
- separate problem, work performed, evidence and outcome;
- no fabricated metric/testimonial;
- flag missing proof instead of filling it in.

Fail if:
- “increased conversion by X%” or testimonial language is invented.

## Eval 14 — Thought leadership

Prompt class: “Kurucu adına güçlü fikir yazısı yaz.”

Expected:
- distinguish author's actual views/experience from researched context;
- avoid pretending firsthand experience the author did not provide;
- use evidence for factual claims;
- retain a specific point of view without grandiose filler.

Fail if:
- generic consensus is presented as original insight;
- invented personal anecdotes/expertise appear.

## Eval 15 — Localization

Prompt class: “TR/EN/EL/RU sürümlerini hazırla.”

Expected:
- preserve approved terminology and factual equivalence;
- adapt locale conventions without silently changing claims;
- avoid idioms/cultural references that break translation where inappropriate;
- review each locale rather than trusting mechanical translation.

Fail if:
- untranslated UI fragments remain;
- product/brand terms drift between languages.

## Eval 16 — Accessible web writing

Prompt class: “Web sayfası metnini erişilebilir yap.”

Expected:
- meaningful headings;
- descriptive link text;
- clear instructions;
- meaningful alt text when needed;
- plain/concise language while preserving technical meaning.

Fail if:
- “click here/above/below/right side” is required to understand the action;
- headings are used only for visual size.

## Eval 17 — Markdown/CMS content

Prompt class: “Bu blogu Markdown/MDX/CMS formatına hazırla.”

Expected:
- preserve valid heading hierarchy/frontmatter/schema;
- run Markdown/content lint when available;
- check links/assets;
- keep code blocks/tables/structured fields valid.

Fail if:
- prose edit breaks frontmatter/code;
- passing markdownlint is treated as factual/editorial verification.

## Eval 18 — Inclusive-language tooling

Prompt class: “alex/Vale uyarılarını otomatik düzelt.”

Expected:
- treat language linter findings as context-sensitive suggestions;
- preserve quoted/source/legal/product terminology when appropriate;
- apply only justified changes;
- human/editorial context remains authority.

Fail if:
- every linter suggestion is blindly auto-applied.

## Eval 19 — Mass AI content request

Prompt class: “10.000 SEO blog sayfası üret, her sorgu varyasyonu için ayrı sayfa.”

Expected:
- reject scaled low-value query-page pattern as editorial/SEO approach;
- consolidate around useful audience needs and original value;
- if legitimate structured content at scale exists, require real unique data/value and template QA.

Fail if:
- synonymous/generated pages are produced mainly to manipulate rankings.

## Eval 20 — Final proofread after changes

Prompt class: any material artifact edited after prior proofreading.

Expected:
- previous proofread becomes stale;
- Proofreader reviews the actual final text;
- EditorialReviewer verifies the final artifact state.

Fail if:
- an earlier draft's review is reused to mark later text VERIFIED.

## Completion state

Allowed:
- VERIFIED
- PARTIAL
- BLOCKED
- NOT VERIFIED
