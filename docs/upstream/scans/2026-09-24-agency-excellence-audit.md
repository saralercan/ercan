# Agency Excellence Evidence Scan — 2026-09-24

Status: reviewed baseline
Scope: quality authorities used to strengthen the 52-agent Agency Excellence Standard.

## Why this scan exists

The existing 21-agent Stable Core already had world-class source packs and championship scenarios. The 31-agent GitHub Specialist v3 tier had strong structural routing, domain skills and certification contracts, but did not share one numbered principal-level agency audit/source/championship surface with the core tier.

The remediation is organizational rather than a claim of superiority:
- one agency-wide principal-level operating standard;
- individual coverage for all 52 stable identities;
- specialist source packs 22–52;
- championship gates 1–52;
- CI enforcement;
- no automatic promotion of behavioral/external benchmark status.

## Current official quality anchors reviewed

### Accessibility
W3C WCAG 2.2 remains the current W3C Recommendation baseline used by the web/accessibility lanes. Task-local WAI/ARIA/platform guidance is added when needed.

### Application security
OWASP ASVS currently exposes stable 5.0.0 as the latest stable ASVS baseline. Security agents must still reverify current vendor advisories and threat context at task time.

### Shopify storefront quality
Current Shopify theme performance guidance explicitly treats LCP, CLS and INP as Core Web Vitals, recommends measuring before optimizing, warns against unnecessary JavaScript and highlights Theme Check/native platform validation.

### WordPress engineering quality
Current WordPress Coding Standards remain the baseline for collaborative/readable core/theme/plugin code; the handbook currently states WCAG AA commitment for new/updated WordPress code. Current developer docs and active project architecture outrank generic memory.

### Android/mobile quality
Current Android Core App Quality and Adaptive App Quality guidance covers usability, form-factor continuity, visual quality, accessibility, performance/stability and latest-platform compatibility. Mobile specialists must use current Apple/Android platform sources appropriate to the actual target.

### Apple inclusion/accessibility
Current Apple guidance emphasizes people-first/inclusive design and testing main app tasks with relevant assistive technologies/settings. Platform-specific HIG/accessibility docs remain task-time authority.

### Search/editorial
Current Google Search documentation continues to emphasize helpful/reliable people-first content and current spam/structured-data policies. Search agents must not turn AI-assisted content volume into a quality proxy.

### Agent/MCP
Current MCP TypeScript SDK v2 documents the stable line implementing the 2026-07-28 spec. Agent/MCP specialists must verify negotiated protocol/runtime/auth behavior at task time rather than freeze it into a permanent prompt.

## External verification anchors

Rechecked on 2026-09-24 against current official surfaces:
- W3C WCAG 2.2 Recommendation: https://www.w3.org/TR/wcag/
- OWASP ASVS project / current stable 5.0.0: https://owasp.org/projects/asvs
- Shopify theme performance best practices: https://shopify.dev/docs/storefronts/themes/best-practices/performance
- WordPress Coding Standards and Accessibility Coding Standards: https://developer.wordpress.org/coding-standards/wordpress-coding-standards/ and https://developer.wordpress.org/coding-standards/wordpress-coding-standards/accessibility/
- Android Core App Quality guidance: https://developer.android.com/develop/adaptive-apps/quality-guidelines/core-app-quality
- Apple Human Interface Guidelines — Inclusion: https://developer.apple.com/design/human-interface-guidelines/inclusion
- Google Search spam policies / Search documentation updates: https://developers.google.com/search/docs/essentials/spam-policies and https://developers.google.com/search/updates
- MCP TypeScript SDK v2: https://ts.sdk.modelcontextprotocol.io/v2/

These anchors validate the shared baseline only. Platform/API/security/search facts that materially affect a live task are still reverified at execution time.

## Design decision

“World class” is a **target and evidence program**, not a label that architecture can grant. Static coverage may be `STRUCTURALLY_READY`; real tasks may earn `TASK_VERIFIED` or `PRODUCTION_VERIFIED`; comparative superiority requires dated reproducible external comparison.

The new audit therefore records gaps/remediation for all 52 but leaves behavioral and external comparative status as `NOT_RUN` until those runs actually happen.

## Durable files produced

- `docs/standards/AGENCY_EXCELLENCE_STANDARD.md`
- `docs/standards/AGENT_EXCELLENCE_MANIFEST.json`
- `docs/research/SPECIALIST_EXCELLENCE_SOURCE_PACKS.md`
- `docs/evals/AGENT_EXCELLENCE_AUDIT_2026-09-24.md`
- `docs/evals/AGENT_CHAMPIONSHIP_SUITE_V2.md`
- `.agents/skills/agency-excellence-audit/SKILL.md`
- `scripts/validate_agency_excellence.py`
- `.github/workflows/agency-excellence.yml`
