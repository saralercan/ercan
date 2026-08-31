# Upstream Intelligence Scan — 2026-08-31 domain expert expansion

Status: reviewed

Scope: authoritative/current sources used to promote seven cross-project expert identities in Ercan OS: SEO, Social Media, Creative Design, Web/App, Security, Performance and Agent/MCP.

No third-party community code was installed or executed and no production credentials were used.

## @SEOExpert

Decision: stable expert identity justified.

Primary evidence:
- Google Search Essentials: https://developers.google.com/search/docs/essentials
- Crawling/indexing: https://developers.google.com/search/docs/crawling-indexing
- Structured data gallery: https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Structured data policies: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Canonicalization: https://developers.google.com/search/docs/crawling-indexing/canonicalization

Important current signal: Google's August 2026 canonicalization documentation reinforces canonical selection as a signal/hint system rather than a guaranteed directive; search expert must verify real index/canonical behavior instead of assuming markup equals outcome.

## @SocialMediaExpert

Decision: stable expert identity justified, but provider rules remain JIT/volatile.

Current evidence example:
- TikTok Content Posting API: https://developers.tiktok.com/products/content-posting-api
- Direct Post guide/reference: https://developers.tiktok.com/docs/en/content-posting-api-get-started and https://developers.tiktok.com/docs/en/content-posting-api-reference-direct-post

August 2026 TikTok docs support direct video/photo posting and upload/draft paths. This is stored as current evidence, not a permanent hardcoded assumption. Meta/Instagram/LinkedIn/X/Pinterest/YouTube provider behavior must be checked from current official provider docs when relevant.

## @CreativeDesignExpert

Decision: stable expert identity justified.

Primary evidence:
- W3C Design Tokens Community Group: https://www.w3.org/community/design-tokens/
- Official DTCG repo: https://github.com/design-tokens/community-group
- Adobe Spectrum design data: https://github.com/adobe/spectrum-design-data

The W3C community group published stable 2025.10 format/color/resolver reports; Adobe Spectrum's maintained design-data tooling includes token validation/diff/migration and MCP-accessible design-system data. Ercan OS uses these as interoperability/pattern references, not brand authority over project-local systems.

## @WebAppExpert

Decision: stable expert identity justified.

Primary evidence:
- Next.js current docs: https://nextjs.org/docs
- current framework/web-platform docs selected by inspected project.

Current Next.js documentation explicitly separates App Router and Pages Router. Expert routing therefore requires project inspection rather than globally assuming one router/framework pattern.

## @SecurityExpert

Decision: stable expert identity justified.

Primary evidence:
- OWASP ASVS: https://github.com/OWASP/ASVS
- OWASP WSTG stable: https://owasp.org/www-project-web-security-testing-guide/stable/

ASVS stable baseline is 5.0.0; WSTG provides current web-app testing coverage for identity, authentication, authorization, sessions, input validation, crypto, business logic, client-side and related surfaces. Use current advisories for concrete dependencies in addition to these baselines.

## @PerformanceExpert

Decision: stable expert identity justified.

Primary evidence:
- Chrome Lighthouse: https://developer.chrome.com/docs/lighthouse
- GoogleChrome/lighthouse and web-vitals repositories under https://github.com/GoogleChrome

Lighthouse covers performance, accessibility, best practices and SEO diagnostics. It is used as measurement/audit input; field data and task-specific runtime evidence remain necessary for production conclusions.

## @AgentMCPExpert

Decision: stable expert identity justified.

Primary evidence:
- MCP specification repo: https://github.com/modelcontextprotocol/modelcontextprotocol
- MCP 2026-07-28 release: https://blog.modelcontextprotocol.io/posts/2026-07-28/
- MCP roadmap 2026-08-22: https://blog.modelcontextprotocol.io/posts/mcp-roadmap/
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/ and https://openai.github.io/openai-agents-js/

Current MCP baseline changed materially in 2026-07-28: stateless core, header-based routing, cacheable list results, authorization hardening, extensions and formal deprecation policy. August roadmap emphasizes agentic messaging, HTTP-native transport hardening, agent identity/security and SDK DX. OpenAI Agents SDK provides current primitives for agents, tools, handoffs, guardrails, sessions/human-in-loop and tracing/evals; OpenAI-specific implementation details must be verified against current SDK docs.

## Ercan OS promotion

Create stable identities:
- `@SEOExpert`
- `@SocialMediaExpert`
- `@CreativeDesignExpert`
- `@WebAppExpert`
- `@SecurityExpert`
- `@PerformanceExpert`
- `@AgentMCPExpert`

Together with the existing 14 stable identities, the stable core becomes **21**.

Training: `docs/standards/DOMAIN_EXPERT_TRAINING.md`.
Certification: `docs/evals/DOMAIN_EXPERT_CERTIFICATION.md`.
Registry extension: `docs/standards/DOMAIN_EXPERT_REGISTRY.md`.

Routing remains minimum-sufficient; 21 stable identities do not imply 21-way execution.
