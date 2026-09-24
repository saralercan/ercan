# JavaScript Specialist Capability Pack — Upstream Scan

Date: 2026-09-24
Scope: JavaScript/TypeScript engineering agents, agent-oriented engineering skills, runtime debugging, browser/memory/performance, lint/type quality, testing, runtimes and current technical guidance.

## Decision

Create one JIT JavaScript/TypeScript capability pack with focused roles rather than a new permanent JavaScript agent tree. Map all roles to existing stable Ercan OS specialists. Stable identity count remains 52.

## High-value upstreams

### addyosmani/agent-skills — ADOPT_PATTERN_ONLY
- MIT.
- Production engineering skill collection organized around spec/plan/build/test/review/ship style workflows.
- Strongest value for this pack: evidence-oriented workflow decomposition and explicit exit criteria.
- Boundary: not JavaScript language authority and not a replacement for project/runtime docs.

### vercel-labs/agent-skills / react-best-practices — ADOPT_JIT
- MIT.
- Agent/LLM-oriented React and Next.js performance rules.
- Current reviewed surface includes elimination of async waterfalls, bundle optimization, server/client performance, rendering and JavaScript hot-path rules.
- Boundary: use only for compatible React/Next tasks; framework-version docs remain authoritative.

### ChromeDevTools/chrome-devtools-mcp — ADOPT_JIT_RUNTIME_INSPECTION
- Apache-2.0.
- Current 2026 surface supports browser control/inspection, network/console/performance traces and memory-debugging tooling including heap snapshot capture/comparison.
- Strong fit for JavaScriptRuntimeDebugger, DOMPerformance and MemoryLeakHunter.
- Boundary: browser content may be sensitive; tool access must remain within authorized surfaces and project privacy constraints.

### typescript-eslint/typescript-eslint — ADOPT
- MIT.
- Typed linting gives deeper semantic analysis by using TypeScript project information, at a real performance cost.
- Use typed presets only when the project benefits; do not enable expensive whole-project analysis by reflex.

### ESLint — ADOPT_PROJECT_NATIVE
- Preserve the repository's current configuration/version.
- Current ecosystem uses flat config; do not revive legacy eslintrc assumptions in new setups.
- Rule output is quality evidence, not runtime proof.

### biomejs/biome — ADOPT_WHEN_NEEDED
- MIT or Apache-2.0.
- Fast unified formatter/linter for JS/TS/JSX/TSX and other web formats.
- Do not replace existing ESLint/Prettier stacks unless migration has a concrete payoff and plugin/rule gaps are understood.

### vitest-dev/vitest — ADOPT_WHEN_NEEDED
- MIT.
- Vite-native testing with TypeScript/JSX, browser mode and V8 coverage.
- Browser mode can use Playwright/WebDriver providers; use it when the project already fits Vitest/Vite or when migration is specifically justified.
- Preserve existing runner by default.

### microsoft/playwright — EXISTING CANONICAL
- Existing Ercan OS browser E2E authority.
- Pair with Chrome DevTools runtime evidence when a test tells *what* broke but deeper runtime profiling is needed.

### Node.js official docs/tooling — AUTHORITY_WHEN_NODE
- Use exact project Node version.
- Prefer built-in inspector/diagnostics/worker/event-loop/runtime controls over stale third-party profiling dependencies when sufficient.

### oven-sh/bun — RUNTIME_WHEN_PROJECT_USES_BUN
- Modern all-in-one JS/TS runtime, package manager, test runner and bundler.
- Do not migrate Node projects merely from headline speed claims; compatibility and workload evidence decide.

### denoland/deno — RUNTIME_WHEN_PROJECT_USES_DENO
- MIT.
- JS/TS runtime with explicit permission model and secure-by-default I/O posture.
- Valuable for permission-constrained runtimes, but migration remains an architecture decision and native/Node compatibility must be checked.

### evanw/esbuild / vitejs/vite — PROJECT_NATIVE
- High-value build graph/bundling references when present in the inspected project.
- Do not replace one with another merely because a benchmark is faster.

### clinicjs/node-clinic — HISTORICAL/PATTERN_ONLY
- MIT.
- Repository explicitly states it is not actively maintained and may produce inaccurate results due to Node-internals coupling.
- Do not promote to a new production default.

## Current article/documentation knowledge promoted into agent behavior

- MDN: independent async operations should not be serialized with sequential await when concurrency semantics permit; Promise combinators have different failure/completion semantics.
- Chrome DevTools: performance and heap evidence should be gathered from repeatable runtime actions; current agent tooling exposes memory snapshot analysis.
- TypeScript-eslint: typed linting is more powerful but slower because TypeScript analyzes the project; enable intentionally.
- Vitest: browser mode runs tests in real browser semantics and V8 coverage uses runtime/CDP collection.
- Deno: permissions are explicit and scoped; broad allow-all style execution defeats the security model.
- OWASP NodeJS guidance: linters complement but do not replace SAST/security review; dangerous dynamic execution and server-side attack surfaces require explicit treatment.

## Rejected architecture

Do not create 20 new stable identities. The JavaScript roles are JIT lanes and user-facing aliases. This avoids routing explosion, duplicated ownership and the false impression that selecting more agents produces better engineering.

## Required integration

- add `.agents/skills/javascript-specialist-capability-pack/SKILL.md`;
- add `docs/standards/JAVASCRIPT_SPECIALIST_ENGINE.md`;
- add `docs/evals/JAVASCRIPT_SPECIALIST_ENGINE_REGRESSION.md`;
- expose `@JavaScript` and specialist JIT roles in the registry/router;
- connect material JS/TS website work from the web-builder pack;
- keep stable identity count unchanged.
