---
name: javascript-specialist-capability-pack
description: Route material JavaScript and TypeScript architecture, debugging, refactoring, async/concurrency, runtime, browser, memory, performance, bundle, testing, dependency and security work through focused JIT capability roles mapped onto existing stable Ercan OS specialists. Use for JS/TS bugs, console/runtime errors, memory leaks, slow scripts, long tasks, bundle bloat, async waterfalls, Node/Bun/Deno runtime issues, React/Next JavaScript performance, TypeScript quality, npm supply-chain review or JavaScript-focused code review.
---

# JavaScript Specialist Capability Pack

Load `docs/standards/JAVASCRIPT_SPECIALIST_ENGINE.md`, root `AGENTS.md`, `docs/standards/AGENT_REGISTRY.md`, the active project adapter and framework/runtime-specific standards.

This is a JIT capability pack. It does **not** add stable routing identities or change the 21 Stable Core + 31 GitHub Specialist v3 Extension = 52 accounting. User-facing `@JavaScript` is a JIT alias that resolves to the smallest sufficient JavaScript/TypeScript pod.

## Capability roles and stable-owner mapping

Use only roles that materially contribute:

- `JavaScriptArchitect` -> `@WebArchitecture + @FrontendSystem`; module boundaries, ESM/CJS, runtime/client/server ownership and public API shape.
- `TypeScriptEngineer` -> `@FrontendSystem` plus the active platform owner; strictness, narrowing, generics, declaration/API contracts and typed-linting fit.
- `JavaScriptRuntimeDebugger` -> `@BrowserQA + @WebPerformance`; reproduce console/runtime/network/source-map failures before patching.
- `AsyncConcurrencyExpert` -> `@FrontendSystem + @WebPerformance`; async/await, Promise composition, cancellation, races, backpressure and waterfall removal.
- `JavaScriptPerformance` -> `@WebPerformance + @BrowserQA`; CPU/long-task/hot-path/trace evidence before optimization.
- `DOMPerformance` -> `@WebPerformance + @BrowserQA + @FrontendSystem`; layout thrashing, excessive DOM work, listeners, observers and main-thread cost.
- `MemoryLeakHunter` -> `@WebPerformance + @BrowserQA`; heap snapshots, detached DOM, retained objects/listeners, runaway caches/timers and before/after comparison.
- `JavaScriptSecurity` -> load `.agents/skills/digital-specialist-agent-pack/SKILL.md`; route secure-code work through the existing security JIT aliases and active platform owner.
- `NPMSupplyChain` -> existing `@SupplyChainSecurityAgent` JIT alias + active platform owner; lockfile, provenance, advisories, scripts and dependency-risk review.
- `JavaScriptCodeQuality` -> `@FrontendSystem`; ESLint/typescript-eslint/Biome selected from inspected project configuration rather than imposed globally.
- `JavaScriptRefactor` -> `@FrontendSystem + @ProductionQA`; behavior-preserving refactors require tests or equivalent executable evidence.
- `JavaScriptTesting` -> `@ComponentWorkshopQA + @BrowserQA` as applicable; select Vitest/Jest/node:test/Bun/Deno-native runners based on the existing stack.
- `JavaScriptBrowserQA` -> `@BrowserQA`; use Playwright-class browser E2E and Chrome DevTools evidence where runtime inspection is material.
- `ReactPerformance` -> `@FrontendSystem + @WebPerformance + @BrowserQA`; Vercel React/Next agent rules are a reviewed JIT reference, not universal JavaScript law.
- `NextJSRuntime` -> `@WebArchitecture + @FrontendSystem + @WebPerformance`; version-matched Next.js documentation remains authoritative.
- `NodeJSEngineer` -> `@WebArchitecture + @FrontendSystem`; event loop, workers, streams, diagnostics, permissions/security and runtime-version compatibility.
- `JavaScriptRuntimeCompatibility` -> `@WebArchitecture + @BrowserQA`; Node/Bun/Deno/browser behavior must be verified against the runtime actually used.
- `BundleOptimizer` -> `@WebPerformance + @FrontendSystem`; inspect module graph, dynamic imports, tree-shaking, source maps and shipped bytes before changing imports/build tooling.
- `JavaScriptDependencyAnalyst` -> `@FrontendSystem + @SupplyChainSecurityAgent`; distinguish maintenance/compatibility risk from known-vulnerability risk.
- `JavaScriptReviewer` -> `@ProductionQA + @BrowserQA` when runtime/UI behavior is touched; reviewer is independent of the primary implementation lane.

## Authority hierarchy

1. Inspected repository: package manager, lockfile, runtime pins, tsconfig/jsconfig, lint config, test config, bundler/framework and CI.
2. ECMAScript/TC39 and MDN for language/Web API semantics.
3. TypeScript official documentation for TypeScript behavior.
4. Runtime authority matching the project: Node.js, Bun or Deno official documentation and current version behavior.
5. Framework authority matching the project: React/Next/Vite/etc. official current docs.
6. Current browser/runtime evidence from tests, Playwright and Chrome DevTools.
7. Reviewed engineering skill packs and community references only when compatible with the inspected stack.

Never rewrite a project around a preferred tool merely because it appears in this pack.

## Reviewed JIT upstreams

- `addyosmani/agent-skills` — ADOPT_PATTERN_ONLY — MIT; production engineering workflow decomposition and evidence-oriented exit criteria.
- `vercel-labs/agent-skills:react-best-practices` — ADOPT_JIT — MIT; React/Next performance rules including waterfalls, bundle, server/client, rendering and JavaScript hot-path guidance.
- `ChromeDevTools/chrome-devtools-mcp` — ADOPT_JIT_RUNTIME_INSPECTION — Apache-2.0; console/network/performance/browser automation plus memory-debugging tools.
- `typescript-eslint/typescript-eslint` — ADOPT — MIT; typed linting when TypeScript project analysis justifies the cost.
- `eslint/eslint` — ADOPT — use the project's current flat-config/version contract rather than legacy assumptions.
- `biomejs/biome` — ADOPT_WHEN_NEEDED — MIT/Apache-2.0; fast lint/format tooling when stack-compatible.
- `vitest-dev/vitest` — ADOPT_WHEN_NEEDED — MIT; Vite-native unit/component/browser testing and V8 coverage when compatible.
- `microsoft/playwright` — existing canonical browser/E2E authority in Ercan OS.
- `oven-sh/bun` — RUNTIME_WHEN_PROJECT_USES_BUN; do not substitute for Node solely for speed claims.
- `denoland/deno` — RUNTIME_WHEN_PROJECT_USES_DENO; permission model is valuable but runtime migration requires explicit product/compatibility justification.
- `evanw/esbuild` / `vitejs/vite` — inspect/use only when the project build graph actually uses them.
- `clinicjs/node-clinic` — HISTORICAL/PATTERN_ONLY; upstream states it is not actively maintained, so do not make it a new production dependency.

## Default execution loop

`inspect stack -> reproduce -> establish baseline -> static/type analysis -> focused tests -> runtime/browser evidence when material -> smallest patch -> regression test -> rerun exact failure -> performance/security/browser verification as applicable -> independent review -> completion state`.

### Baseline evidence examples

- exact failing command/test and stack trace;
- console/network failure with source map;
- performance trace/long task;
- heap snapshot and retained-object path;
- bundle output/module graph;
- type/lint diagnostics;
- dependency/advisory evidence.

Do not optimize from intuition when an executable measurement is available.

## JavaScript-specific rules

- Independent async work should not be serialized by default; choose `Promise.all`, `allSettled`, race/cancellation or deliberate sequencing according to failure semantics.
- Do not replace algorithms with micro-optimizations without evidence that the hot path matters.
- Avoid layout read/write interleaving in browser hot paths.
- Avoid unbounded caches, timers, observers and event listeners; cleanup must be tied to lifecycle/ownership.
- Treat Server Actions/API handlers/mutations as public security boundaries when the framework exposes them that way.
- Do not use `eval`, `new Function`, unsafe HTML injection or shell execution as convenience fixes.
- Preserve ESM/CJS/package exports semantics; do not mass-convert module format without consumer/runtime evidence.
- TypeScript suppression (`any`, `@ts-ignore`, broad casts) is not a valid default fix.
- A passing formatter/linter is not proof of runtime correctness.
- A passing unit test is not proof of browser behavior when DOM/network/hydration/browser APIs are involved.
- A clean dependency audit is not a security certification.
- Runtime migration (Node <-> Bun <-> Deno) is an architecture decision, not a performance quick fix.

## Completion gate

A material JavaScript task is `VERIFIED` only when the originally observed failure/regression is rerun successfully, applicable tests/type/lint/build gates pass, runtime/browser evidence is refreshed where relevant, and independent QA confirms no material regression. Otherwise report `PARTIAL`, `BLOCKED`, or `NOT VERIFIED`.
