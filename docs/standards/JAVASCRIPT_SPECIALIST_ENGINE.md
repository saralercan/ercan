# Ercan OS — JavaScript Specialist Engine

Status: active
Date: 2026-09-24
Skill: `.agents/skills/javascript-specialist-capability-pack/SKILL.md`
Regression eval: `docs/evals/JAVASCRIPT_SPECIALIST_ENGINE_REGRESSION.md`
Evidence scan: `docs/upstream/scans/2026-09-24-javascript-specialist-capability-pack.md`

## Purpose

Provide a disciplined JavaScript/TypeScript engineering layer for browser, frontend, Node/server, React/Next and mixed JS runtimes without creating duplicate permanent agents. The engine converts the user-facing `@JavaScript` alias into focused JIT capability roles mapped onto existing Ercan OS owners.

The engine is execution-first: reproduce and measure before patching, preserve existing project/runtime choices unless evidence justifies migration, and verify the original failure after every material fix.

## Stable-routing contract

No new stable identity is created. The stable count remains **52**.

`@JavaScript` is a JIT alias. It may compose:

`JavaScriptArchitect, TypeScriptEngineer, JavaScriptRuntimeDebugger, AsyncConcurrencyExpert, JavaScriptPerformance, DOMPerformance, MemoryLeakHunter, JavaScriptSecurity, NPMSupplyChain, JavaScriptCodeQuality, JavaScriptRefactor, JavaScriptTesting, JavaScriptBrowserQA, ReactPerformance, NextJSRuntime, NodeJSEngineer, JavaScriptRuntimeCompatibility, BundleOptimizer, JavaScriptDependencyAnalyst, JavaScriptReviewer`.

Each role maps to existing stable/JIT owners defined by the skill; roles are capabilities, not additional routing identities.

## Intake contract

Before editing material JS/TS code, inspect as available:

- `package.json`, workspaces and package manager;
- lockfile and overrides/resolutions;
- Node/Bun/Deno/runtime pins and CI runtime;
- `tsconfig*.json` / `jsconfig.json`;
- ESLint/typescript-eslint/Biome/Prettier configuration;
- test runner and browser-test configuration;
- build/bundler/framework version;
- server/client boundaries;
- deployment runtime and environment;
- exact failure evidence.

Do not infer framework/runtime versions from memory when the repository states them.

## Source hierarchy

For language semantics, prefer ECMAScript/TC39 + MDN. For TypeScript use official TypeScript docs. For runtime behavior use the exact project's Node/Bun/Deno official docs. For React/Next/Vite use version-matched official framework docs. Use Vercel's reviewed agent performance rules as a high-value implementation reference for React/Next but never as a substitute for framework/runtime authority.

Current runtime measurements outrank generic advice when diagnosing a specific project.

## Diagnosis lanes

### Runtime and console failures
Capture the exact repro, stack/source map, console, network and environment. Fix the smallest causal surface, then rerun the same repro.

### Async and concurrency
Build a dependency graph of async operations. Parallelize only independent work; preserve required sequencing. Explicitly choose error/cancellation semantics rather than reflexively replacing every sequence with `Promise.all`.

### Performance
Separate architecture-level issues from micro-optimizations. Prefer trace evidence. Diagnose network waterfalls, bundle/startup cost, long tasks, layout/reflow, serialization, render churn and hot loops separately.

### Memory
Use repeatable actions and before/after snapshots. Look for detached DOM, retained listeners/observers/timers, accidental globals, unbounded caches/queues and request/session state retained beyond ownership.

Chrome DevTools MCP memory tools may be used JIT when available. A single heap snapshot without a reproduction sequence is rarely enough to prove a leak.

### TypeScript
Prefer narrowing and API/contract repair over suppression. Typed linting is enabled only when its additional project-analysis cost is justified. Do not force TS migration onto a JavaScript codebase unless requested or materially justified.

### Bundle
Measure shipped output before changing imports/build tooling. Check accidental server/client crossings, barrel imports, duplicated packages, dynamic-import opportunities, tree-shaking blockers and large third-party code.

### Security and dependencies
Load the existing digital security specialist pack for threat-sensitive work. Review package provenance/maintenance, lifecycle scripts, advisories, lockfile integrity and dangerous dynamic execution surfaces. Keep security findings distinct from style/code-quality findings.

## Tool-selection policy

- ESLint/typescript-eslint vs Biome: follow existing project choice first; introduce a new tool only for a concrete gap/migration task.
- Vitest/Jest/node:test/Bun test/Deno test: preserve existing runner unless migration itself is in scope.
- Playwright: browser/E2E verification authority when a real browser flow matters.
- Chrome DevTools MCP: runtime/performance/memory inspection when available and useful.
- Bun/Deno: only when the project already uses them or explicit runtime evaluation/migration is requested.
- Clinic.js: historical reference only because the upstream states it is not actively maintained.

## Refactor contract

A behavior-preserving refactor must preserve externally observable behavior and add or reuse regression evidence. Large refactors should be sliced so the exact behavior remains testable between steps.

Do not combine unrelated formatter churn, dependency upgrades, module-format migrations and behavioral fixes in one patch unless the task explicitly requires them.

## Verification matrix

Select the smallest sufficient set:

`lint/static -> typecheck -> unit -> integration -> build -> browser E2E -> console/network -> performance trace -> heap comparison -> bundle diff -> dependency/security checks -> independent review`.

Not every task needs every gate. Every task needs evidence tied to its failure/risk.

## Completion vocabulary

- `VERIFIED`: original repro is resolved and relevant gates were rerun successfully with fresh evidence.
- `PARTIAL`: useful implementation completed but one or more material verification surfaces remain.
- `BLOCKED`: an external/runtime/access/dependency condition prevents required progress.
- `NOT VERIFIED`: code or advice exists but executable evidence is absent or stale.
