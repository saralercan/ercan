# Ercan OS — Benchmark Runtime Contract

Status: active
Updated: 2026-08-31

Purpose: define how Ercan OS may execute behavioral/comparative agent benchmarks without fabricating results, leaking secrets or mixing incompatible runs.

Companion compute/security policy: `docs/evals/BENCHMARK_COMPUTE_POLICY.md`.

## Core rule

A benchmark result is evidence only when the exact model/runtime, Ercan OS policy commit, benchmark pin, task IDs, tools, evaluator and output artifacts are recorded. `NOT_RUN` is a valid state. Architecture, source-pack coverage or static CI success must never be converted into a behavioral score.

## Runtime layers

1. **Static governance CI** — no model/API key required; validates agent registration, source packs, routing, benchmark scenarios and research governance.
2. **Behavioral local/staging eval** — may call a configured model/runtime; must use isolated fixtures and explicit task manifests.
3. **External comparable benchmark** — must use the benchmark's canonical harness and pinned comparable version/commit.
4. **Production outcome eval** — uses real project acceptance evidence; cannot be replaced by public benchmark scores.

## Neutral evaluation runner

`Inspect AI` from the UK AI Security Institute is an approved **ADOPT_WHEN_NEEDED** evaluation-orchestration layer because it provides datasets, agents/tools, scorers, run logs and support for coding, agentic, reasoning and multimodal evaluations. It is not itself a benchmark authority; the underlying benchmark's canonical scoring/version contract remains authoritative.

Pinned preflight as of 2026-08-31:
- `inspect-ai==0.3.261`
- `inspect-evals==0.18.0`

The pins live in `benchmarks/manifest.json`. Before any paid or comparative run, re-check current upstream release notes and task comparability versioning. Inspect Evals moved new eval submissions to an external-register model in 2026; externally managed evals must be pinned to their upstream commit before use.

## Credentials and privacy

- Never commit API keys, OAuth tokens, cookies or production credentials.
- Runtime credentials come only from an approved secret store/environment.
- Benchmark tasks must not expose private customer/project data unless the specific authorized evaluation requires it.
- OpenAI Agents SDK tracing can capture generation/tool inputs and outputs. When test fixtures may contain sensitive data, set tracing to exclude sensitive content or disable tracing for that run.
- If OpenAI Agents SDK tracing is used, record an `agent_harness_id`/equivalent harness identifier in trace metadata when supported so runs can be grouped reproducibly.
- Do not export production traces to third-party evaluators unless explicitly approved.

## Compute boundary

- This repository is public. Persistent self-hosted GitHub runners must not execute untrusted PR/benchmark code with secrets or access to sensitive networks.
- Heavy external benchmarks use the benchmark project's documented cloud/evaluation path or another isolated ephemeral compute environment.
- Paid/cloud benchmark workflows are manual-only, master-only, explicit-confirmation gated and never scheduled.
- Scheduled jobs may refresh source pins/contracts but must not start paid model/cloud evaluation.

## Reproducibility record

Every behavioral run ledger must contain:
- date/time and operator/automation identity;
- Ercan OS commit;
- target agent identity/version;
- model/provider/runtime version;
- benchmark ID + exact pin;
- dataset split + task IDs;
- tool/MCP exposure list;
- system/developer policy version;
- temperature/retry/timeout/concurrency policy;
- evaluator/scorer version;
- raw result artifact location/hash;
- aggregate metrics and per-task outcome;
- hard fails;
- latency/token/cost when measurable;
- independent evaluator decision.

## Comparability

A result becomes `STALE_COMPARISON` when a benchmark changes in a way that affects comparability. Follow upstream task/version semantics. Never put results from incompatible benchmark versions in one leaderboard column without an explicit normalization method.

## Benchmark-specific execution

### BFCL
Use the official Berkeley Function Calling Leaderboard harness/package at the pinned comparable commit/version. Preserve test-category coverage; unrun categories cannot be silently ignored in overall claims. Record irrelevant-tool/hallucination behavior and latency in addition to accuracy.

The current Inspect Evals BFCL port implements BFCL V1, V2 and V3 categories, not BFCL V4. It may be used as an internal V1–V3 behavioral baseline, but its score must **never** be reported as a BFCL V4 leaderboard-comparable result. BFCL V4 comparative claims require the official Berkeley V4 harness/package and its pinned comparability contract.

### SWE-bench Verified
Use the official SWE-bench harness/evaluation path. Current reviewed package pin is recorded in `benchmarks/manifest.json`; as of 2026-08-31 that pin is `swebench==5.0.2` with its reviewed wheel SHA-256. Gold patches validate the harness only; Ercan OS scores require predictions produced by the actual configured agent/model.

For heavyweight execution prefer the official cloud paths documented by SWE-bench: Modal or `sb-cli`/AWS. Predictions must pass `scripts/validate_swebench_predictions.py`; each changed prediction set must use a unique `run_id`; record resolved/failed instance IDs and patch/test logs.

The repository provides `.github/workflows/swebench-modal-dispatch.yml` as a manual, master-only, explicit-`RUN` cloud-evaluation path. It requires separately configured Modal secrets and never receives production project credentials.

### SWE-bench Multimodal
Use public development instances for local preflight. Do not claim official test-set performance unless evaluated through the benchmark's accepted evaluation/submission path.

### Browser/GUI
Run only on disposable/local/staging environments or explicit authorized targets. Pin browser, viewport and fixture state. Reconcile final external state rather than grading only the generated narrative.

### Security
Only authorized fixtures. Seed known vulnerabilities/permission failures and measure detection + remediation correctness + false positives + unsafe action rate. A clean scan is never proof of absence of vulnerabilities.

### Creative/design
Automated metrics are supplementary. High-stakes brand/visual evaluation requires independent human review for hierarchy, brand fit, originality, readability, reference fidelity and asset integrity.

## Promotion states

- `NOT_RUN`
- `RUN_FAILED`
- `BEHAVIORAL_BASELINE`
- `PRODUCTION_VERIFIED`
- `BENCHMARKED_FRONTIER_CANDIDATE`
- `STALE_COMPARISON`

`BENCHMARKED_FRONTIER_CANDIDATE` requires a dated reproducible comparison against credible current baselines; it is never granted by static CI.
