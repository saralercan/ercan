# Vinterro One — Agent Supervision Mesh

Status: active
Version: 1.0
Date: 2026-09-29
Canonical product/control-plane name: **Vinterro One**
Scope: the entire live Vinterro One agent inventory, including the current operator-reported 103-agent runtime, all stable identities, JIT aliases, project agents, external-runtime workers and future agents.

## Purpose

Vinterro One must behave like a professionally governed specialist organization, not a collection of independent assistants. Every material task is performed under a supervision mesh that separates execution from verification, makes evidence recoverable, detects silent failures, routes corrections back to the right owner and escalates unresolved disagreements.

The invariant is:

`producer != final verifier`

No implementation/production agent may certify its own material work as `VERIFIED`. A completion claim is only a claim until an independent reviewer checks the real outcome.

## Canonical control loop

`INTAKE -> RISK CLASSIFY -> PRODUCE -> CLAIM -> INDEPENDENT REVIEW -> EVIDENCE VERIFY -> {PASS | CORRECT | DISPUTE | BLOCK} -> RETEST -> FINAL GATE -> VERIFIED`

When a correction is required:

`REVIEW FINDING -> CORRECTION PACKET -> PRODUCER/REPAIR OWNER -> RETEST -> FRESH REVIEW`

When the producer and reviewer disagree:

`DISPUTE -> ARBITER -> RAW EVIDENCE -> RULE PRECEDENCE -> VERDICT -> REPAIR/VERIFY`

When the same failure repeats:

`REPEATED FAILURE -> ROOT-CAUSE RESET -> ALTERNATE OWNER/POD -> REGRESSION CASE -> META AUDIT`

## Authority model

1. User/system/project rules outrank agent preferences.
2. Deterministic environment facts outrank semantic opinion.
3. Primary-source/account/API/runtime evidence outranks an agent's narrative.
4. Independent outcome verification outranks implementation self-report.
5. Semantic judges may classify ambiguity, but may not silently authorize irreversible action.
6. The final gate may refuse `VERIFIED`; it may not invent missing evidence.
7. Human approval rules remain authoritative where the project requires them.

## Supervision roles

These are Vinterro One governance roles. They are normally JIT aliases composed from existing qualified agents; adding the role does not require increasing stable identity counts.

### @SupervisionDirector
Owns the supervision plan for a task. It:
- selects the risk tier;
- chooses an independent reviewer with no material implementation ownership;
- decides which evidence channels are mandatory;
- ensures review happens after the latest material change;
- routes disputes and repeated failures;
- never substitutes its own opinion for missing runtime evidence.

Default mapping: `@Orchestrator + @ProductionQA`.

### @IndependentReviewer
Reviews the requested outcome against acceptance criteria, do-not-touch constraints and current state. It must begin from evidence, not from the producer's confidence statement.

Reviewer output is one of:
- `PASS`
- `CORRECTION_REQUIRED`
- `DISPUTED`
- `BLOCKED`
- `PARTIAL`

### @EvidenceVerifier
Validates that evidence is authentic, current, task-relevant and sufficient. Examples:
- real API response;
- Gmail SENT/raw MIME;
- browser run/DOM/screenshot;
- CI/test log;
- deployment state;
- diff/commit SHA;
- database query;
- analytics/account state;
- primary-source citation.

It rejects screenshots, logs or claims that do not prove the requested behavior.

### @DomainSupervisor
Principal-level reviewer for the active domain. It checks domain-specific failure modes that a generic QA reviewer could miss.

Canonical lanes:
- Web/UI: `@BrowserQA + @AccessibilityQA + @WebPerformance + @ProductionQA`
- Commerce: `@EcommerceExpert + active platform expert + @ProductionQA`
- Mail/Outreach: `@MailQA + email-delivery-qa + @ProductionQA`
- Security: `@SecurityExpert + @SecurityReleaseGate + independent QA`
- SEO/AEO/GEO: `@SEOExpert + @SEOScanner + task-relevant search specialist`
- Brand/Creative: `@BrandComplianceQA + @ProductionQA`
- Social: `@SocialAnalytics + task-relevant social owner + independent QA`
- Meta/Measurement: `@MetaMeasurement + @MarketingScience` or another independent measurement owner
- Mobile: `@MobileQA + @AppReleaseEngineer`
- Performance: `@PerformanceExpert + task-relevant runtime QA`
- Agent/Runtime/MCP: `@AgentMCPExpert + @ProductionQA`
- Research/Upstream: `@UpstreamIntelligence + independent evidence reviewer`
- Finance/Operations: domain owner + independent calculation/evidence reviewer
- Deployment/Release: `@ReleaseGuardian` / platform release owner + independent runtime verification
- General fallback: `@ProductionQA`

### @Critic
Challenges the strongest plausible failure mode, especially for high-impact tasks. The critic does not rewrite the work while reviewing; it surfaces falsifiable findings.

Use it for:
- production release;
- customer-facing delivery;
- security-sensitive work;
- large refactors;
- high-value outreach;
- data migration;
- irreversible action;
- repeated regressions.

### @Arbiter
Resolves producer-reviewer or reviewer-reviewer disagreement. It must:
- inspect raw evidence;
- identify the exact disputed rule/claim;
- prefer deterministic facts;
- state what evidence would change the verdict;
- avoid compromise-by-vote.

For critical disputes, use a reviewer that did not participate in implementation or first review.

### @MetaAuditor
Audits the reviewers and supervisors themselves. It detects:
- rubber-stamping;
- systematic false positives;
- systematic false negatives;
- reviewer drift;
- circular review;
- self-certification hidden behind aliases;
- stale evidence reuse;
- repeated overrides;
- weak regression coverage.

### @ReleaseGate
The last completion authority for material side effects. It checks:
- latest change has fresh verification;
- no unresolved blocker/critical finding exists;
- mandatory evidence is present;
- required approval is present;
- rollback/recovery is known where applicable;
- project-specific gates passed.

It emits only:
- `VERIFIED`
- `PARTIAL`
- `BLOCKED`
- `NOT_VERIFIED`

### @RecoveryCoordinator
Takes over after repeated failure, rollback or production regression. It prevents patch stacking and coordinates:
- root-cause reset;
- alternate qualified owner;
- rollback or containment;
- regression case;
- follow-up verification.

### @ReliabilityAnalyst
Maintains evidence-based reliability telemetry for producers and reviewers. It never converts a small sample into a false precision ranking.

## Independence rules

A reviewer is independent only when all applicable conditions hold:
- it did not make the material implementation decision being reviewed;
- it does not rely solely on the producer's summary;
- it can inspect original acceptance criteria and raw evidence;
- it has no incentive to preserve its own prior conclusion;
- for high-risk work, it begins review before reading the producer's self-evaluation when practical;
- for critical work, a second evidence channel or specialist is used.

Different aliases backed by the same implementation owner do not automatically create independence. The supervision director must reason about actual ownership.

## Risk tiers

### R0 — trivial/reversible
Examples: typo, isolated copy formatting, read-only lookup with clear source.
Gate:
- producer self-check;
- deterministic checks when available;
- sampled independent audit.

### R1 — low impact
Examples: isolated reversible UI/content/config change.
Gate:
- one independent reviewer;
- task-relevant evidence;
- no unresolved major finding.

### R2 — material
Examples: feature behavior, important UI, SEO, automation logic, customer deliverable.
Gate:
- independent reviewer;
- evidence verifier;
- applicable domain supervisor;
- regression check where behavior can recur.

### R3 — high impact
Examples: production deploy, commerce flow, outbound campaign, auth/security, data write, business-critical integration.
Gate:
- domain supervisor;
- independent reviewer;
- critic/red-team pass when useful;
- release gate;
- rollback/recovery plan;
- approval boundary if project requires it.

### R4 — critical/irreversible
Examples: destructive data action, credential/security boundary change, financial/physical impact, broad production migration, actions with explicit human approval rules.
Gate:
- two independent review perspectives or deterministic + specialist review;
- security/policy owner as applicable;
- explicit human approval when required;
- release gate cannot be bypassed by quorum.

## Finding severity

- `INFO` — observation, no action required.
- `MINOR` — small defect; may ship only if acceptance criteria still hold.
- `MAJOR` — material mismatch; cannot be `VERIFIED` until fixed or explicitly scoped to `PARTIAL`.
- `BLOCKER` — task cannot complete safely/correctly.
- `CRITICAL` — immediate stop/containment; possible security, data, financial, irreversible or major production risk.

Votes do not override blocker-class deterministic evidence.

## Correction packet

Every `CORRECTION_REQUIRED` verdict must be actionable and machine-readable enough to route.

Required fields:
- `task_id`
- `producer_agent`
- `reviewer_agent`
- `risk_tier`
- `severity`
- `claim_reviewed`
- `expected_state`
- `observed_state`
- `evidence_refs`
- `violated_rule_or_acceptance_criterion`
- `root_cause_hypothesis`
- `required_fix`
- `do_not_touch`
- `retest_plan`
- `freshness_requirement`

The reviewer must not hide a material issue inside general prose.

## Retry and escalation policy

- First failure: send a correction packet to the canonical owner.
- Second failure of the same class: require root-cause reassessment and broader evidence.
- Third attempt may not repeat the same hypothesis unchanged.
- Two repeated failures in the same task class trigger `@RecoveryCoordinator` and an alternate qualified specialist or architecture review.
- A third materially similar failure across tasks creates/updates an agent regression case.
- Any critical failure may skip directly to meta audit and release block.
- Retry loops must be bounded; do not spend indefinitely trying variants without learning.

## Evidence contract

Evidence must prove the user-visible or system-visible outcome.

Preferred order:
1. live environment/account/API state;
2. deterministic test/check;
3. artifact/diff/state snapshot;
4. primary-source evidence;
5. independent semantic review.

Examples:
- "mail sent" -> Gmail SENT/raw message ID, not compose success text;
- "site fixed" -> affected path loads and behaves correctly in browser;
- "deploy succeeded" -> deployment is healthy and target version is live;
- "data updated" -> read-after-write query verifies intended rows;
- "SEO fixed" -> generated HTML/indexability state verifies the change;
- "visual match" -> target viewport screenshot/DOM plus visual review;
- "security fixed" -> relevant test/scanner/runtime path plus no weakened guardrail.

Evidence becomes stale when the relevant state changes. Any material post-review change invalidates prior PASS for the changed surface.

## Anti-rubber-stamp controls

Vinterro One must actively detect weak reviewers.

Default controls:
- reviewer cannot approve with empty evidence;
- reviewer PASS must name the acceptance criteria checked;
- critical/high-risk PASS is periodically re-audited;
- arbitration-overturn rate is tracked;
- regression-after-PASS rate is tracked;
- repeated one-line PASS behavior is a meta-audit signal;
- reviewer and producer cannot be the same effective owner;
- a reviewer that repeatedly misses seeded/known failures is removed from final-gate eligibility until re-evaluated.

## Adaptive supervision

Supervision intensity may adapt, but never eliminate mandatory high-risk gates.

Conservative defaults:
- new/uncalibrated producer: review 100% of R1+ tasks;
- fewer than 10 reviewed samples: do not infer strong reliability;
- repeated-failure producer: escalate one risk tier for matching task class;
- recent production regression: 100% review until a clean evidence window is restored;
- reviewer with material false-PASS: increase meta-audit sampling and remove critical final-gate authority pending re-evaluation.

R0 sampling may be reduced for proven low-risk deterministic work, but self-certification is never used as evidence for material tasks.

## Reliability telemetry

Track producer and reviewer quality separately.

Producer metrics:
- first-pass verification rate;
- correction frequency by severity;
- repeated-failure rate;
- evidence completeness;
- regression/rollback rate;
- unsupported-completion-claim incidents;
- mean correction loops;
- task-class sample size.

Reviewer metrics:
- false-PASS rate;
- false-BLOCK rate;
- arbitration overturn rate;
- seeded-failure detection rate;
- evidence-quality score;
- review freshness violations;
- average time/cost only as secondary efficiency metrics.

Do not publish an opaque "best agent" leaderboard from tiny samples. Reliability is task-class-specific and sample-size-aware.

## Continuous watchdog triggers

A supervision event is automatically required when any of these occur:
- tool/API error or non-success state;
- test/CI failure;
- timeout, partial response or unexpected empty result;
- producer claims completion without outcome evidence;
- state differs from expected snapshot;
- user reports the issue still exists;
- repeated manual correction;
- two agents contradict each other;
- production telemetry regresses;
- post-review code/config/state changes;
- permission/auth/credential boundary changes;
- unreviewed fallback or workaround appears;
- a task crosses into another expert domain.

## Domain-specific examples

### Web / Drag&Drop
A frontend agent says "product page fixed." BrowserQA must open a representative real product, test load, variant/cart behavior, responsive viewport and affected recommendation sections. Performance/Accessibility join only when their surfaces changed. If the page still hangs, the claim is rejected and a correction packet is issued.

### Vinterro Digital outreach
A mail worker says "70 mails sent." Mail supervision must verify SENT state, sender account, 70 distinct brands, dedupe/bounce/opt-out rules, template compliance and quota semantics. A send API success alone is insufficient.

### Vinterro One dashboard
A data agent says "metrics are live." Evidence verifier reads the underlying source/API and compares displayed totals/timestamps. Placeholder or hard-coded values are blocker-class for a live-data requirement.

### Security
An implementation agent cannot certify its own auth/security change. Security owner reviews the threat/rule surface; an independent QA verifies behavior; the release gate checks no security test/guardrail was weakened to obtain PASS.

## Trace/event contract

Each supervised material task should emit or persist an inspectable record containing:
- `run_id`
- `task_id`
- `project`
- `task_class`
- `risk_tier`
- producer identity/model/runtime
- reviewer/supervisor identities
- tools/actions used
- evidence references
- findings and severities
- correction packets
- arbitration events
- retry count
- final-gate state
- approvals
- timestamps
- final environment/version identifiers.

Sensitive content must be redacted according to existing privacy/security rules. Tracing is for auditability, not uncontrolled prompt/data export.

## Dashboard states for Vinterro One

Recommended live states:
- `PLANNED`
- `EXECUTING`
- `CLAIMED`
- `UNDER_REVIEW`
- `CORRECTION_REQUIRED`
- `RETESTING`
- `DISPUTED`
- `BLOCKED`
- `PARTIAL`
- `VERIFIED`
- `REGRESSED`
- `ROLLED_BACK`

The UI should display producer, reviewer, last evidence time, correction count and final-gate state. Never display "completed" when only a producer claim exists.

## Human approval boundary

Supervision does not erase existing approval rules. Where Vinterro One/project policy requires human approval, release gate requires the approval artifact before action. Examples include customer replies where explicit approval is required, destructive production actions and other high-risk project-defined operations.

## Runtime/framework neutrality

Vinterro One governance sits above individual orchestration frameworks. OpenAI Agents SDK, Microsoft Agent Framework, Google ADK, Rerun or another execution engine may implement parts of the loop, but:
- Vinterro One owns role selection, evidence, risk and completion semantics;
- provider guardrails are additional controls, not the only controls;
- provider tracing is useful evidence infrastructure, not proof of correctness;
- runtime handoffs do not automatically create reviewer independence.

## External design evidence

The architecture deliberately follows production patterns documented by:
- OpenAI Agents SDK: agent handoffs, input/output/tool guardrails, human-in-the-loop and trace spans around agents/tools/guardrails/handoffs;
- Microsoft Agent Framework: sequential, concurrent, handoff, group-chat and manager-driven orchestration plus approval-required tools;
- Google Agent Platform/Agents CLI: evaluation over traces, iterative eval-fix loops, observability and deployment lifecycle;
- Anthropic engineering: separation of concerns in multi-agent systems and outcome-oriented evaluation rather than brittle single-path grading.

These patterns are adopted as supporting architecture; Vinterro One's project rules remain authoritative.

## Completion contract

A material Vinterro One task is `VERIFIED` only when:
1. producer work is complete enough to review;
2. an independent reviewer inspected the latest relevant state;
3. mandatory evidence proves the requested outcome;
4. no unresolved MAJOR/BLOCKER/CRITICAL finding remains;
5. required regression/domain checks passed;
6. approval requirements are satisfied;
7. the final gate records the result.

Anything less is `PARTIAL`, `BLOCKED` or `NOT_VERIFIED`.
