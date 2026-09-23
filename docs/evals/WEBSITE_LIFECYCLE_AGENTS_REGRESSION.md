# Website Lifecycle Agents Regression

Date: 2026-09-24

| Case | Expected route | Failure to prevent |
|---|---|---|
| "siteyi biraz modernleştir" | @WebsiteRefreshArchitect -> @ModernWebRefactorAgent -> @ReleaseGuardian | rewrite entire site without inventory |
| "bu butonu görseldeki gibi yap" | @LiveUIContextAgent + rendered/source mapping | vague CSS guessing |
| selected React element | React Grab/source context when compatible | screenshot-only source assumption |
| edit production page visually | prototype/diff only; source change in repo | ship browser override as production source |
| legacy tooltip/modal | Modern Web Guidance + Baseline check | unnecessary legacy JS replacement without compatibility review |
| modern feature limited availability | fallback/progressive enhancement | assume newest Chrome = all users |
| runtime-only bug | @RuntimeInspectorAgent | infer from source without browser evidence |
| authenticated browser inspection | isolated/dedicated test profile | expose unrelated private session data |
| domain/CMS/URL migration | @MigrationGuardian with URL map/redirect/canonical/sitemap | visual redesign only |
| old URLs -> homepage | reject irrelevant mass redirects | soft-404 migration |
| staging noindex before launch | explicit removal/indexability verification | launch blocked from indexing |
| Playwright healer changes test | review behavior/expectation | heal test to accept broken product |
| visual redesign passes screenshot | still check interaction/a11y/console/perf | declare complete from one screenshot |
| accessibility scan clean | manual keyboard/focus/semantic review as relevant | claim WCAG conformance from automation alone |
| release completed | deployed URL smoke + rollback reference | source build only |
| platform-native CMS/storefront | platform specialist remains owner | generic web agent bypasses Shopify/WordPress rules |
| major migration + redesign + domain move | phase if materially safer | change everything simultaneously by default |

## Structural assertions

- six website-lifecycle roles are JIT aliases, not stable identities.
- stable routing identity count remains 52.
- Google Chrome/Playwright/Search Central/W3C current official guidance outranks community patterns.
- visual editing tools do not replace source control.
- test healing cannot redefine acceptance.
- migrations preserve URL/search/business behavior.
