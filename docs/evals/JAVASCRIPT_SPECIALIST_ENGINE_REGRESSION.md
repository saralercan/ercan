# Ercan OS — JavaScript Specialist Engine Regression Eval

Date: 2026-09-24
Standard: `docs/standards/JAVASCRIPT_SPECIALIST_ENGINE.md`
Skill: `.agents/skills/javascript-specialist-capability-pack/SKILL.md`

Purpose: prevent JavaScript work from regressing into guess-first patches, tool-driven rewrites, type suppression, unmeasured performance claims or build-only completion.

## Eval 1 — Console/runtime bug

Prompt class: “Bu sayfada JavaScript hatası var, düzelt.”

Expected:
- inspect stack/framework/runtime;
- reproduce the error and capture exact console/stack evidence;
- make the smallest causal patch;
- rerun the same reproduction plus relevant tests;
- use browser evidence when the bug occurs in browser state.

Fail if:
- patch is based only on source reading when reproduction is available;
- final state is VERIFIED without rerunning the original failure.

## Eval 2 — Async waterfall

Prompt class: “API çok yavaş; bir sürü await var.”

Expected:
- map dependencies before parallelizing;
- parallelize only independent work;
- preserve failure semantics/cancellation;
- compare before/after timing when material.

Fail if:
- every sequential await is mechanically replaced with Promise.all;
- dependent operations become racy.

## Eval 3 — Memory leak

Prompt class: “Sayfayı birkaç kez açınca RAM artıyor.”

Expected:
- define a repeatable interaction;
- capture baseline and post-repro memory evidence;
- inspect detached DOM/listeners/timers/observers/caches;
- compare after the fix.

Fail if:
- a single snapshot is treated as proof;
- calling GC or clearing data is presented as the root-cause fix.

## Eval 4 — DOM performance

Prompt class: “Scroll animasyonu takılıyor.”

Expected:
- inspect long tasks/layout/style/repaint evidence;
- check layout read/write interleaving and event frequency;
- patch only demonstrated bottlenecks;
- browser-verify the interaction after the patch.

Fail if:
- generic debounce/throttle is added without evidence;
- smoothness is claimed from code inspection only.

## Eval 5 — TypeScript error

Prompt class: “TypeScript build kırıldı; hızlıca geçir.”

Expected:
- fix the contract/narrowing/root type mismatch;
- keep strictness intact unless the repository intentionally configures otherwise;
- use suppressions only with explicit narrow justification;
- rerun typecheck/build.

Fail if:
- `any`, broad casts or `@ts-ignore` are the default solution.

## Eval 6 — Bundle bloat

Prompt class: “JS bundle çok büyüdü.”

Expected:
- establish bundle/module graph evidence;
- distinguish first-load vs lazy chunks;
- check duplicate packages, barrels, client/server crossings and heavy third parties;
- verify an actual bundle reduction and behavior.

Fail if:
- build tooling is replaced before measuring;
- tree-shaking is assumed rather than verified.

## Eval 7 — React/Next performance

Prompt class: “Next.js siteyi JavaScript açısından hızlandır.”

Expected:
- load ReactPerformance/NextJSRuntime lanes;
- use version-matched framework docs and Vercel reviewed rules;
- prioritize waterfalls/bundle/server-client boundaries before hot-loop micro-optimizations;
- rerun browser/performance evidence.

Fail if:
- React/Next-specific rules are applied to unrelated JS runtimes;
- micro-optimizations are reported as a major win without measurement.

## Eval 8 — Dependency/security

Prompt class: “npm paketlerini kontrol et.”

Expected:
- separate known vulnerabilities from maintenance/provenance/compatibility concerns;
- inspect lockfile/package manager and lifecycle scripts as relevant;
- route security-sensitive findings through existing security specialists;
- never call a clean audit a security certification.

Fail if:
- package updates are made blindly;
- semver-major migrations are bundled into an unrelated fix.

## Eval 9 — Test-runner choice

Prompt class: “Testleri güçlendir.”

Expected:
- preserve existing Jest/Vitest/node:test/Bun/Deno runner unless migration is requested;
- add browser-mode/Playwright only where browser semantics matter;
- add regression coverage tied to observed risks.

Fail if:
- a favorite runner is imposed without a gap analysis.

## Eval 10 — Runtime compatibility

Prompt class: “Node yerine Bun’a geçir, daha hızlı olsun.”

Expected:
- treat runtime migration as architecture/compatibility work;
- inventory Node APIs/native deps/deployment assumptions/tests;
- benchmark relevant workloads;
- report migration risk and actual compatibility.

Fail if:
- speed marketing claims are sufficient evidence;
- Node is replaced without compatibility/regression validation.

## Eval 11 — Stale tooling

Prompt class: “Clinic.js’i standart profiler yap.”

Expected:
- recognize reviewed upstream note that Clinic.js is not actively maintained;
- keep it historical/pattern-only;
- prefer current Node/browser diagnostics compatible with the inspected runtime.

Fail if:
- it is promoted to a default production dependency.

## Eval 12 — Code-quality tool choice

Prompt class: “ESLint mi Biome mu? Projeye uygula.”

Expected:
- inspect current config, plugins and CI contracts;
- preserve project semantics;
- quantify migration gaps before replacing tools;
- validate lint/type/build after any migration.

Fail if:
- formatter/linter choice is treated as runtime correctness.

## Eval 13 — Review independence

Prompt class: any material JS refactor.

Expected:
- primary implementation and JavaScriptReviewer/ProductionQA are logically separated;
- reviewer checks original requirement, failure evidence, tests and hidden behavioral drift.

Fail if:
- the same implementation pass self-certifies without fresh evidence.

## Eval 14 — Completion state

`VERIFIED` requires fresh task-relevant executable evidence. File existence, successful edit, lint-only success or “looks correct” are insufficient.

Allowed states:
- VERIFIED
- PARTIAL
- BLOCKED
- NOT VERIFIED

## Eval 15 — Premium website motion

Prompt class: “Hero, menü, kartlar ve scroll alanları hareketli olsun; premium görünsün.”

Expected:
- route MotionInteractionEngineer + ScrollStorytellingEngineer and design/brand owners as needed;
- choose native CSS/WAAPI/Motion/GSAP by actual complexity;
- preserve keyboard/focus behavior and reduced-motion fallback;
- browser-verify mobile and desktop motion;
- inspect jank/long-task/layout cost before VERIFIED.

Fail if:
- every element receives decorative motion without hierarchy;
- animation makes content harder to use;
- no reduced-motion path exists.

## Eval 16 — Animated data chart

Prompt class: “Canlı veriyi hareketli grafiklerle göster.”

Expected:
- route DataVizEngineer;
- select Recharts/ECharts/D3 by framework and chart needs;
- preserve truthful axes, units, labels and source data;
- provide accessible interpretation/summary where needed;
- verify update/animation behavior with representative data.

Fail if:
- animation fabricates/interpolates meaning not present in data;
- chart is unreadable without hover or color alone.

## Eval 17 — Canvas/particle scene

Prompt class: “Arka planda interaktif parçacık sistemi yap.”

Expected:
- consider Canvas 2D/PixiJS before WebGL/Three.js;
- pause or reduce offscreen/background animation;
- cap DPR/particle count for mobile when required;
- respect reduced motion;
- measure frame/render cost.

Fail if:
- an unnecessary 3D engine is added for a simple 2D effect;
- continuous render loop leaks after navigation/unmount.

## Eval 18 — 3D website object

Prompt class: “Ürünü/tekneyi gerçek 3D olarak web sitesinde döndür ve hareket ettir.”

Expected:
- route WebGL3DEngineer;
- use Three.js-class tooling only when actual 3D is required;
- load optimized authorized model assets;
- handle camera/lighting/controls, resize, teardown and GPU fallback;
- test representative mobile/desktop hardware classes and interaction fallbacks.

Fail if:
- CSS faux-3D is called a real 3D model;
- heavy scene blocks core page interaction or has no fallback.

## Eval 19 — SVG/logo motion

Prompt class: “Bu çizgisel logo/harita/ikon SVG olarak çizilsin ve animasyonlu olsun.”

Expected:
- route SVGAnimationEngineer and brand/asset owners;
- preserve exact geometry/brand fidelity;
- prefer SVG/CSS/WAAPI for simple path/stroke motion, GSAP only when advanced choreography/morphing warrants it;
- test responsiveness and reduced motion.

Fail if:
- logo geometry is altered for animation convenience;
- raster screenshots replace requested vector output.

## Eval 20 — Page transitions

Prompt class: “Sayfalar arasında akıcı geçişler istiyorum.”

Expected:
- consider native View Transition API first where supported;
- provide fallback for unsupported/older contexts;
- preserve navigation semantics, focus and history behavior;
- avoid delaying navigation just for animation.

Fail if:
- transition requires JavaScript for basic navigation to function;
- animation breaks browser back/forward or accessibility.
