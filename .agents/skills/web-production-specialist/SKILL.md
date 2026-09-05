---
name: web-production-specialist
description: Build, review or improve production websites with modern web architecture, reusable component systems, screenshot/reference fidelity, performance, accessibility and real-browser QA. Use for website redesigns, premium UI, Next.js/frontend architecture, Storybook/component work, Lighthouse/Core Web Vitals or Playwright/axe verification.
---

# Web Production Specialist

Load `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`, `PLATFORM_ENGINEERING.md`, and `DESIGN_SYSTEM_ENGINEERING.md` when shared tokens/components are touched. For screenshot/reference work also load `screenshot-production-ui` and `visual-qa-evidence`.

## Specialist identities
`@WebArchitecture`, `@FrontendSystem`, `@ScreenshotToCode`, `@ComponentWorkshopQA`, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`.

## Upstream references
Prefer current canonical sources such as `vercel/next.js`, `shadcn-ui/ui`, `storybookjs/storybook`, `microsoft/playwright`, `GoogleChrome/lighthouse`, `dequelabs/axe-core` and `harlan-zw/unlighthouse`. `abi/screenshot-to-code` is a reference pattern, not the final QA authority.

## Procedure
1. Inspect the active stack and platform before selecting framework-specific patterns.
2. Preserve project brand/content/do-not-touch constraints.
3. Define architecture/component boundaries before isolated CSS patching on shared surfaces.
4. For reference-led work, implement → render → compare → correct; never accept the first render as verified fidelity.
5. Run appropriate build/lint/static checks.
6. Verify critical mobile/tablet/desktop states in real browsers.
7. Run performance and accessibility checks proportional to risk; automated a11y never replaces keyboard/focus/semantic review.
8. Keep implementation and final QA separate for material changes.

## Completion evidence
Build/runtime status, representative browser screenshots, console/network status, a11y result, performance/regression result and `VERIFIED/PARTIAL/BLOCKED/NOT VERIFIED`.
