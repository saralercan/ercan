---
name: vinterro-one-agent-supervision
description: Enforce independent cross-agent review, domain supervision, evidence-backed correction loops, arbitration, meta-audit and release gates across Vinterro One. Load for material multi-agent work, production changes, explicit all-agents routing, repeated failures, reviewer conflicts or agent-infrastructure changes.
---

# Vinterro One Agent Supervision

Load:
- `docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md`
- `docs/standards/VINTERRO_ONE_SUPERVISION_MANIFEST.json`
- `docs/standards/AGENT_ENGINEERING.md`
- task/project/domain standards
- `.agents/skills/agent-eval-regression/SKILL.md` when a failure should become durable regression coverage.

## Operating rule

A material worker cannot be its own final evaluator.

Route the smallest sufficient supervision chain by risk:

- R0 -> worker self-check if allowed;
- R1 -> independent reviewer;
- R2 -> independent reviewer + domain supervisor;
- R3 -> independent reviewer + domain supervisor + release gate;
- R4 -> reviewer + Agent Runtime Supervisor + Meta Auditor + regression/eval + release gate.

Use an Arbiter on material disagreement.

## Procedure

1. Compile task contract and acceptance criteria before review.
2. Identify worker ownership and relevant domain.
3. Select a reviewer that did not produce the material output.
4. Prefer direct/deterministic evidence over narrative.
5. Reviewer actively attempts to falsify the worker's completion claim.
6. On failure, emit structured correction packet.
7. Worker corrects only within scope.
8. Re-run all checks invalidated by the correction.
9. Escalate repeated same-class failure to domain supervisor/root-cause review.
10. Escalate disputed facts/judgments to Arbiter.
11. For R3/R4, run final/release gate after the latest material change.
12. Emit only an evidence-supported completion state.

## Hard fails

- worker self-certifies material work;
- reviewer PASS has no evidence;
- PASS predates a later material change;
- unexecuted check is described as executed;
- majority vote substitutes for evidence;
- supervisor ignores deterministic contradictory evidence;
- release/send/deploy proceeds without required gate;
- repeated failure causes patch stacking without root-cause reassessment;
- user correction after VERIFIED is ignored instead of becoming an eval candidate.

## Output contract

Return or log:
- worker;
- reviewer;
- supervisor;
- risk class;
- evidence;
- findings;
- correction/retest state;
- arbiter result if any;
- gate result if any;
- final state: VERIFIED / PARTIAL / BLOCKED / NOT_VERIFIED.
