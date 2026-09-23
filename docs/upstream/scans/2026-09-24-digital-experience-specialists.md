# Research Scan — Specialized Digital Experience Agents

Date: 2026-09-24

## Scope
UI/UX, accessibility, SEO/AEO, Meta ads, graphic design, CRO, analytics, privacy and web security.

## Strong ready-made skill sources

### wshobson/agents
License: MIT.
Useful existing agents/skills include:
- ui-designer
- accessibility-expert
- design-system-architect
- interaction-design
- visual-design-foundations
- responsive-design
- WCAG audit patterns
- security threat/SAST patterns

Decision:
ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Use the strongest domain patterns but keep Ercan OS routing/QA authority.

### addyosmani/web-quality-skills
Measurement-first web quality skills covering:
- performance;
- Core Web Vitals;
- accessibility;
- SEO;
- best practices/security;
- Lighthouse + Chrome DevTools evidence.

Decision:
ADOPT_WHEN_NEEDED / MIT.
Prefer its measurement model that separates field, RUM, lab trace and source evidence.

### addyosmani/agentic-seo
License: MIT.
Audits documentation/site readiness for coding agents/AI consumption.

Decision:
ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Scores are directional heuristics and not proof of AI-engine ranking/recommendation.

## Official authority findings

### W3C
WCAG 2.2 remains the stable accessibility standard.
WCAG-EM 2 was published in July 2026 as evaluation methodology.

### Google Search Central
SEO Starter Guide/Search Essentials emphasize crawlability, indexability, understandable content and Search Console monitoring. No ranking guarantee exists.

### Google Analytics
Current GA4 docs center event-based measurement, recommended/custom events, GTM/gtag, DebugView/realtime validation, SPA pageview correctness and supplemental Measurement Protocol.

### Google consent
Consent types include analytics_storage, ad_storage, ad_user_data and ad_personalization. Modeled data is distinct from observed data.

### Meta
Current Meta for Business materials emphasize placement-native creative, safe zones, vertical 9:16 video/audio for Reels, Advantage placements/creative and A/B testing. Platform study results are context-specific, not universal guarantees.

### OWASP
Top 10:2025 is the current awareness list.
ASVS 5.0.0 is the current application security verification standard.

### MDN
Current browser security guidance includes CSP/Trusted Types and compatibility status; browser-support checks remain necessary.

### UX research
USWDS explicitly says start with real user needs and test assumptions with real people.
GOV.UK components/patterns expose user-research evidence.
NN/g remains a strong research/practice reference for heuristics, journey mapping and mixed-method UX research.

### Graphic design
Adobe web-graphics guidance remains useful for format/export/image-quality/file-size decisions, but project brand system remains the visual authority.

## Architecture decision
Create one JIT `digital-experience-specialists` pack with 12 specialized aliases mapped to existing stable identities.

No stable identity count change.
