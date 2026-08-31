# Ercan OS Agent Readiness Run — 2026-08-31

Run type: deterministic structural benchmark
Repository: `saralercan/ercan`
Stable identities: 21
Final policy/validator commit under test: `68f2c3b12e014491b945be8737b98fdea979997e`

## What was actually executed

GitHub Actions workflow: `Ercan OS Agent Scoreboard`
Workflow file: `.github/workflows/agent-scoreboard.yml`
Validator: `scripts/validate_agent_scoreboard.py --check`

Five checks per stable identity:
1. stable-core registration;
2. dedicated source-pack heading;
3. agent-specific championship scenario;
4. maintained registry/routing identity;
5. world-class research/JIT governance integration.

This is a structural/governance benchmark only. It is not a behavioral model benchmark.

## Run history

### Run 2 — first master execution
Workflow run: `33345308962`
Result: **FAIL**
Reason: byte-for-byte generated Markdown drift gate was too brittle and failed before structural result could be trusted.
Action: changed scoreboard checking to semantic rows/summary plus independent structural exit state.

### Run 3 — semantic validator execution
Workflow run: `33345382044`
Result: **FAIL**
Real finding: five screenshot-production identities (`@ScreenshotToCode`, `@RealAsset`, `@PixelMatch`, `@UXEnhancement`, `@ProductionQA`) are intentionally nested under `###` headings in `AGENT_REGISTRY.md`; validator incorrectly accepted only top-level `##` headings and scored those agents 80/100.
Action: routing-contract validation was corrected to accept maintained top-level or nested stable identities.

### Run 4 — corrected PR execution
Workflow run: `33345421237`
Job: `static-agent-readiness`
Result: **SUCCESS**
Critical validation step: **SUCCESS**
Result: **21/21 structural contracts pass**.

### Run 5 — master post-merge execution
Workflow run: `33345440306`
Job: `static-agent-readiness`
Result: **SUCCESS**
Critical validation step: **SUCCESS**
Result: **21/21 structural contracts pass on master**.

## Current scoreboard interpretation

- Static readiness: **21/21 PASS, 100/100 each under the five-contract static rubric**.
- Behavioral championship suite: **NOT_RUN**.
- External SWE-bench/BFCL/HELM/WebArena-style comparative benchmarks: **NOT_RUN** unless an actual pinned model/runtime/tool harness executes them.
- No agent is labeled perfect or best-in-world from this static result.

## Why the failed runs are retained

The first two failures are evidence that the validator is not a decorative green check. They exposed weaknesses in the benchmark implementation itself, were diagnosed from real CI logs, and were corrected before the final master success. Keeping them prevents rewriting history and supports reproducibility.
