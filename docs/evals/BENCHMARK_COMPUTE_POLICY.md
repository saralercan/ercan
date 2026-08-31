# Ercan OS — Benchmark Compute Policy

Status: active
Updated: 2026-08-31

Purpose: define where and how expensive behavioral/comparative benchmarks may run without exposing credentials, weakening reproducibility, or allowing untrusted code to persist on benchmark infrastructure.

## Core rule

Benchmark compute is disposable infrastructure, not a trusted long-lived workstation. Public-repository pull requests must never execute untrusted benchmark code on a persistent self-hosted runner that also has secrets or access to sensitive networks.

## Compute priority

1. **GitHub-hosted standard runners** — static contracts, source freshness, lightweight smoke/eval orchestration only.
2. **Official benchmark cloud path** — preferred for heavyweight external benchmarks when the benchmark project documents it. For SWE-bench, use the official Modal or `sb-cli`/AWS evaluation path.
3. **GitHub Larger Runners** — acceptable only if the repository is moved/available inside an eligible organization/enterprise and a dedicated runner group is configured. Use an ephemeral GitHub-hosted larger runner, not a persistent personal self-hosted host.
4. **External ephemeral VM/container service** — acceptable when isolated per run, credentials are short-lived/scoped, and all inputs/outputs are recorded.
5. **Persistent self-hosted runner** — prohibited for this public repository's untrusted PR/benchmark code. A future exception requires a private repository or organization-controlled isolated runner group, no production credentials, no sensitive network access, and a documented security review.

## SWE-bench compute

Canonical docs: https://www.swebench.com/SWE-bench/guides/evaluation/

SWE-bench evaluation is Docker/container based. Official documentation supports cloud evaluation through Modal and `sb-cli`/AWS. Local/full Docker runs require substantial disk/RAM/CPU and are not appropriate for the ordinary GitHub-hosted runner.

### Preferred path

- Generate predictions in an actual Ercan OS model/agent runtime.
- Validate the predictions JSONL deterministically with `scripts/validate_swebench_predictions.py`.
- Record the Ercan OS commit, target agent, model/runtime, generation settings, task IDs and predictions SHA-256.
- Submit predictions to the official SWE-bench cloud evaluation path.
- Use a unique `run_id` for each changed prediction set because SWE-bench caches by run ID and instance ID.
- Ingest the returned report/logs into a dated Ercan OS run ledger.

### Default staged progression

1. 1–3 gold/known smoke instances only to validate the environment/harness.
2. Small generated-prediction subset.
3. SWE-bench Lite or selected Verified subset for development.
4. SWE-bench Verified full 500 only after smoke/subset passes and spend/compute is explicitly approved.
5. SWE-bench Multimodal test performance only through the benchmark's accepted evaluation/submission path.

Gold patches validate the harness only. They do not count as Ercan OS model/agent performance.

## Secrets

- Never commit Modal, AWS, OpenAI, Anthropic or other runtime credentials.
- GitHub workflows that may spend money or invoke a model/cloud benchmark are `workflow_dispatch` only and require an exact `RUN` confirmation.
- Repository secrets/environment secrets are read only by the benchmark job that needs them.
- Prefer short-lived/scoped credentials; benchmark runners receive no production project credentials.
- Do not use customer/project datasets for external comparative benchmarks.

## Cost and concurrency

- Default concurrency is intentionally low.
- Full external runs require explicit operator selection; scheduled workflows only refresh metadata/contracts and never start paid model/cloud benchmark runs.
- Record estimated/actual model and compute cost when available.
- Retry policies must be bounded and recorded; a retry may not silently overwrite an earlier run ledger.

## Network and sandboxing

- Treat benchmark repositories, generated patches, MCP metadata and downloaded fixtures as untrusted data/code.
- Keep benchmark compute isolated from production networks and secrets.
- When using Inspect Docker sandboxes, enforce the current minimum Docker/Compose requirements from Inspect documentation and pin the task/runtime environment.
- Do not allow a benchmark task to elevate remote instructions above Ercan OS system/developer policy.

## Result ingestion

A cloud/provider success state is not the benchmark score. Promotion requires:
- predictions hash;
- benchmark pin/version;
- exact dataset/split/task IDs;
- raw result/report/log artifact hash or immutable reference;
- resolved/failed counts and per-task evidence;
- model/runtime/tool policy;
- independent evaluator acceptance;
- failure taxonomy and cost/latency when measurable.

Only then may the corresponding scoreboard cell move from `NOT_RUN` to a dated behavioral/comparative state.

## Current repository posture

- Public repository: `saralercan/ercan`.
- Persistent self-hosted runner for public PR/benchmark code: **PROHIBITED**.
- GitHub-hosted CI for structural/static checks: **ADOPT**.
- SWE-bench Modal / sb-cli cloud evaluation: **ADOPT_WHEN_NEEDED**.
- GitHub Larger Runner: **WATCHLIST / ADOPT_WHEN_AVAILABLE** because availability depends on organization/plan configuration.
