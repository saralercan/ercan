# JavaScript Motion Graphics & Interactive Web Expansion — Upstream Scan

Date: 2026-09-24
Parent skill: `.agents/skills/javascript-specialist-capability-pack/SKILL.md`
Parent standard: `docs/standards/JAVASCRIPT_SPECIALIST_ENGINE.md`

## Goal

Expand the JavaScript/TypeScript capability pack beyond debugging and code quality so it can build the interaction and visual-computation layer required by modern websites: UI behavior, premium motion, scroll storytelling, animated charts, SVG motion, Canvas graphics, particles/generative visuals, vector animation and genuine 3D/WebGL scenes.

The expansion remains JIT and does not add stable routing identities.

## Platform-native first

### Web Animations API
Use for JavaScript-controlled DOM animation when native timing/playback is sufficient. It exposes the browser animation engine directly and should be preferred over a dependency for ordinary transitions/timelines that do not need a richer orchestration layer.

Accessibility rule: provide reduced/static behavior for users who request reduced motion and avoid uncontrolled flashing/vestibular-heavy effects.

### View Transition API
Current MDN baseline indicates broad latest-browser availability from October 2025 for the core ViewTransition/startViewTransition surface. Use for SPA and same-origin MPA view changes when it improves continuity. Preserve normal navigation as fallback; transition support must never be required for the website to function.

### CSS scroll-driven animations
Use scroll/view timelines when browser support and fallback requirements fit the target audience. Prefer browser-driven timelines over main-thread scroll listeners for effects that can be expressed declaratively.

Some related ViewTimeline surfaces remain less universally available; verify current compatibility for the actual target browser matrix.

## Motion engines

### greensock/GSAP — ADOPT_WHEN_NEEDED
- Framework-agnostic JavaScript animation platform.
- Strong fit: advanced sequencing/timelines, ScrollTrigger, SVG/path/morph choreography, Canvas/WebGL property orchestration, highly controlled branded motion.
- Current upstream states the full toolset is free including commercial use, but it remains under GreenSock's standard license rather than MIT/Apache-style OSS terms.
- Do not add GSAP for ordinary CSS hover/fade/slide effects.

### motiondivision/motion — ADOPT_WHEN_NEEDED
- MIT.
- Current package: `motion`; React entry point: `motion/react`.
- Strong fit: React/component animation, gestures, springs, layout transitions, scroll-linked effects, enter/exit flows and compact production UI motion.
- Hybrid implementation can use browser-native animation capabilities where appropriate.
- Prefer it over GSAP when the problem is primarily component/layout/gesture-oriented and the project already fits its framework model.

## Data visualization

### recharts/recharts — ADOPT_WHEN_NEEDED
- MIT.
- React + D3-based declarative SVG charting.
- Strong fit: conventional dashboards and product/admin charts in React where component composition and accessible DOM/SVG output matter.
- Keep React version/package compatibility in scope.

### Apache ECharts (`apache/echarts`) — ADOPT_WHEN_NEEDED
- Apache-2.0.
- Strong fit: rich interactive dashboards, large chart vocabulary and heavily interactive Canvas/SVG visualization.
- Avoid importing the full feature set when tree-shakable modular use is available.

### d3/d3 — ADOPT_WHEN_NEEDED
- Permissive license.
- Strong fit: bespoke visualization geometry, scales, layouts and interactions when higher-level chart libraries constrain the design.
- D3 is not the default for ordinary line/bar charts merely because it is powerful.

Data integrity rule: animation may reveal or transition real data but must not invent values, hide units, distort scales or imply unsupported causal relationships.

## 2D creative rendering

### PixiJS (`pixijs/pixijs`) — ADOPT_WHEN_NEEDED
- MIT.
- Current upstream supports WebGL and WebGPU rendering with asset loading, text, primitives/SVG drawing, textures, filters, blending and pointer/touch interaction.
- Strong fit: many animated 2D objects, particles, interactive backgrounds, generative graphics and rich canvas-like experiences.
- Prefer stable WebGL renderer when the WebGPU target matrix is uncertain; current upstream documentation still describes WebGPU as maturing/experimental in some contexts.
- Add visibility pause, cleanup, DPR/quality caps and mobile budgets.

### Canvas 2D — PREFER_NATIVE_WHEN_SUFFICIENT
Use the native Canvas API before a renderer dependency for small custom drawing, charts, signatures, particle counts and procedural effects that do not require a scene graph.

## 3D / GPU

### mrdoob/three.js — ADOPT_WHEN_NEEDED
- MIT.
- Strong fit: actual 3D product/object presentation, camera scenes, model animation, morph targets, materials/shaders and WebGL/WebGPU experiences.
- Current upstream marks the CommonJS build as deprecated; prefer ESM for new work.
- Three.js animation supports model clips, mixers, crossfades and synchronized property/bone/morph animation.
- Require optimized model/texture assets, resize/teardown, device capability checks and a functional fallback where core content must remain available.

Do not use a 3D engine for ordinary DOM/card/page animation.

## Vector motion assets

### airbnb/lottie-web — ADOPT_WHEN_NEEDED
- Strong fit: authorized After Effects/Bodymovin JSON animations rendered through SVG/Canvas/HTML.
- Verify the specific exported feature set, renderer, file size and mobile performance instead of assuming every After Effects construct is reproduced exactly.
- Motion asset provenance/rights remain mandatory.

### Rive-class interactive vector runtime — EVALUATE_WHEN_NEEDED
Use when the project supplies/chooses state-machine-driven interactive vector assets and the current runtime/license/toolchain has been reviewed. Do not add a second vector runtime when Lottie/SVG/native animation already satisfies the requirement.

## Routing additions

JIT roles added:
- WebInteractionEngineer
- MotionInteractionEngineer
- ScrollStorytellingEngineer
- PageTransitionEngineer
- SVGAnimationEngineer
- DataVizEngineer
- CanvasGraphicsEngineer
- WebGL3DEngineer
- CreativeCodingEngineer
- VectorMotionEngineer
- MotionAccessibilityQA

They map to existing stable web/frontend/performance/browser/accessibility/brand/asset/QA owners and do not change the stable identity count.

## Required behavior

When a user asks for “animated”, “moving graphics”, “premium motion”, “interactive chart”, “particles”, “3D”, “scroll animation”, “parallax”, “animated SVG/logo/map”, “live dashboard” or equivalent:

1. inspect the framework, browser matrix and current dependencies;
2. define the visual/interaction requirement before selecting a library;
3. prefer the lightest sufficient renderer/animation system;
4. implement responsive behavior and teardown/lifecycle management;
5. preserve keyboard/touch/focus semantics;
6. implement reduced-motion behavior;
7. verify browser/mobile behavior and performance;
8. run visual/interaction QA;
9. report VERIFIED only with rendered/runtime evidence.

## Non-goals

This pack does not make motion mandatory. Static pages remain static when motion does not improve communication or product behavior. It also does not treat ornamental effects as more important than content, conversion, accessibility or performance.
