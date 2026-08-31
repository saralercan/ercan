# Ercan OS — External Benchmark Matrix

Status: active execution contract
Updated: 2026-08-31

Purpose: define reproducible external behavioral/comparative benchmark runs for the 21-agent Ercan OS stable core. This file does **not** mark a benchmark as passed unless a real runtime/model/tool harness executed it and an evidence ledger exists.

## Global rules

- Pin benchmark version/commit/package and record the pin in every run ledger.
- Record model, runtime, Ercan OS policy commit, toolset, temperature/retry policy, timeouts and material prompts.
- Separate base-model performance from Ercan OS harness/routing performance.
- Do not cherry-pick passing cases after seeing results.
- Store task IDs, raw outcome state, evaluator result, failure taxonomy, latency and cost when measurable.
- `NOT_RUN` is preferable to fabricated or incomparable results.

## BFCL V4 — tool use / orchestration

Official source: https://gorilla.cs.berkeley.edu/leaderboard.html

Current reproducibility anchor observed 2026-08-31:
- BFCL V4 leaderboard.
- Official leaderboard states evaluated results are reproducible against commit `f7cf735` and `bfcl-eval==2025.12.17` for the published checkpoint.
- Metrics include agentic web-search/memory, multi-turn, single-turn function calling, hallucination measurement, format sensitivity and latency.

Primary Ercan OS targets:
- `@Orchestrator`
- `@AgentMCPExpert`
- platform experts when tool/API calling is material
- project agents for connector/tool routing subsets

Required run evidence:
- exact BFCL commit/package;
- model/runtime adapter;
- tool schema exposure policy;
- result JSON/logs;
- per-category accuracy + hallucination/irrelevant-tool behavior + latency.

Current status: **NOT_RUN** — no independent callable 21-agent runtime/model adapter is connected to this repository in the current execution environment.

## SWE-bench Verified — repository issue resolution

Official source: https://github.com/SWE-bench/SWE-bench

Current dataset/evaluation facts observed 2026-08-31:
- SWE-bench Verified contains 500 expert-verified solvable problems.
- Current upstream CLI supports `swebench eval verified` and Docker-backed reproducible evaluation.
- Predictions must come from an actual agent/model run; gold patches are only harness validation.

Primary Ercan OS targets:
- `@WebAppExpert`
- `@ShopifyExpert`, `@WordPressExpert`, `@WixExpert` only on compatible repository tasks or Ercan-specific adapted suites
- `@AgentMCPExpert` when implementing agent/tool code

Required run evidence:
- SWE-bench repository commit;
- exact dataset split;
- Docker image/harness version;
- generated predictions;
- resolved/failed task IDs;
- patch/test logs;
- latency/cost and retry policy.

Current status: **NOT_RUN** — this ChatGPT session does not expose a Docker/model inference runner capable of independently executing all benchmark instances.

## SWE-bench Multimodal — visual software engineering

Official source: https://github.com/SWE-bench/SWE-bench

Current dataset facts:
- 100 public dev instances and 500 test instances are documented upstream.
- Upstream states the test evaluation is private/leaderboard-submission oriented; use the public dev split for local preflight and official submission for comparable test claims.

Primary Ercan OS targets:
- `@ScreenshotToCode`
- `@PixelMatch`
- `@WebAppExpert`
- `@ProductionQA`

Current status: **NOT_RUN**.

## Stanford HELM / HEIM — multi-dimensional methodology

Official sources:
- https://crfm.stanford.edu/helm/
- https://github.com/stanford-crfm/helm

Use:
- HELM principles for multi-dimensional reporting rather than one-score claims.
- HEIM-style human/multi-metric evaluation for creative/image systems.

Maintenance note observed 2026-08-31:
- the HELM GitHub repository states the framework entered maintenance mode on 2026-06-01.
- therefore HELM remains a strong methodology/reference framework, but Ercan OS should not treat it as the sole current frontier comparator.

Primary targets:
- all experts for reporting methodology;
- `@CreativeDesignExpert` for human-rated multi-dimensional output evaluation.

Current status: **METHODOLOGY_ADOPTED / EXTERNAL MODEL RUN NOT_RUN**.

## Security behavioral suite

Normative/current sources:
- OWASP ASVS 5.0.0 stable: https://github.com/OWASP/ASVS
- OWASP WSTG: https://owasp.org/www-project-web-security-testing-guide/
- NIST SSDF: https://csrc.nist.gov/Projects/ssdf

Primary targets:
- `@SecurityExpert`
- `@AgentMCPExpert`
- `@ProductionQA`
- any platform/project agent touching auth, secrets, network, permissions or production data.

Execution model:
- authorized local/staging fixtures only;
- seeded authz/input/SSRF/secrets/supply-chain failures;
- score detection, remediation correctness, false-positive rate and unsafe-action rate.

Current status: **SCENARIOS_DEFINED / FULL BEHAVIORAL RUN NOT_RUN**.

## MCP protocol conformance/security

Current source:
- MCP specification release 2026-07-28: https://blog.modelcontextprotocol.io/posts/2026-07-28/

Primary target:
- `@AgentMCPExpert`

Required cases:
- stateless current protocol behavior;
- current authorization/issuer handling;
- deprecated feature recognition;
- malicious server/tool instructions treated as untrusted data;
- failure recovery and external-state reconciliation.

Current status: **SCENARIOS_DEFINED / FULL BEHAVIORAL RUN NOT_RUN**.

## Promotion rule

An agent may move from `NOT_RUN` to a behavioral/comparative status only when a dated run ledger records actual execution evidence. Static structural readiness alone cannot grant `PRODUCTION_VERIFIED` or `BENCHMARKED_FRONTIER_CANDIDATE`.
