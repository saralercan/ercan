# Ercan OS — Upstream Intelligence Catalog

Status: active
Reviewed baseline: 2026-08-29

Purpose: provide GPT/Codex/Orchestrator with a broad, task-routed catalog of high-value public GitHub upstreams for web, app, UI/UX, design systems, visual production, social media, WordPress, Shopify, testing, performance, SEO, maps, automation and agent engineering.

This is **not** an instruction to install every repository. Every task must still apply `UPSTREAM_TOOLCHAIN.md`, `DISCOVERY_ADOPTION_LEDGER.md`, `upstream-adoption-audit`, license/security/maintenance checks, project fit, least privilege and the qualified-agent routing contract. Runtime versions and current project status must be re-verified before adoption.

Decision vocabulary:
- `ADOPT` — canonical/strong default reference or tool when capability is required.
- `ADOPT_WHEN_NEEDED` — strong task-specific option; do not load globally.
- `ADOPT_PATTERN_ONLY` — reuse architecture/patterns/ideas, not a default dependency.
- `WATCHLIST` — useful discovery/reference source requiring stronger case-specific review.
- `SUPERSEDED` — historical/reference only for new work.
- `DISCOVERY_SOURCE` — recursive curated catalog used to discover additional candidates JIT.

## 1. Core web application platforms

- `facebook/react` — ADOPT — React runtime/reference for React projects.
- `vercel/next.js` — ADOPT — Next.js application architecture, routing, rendering and production patterns.
- `vitejs/vite` — ADOPT — modern frontend build/dev tooling.
- `withastro/astro` — ADOPT_WHEN_NEEDED — content/editorial/marketing sites with island architecture.
- `vuejs/core` — ADOPT_WHEN_NEEDED — Vue application/runtime reference.
- `nuxt/nuxt` — ADOPT_WHEN_NEEDED — Vue full-stack/meta-framework reference.
- `sveltejs/svelte` — ADOPT_WHEN_NEEDED — Svelte UI/runtime reference.
- `sveltejs/kit` — ADOPT_WHEN_NEEDED — Svelte application framework.
- `remix-run/react-router` — ADOPT_WHEN_NEEDED — data-aware routing/application patterns.
- `angular/angular` — ADOPT_WHEN_NEEDED — Angular platform reference.
- `solidjs/solid` — WATCHLIST — fine-grained reactive UI patterns.
- `QwikDev/qwik` — WATCHLIST — resumability/performance architecture reference.
- `preactjs/preact` — ADOPT_WHEN_NEEDED — lightweight React-compatible UI runtime.
- `tanstack/query` — ADOPT — async/server-state management patterns.
- `TanStack/router` — ADOPT_WHEN_NEEDED — type-safe routing for React apps.
- `TanStack/table` — ADOPT_WHEN_NEEDED — headless complex data tables.
- `pmndrs/zustand` — ADOPT_WHEN_NEEDED — small React state management.
- `reduxjs/redux-toolkit` — ADOPT_WHEN_NEEDED — structured complex client state.
- `colinhacks/zod` — ADOPT — schema validation at frontend/backend boundaries.
- `trpc/trpc` — ADOPT_WHEN_NEEDED — end-to-end typed TypeScript APIs.

## 2. CSS, primitives, component systems and UI libraries

- `tailwindlabs/tailwindcss` — ADOPT — utility-first styling when project stack uses Tailwind.
- `shadcn-ui/ui` — ADOPT_PATTERN_ONLY — copy-owned component architecture and registry patterns.
- `radix-ui/primitives` — ADOPT — accessible headless React primitives.
- `mui/base-ui` — ADOPT_WHEN_NEEDED — unstyled accessible UI primitives.
- `tailwindlabs/headlessui` — ADOPT_WHEN_NEEDED — accessible headless components.
- `ariakit/ariakit` — ADOPT_WHEN_NEEDED — accessible React primitives.
- `chakra-ui/chakra-ui` — ADOPT_WHEN_NEEDED — component/design-system reference.
- `chakra-ui/ark` — ADOPT_WHEN_NEEDED — framework-agnostic headless components.
- `chakra-ui/panda` — ADOPT_PATTERN_ONLY — type-safe styling/token generation patterns.
- `saadeghi/daisyui` — WATCHLIST — fast Tailwind component patterns; project brand must override defaults.
- `themesberg/flowbite` — WATCHLIST — Tailwind component/reference library.
- `themesberg/flowbite-react` — WATCHLIST — React component variants for Flowbite.
- `magicuidesign/magicui` — ADOPT_PATTERN_ONLY — animated landing/marketing component ideas.
- `DavidHDev/react-bits` — ADOPT_PATTERN_ONLY — interactive/animated React component patterns.
- `ibelick/motion-primitives` — ADOPT_PATTERN_ONLY — composable motion UI patterns.
- `nolly-studio/cult-ui` — WATCHLIST — experimental premium UI patterns.
- `unovue/reka-ui` — ADOPT_WHEN_NEEDED — Vue headless accessible primitives.
- `unovue/inspira-ui` — ADOPT_PATTERN_ONLY — animated Vue UI patterns.
- `nuxt/ui` — ADOPT_WHEN_NEEDED — Nuxt-native UI system.
- `skeletonlabs/skeleton` — WATCHLIST — Svelte/Tailwind component system.
- `tremorlabs/tremor` — ADOPT_WHEN_NEEDED — dashboard/data visualization UI patterns.
- `primer/react` — ADOPT_PATTERN_ONLY — GitHub design-system implementation patterns.
- `pinterest/gestalt` — ADOPT_PATTERN_ONLY — Pinterest design-system/accessibility patterns.
- `carbon-design-system/carbon` — ADOPT_PATTERN_ONLY — mature enterprise design-system architecture.
- `cloudscape-design/components` — ADOPT_PATTERN_ONLY — AWS enterprise component/accessibility patterns.
- `DouyinFE/semi-design` — WATCHLIST — large-scale design-system patterns.
- `arco-design/arco-design` — WATCHLIST — enterprise UI design-system patterns.
- `gluestack/gluestack-ui` — ADOPT_WHEN_NEEDED — cross-platform React/React Native UI primitives.
- `themeselection/flyonui` — WATCHLIST — Tailwind component/reference source.
- `intentui/intentui` — WATCHLIST — modern accessible UI component patterns.
- `TailGrids/tailgrids` — WATCHLIST — landing/dashboard block references.
- `ui-layouts/uilayouts` — ADOPT_PATTERN_ONLY — layout/motion inspiration blocks.
- `kokonut-labs/kokonutui` — WATCHLIST — modern copy-owned UI references.
- `PageAI-Pro/page-ui` — WATCHLIST — AI/landing oriented component references.

## 3. Motion, immersive web and creative frontend

- `motiondivision/motion` — ADOPT — React/web animation primitives when motion is in scope.
- `darkroomengineering/lenis` — ADOPT_WHEN_NEEDED — smooth-scroll architecture; test accessibility/performance.
- `greensock/GSAP` — ADOPT_WHEN_NEEDED — advanced timeline/scroll motion; verify current license/runtime terms.
- `mrdoob/three.js` — ADOPT_WHEN_NEEDED — WebGL/3D web experiences.
- `pmndrs/react-three-fiber` — ADOPT_WHEN_NEEDED — React renderer for Three.js.
- `pmndrs/drei` — ADOPT_WHEN_NEEDED — helpers for react-three-fiber.
- `theatre-js/theatre` — ADOPT_PATTERN_ONLY — timeline/creative coding animation authoring patterns.
- `airbnb/lottie-web` — ADOPT_WHEN_NEEDED — deterministic vector animation playback.
- `fand/vfx-js` — WATCHLIST — WebGL/VFX interaction ideas.
- `DavidHDev/canvas-ui` — WATCHLIST — modern canvas-based UI experiments.

## 4. Design systems, design tokens and component workshops

- `storybookjs/storybook` — ADOPT — isolated component states, docs and visual regression workflows.
- `amzn/style-dictionary` — ADOPT_PATTERN_ONLY — semantic token transforms/build lifecycle.
- `figma/code-connect` — ADOPT_WHEN_NEEDED — Figma/code component mapping when supported.
- `figma/sds` — ADOPT_PATTERN_ONLY — design-system bridge/reference patterns.
- `tokens-studio/figma-plugin` — ADOPT_WHEN_NEEDED — token authoring/sync reference.
- `vanilla-extract-css/vanilla-extract` — ADOPT_WHEN_NEEDED — type-safe zero-runtime styling.
- `stenciljs/core` — ADOPT_WHEN_NEEDED — design-system/web-component compiler.
- `webcomponents/custom-elements` — ADOPT_PATTERN_ONLY — standards polyfill/reference.
- `lit/lit` — ADOPT_WHEN_NEEDED — standards-based web components.
- `patternfly/patternfly` — ADOPT_PATTERN_ONLY — enterprise design-system architecture.

## 5. Screenshot, design-to-code and visual fidelity

- `abi/screenshot-to-code` — ADOPT_PATTERN_ONLY — screenshot/mockup/Figma/video → code + browser self-check pattern.
- `leigest519/ScreenCoder` — ADOPT_PATTERN_ONLY — multi-agent screenshot-to-code + benchmark methodology.
- `zwq-top/ui-image-to-code-studio` — WATCHLIST — Codex-oriented visual parity/editor roundtrip ideas.
- `garris/BackstopJS` — ADOPT_WHEN_NEEDED — visual regression screenshot diffing.
- `mapbox/pixelmatch` — ADOPT_WHEN_NEEDED — low-level pixel comparison.
- `reg-viz/reg-suit` — ADOPT_WHEN_NEEDED — visual regression workflow patterns.
- `oblador/loki` — WATCHLIST — Storybook/component screenshot regression.

## 6. Browser automation, testing and QA

- `microsoft/playwright` — ADOPT — canonical E2E/browser verification default.
- `cypress-io/cypress` — ADOPT_WHEN_NEEDED — browser testing alternative for existing Cypress stacks.
- `puppeteer/puppeteer` — ADOPT_WHEN_NEEDED — Chrome automation/screenshot/runtime diagnostics.
- `vitest-dev/vitest` — ADOPT — fast JS/TS unit/integration test runner for Vite ecosystems.
- `jestjs/jest` — ADOPT_WHEN_NEEDED — mature JS testing where existing projects use Jest.
- `testing-library/dom-testing-library` — ADOPT — user-oriented DOM testing patterns.
- `testing-library/react-testing-library` — ADOPT — React testing patterns.
- `mswjs/msw` — ADOPT_WHEN_NEEDED — API/network mocking across browser/tests.
- `microsoft/accessibility-insights-web` — ADOPT_PATTERN_ONLY — accessibility inspection/test patterns.
- `openai/openai-testing-agent-demo` — ADOPT_PATTERN_ONLY — CUA + Playwright testing-agent architecture; preview/high-risk restrictions remain.

## 7. Accessibility, performance and web quality

- `dequelabs/axe-core` — ADOPT — automated accessibility detection paired with manual QA.
- `pa11y/pa11y` — ADOPT_WHEN_NEEDED — accessibility CI/CLI checks.
- `jsx-eslint/eslint-plugin-jsx-a11y` — ADOPT — JSX static accessibility linting.
- `adobe/react-spectrum` — ADOPT_PATTERN_ONLY — React Aria accessibility/interaction architecture.
- `GoogleChrome/lighthouse` — ADOPT — performance/accessibility/SEO/best-practices audits.
- `GoogleChrome/lighthouse-ci` — ADOPT — Lighthouse budgets and CI regression.
- `GoogleChrome/web-vitals` — ADOPT — field-oriented Core Web Vitals measurement library.
- `sitespeedio/sitespeed.io` — ADOPT_WHEN_NEEDED — repeatable performance monitoring/analysis.
- `webpack-contrib/webpack-bundle-analyzer` — ADOPT_WHEN_NEEDED — JS bundle composition diagnosis.
- `vercel/next.js` — ADOPT — also canonical Next.js performance guidance/source.
- `code2ahm/crawlscope` — WATCHLIST — combined Lighthouse + SEO + accessibility audit architecture.

## 8. SEO, metadata, crawling and structured content

- `garmeeh/next-seo` — ADOPT_WHEN_NEEDED — reusable Next.js SEO metadata patterns.
- `iamvishnusankar/next-sitemap` — ADOPT_WHEN_NEEDED — sitemap/robots generation in Next.js.
- `google/schema-dts` — ADOPT_WHEN_NEEDED — typed Schema.org JSON-LD modeling.
- `unjs/unhead` — ADOPT_WHEN_NEEDED — head/SEO metadata management across frameworks.
- `microlinkhq/metascraper` — ADOPT_WHEN_NEEDED — metadata extraction for research/content ingestion.
- `apify/crawlee` — ADOPT_WHEN_NEEDED — production crawling/scraping workflows.
- `firecrawl/firecrawl` — ADOPT_WHEN_NEEDED — web extraction/crawl patterns for agent research.
- `unclecode/crawl4ai` — ADOPT_WHEN_NEEDED — LLM-oriented crawling/content extraction patterns.

## 9. Image processing, generation and creative production

- `lovell/sharp` — ADOPT — deterministic resize/crop/composite/export for Node pipelines.
- `libvips/libvips` — ADOPT_PATTERN_ONLY — high-performance image processing engine behind Sharp.
- `ImageMagick/ImageMagick` — ADOPT_WHEN_NEEDED — broad deterministic image conversion/composition.
- `python-pillow/Pillow` — ADOPT_WHEN_NEEDED — Python raster image processing.
- `svg/svgo` — ADOPT — SVG optimization with visual/logo regression safeguards.
- `danielgatis/rembg` — ADOPT_WHEN_NEEDED — local background removal; verify model/runtime/privacy fit.
- `xinntao/Real-ESRGAN` — ADOPT_WHEN_NEEDED — image upscaling/restoration pattern.
- `TencentARC/GFPGAN` — ADOPT_WHEN_NEEDED — face restoration when legitimate and disclosed.
- `facebookresearch/segment-anything` — ADOPT_PATTERN_ONLY — segmentation/masking architecture.
- `huggingface/diffusers` — ADOPT_WHEN_NEEDED — open diffusion model pipelines.
- `comfyanonymous/ComfyUI` — ADOPT_WHEN_NEEDED — node-based image generation workflow architecture.
- `lllyasviel/ControlNet` — ADOPT_PATTERN_ONLY — structural conditioning/reference guidance concepts.

## 10. Video, motion graphics and deterministic social exports

- `remotion-dev/remotion` — ADOPT_WHEN_NEEDED — code-driven deterministic video/social exports.
- `FFmpeg/FFmpeg` — ADOPT — media encode/transcode/composite foundation.
- `zulko/moviepy` — ADOPT_WHEN_NEEDED — Python video composition automation.
- `airbnb/lottie-web` — ADOPT_WHEN_NEEDED — motion asset playback.
- `fabricjs/fabric.js` — ADOPT_WHEN_NEEDED — interactive canvas/image/text editor surfaces.
- `konvajs/konva` — ADOPT_WHEN_NEEDED — 2D canvas scene/editor architecture.

## 11. Visual editors, whiteboards and content authoring

- `penpot/penpot` — ADOPT_PATTERN_ONLY — open design/prototyping system architecture.
- `excalidraw/excalidraw` — ADOPT_PATTERN_ONLY — collaborative canvas/diagram UX patterns.
- `tldraw/tldraw` — ADOPT_PATTERN_ONLY — extensible canvas editor architecture.
- `GrapesJS/grapesjs` — ADOPT_WHEN_NEEDED — block/page-builder architecture.
- `prevwong/craft.js` — ADOPT_PATTERN_ONLY — React page-editor component model.
- `ueberdosis/tiptap` — ADOPT_WHEN_NEEDED — extensible rich text editor.
- `facebook/lexical` — ADOPT_WHEN_NEEDED — structured extensible editor framework.
- `ianstormtaylor/slate` — ADOPT_WHEN_NEEDED — editor composition patterns.
- `microsoft/monaco-editor` — ADOPT_WHEN_NEEDED — embedded code editor.
- `codemirror/dev` — ADOPT_WHEN_NEEDED — extensible browser code/text editor.

## 12. Icons and reusable visual assets

- `lucide-icons/lucide` — ADOPT — default high-quality open icon candidate.
- `tailwindlabs/heroicons` — ADOPT_WHEN_NEEDED — clean UI icon set.
- `phosphor-icons/core` — ADOPT_WHEN_NEEDED — flexible icon family.
- `tabler/tabler-icons` — ADOPT_WHEN_NEEDED — broad SVG icon set.
- `simple-icons/simple-icons` — ADOPT_WHEN_NEEDED — brand/service icons; verify trademark/brand usage.

## 13. Social media scheduling, publishing and automation

- `gitroomhq/postiz-app` — ADOPT_PATTERN_ONLY — provider-neutral scheduler architecture, retries, calendars, multi-platform publishing.
- `inovector/mixpost` — ADOPT_PATTERN_ONLY — self-hosted social scheduling/product architecture.
- `trypostit/trypost` — WATCHLIST — multi-network scheduler + MCP/AI copilot patterns.
- `coollabsio/shoutrrr` — WATCHLIST — self-hosted cross-platform scheduling patterns.
- `rodrgds/openpost` — WATCHLIST — small self-hosted scheduler with API/CLI/MCP patterns.
- `notherobot/social-media-scheduler` — WATCHLIST — cross-platform short-video scheduling workflow ideas.
- `Liparoto/Social-Scheduler` — WATCHLIST — Meta-focused local scheduler architecture.
- `DeliciousHouse/aries-app` — WATCHLIST — weekly content generation/review/approve/schedule flow.
- `YusufSizmaz/social-agent-ai` — WATCHLIST — autonomous content/publishing/analytics architecture; requires strong policy/provider review.

## 14. Mobile app foundations

- `flutter/flutter` — ADOPT — canonical Flutter framework/source.
- `facebook/react-native` — ADOPT — canonical React Native framework/source.
- `expo/expo` — ADOPT — default React Native app/tooling ecosystem candidate.
- `react-navigation/react-navigation` — ADOPT — React Native navigation.
- `software-mansion/react-native-reanimated` — ADOPT_WHEN_NEEDED — native-quality React Native motion.
- `software-mansion/react-native-gesture-handler` — ADOPT — gesture foundation for React Native.
- `NativeWind/nativewind` — ADOPT_WHEN_NEEDED — Tailwind-style React Native styling.
- `callstack/react-native-paper` — ADOPT_WHEN_NEEDED — Material-based RN component system.
- `infinitered/ignite` — ADOPT_PATTERN_ONLY — production React Native starter/architecture patterns.
- `rrousselGit/riverpod` — ADOPT_WHEN_NEEDED — Flutter state/dependency management.
- `felangel/bloc` — ADOPT_WHEN_NEEDED — Flutter BLoC architecture.
- `flutter/packages` — ADOPT — official Flutter packages/examples source.
- `gluestack/gluestack-ui` — ADOPT_WHEN_NEEDED — cross-platform UI system.
- `heroui-inc/heroui-native` — WATCHLIST — modern React Native design-system patterns.

## 15. WordPress engineering

- `WordPress/wordpress-develop` — ADOPT — canonical WordPress core development source.
- `WordPress/gutenberg` — ADOPT — block editor/components/wp-scripts architecture.
- `wp-cli/wp-cli` — ADOPT — command-line WordPress operations.
- `WordPress/WordPress-Coding-Standards` — ADOPT — PHP coding standards/lint reference.
- `WordPress/plugin-check` — ADOPT — plugin compatibility/quality checks.
- `johnbillion/query-monitor` — ADOPT_WHEN_NEEDED — runtime/debug/performance diagnostics.
- `DevinVinson/WordPress-Plugin-Boilerplate` — ADOPT_PATTERN_ONLY — plugin organization patterns, not mandatory architecture.
- `WPBP/WordPress-Plugin-Boilerplate-Powered` — WATCHLIST — generator/quality-tool integration ideas.
- `wp-hub/awesome-wordpress` — DISCOVERY_SOURCE — curated WordPress ecosystem discovery.

## 16. Shopify engineering

- `Shopify/cli` — ADOPT — canonical app/theme/Hydrogen development CLI.
- `Shopify/theme-tools` — ADOPT — Liquid/theme language server/theme-check tooling.
- `Shopify/dawn` — ADOPT — canonical reference theme architecture.
- `Shopify/hydrogen` — ADOPT_WHEN_NEEDED — headless Shopify storefront framework/reference.
- `Shopify/hydrogen-react` — ADOPT_WHEN_NEEDED — Shopify storefront React primitives.
- `Shopify/shopify-app-template-react-router` — ADOPT_WHEN_NEEDED — current app template architecture when applicable.
- `yakohere/shopify-theme-devtools` — WATCHLIST — unpublished-theme developer diagnostics; review injection/security before use.
- `Shopify/themekit` — SUPERSEDED — deprecated; use Shopify CLI for new work.
- `Shopify/polaris-react-archive` — SUPERSEDED — archived React implementation; design principles may remain reference only.
- `MentionNetwork/awesome-shopify` — DISCOVERY_SOURCE — current broad Shopify/API/MCP/theme/headless discovery.
- `LeCoupa/awesome-shopify` — DISCOVERY_SOURCE — historical/broad Shopify resource discovery; verify freshness per item.

## 17. Backend, CMS, commerce and product infrastructure

- `supabase/supabase` — ADOPT_WHEN_NEEDED — Postgres/Auth/Storage/Realtime backend platform reference.
- `appwrite/appwrite` — ADOPT_WHEN_NEEDED — self-hostable application backend alternative.
- `pocketbase/pocketbase` — ADOPT_WHEN_NEEDED — small embedded backend for simple products/prototypes.
- `directus/directus` — ADOPT_WHEN_NEEDED — headless data/CMS platform.
- `payloadcms/payload` — ADOPT_WHEN_NEEDED — TypeScript-first CMS/app backend.
- `strapi/strapi` — ADOPT_WHEN_NEEDED — headless CMS ecosystem.
- `medusajs/medusa` — ADOPT_PATTERN_ONLY — composable commerce architecture outside Shopify-specific work.
- `saleor/saleor` — ADOPT_PATTERN_ONLY — GraphQL commerce architecture reference.
- `nextauthjs/next-auth` — ADOPT_WHEN_NEEDED — Auth.js authentication patterns for compatible stacks.

## 18. Analytics, product telemetry and observability

- `umami-software/umami` — ADOPT_WHEN_NEEDED — privacy-conscious web analytics.
- `plausible/analytics` — ADOPT_WHEN_NEEDED — lightweight analytics architecture.
- `PostHog/posthog` — ADOPT_WHEN_NEEDED — product analytics/session replay/feature experimentation architecture.
- `open-telemetry/opentelemetry-js` — ADOPT_WHEN_NEEDED — JS telemetry standard instrumentation.
- `getsentry/sentry-javascript` — ADOPT_WHEN_NEEDED — frontend/runtime error monitoring integration reference.

## 19. Email and notification production

- `resend/react-email` — ADOPT_WHEN_NEEDED — deterministic React email templates.
- `mjmlio/mjml` — ADOPT_WHEN_NEEDED — responsive email compilation.
- `nodemailer/nodemailer` — ADOPT_WHEN_NEEDED — Node mail transport/message composition.
- `PHPMailer/PHPMailer` — ADOPT — maintained PHP mail construction/SMTP reference.
- `axllent/mailpit` — ADOPT — local/staging SMTP capture and QA.
- `knadh/listmonk` — ADOPT_WHEN_NEEDED — self-hosted newsletter/list management after operational/license review.

## 20. Maps, geospatial and local-guide experiences

- `maplibre/maplibre-gl-js` — ADOPT — preferred rich open web-map renderer candidate.
- `Leaflet/Leaflet` — ADOPT — lightweight web/WordPress map candidate.
- `openlayers/openlayers` — ADOPT_WHEN_NEEDED — advanced GIS/web map framework.
- `mapbox/supercluster` — ADOPT_WHEN_NEEDED — high-density point clustering.
- `protomaps/PMTiles` — ADOPT_WHEN_NEEDED — static/serverless/offline vector tile distribution.
- `Turfjs/turf` — ADOPT_WHEN_NEEDED — browser/server geospatial operations.
- `protomaps/protomaps-leaflet` — SUPERSEDED_FOR_NEW_WORK — legacy/maintenance-mode integration reference.

## 21. Charts, dashboards and data visualization

- `apache/echarts` — ADOPT_WHEN_NEEDED — rich performant charts.
- `recharts/recharts` — ADOPT_WHEN_NEEDED — React chart components.
- `airbnb/visx` — ADOPT_PATTERN_ONLY — low-level visualization primitives.
- `plouc/nivo` — ADOPT_WHEN_NEEDED — React visualization components.
- `observablehq/plot` — ADOPT_WHEN_NEEDED — concise grammar-oriented visualization.

## 22. Agent, AI developer and browser-research infrastructure

- `openai/codex` — ADOPT — Codex runtime/source patterns where relevant.
- `openai/openai-agents-python` — ADOPT_WHEN_NEEDED — OpenAI agent SDK patterns for Python.
- `openai/openai-agents-js` — ADOPT_WHEN_NEEDED — OpenAI agent SDK patterns for JavaScript/TypeScript.
- `vercel/ai` — ADOPT_WHEN_NEEDED — provider-neutral AI application UI/streaming/tool-call patterns.
- `browser-use/browser-use` — ADOPT_PATTERN_ONLY — browser-agent architecture; authenticated/high-risk usage needs guardrails.
- `browserbase/stagehand` — ADOPT_PATTERN_ONLY — browser automation abstraction/agent patterns.
- `microsoft/playwright-mcp` — ADOPT_WHEN_NEEDED — MCP browser automation in trusted environments.
- `modelcontextprotocol/servers` — DISCOVERY_SOURCE — MCP server reference implementations/catalog.
- `modelcontextprotocol/typescript-sdk` — ADOPT_WHEN_NEEDED — MCP TypeScript implementation reference.
- `modelcontextprotocol/python-sdk` — ADOPT_WHEN_NEEDED — MCP Python implementation reference.
- `github/github-mcp-server` — ADOPT_WHEN_NEEDED — GitHub MCP patterns subject to least privilege.
- `langchain-ai/langchain` — ADOPT_PATTERN_ONLY — orchestration/tool abstractions; avoid unnecessary framework lock-in.
- `run-llama/llama_index` — ADOPT_PATTERN_ONLY — RAG/data-agent architecture patterns.
- `crewAIInc/crewAI` — WATCHLIST — multi-agent orchestration patterns; Ercan OS contract remains authoritative.
- `microsoft/autogen` — ADOPT_PATTERN_ONLY — agent conversation/orchestration research patterns.

## 23. Security, supply-chain and dependency quality

- `gitleaks/gitleaks` — ADOPT — secret scanning.
- `aquasecurity/trivy` — ADOPT_WHEN_NEEDED — dependency/container/filesystem vulnerability scanning.
- `github/codeql-action` — ADOPT — GitHub-native code scanning workflows when supported.
- `ossf/scorecard` — ADOPT_WHEN_NEEDED — upstream/open-source security posture signals.
- `dependabot/dependabot-core` — ADOPT_PATTERN_ONLY — dependency update/security automation reference.
- `google/osv-scanner` — ADOPT_WHEN_NEEDED — open-source vulnerability scanning.

## 24. Recursive discovery sources — high leverage catalogs

These are not automatically trusted dependencies. They are searchable upstream catalogs used by `upstream-intelligence-scan` to find additional candidates and then run normal Ercan OS verification.

- `sindresorhus/awesome` — DISCOVERY_SOURCE — broad curated list ecosystem.
- `bayandin/awesome-awesomeness` — DISCOVERY_SOURCE — index of awesome lists.
- `awesome-selfhosted/awesome-selfhosted` — DISCOVERY_SOURCE — thousands of self-hostable applications/services.
- `awesome-selfhosted/awesome-selfhosted-data` — DISCOVERY_SOURCE — machine-readable self-hosted catalog.
- `aniftyco/awesome-tailwindcss` — DISCOVERY_SOURCE — Tailwind tools/components/templates/plugins.
- `brillout/awesome-react-components` — DISCOVERY_SOURCE — React component ecosystem.
- `enaqx/awesome-react` — DISCOVERY_SOURCE — React ecosystem references.
- `jondot/awesome-react-native` — DISCOVERY_SOURCE — React Native ecosystem; verify item freshness.
- `eric-erki/awesome-react-native` — DISCOVERY_SOURCE — React Native ecosystem mirror/curation.
- `nepaul/awesome-flutter` — DISCOVERY_SOURCE — Flutter ecosystem discovery.
- `wp-hub/awesome-wordpress` — DISCOVERY_SOURCE — WordPress frameworks/plugins/themes/tools.
- `MentionNetwork/awesome-shopify` — DISCOVERY_SOURCE — Shopify APIs/SDKs/themes/headless/MCP/agentic commerce.
- `LeCoupa/awesome-shopify` — DISCOVERY_SOURCE — Shopify historical resource index.
- `klaufel/awesome-design-systems` — DISCOVERY_SOURCE — design systems/tokens/testing resources.
- `saadeghi/design-systems` — DISCOVERY_SOURCE — public design-system/style-guide index.
- `brandonhimpfen/awesome-ui-components` — DISCOVERY_SOURCE — UI component libraries/frameworks/kits.
- `brandonhimpfen/awesome-ux` — DISCOVERY_SOURCE — UX research/writing/prototyping/resources.
- `brandonhimpfen/awesome-design` — DISCOVERY_SOURCE — design/UI/UX/inspiration/tool index.
- `faheemkodi/design-resources` — DISCOVERY_SOURCE — design assets/templates/frameworks/tools.
- `codesandtags/frontend-resources` — DISCOVERY_SOURCE — community-curated frontend resources.
- `lukeslp/awesome-accessibility` — DISCOVERY_SOURCE — accessibility resources/tools/testing.

## 25. Explicit superseded / caution examples discovered during research

- `Shopify/themekit` — SUPERSEDED — repository itself states Shopify CLI should be used for theme development.
- `Shopify/polaris-react-archive` — SUPERSEDED — archived implementation; do not introduce as new runtime dependency.
- `pedronauck/docz` — SUPERSEDED — archived.
- `geist-org/geist-ui` — SUPERSEDED — archived.
- `vue-styleguidist/vue-styleguidist` — SUPERSEDED — archived.
- screenshot-to-code forks that merely mirror `abi/screenshot-to-code` without material independent value — REJECT_DUPLICATE — use canonical upstream instead.

## 26. JIT routing rule

Do not load this full catalog into every task. `@Orchestrator` or Codex should consult it only when the task requires choosing/researching implementation tools, UI patterns, platform references, QA tooling, image/video pipelines, social automation, or new capabilities.

Selection order:
`task capability → project constraints → canonical ADOPT candidates → ADOPT_WHEN_NEEDED → pattern references → recursive discovery sources if gap remains → upstream audit → narrow integration → QA/eval → ledger update`.

Stars are discovery signals only, never adoption authority. Archived/deprecated repos, weak provenance, unclear licenses, excessive permissions, broad credential requirements, unmaintained forks, or redundant capability are filtered out before any integration.
