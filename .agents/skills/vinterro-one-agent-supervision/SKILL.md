---
name: vinterro-one-agent-supervision
description: Apply Vinterro One's independent producer-reviewer-arbiter-meta-audit supervision mesh to material multi-agent work. Use for any task with material implementation, customer communication, production mutation, data writes, security, deployment, repeated failures, disputed agent conclusions or completion claims that need independent evidence.
---

# Vinterro One Agent Supervision

Load:
- `docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md`
- `docs/standards/VINTERRO_ONE_SUPERVISION_MANIFEST.json`
- task-relevant project/domain rules
- `.agents/skills/execution-governance/SKILL.md` for bugs/regressions/repeated fixes
- `.agents/skills/agent-eval-regression/SKILL.md` when a failure should become durable regression coverage.

## Non-negotiable invariant

The material producer cannot be the final verifier.

Do not mark a material task `VERIFIED` because:
- the worker says it succeeded;
- a write tool returned success;
- a build passed while runtime behavior is untested;
- a second alias repeats the first agent's conclusion without raw evidence.

## Runtime procedure

1. Compile acceptance criteria and do-not-touch constraints.
2. Assign risk tier R0-R4.
3. Choose producer(s).
4. Choose an independent reviewer and mandatory evidence channels before final completion.
5. Execute the task.
6. Record the producer's claim separately from verified state.
7. Review the latest environment/artifact/account state.
8. On mismatch, issue a structured correction packet.
9. Retest after the fix; old PASS is invalid after material changes.
10. Route disagreement to `@Arbiter`.
11. Route repeated failures to `@RecoveryCoordinator` and regression coverage.
12. Run the appropriate release gate.
13. Emit only `VERIFIED`, `PARTIAL`, `BLOCKED` or `NOT_VERIFIED`.

## Reviewer selection

Prefer task-specific independent QA:
- browser/UI -> BrowserQA / AccessibilityQA / WebPerformance
- commerce -> Ecommerce + platform QA
- mail -> MailQA + email delivery QA
- security -> SecurityExpert / SecurityReleaseGate
- brand -> BrandComplianceQA
- SEO -> SEOScanner / technical search QA
- mobile -> MobileQA / AppReleaseEngineer
- runtime/agent -> AgentMCPExpert + ProductionQA
- unknown domain -> ProductionQA plus a domain owner.

A reviewer may be a JIT composition; independence is about actual implementation ownership, not label count.

## Correction format

Return:
`severity | claim | expected | observed | evidence | violated rule | required fix | do-not-touch | retest`.

Do not give a vague "please check again" response.

## Escalation

- repeated same-class failure twice -> root-cause reset;
- third attempt cannot repeat the same failed hypothesis unchanged;
- critical finding -> stop/contain and escalate immediately;
- reviewer/producer disagreement -> arbiter;
- suspicious reviewer PASS pattern -> meta audit.

## Efficiency

Do not create ceremony for trivial R0 work. Supervision should reduce rework. Use deterministic checks first, semantic review where judgment is actually needed, and the smallest qualified review pod that covers the risk.

## Completion

The skill passes only when the final status matches real evidence and no worker has self-certified its material output.
