# Vinterro One — Agent Supervision Mesh

Status: active  
Version: 1.0  
Date: 2026-09-29  
Scope: every Vinterro One runtime agent, stable routing identity, project agent, JIT role, tool-using worker, reviewer, supervisor and release gate.

## Canonical identity

**Vinterro One** is the canonical product and control-plane name.

Historical references to **Ercan OS** in older repository documents are legacy implementation terminology only. They must not be used as the canonical name for new architecture, governance, routing, supervision, runtime or user-facing system documentation.

## Purpose

Vinterro One must behave as a supervised multi-agent organization, not a collection of isolated agents.

No material producer may certify its own work. A material task is complete only when independent evidence supports the requested outcome and the applicable supervision path has passed.

Canonical loop:

`PLAN -> EXECUTE -> OBSERVE -> REVIEW -> CHALLENGE -> CORRECT -> RE-TEST -> GATE -> COMPLETE`

For production/high-risk work:

`Worker -> Independent Reviewer -> Domain Supervisor -> Arbiter when disputed -> Meta Auditor when systemic risk exists -> Final/Release Gate`

## Core invariants

1. **Creator != final evaluator.**
   The agent that materially produced an output cannot be the sole final verifier of that output.

2. **Claims are not evidence.**
   "Done", "fixed", "sent", "deployed", "works", "passed" and similar statements are never completion evidence by themselves.

3. **Review must inspect the real outcome.**
   Prefer environment state, diff, browser behavior, API response, Gmail SENT/thread state, CI/test result, database state, rendered artifact, analytics source, screenshot or other direct evidence.

4. **Reviewer independence is structural.**
   A reviewer must not merely repeat the worker's reasoning. It receives the task contract, acceptance criteria and evidence, then attempts to falsify completion.

5. **Disagreement is preserved, not averaged away.**
   Worker/reviewer conflicts escalate to an Arbiter with access to evidence. Majority vote is not proof.

6. **Supervisors supervise the process, not only the artifact.**
   They detect missing tests, scope drift, stale evidence, unsupported claims, weak reviewers, repeated failures and bad routing.

7. **Meta-audit supervises supervisors.**
   A supervisor or reviewer that rubber-stamps, systematically misses seeded failures, produces high false-pass rates or repeatedly contradicts deterministic evidence is itself subject to audit and confidence downgrade.

8. **Critical external effects require a gate.**
   Production deploys, customer email sends, destructive data operations, auth/security changes, payments, DNS, campaign mutation, theme publish and other material external effects require the relevant final gate.

9. **Retries are bounded.**
   Repeated failure must trigger root-cause/ownership reassessment; do not stack patches indefinitely.

10. **Uncertainty is explicit.**
    Use `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT_VERIFIED`. Do not translate missing evidence into confidence.

## Supervision roles

### 1. Worker
Owns bounded execution.

Required output:
- task contract understood;
- changes/actions performed;
- evidence produced;
- known limitations stated;
- no self-issued final verification.

### 2. Independent Reviewer
Attempts to disprove the worker's completion claim.

Required checks:
- acceptance criteria coverage;
- direct evidence freshness;
- scope preservation;
- regression surface;
- project/brand/platform rules;
- unsupported assumptions;
- edge cases proportional to risk.

Reviewer verdicts:
- `PASS`
- `PASS_WITH_NOTES`
- `REWORK`
- `BLOCKED`

A reviewer may not return PASS without naming the evidence inspected.

### 3. Domain Supervisor
Owns supervision quality for a domain and decides whether the evidence/review path is sufficient.

Canonical supervisor capabilities:
- `@WebSupervisor`
- `@CommerceSupervisor`
- `@EmailSupervisor`
- `@ContentSupervisor`
- `@BrandSupervisor`
- `@SEOSupervisor`
- `@SocialSupervisor`
- `@AdsMeasurementSupervisor`
- `@DataSupervisor`
- `@SecuritySupervisor`
- `@PerformanceSupervisor`
- `@MobileSupervisor`
- `@PresentationSupervisor`
- `@InfrastructureSupervisor`
- `@ResearchEvidenceSupervisor`
- `@AgentRuntimeSupervisor`

These are JIT supervision capabilities mapped onto existing qualified owners and QA roles. They do not automatically become duplicate stable identities.

### 4. Arbiter
Used when:
- worker and reviewer disagree materially;
- two reviewers conflict;
- deterministic evidence conflicts with semantic review;
- project rules conflict or are ambiguous;
- a rollback/release decision has material uncertainty.

Arbiter contract:
- inspect task contract and evidence;
- state disputed propositions;
- distinguish facts from judgments;
- prefer deterministic/current evidence;
- request or execute one decisive additional check when practical;
- return `UPHOLD_REVIEW`, `OVERTURN_REVIEW`, `RETEST_REQUIRED`, or `BLOCKED`.

The Arbiter must not resolve disagreement by personality, seniority or majority vote.

### 5. Meta Auditor
Audits supervision quality over time.

Detects:
- suspiciously high reviewer pass rate;
- reviewer/worker coupling;
- repeated same-class escape defects;
- stale evidence accepted as current;
- unexecuted tests represented as executed;
- recurring rollback after PASS;
- repeated user correction after VERIFIED;
- supervisors that skip escalation;
- graders that can be gamed;
- domain gaps with no qualified reviewer.

Meta-audit outputs feed agent eval/regression and reliability scoring.

### 6. Final / Release Gate
Owns final irreversible or externally visible transition.

A release gate checks:
- required independent review passed;
- blocking findings resolved;
- current evidence exists after latest material change;
- relevant security/privacy/permission requirements pass;
- rollback/recovery path exists when applicable;
- external action matches user authorization;
- no stale PASS predates a later change.

Gate verdicts:
- `RELEASE_APPROVED`
- `RELEASE_DENIED`
- `RELEASE_BLOCKED`

## Risk classes

### R0 — Trivial
Examples: isolated reversible copy/style change with no external side effect.

Minimum: worker self-check may be sufficient only when project rules allow.

### R1 — Material
Examples: normal code/content/config change.

Minimum: independent reviewer.

### R2 — Production-impacting
Examples: shared component change, live website behavior, CRM state, campaign configuration, SEO-wide change.

Minimum: independent reviewer + domain supervisor + direct runtime/environment evidence.

### R3 — Critical
Examples: send/publish/deploy, auth/security, payment, DNS, destructive data mutation, customer-facing bulk operation.

Minimum: independent reviewer + domain supervisor + release gate. Arbiter required on material disagreement.

### R4 — Systemic / supervision-risk
Examples: new agent infrastructure, evaluator changes, routing policy, permissions model, recurring false completion, broad automation.

Minimum: independent reviewer + Agent Runtime Supervisor + Meta Auditor + regression/eval evidence + release gate.

## Evidence classes

Prefer evidence in this order when applicable:

1. deterministic environment state;
2. reproducible automated test/CI;
3. direct tool/API/provider state;
4. browser/runtime observation;
5. diff/static analysis;
6. rendered artifact inspection;
7. primary-source factual evidence;
8. structured semantic review;
9. worker narrative.

Higher-numbered evidence must not override contradictory lower-numbered evidence without explaining why the lower-numbered evidence is invalid/stale.

## Correction protocol

When review fails, return a structured correction packet:

- `finding_id`
- `severity`: BLOCKER / MAJOR / MINOR
- `criterion`
- `expected`
- `observed`
- `evidence`
- `likely_owner`
- `smallest_compliant_fix`
- `retest_required`
- `regression_scope`

The worker must respond to findings, not silently replace them with a new completion claim.

After material correction, any stale PASS is invalidated and relevant checks must run again.

## Retry and escalation policy

- attempt 1 failure -> worker corrects;
- attempt 2 same-class failure -> domain supervisor performs root-cause review;
- attempt 3 same-class failure -> Arbiter + architecture/ownership reassessment;
- repeated production escape or user correction -> Meta Auditor + regression case;
- do not exceed bounded retries by stacking speculative patches.

## Reliability scoring

Vinterro One may maintain evidence-backed reliability metrics per runtime agent/reviewer.

Recommended signals:
- first-pass acceptance rate;
- reviewer rejection rate;
- false-pass rate;
- post-PASS rollback rate;
- repeated user-correction rate;
- escaped regression rate;
- evidence-completeness rate;
- stale-evidence incidents;
- unsupported completion claims;
- average rework loops;
- domain-specific certification status.

Rules:
- reliability is advisory for routing, never proof of correctness;
- low-confidence agents receive stronger review, not silent exclusion unless policy requires it;
- reviewers are scored on false passes as well as false blocks;
- no score is self-reported;
- do not optimize agents to game the metric.

## Pairing strategy

Do **not** create one permanent reviewer clone for every worker.

Use capability-aware cross-review:
- implementer reviewed by a role with independent verification competence;
- security review separated from feature ownership;
- content author separated from fact/citation/editorial QA when material;
- mail composition separated from Gmail send/SENT verification;
- web implementation separated from browser/accessibility/performance QA as applicable;
- data transformation separated from reconciliation/source-total checks;
- deployment separated from post-deploy health verification.

## Domain examples

### Web / Shopify / WordPress
`Implementation -> BrowserQA/ComponentQA -> WebSupervisor -> ReleaseGuardian -> VERIFIED`

Evidence may include:
- exact diff;
- console/network;
- target routes;
- mobile/desktop viewport checks;
- add-to-cart/form/navigation behavior;
- accessibility/performance checks proportional to change;
- post-deploy verification.

### Vinterro Digital mail / outreach
`Discovery/Copy Worker -> MailQA -> EmailSupervisor -> Send Gate -> Gmail SENT verification -> pipeline reconciliation`

A "sent" count must reconcile with real SENT state and dedupe rules. A draft or API acceptance is not equivalent to successful SENT state.

### Research / analytics
`Researcher -> Evidence Reviewer -> ResearchEvidenceSupervisor -> Arbiter on conflicting sources`

Claims retain source/time/population scope. Unsupported synthesis is rejected.

### Security
`Implementer -> SecureCodeReviewer/authorized tester -> SecuritySupervisor -> SecurityReleaseGate`

Security implementers cannot waive their own findings.

## Supervision event ledger

Material tasks should emit a compact supervision trace when runtime supports it:

- task/run id;
- worker(s);
- reviewer(s);
- supervisor;
- risk class;
- acceptance criteria;
- evidence refs;
- findings;
- corrections;
- retests;
- arbiter decision if any;
- final gate;
- completion state;
- timestamps;
- material changes after last PASS.

The ledger must avoid secrets and unnecessary private content.

## Anti-collusion / anti-rubber-stamp rules

- reviewer must receive independent acceptance criteria, not only worker summary;
- reviewer should inspect raw evidence where practical;
- random seeded regression/eval cases may be used to detect rubber-stamping;
- repeated exact wording between worker/reviewer with no new evidence is a QA smell;
- a reviewer that cannot access the required evidence returns BLOCKED/PARTIAL, not PASS;
- supervisor may rotate reviewer capability for high-risk or repeated-failure tasks.

## Mandatory regression learning

Any of these create an eval/regression candidate:
- user says a VERIFIED task is still broken;
- production rollback after PASS;
- customer email sent with template/routing/dedupe error;
- security issue escapes review;
- repeated same-class defect;
- reviewer false PASS;
- reviewer false BLOCK that deterministic evidence disproves;
- task completed outside user scope;
- unexecuted agent/tool represented as executed.

Use `.agents/skills/agent-eval-regression/SKILL.md`.

## Completion states

### VERIFIED
All applicable gates passed on current evidence after the latest material change.

### PARTIAL
Some requested outcome is complete, but a known bounded portion lacks evidence or remains unresolved.

### BLOCKED
A required permission, dependency, environment, source or safety boundary prevents completion.

### NOT_VERIFIED
Work may have been attempted or changed, but the evidence/gates required for verification did not pass.

## Runtime-count rule

The live Vinterro One runtime inventory may exceed the stable routing identity count and may change over time. Supervision applies to **every active runtime agent**, including the currently reported 103+ agents, without hardcoding that number into routing semantics.

New agents inherit this standard automatically.

## Enforcement

This standard must be loaded for:
- every material multi-agent task;
- every explicit "tüm ajanları çalıştır" request;
- every production mutation;
- every task with independent QA;
- every repeated-failure/debug path;
- every new runtime-agent/supervisor/evaluator architecture change.

Machine-readable policy lives in:
`docs/standards/VINTERRO_ONE_SUPERVISION_MANIFEST.json`

Regression contract:
`docs/evals/VINTERRO_ONE_SUPERVISION_REGRESSION.md`

Skill:
`.agents/skills/vinterro-one-agent-supervision/SKILL.md`
