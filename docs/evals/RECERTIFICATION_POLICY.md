# Ercan OS — Re-certification and Benchmark Evidence Policy

Status: active
Updated: 2026-08-31

Purpose: prevent benchmark results from being over-interpreted and define when an Ercan OS stable agent must be re-trained, re-tested, downgraded, or may be promoted.

## Evidence classes

1. `STATIC_READY` — registry/source-pack/routing/research/eval contracts exist and pass deterministic CI.
2. `SMOKE_BEHAVIORAL_EVIDENCE` — a small representative task set ran through a real model/agent runtime and a canonical evaluator.
3. `REPRESENTATIVE_BEHAVIORAL_EVIDENCE` — a predefined, versioned task set large/diverse enough to support domain certification.
4. `EXTERNAL_COMPARATIVE_EVIDENCE` — a canonical public benchmark ran at a pinned comparable version.
5. `PRODUCTION_OUTCOME_EVIDENCE` — representative real-project acceptance with independent QA and preserved constraints.

These classes are complementary. A public benchmark cannot replace production QA; static readiness cannot replace behavioral evidence.

## No automatic promotion from smoke tests

A 1–3 case SWE-bench smoke run validates the end-to-end generation/evaluation path and supplies behavioral evidence. It does **not** grant `PRODUCTION_VERIFIED`, `BENCHMARKED_FRONTIER_CANDIDATE`, or a world-class claim, regardless of whether every smoke case resolves.

## No automatic demotion from one ordinary unresolved task

An unresolved benchmark task is a learning/regression signal, not automatically a qualification failure. It enters failure taxonomy and training review when representative of the agent's domain.

## Immediate re-certification triggers

A stable agent is moved to `RECERTIFICATION_REQUIRED` when verified evidence shows any of the following:
- fabricated source, test, deployment, browser result, benchmark result, or completion claim;
- credential/secret exposure caused by agent behavior;
- unapproved destructive or production-scope action;
- remote prompt/tool/repository instruction overriding Ercan OS policy;
- material authorization/security-boundary failure;
- repeated use of deprecated/currently unsupported platform behavior after current-source verification was required;
- evaluator/implementation independence violated where the contract requires separation;
- severe production regression attributable to the agent/harness.

These are hard fails and do not require a numerical benchmark threshold.

## Comparative regression trigger

A public benchmark regression may trigger re-certification only when all comparison coordinates match or are explicitly normalized:
- benchmark/dataset version and task IDs;
- agent harness ID and policy commit family;
- model/runtime or an approved model-change comparison design;
- tool exposure and permission profile;
- scorer/evaluator version;
- retry/timeout/concurrency policy.

A tolerance must be defined before observing the new run. Do not invent a regression threshold after seeing results.

## Promotion requirements

### `QUALIFIED`
Requires the relevant domain/platform certification gate, zero hard fails, current authoritative sources and native/runtime validation.

### `PRODUCTION_VERIFIED`
Requires representative behavioral evidence plus independent production/staging acceptance for the actual class of work. External leaderboard performance alone is insufficient.

### `BENCHMARKED_FRONTIER_CANDIDATE`
Requires a dated reproducible report showing competitive performance against credible current external baselines on a canonical comparable benchmark. The report must disclose model/runtime/tooling, cost/latency where measurable and failure taxonomy. This label does not mean objectively best in the world.

## SWE-bench interpretation

Canonical run reports expose submitted, completed, resolved, unresolved, empty-patch and error outcomes. Ercan OS normalizes those fields through `scripts/ingest_swebench_report.py`.

- `resolved` = behavioral success for that benchmark instance.
- `unresolved` = valid evaluator result but solution did not satisfy required tests.
- `empty_patch` = no meaningful prediction was evaluated; classify separately.
- `error` = evaluator could not produce a normal result; requires log review before attributing the failure to agent quality vs harness/environment.
- incomplete dataset items that were never submitted are not model failures for subset runs.

Never compute full-dataset accuracy from a deliberately small subset as though all unsubmitted instances were failures or passes.

## Re-training loop

When re-certification is required:
1. preserve the failing evidence and exact pins;
2. classify root cause: knowledge, reasoning, routing, tool-use, policy, implementation, evaluator, infrastructure, or ambiguous;
3. update only the smallest relevant source pack/skill/routing/policy;
4. add the failure as a regression case before re-running;
5. run the affected representative suite plus adjacent hard-fail cases;
6. independent QA accepts or rejects the repair;
7. only then restore the previous certification state.

## Truth rule

If evidence is incomplete, state `NOT_RUN`, `NO_COMPARABLE_BASELINE`, `EVIDENCE_REVIEW_REQUIRED`, or `RECERTIFICATION_REQUIRED`. Never fill evidence gaps with confidence language.
