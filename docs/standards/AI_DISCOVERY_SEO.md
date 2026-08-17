# Ercan OS — AI Discovery, SEO, Entity & Search Visibility Standard

Version: 1.0 (2026-08-18)

This standard applies whenever an Ercan OS agent works on SEO, metadata, structured data, local discovery, ecommerce discovery, AI-search visibility, answer-engine visibility, content architecture, reputation/mentions, search measurement, or agent-friendly web surfaces.

## 1. No ranking guarantees / no GEO magic
- Never promise that a brand will rank first or be named by ChatGPT, Google AI Overviews/AI Mode, Perplexity, Bing/Copilot, Claude, or another answer engine.
- Treat AI discovery as an extension of strong search/entity/content engineering, not a bag of ranking hacks.
- For Google generative search, foundational SEO remains the primary path: indexability, helpful/non-commodity content, page experience, business/product data, and Search quality systems.
- Do not create doorway pages, scaled near-duplicate query pages, fake reviews, fake awards, fake citations, fake mentions, link schemes, or keyword-stuffed AI-only content.
- `llms.txt` is optional/experimental interoperability metadata. Google explicitly does not require or use it for ranking in Search/AI features. Do not sell it as a Google ranking factor.

## 2. Search discovery stack
The default stack is:
`crawlability → indexability → canonical entity → information architecture → intent-relevant pages → structured data → business/product feeds → evidence/authority → external corroboration → measurement → iteration`.

A page cannot become a reliable AI/search source if crawlers cannot access it, search engines cannot index it, the entity is ambiguous, or the page lacks useful evidence.

## 3. Crawler policy
### Google/Bing
- Keep important public pages crawlable/indexable unless there is a specific reason not to.
- Maintain valid `robots.txt`, XML sitemap(s), canonical URLs, status codes, internal links and noindex rules.
- Use Search Console and Bing Webmaster Tools for diagnosis.
- For frequently changing URLs, evaluate IndexNow where technically appropriate; it is a discovery notification mechanism, not a ranking guarantee.

### OpenAI
- If the business wants eligibility for ChatGPT Search citations/snippets, do not block `OAI-SearchBot` on public discovery pages.
- `GPTBot` is a separate training-related control; allowing Search does not require allowing training.
- Verify CDN/WAF/bot protection does not unintentionally block OpenAI published crawler IPs.
- Track ChatGPT referral traffic where available; preserve `utm_source=chatgpt.com` attribution.

### Perplexity
- If visibility in Perplexity is desired, allow `PerplexityBot` for public discovery pages and ensure the WAF/CDN allows the published crawler ranges.
- Treat user-triggered fetchers and autonomous crawlers as distinct capabilities when configuring policy.

### Security
- Crawler allowlisting never means weakening private/admin/account/checkout/security paths.
- Public content and sensitive application surfaces should have separate access policies.

## 4. Entity clarity / canonical business graph
Every commercial brand should have a consistent machine-readable and human-readable identity.

Maintain, as applicable:
- canonical brand name and `alternateName`;
- canonical domain;
- logo/brand asset URL;
- contact methods;
- legal/business name where appropriate;
- physical/service-area address where truthful;
- telephone/email;
- founding/about information when useful;
- social/portfolio/profile URLs using `sameAs` only for real identity-equivalent profiles;
- brand/designer/manufacturer relationships;
- consistent NAP (name/address/phone) across website and trusted external profiles.

Do not create conflicting entity names across title tags, headings, schema, social accounts and Business Profiles.

## 5. Structured data contract
Use JSON-LD where appropriate and validate it. Prefer the most specific truthful Schema.org types and Google-supported rich-result properties where relevant.

Common types:
- `WebSite` — site name / alternate name / canonical URL.
- `Organization` or suitable subtype — brand/company identity, logo, contact, sameAs.
- `LocalBusiness` or specific subtype — real local/service-location business details.
- `OnlineStore` / Organization semantics for ecommerce brand identity where appropriate.
- `Product` + `ProductGroup` / variants — ecommerce products and variants.
- `BreadcrumbList` — hierarchy.
- `Article` / `BlogPosting` — authored editorial content with accurate dates/authorship.
- `ProfilePage` / Person/Organization — genuine designer/creator profile pages where appropriate.
- `VideoObject` — useful original video content where supported.

Rules:
- Structured data must match visible page content.
- No fabricated `Review`, `AggregateRating`, award or claim markup.
- Do not add schema solely because a third-party GEO tool gives points for it.
- Structured data helps machines understand entities and can enable rich results; it is not a guaranteed AI-answer ranking lever.

## 6. Google business/local visibility
For a real local or service business:
- Claim and verify the Google Business Profile.
- Keep primary/secondary categories truthful and current; verify current category/service options at runtime.
- Add real services/service items when supported.
- Maintain correct site, phone, hours, location/service area, photos and business description.
- Encourage genuine customer reviews without gating, fabrication or incentives that violate platform policy.
- Ensure website entity details match the Business Profile.

For recommendation-style queries such as “best ... near me”, candidate eligibility is strengthened by truthful local entity data, real reputation/reviews, relevant content and corroborating sources; self-proclaiming “best” is not evidence.

## 7. Ecommerce / design-store visibility
For Shopify/commerce projects:
- Use accurate `Product`/variant structured data and canonical product URLs.
- Keep product title, brand/designer, category, price, availability, image, variant and identifiers consistent between storefront, structured data and feeds.
- Use Google Merchant Center / product feeds where eligible and keep them fresh.
- Preserve shipping/return policies and organization/merchant data.
- Build meaningful designer/brand profile pages and internal links from products/collections to those entities.
- Build editorial buying guides, material/process stories, designer interviews and category expertise that add real value beyond product-grid copy.
- Avoid thin auto-generated collection descriptions and thousands of near-duplicate taxonomy pages.

## 8. Service-company / agency visibility
For agencies and service companies, build dedicated, useful service entities/pages rather than placing every keyword on the homepage.

A strong service page should usually answer:
- what the service is;
- who it is for / fit criteria;
- business outcomes;
- process/method;
- deliverables;
- technology/platform expertise;
- real work/case evidence;
- common constraints and questions;
- geographic/service coverage when truthful;
- next action / contact.

Recommended page families when actually offered:
- web design / website development;
- WordPress development;
- Shopify development/ecommerce;
- branding/brand identity;
- digital advertising / Google Ads / Meta Ads;
- social media management/creative;
- SEO/search optimization;
- photo/video/creative production;
- case studies / projects;
- about/team/expertise;
- contact/location/service area.

Do not generate one low-value city page for every Turkish city. Location pages require real local relevance, work, presence, clients, data or service context.

## 9. Content built to be useful and citable
Prefer first-hand, non-commodity evidence:
- original case studies with problem → work → measurable outcome;
- before/after with verifiable context;
- original photography/video/process documentation;
- founder/expert commentary;
- research, data, benchmarks or experiments the brand actually performed;
- designer/maker interviews and profiles;
- product/material provenance;
- transparent methodology;
- useful tables/checklists/definitions when they improve human comprehension;
- sources/citations for factual claims where relevant.

Do not manufacture statistics, quotations or third-party citations merely because GEO research finds that citations/statistics can improve source visibility in some experimental settings.

## 10. Recommendation-query strategy
Queries such as:
- “en iyi tasarım dükkanı”
- “reklam ajansları”
- “web site oluşturan şirket”
- “Shopify ajansı”
- “branding ajansı”

are recommendation/entity-retrieval queries, not merely keyword matches.

Optimize the candidate entity by strengthening:
1. category relevance;
2. entity clarity;
3. service/product depth;
4. geographic relevance when applicable;
5. first-party evidence/case studies;
6. genuine reviews and reputation;
7. authoritative third-party corroboration (press, interviews, client/partner pages, reputable directories/associations, creator/designer profiles);
8. technical crawl/index health;
9. freshness;
10. conversion/page experience.

Never build “we are the best” pages as the primary tactic. Earn the evidence that allows external/search/AI systems to make that recommendation.

## 11. External authority / corroboration
Prioritize authentic, relevant mentions over bulk backlink acquisition.
Good examples:
- clients naming/linking the agency on project/case pages where truthful;
- designers/makers linking their official DragDrop profile;
- reputable local/business/industry directories;
- press/editorial coverage;
- interviews/podcasts/events;
- portfolio platforms relevant to the discipline;
- Google Business Profile and trusted social profiles;
- partner/vendor directories where an actual partnership exists.

Avoid paid-spam directory blasts, fake forum seeding, mass guest-post networks and fabricated comparison sites.

## 12. Titles, metadata and page semantics
- Every important page gets a unique, descriptive `<title>` aligned with real search intent and brand.
- Maintain useful meta descriptions for click comprehension; do not stuff keyword variants.
- One clear page-level H1 unless the architecture validly requires otherwise.
- Use semantic headings for sections.
- Use canonical tags correctly.
- Use Open Graph/social metadata for share previews and entity consistency.
- Use descriptive image alt text where the image conveys content.
- Keep visible copy and metadata consistent.

## 13. International / multilingual
- Use stable locale URLs and accurate `hreflang` when multiple language versions exist.
- Avoid untranslated/hybrid pages and locale metadata mismatches.
- Keep canonical/hreflang reciprocal and consistent.
- Do not machine-expand languages without QA and real user value.

## 14. `llms.txt` policy
- Optional experiment, never required for Google visibility.
- If maintained, generate it from the same canonical content/data source to avoid stale contradictions.
- Keep it concise: entity summary + authoritative pages/services/products/policies/contact/reference links.
- Do not put secret/internal material in `llms.txt`; it is public.
- A stale or contradictory `llms.txt` is worse than none.
- Measure whether target systems actually fetch/use it before investing heavily.

Reference implementation/proposal: `AnswerDotAI/llms-txt`; treat it as a community proposal, not a universal web standard.

## 15. Upstream references / GitHub watchlist
### Authoritative/current
- `schemaorg/schemaorg` — Schema.org vocabulary/source.
- `google/site-kit-wp` — official Google WordPress integration reference for Search Console/Analytics-related surfaces.
- Google Search Central official documentation — source of truth for Google Search/AI feature behavior.
- OpenAI crawler/publisher documentation — source of truth for `OAI-SearchBot`, GPTBot and ChatGPT Search inclusion guidance.
- Perplexity crawler docs — source of truth for PerplexityBot policy.

### Research / experimental
- `GEO-optim/GEO` — Generative Engine Optimization research/code; use for hypotheses/evals, not platform guarantees.
- `AnswerDotAI/llms-txt` — proposed LLM discovery/context file; optional experiment.

### Community audit candidates (evaluate license/maintenance/methodology before adoption)
- `spronta/crawlie`
- `agencyenterprise/aiseo-audit`
- `ngstcf/ai-seo-auditor`
- other SEO/GEO audit repos discovered at runtime.

Do not let third-party audit scoring override official platform guidance.

## 16. Measurement
Track by query cluster and entity, not only overall traffic.

Google:
- Search Console impressions/clicks/position by page/query;
- Generative AI performance report where available;
- index coverage / URL inspection;
- rich-result / Merchant Center / Business Profile diagnostics.

Bing:
- Bing Webmaster Tools;
- IndexNow submission health when used.

AI/referral:
- ChatGPT referral traffic (`utm_source=chatgpt.com` where provided);
- Perplexity/other referral sources;
- server/CDN crawler logs by user agent;
- manual recurring benchmark prompts as an observation layer, not a deterministic ranking metric.

Business:
- qualified leads;
- sales;
- branded search growth;
- assisted conversions;
- product/service page engagement.

## 17. AI/search visibility evals
For important brands, maintain a benchmark query set with classes:
- brand/entity queries;
- category queries;
- service queries;
- local queries;
- comparison/recommendation queries;
- product/category queries;
- informational queries where the brand has genuine expertise.

Each benchmark observation stores:
- date;
- engine;
- location/language if relevant;
- query;
- whether brand appeared;
- cited URL/source;
- competitors/sources shown;
- reason/evidence hypothesis;
- next action.

Do not interpret one AI answer as stable ranking truth; generative outputs and search indices are stochastic/dynamic.

## 18. Release gate
SEO/AI-discovery changes are VERIFIED only when the relevant subset passes:
- public URL returns intended 2xx;
- robots policy is correct;
- sitemap exists and contains canonical important URLs;
- canonical/noindex are correct;
- titles/descriptions/H1 are not accidentally missing/duplicated for target pages;
- structured data parses and matches visible content;
- Search/AI crawlers are not unintentionally WAF-blocked;
- important locale/hreflang relationships are valid;
- product/business feed consistency checks pass where applicable;
- Search Console/analytics tracking remains functional;
- no material performance/accessibility regression.

Completion state must be `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT VERIFIED` with evidence.