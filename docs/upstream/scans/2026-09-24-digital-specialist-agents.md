# Upstream Scan — UI/UX, SEO, Meta, Graphic Design, Security Specialists

Date: 2026-09-24

## Research objective

Find ready-made, current, high-quality agent skills/tools for agency-grade UI/UX, SEO, Meta advertising/measurement, graphic design and web security. Where no single trustworthy ready-made agent covers the full job, synthesize a JIT Ercan OS specialist from official standards plus audited upstream patterns.

## UI / UX

### anthropics/skills — frontend-design
Already adopted in Design Quality Engine.
Decision: retain as a high-quality official design reference.

### hueyexe/frontend-agent-skills
MIT.
Current pack includes:
- accessibility/inclusive design;
- design systems/frontend architecture;
- forms/checkout;
- information architecture/navigation;
- UX writing/content design;
- visual composition and related UX disciplines.

Decision:
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.
Useful for missing UX/IA/form/content-design judgment, but Ercan OS retains project research/brand/runtime authority.

### pbakaus/impeccable
Already reviewed.
Decision remains:
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.

### W3C
Current:
- WCAG 2.2 = production accessibility standard;
- WCAG-EM 2.0 published 2026-07-23 as evaluation methodology;
- WCAG 3 remains Working Draft.

Decision:
official authority for accessibility evaluation.

## SEO

### Google Search Central
Primary authority.

Current guidance confirms:
- SEO supports crawling/indexing/understanding and user discovery;
- Search Console is the direct Google Search performance source;
- GA measures behavior inside the site;
- structured data must reflect page truth and does not guarantee rich results;
- third-party SEO services/tools have no access to Google's internal ranking data and cannot guarantee outcomes;
- foundational SEO remains relevant to AI Overviews/AI Mode.

Decision:
`PRIMARY_SEARCH_AUTHORITY`.

### marketingskills/seo
MIT.
Current skill pack includes technical triage, keyword opportunity, content decay, competitor SERP monitoring, cannibalization, content refresh briefs, internal linking, schema fixes, metadata, reports and SEO strategy.

Decision:
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.

Useful operations layer, not Google authority.

## Meta advertising / measurement

Existing Ercan OS stable specialists already represent the correct separation:
- campaign engineering;
- measurement;
- creative testing;
- MMM;
- incrementality.

### facebookexperimental/Robyn
MIT.
Current Meta Marketing Science open-source MMM system.
Python implementation is described upstream as beta/LLM-translated relative to the mature R path.

Decision:
existing `ADOPT_WHEN_NEEDED`; prefer mature/validated path appropriate to project.

### facebookincubator/GeoLift
MIT.
End-to-end geo-experiment / synthetic-control incrementality methodology with market selection, power and inference.

Decision:
existing `ADOPT_WHEN_NEEDED`.

No new Meta stable/JIT identity is justified; strengthen current pod instead.

## Graphic design

### anthropics/skills — canvas-design
Apache-2.0.
Visual philosophy/art-direction workflow for original static design.

Decision:
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.

### anthropics/skills — theme-factory
Apache-2.0.
Reusable color/font theme system.

Decision:
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.

### ArnavPuri/designskills
MIT.
Current pack covers graphic design, social graphics, poster, thumbnail, ad creative, product mockups, infographic, banners, UI, color, typography, composition, brand identity and pre/post-process skills.

Decision:
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.
Its Gemini-specific production pipeline is optional; Ercan OS remains provider-neutral and uses approved image/design providers.

## Security

### OWASP ASVS
Current stable version:
ASVS 5.0.0.

Decision:
`PRIMARY_APPSEC_REQUIREMENTS_AUTHORITY`.

### OWASP WSTG
Current stable:
v4.2.
WSTG v5.0 is under active development.

Decision:
stable testing authority + clearly labeled latest/dev reference when useful.

### Semgrep
Open-source static analysis engine.
Decision:
existing/expanded `ADOPT_WHEN_NEEDED`.
Community rules have separate Semgrep Rules License.

### ZAP
Current `zaproxy/zaproxy` is Apache-2.0 and actively maintained.
2026 project updates include deeper browser/PTK integration and an MCP server direction.

Decision:
`ADOPT_WHEN_NEEDED / AUTHORIZED_DAST`.

Only authorized targets.

### trailofbits/skills
CC BY-SA 4.0.
Current marketplace includes security/audit skills and explicit quality/security-skill authoring standards.

Decision:
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.
Respect share-alike obligations before copying/adapting material; prefer workflow concepts unless exact reuse is appropriate.

Trail of Bits also maintains a curated marketplace because public skills can contain malicious behavior. This reinforces Ercan OS's existing per-skill audit rule.

### OWASP/secure-agent-playbook
Current public security-guidance skill is grounded in ASVS and provides useful secure-development routing patterns.
No root LICENSE was observed in the reviewed path.

Decision:
`PATTERN_ONLY / LICENSE_CLARIFICATION_REQUIRED`.

### UnitOneAI/SecuritySkills
MIT, but current application-security skill descriptions still reference older ASVS 4.0.3 in parts.

Decision:
`WATCHLIST / DO_NOT_USE_AS_CURRENT_AUTHORITY`.
Useful structure, but current OWASP ASVS 5.0 outranks it.

## Architecture decision

Create one JIT `digital-specialist-agent-pack` with:
- 4 UI/UX aliases;
- 5 SEO aliases;
- existing five Meta stable specialists upgraded/reaffirmed;
- 4 graphic-design aliases;
- 6 security aliases.

No stable identity count change.
