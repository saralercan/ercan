# Ercan OS — GitHub Specialist v3 Scoreboard

Status: structural-readiness audit
Audit date: 2026-09-07
Specialist-extension identities checked: **31**
Stable Core identities (separate scoreboard): **21**
Total named stable routing identities: **52**

This scoreboard measures **static specialist-extension governance/readiness only**. It does not claim that the 31 specialists executed behavioral certification, production tasks, external comparative benchmarks, or world-class benchmarks.

Canonical machine-readable source: `docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json`.
Behavioral certification contract: `docs/evals/GITHUB_SPECIALIST_CERTIFICATION_V3.md`.

## Static readiness rubric

Each specialist receives 20 points for each required structural surface:
1. stable identity registered in `AGENT_REGISTRY.md`;
2. identity defined in `GITHUB_SPECIALIST_EXPANSION_V3.md`;
3. domain JIT skill exists and is linked;
4. upstream/canonical evidence is represented by the v3 catalog/current/ledger system;
5. qualified routing + regression/doctor governance covers the specialist domain.

A 100/100 static score means the routing/governance surface is complete. It does **not** mean behavioral certification passed.

| Domain | Agent | Static readiness | Structural status | Behavioral certification | External comparative benchmark |
|---|---|---:|---|---|---|
| Web | `@WebArchitecture` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Web | `@FrontendSystem` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Web | `@BrowserQA` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Web | `@AccessibilityQA` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Web | `@WebPerformance` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Web | `@ComponentWorkshopQA` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Mobile | `@MobileArchitect` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Mobile | `@FlutterSpecialist` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Mobile | `@ReactNativeSpecialist` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Mobile | `@MobileQA` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Mobile | `@AppReleaseEngineer` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Social | `@SocialStrategy` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Social | `@SocialPublishingOps` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Social | `@SocialAgentOps` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Social | `@SocialAnalytics` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Social | `@ContentRecycling` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| SEO | `@TechnicalSEO` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| SEO | `@SEOScanner` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| SEO | `@WordPressSEO` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| SEO | `@ShopifySEO` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| SEO | `@AEO_GEO` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Meta | `@MetaAdsEngineer` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Meta | `@MetaMeasurement` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Meta | `@MarketingScience` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Meta | `@IncrementalityAnalyst` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Meta | `@AdsCreativeStrategist` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Branding | `@BrandSystemArchitect` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Branding | `@BrandBehavior` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Branding | `@DesignTokenArchitect` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Branding | `@BrandRuntimeEngineer` | 100/100 | PASS | NOT_RUN | NOT_RUN |
| Branding | `@BrandComplianceQA` | 100/100 | PASS | NOT_RUN | NOT_RUN |

## Summary

- Specialist-extension structural readiness: **31/31 PASS**.
- Stable Core structural readiness is maintained separately in `AGENT_SCOREBOARD.md`: **21/21 PASS** at its latest audited state.
- Combined named stable routing identities: **52**.
- Behavioral specialist certification: **NOT_RUN** until scenarios in `GITHUB_SPECIALIST_CERTIFICATION_V3.md` execute with evidence.
- External comparative benchmark: **NOT_RUN**.
- `PRODUCTION_VERIFIED` cannot be granted by this scoreboard alone.

## Domain counts

- Web: 6
- Mobile: 5
- Social: 5
- SEO/AEO/GEO: 5
- Meta ads/measurement: 5
- Branding: 5
- Total: 31

## Drift rule

`github-specialist-v3-doctor.yml` must fail when the manifest count, registry identities, required JIT skills, upstream decision surfaces, routing/eval references, this scoreboard, or the 21 + 31 = 52 identity accounting drifts.
