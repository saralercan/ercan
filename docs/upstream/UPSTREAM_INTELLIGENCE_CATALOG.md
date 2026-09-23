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

### Judgment / typed-decision providers and patterns

- `typesafe-ai/skills` — ADOPT_WHEN_NEEDED — official TypeSafe System One/Jev Agent Skill reference.
- `typesafe-ai/typesafe-sdk-js` — ADOPT_WHEN_NEEDED — official JS/TS SDK for typed judgment integration.
- `typesafe-ai/typesafe-sdk-python` — ADOPT_WHEN_NEEDED — official Python SDK; re-verify current metadata before production use.
- `lahfir/agent-desktop` — ADOPT_WHEN_NEEDED — authorized accessibility-tree desktop automation and stable-ref pattern.
- `qkal/Canny` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — evidence-led coding-agent completion supervision.
- `jexp/neo4jev` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — bounded graph navigation/beam-search pattern.
- `AkashPriyadarshii/jev-curate` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — structured dataset curation/sifting pattern.
- `fhshaik/typesafe-mario` — ADOPT_PATTERN_ONLY — emulator-state to bounded-action loop; root license not established in review.
- `RomanSlack/jev-drone` — ADOPT_PATTERN_ONLY — simulation-only hierarchical control/safety pattern.
- `emrickgarrett/OneVOneJev` — ADOPT_PATTERN_ONLY — real-time bounded multi-action judgment pattern; root license not established in review.
- `jarrodwatts/jev-trader` — ADOPT_PATTERN_ONLY — paper/dry-run latency and risk-accounting reference.
- `irfndi/prism-liquidity-agent` — ADOPT_PATTERN_ONLY — paper/backtest/replay/risk-gate architecture reference.
- `monteduro/killmyidea` — ADOPT_PATTERN_ONLY — versioned multi-dimensional product/startup scoring pattern; root license not established in review.

### Design quality / UI craft references

- `anthropics/skills:frontend-design` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — official distinctive frontend-design reference.
- `emilkowalski/skills:apple-design` — ADOPT_PATTERN_ONLY — fluid Apple-style web interaction reference.
- `emilkowalski/skills:emil-design-eng` — ADOPT_PATTERN_ONLY — UI polish and motion-decision reference.
- `MengTo/Skills:beautiful-shadows` — ADOPT_PATTERN_ONLY — layered neutral elevation/shadow reference.
- `addyosmani/web-quality-skills:accessibility` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — evidence-led WCAG-oriented accessibility workflow.
- `Superfuture/design-review` — ADOPT_PATTERN_ONLY — ranked UI critique patterns; telemetry/Pro service excluded.
- `shadcn-ui/ui:shadcn` — ADOPT_WHEN_NEEDED / CANONICAL — project-aware shadcn component/CLI workflow.
- `pbakaus/impeccable:adapt` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — adaptive/responsive context and input-mode patterns.
- `jakubkrehel/skills:better-interface` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — cross-discipline evidence-led interface review.
- `wshobson/agents:interaction-design` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — microinteraction, feedback, loading-state, motion and gesture patterns.

### High-recall discovery indexes — 2026-09-24

- `punkpeye/awesome-mcp-servers` — DISCOVERY_SOURCE / MCP_CATALOG — candidate MCP server discovery; every server requires original-source, publisher, license, permission, install and network/security audit before connection.
- `Shubhamsaboo/awesome-llm-apps` — DISCOVERY_SOURCE / APP_PATTERN_LIBRARY — agent/RAG/voice/skill application examples; audit only the exact subproject needed.
- `composio-community/awesome-codex-skills` — DISCOVERY_SOURCE_ONLY / PER_SKILL_AUDIT_REQUIRED — curated Codex skills; current canonical repository is under `composio-community`; root license not established and individual skills may differ.
- `sindresorhus/awesome` — DISCOVERY_SOURCE / ROOT_RECURSIVE_INDEX — CC0 meta-index; use when narrower domain catalogs are insufficient, then audit original candidate projects.
- `x1xhlol/system-prompts-and-models-of-ai-tools` — RESEARCH_REFERENCE_ONLY / DO_NOT_COPY / DO_NOT_EXECUTE — defensive prompt-leak/prompt-injection research; no root license observed and leaked/proprietary prompt material is not an Ercan OS instruction source.

### Weekly SEO diagnostic / DataForSEO

- DataForSEO OnPage API — ADOPT_WHEN_NEEDED / EXTERNAL_SEO_DIAGNOSTIC_PROVIDER — customizable site crawl, technical checks, selected browser/Lighthouse evidence.
- DataForSEO Labs Ranked Keywords — ADOPT_WHEN_NEEDED — external ranking/search-landscape and AI Overview reference evidence with explicit data freshness.
- DataForSEO SERP API — ADOPT_WHEN_NEEDED — priority live SERP verification by query/location/language/device.
- DataForSEO Backlinks API — ADOPT_WHEN_NEEDED — new/lost/referring-domain diagnostics; not an auto-disavow authority.
- DataForSEO AI Optimization / LLM Mentions — ADOPT_WHEN_NEEDED — optional AI-search visibility observation layer.
- Rerun `weekly-seo-diagnostic-dataforseo` — MANAGED_WORKFLOW_REFERENCE — optional weekly recurrence through managed deployment/API bridge; exact current template body requires live verification.

### Competitor creative intelligence

- Meta Ad Library / current official Meta transparency documentation — PRIMARY_EVIDENCE_SOURCE — public competitor ad creative/delivery evidence; performance inference restricted.
- `novoads/agent-skills:spy-competitor-ads` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — optional paid Meta-ad collection mechanics, durable provenance and brand/page disambiguation.
- Rerun `recreate-competitor-ads-meta` — MANAGED_WORKFLOW_REFERENCE — optional recurring execution surface; exact current template behavior requires live verification.

### Rerun API / workspace bridge

- `https://docs.rerun.build/` — PRIMARY_PROVIDER_DOCS — current Rerun workspace/MCP/API authority for agents, skills, schedules, triggers, runs, databases, connectors, share links and templates.
- `rerun-api-bridge` — ADOPT / JIT — Ercan OS -> Rerun workspace synchronization beneath managed-agent-deployment.
- Current architecture: one private machine per workspace; Boxes are organizational, not isolation walls. Official DPA/Privacy/marketing conflicts remain explicit `PROVIDER_STATE_CONFLICT` items.
- Pricing/package/Expert Program percentages are volatile commercial facts and must be re-read live.

### Managed agent deployment providers

- `https://rerun.build/` — ADOPT_WHEN_NEEDED / MANAGED_AGENT_DEPLOYMENT_PROVIDER / CLOSED_SOURCE_SAAS — managed recurring-agent runtime with Boxes, approvals, connectors/MCP/API, client/team handoff and live visibility. Ercan OS retains policy/eval authority; current Gmail/AUP/data/commercial limits must be reverified before production use.

### Agent runtime / orchestration / execution stack

- `ollama/ollama` — ADOPT_WHEN_NEEDED — local/open-model serving runtime.
- `langchain-ai/langchain` — ADOPT_WHEN_NEEDED — agent/application abstractions when they materially reduce integration complexity.
- `openinterpreter/openinterpreter` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — coding/computer-use harness with sandbox/approval boundaries.
- `microsoft/autogen` — SUPERSEDED_FOR_NEW_WORK — maintenance mode; use `microsoft/agent-framework` for new Microsoft-oriented systems.
- `microsoft/agent-framework` — ADOPT_WHEN_NEEDED — production multi-agent/workflow runtime with graph/handoff/checkpoint/HITL/observability patterns.
- `Aider-AI/aider` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — repo-map, Git-aware coding and lint/test-loop patterns.
- `Significant-Gravitas/AutoGPT` — ADOPT_PATTERN_ONLY / WATCHLIST — mixed-license agent/workflow platform reference; exact-path license required.
- `FoundationAgents/MetaGPT` — ADOPT_PATTERN_ONLY — SOP/role-decomposition patterns.
- `crewAIInc/crewAI` — ADOPT_WHEN_NEEDED — crew/flow runtime when project fit is verified.
- `stanfordnlp/dspy` — ADOPT_WHEN_NEEDED — modular LM programs and eval-driven optimization.
- `camel-ai/camel` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — multi-agent research/simulation/data-generation.
- `FlowiseAI/Flowise` — SUPERSEDED / HISTORICAL — reviewed canonical repository archived.
- `continuedev/continue` — SUPERSEDED / HISTORICAL — reviewed repository read-only/no longer actively maintained.
- `vercel/ai` — ADOPT_WHEN_NEEDED — provider-neutral AI application streaming/tool/UI SDK for compatible JS/TS stacks.
- `e2b-dev/E2B` — ADOPT_WHEN_NEEDED — isolated cloud code/computer-use sandbox.
- `ComposioHQ/composio` — ADOPT_WHEN_NEEDED — authenticated external tools/actions with per-user sessions.
- `zylon-ai/private-gpt` — ADOPT_WHEN_NEEDED — private/local AI API/RAG layer over compatible inference servers.
- `mem0ai/mem0` — ADOPT_WHEN_NEEDED — application memory layer with explicit tenancy/provenance/privacy.
- `AgentOps-AI/agentops` — ADOPT_WHEN_NEEDED — agent observability/session replay when incremental over existing telemetry.
- `THUDM/AgentBench` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED_FOR_BENCHMARKING — benchmark environments/methodology.
- `elevenlabs/elevenlabs-python` — ADOPT_WHEN_NEEDED — official voice/TTS/realtime voice SDK.
- `deepgram/deepgram-python-sdk` — ADOPT_WHEN_NEEDED — official STT/TTS/voice SDK.

### JEV runtime extension ecosystem

- `browser-use/jev-ultrafast` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — bounded structured browser operation.
- `tamaratran/fast-jev-compaction` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — transcript/history compaction without rewriting retained text.
- `vercel-labs/json-render` — ADOPT_WHEN_NEEDED — schema/catalog-constrained Generative UI; web/design route.
- `itsmostafa/typesafe-mcp` — ADOPT_WHEN_NEEDED — minimal generic MCP judgment adapter.
- `jkudish/jev-mcp` — ADOPT_WHEN_NEEDED — purpose-built semantic MCP toolset.
- `sharziki/semdecide` — ADOPT_WHEN_NEEDED — semantic CLI/CI primitive.
- `0xNatoshi/jev-codex-router` — ADOPT_PATTERN_ONLY / WATCHLIST — model/effort routing, fallback and calibration architecture.
- `GhalebDweikat/winnow` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — reversible context ingress sieve.
- `devagrawal09/jev-review` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED — staged review triage.
- `ellipsis-dev/blink` — ADOPT_PATTERN_ONLY — semantic file-tree navigation; root license not established.

## 23. Security, supply-chain and dependency quality

- `gitleaks/gitleaks` — ADOPT — secret scanning.
- `aquasecurity/trivy` — ADOPT_WHEN_NEEDED — dependency/container/filesystem vulnerability scanning.
- `github/codeql-action` — ADOPT — GitHub-native code scanning workflows when supported.
- `ossf/scorecard` — ADOPT_WHEN_NEEDED — upstream/open-source security posture signals.
- `dependabot/dependabot-core` — ADOPT_PATTERN_ONLY — dependency update/security automation reference.
- `google/osv-scanner` — ADOPT_WHEN_NEEDED — open-source vulnerability scanning.

## 24. Recursive discovery sources — high leverage catalogs

These are not automatically trusted dependencies. They are searchable upstream catalogs used by `upstream-intelligence-scan` and, where applicable, `developer-resource-discovery` to find additional candidates and then run normal Ercan OS verification.

- `sindresorhus/awesome` — DISCOVERY_SOURCE — broad curated list ecosystem.
- `bayandin/awesome-awesomeness` — DISCOVERY_SOURCE — index of awesome lists.
- `awesome-selfhosted/awesome-selfhosted` — DISCOVERY_SOURCE — thousands of self-hostable applications/services; list licensing and each project's license/security/ops are separate concerns.
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
- `ripienaar/free-for-dev` — DISCOVERY_SOURCE — developer SaaS/PaaS/IaaS free-tier candidate discovery; provider pricing/limits/production terms are volatile and must be rechecked.
- `public-apis/public-apis` — DISCOVERY_SOURCE — public API candidate discovery with Auth/HTTPS/CORS metadata; actual API docs/terms/quota/licensing remain authoritative.
- `hesreallyhim/awesome-claude-code` — DISCOVERY_SOURCE_ONLY — Claude Code/agent tooling catalog; restrictive CC BY-NC-ND list license means use only to locate original upstreams.
- `Alishahryar1/free-claude-code` — ADOPT_WHEN_NEEDED / CONDITIONAL_PROVIDER_ROUTER — multi-harness coding-model/provider proxy, shared catalog and fallback architecture; mandatory loopback+auth hardening and provider-by-provider terms/privacy/quota review before runtime use.
- `anthropics/skills` — ADOPT_WHEN_NEEDED / OFFICIAL_REFERENCE — official Anthropic Agent Skills examples/implementation patterns; exact sub-skill licensing varies, and canonical Agent Skills specification remains format authority.

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

## Web builder capability expansion — 2026-09-19

These are JIT engines/references for `.agents/skills/web-builder-capability-pack/SKILL.md`; they do not create stable agent identities.

- `OpenHands/OpenHands` — ADOPT_WHEN_NEEDED — autonomous coding/orchestration in isolated repo-scoped execution.
- `stackblitz-labs/bolt.diy` — ADOPT_PATTERN_ONLY — rapid AI app-builder workflow/reference.
- `dyad-sh/dyad` — ADOPT_WHEN_NEEDED — local AI application-builder option.
- `onlook-dev/onlook` — ADOPT_PATTERN_ONLY — visual code-editing workflow/reference.
- `BuilderIO/mitosis` — ADOPT_WHEN_NEEDED — cross-framework component generation where a real multi-framework/migration requirement exists.
- `WordPress/theme-check` — ADOPT_WHEN_NEEDED — WordPress theme conformance checking.
- `i18next/i18next` — ADOPT_WHEN_NEEDED — localization architecture for compatible JavaScript stacks.
- `GoogleChrome/workbox` — ADOPT_WHEN_NEEDED — service-worker/PWA/offline cache architecture.
- `semgrep/semgrep` — ADOPT_WHEN_NEEDED — source/static security analysis.
- `biomejs/biome` — ADOPT_WHEN_NEEDED — compatible JS/TS/JSON/CSS lint/format.
- `stylelint/stylelint` — ADOPT_WHEN_NEEDED — CSS linting where compatible.
- `html-validate/html-validate` — ADOPT_WHEN_NEEDED — structural HTML validation.

