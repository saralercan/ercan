# Screenshot → Production UI Regression Cases

Purpose: prevent regression to one-shot, placeholder-heavy or unverified screenshot-to-code output.

## Case STP-001 — Screenshot reproduction activates full loop
- case_id: `STP-001`
- project/domain: web/UI
- input/context fixture: user supplies a screenshot and asks to reproduce it in the current project.
- expected outcome: Orchestrator loads `screenshot-production-ui`, resolves project assets, produces a browser render, runs explicit reference-vs-render comparison, applies at least one correction pass, then independent Production QA.
- forbidden outcome: returning after first code generation or first render with `VERIFIED`.
- grader/oracle: execution trace + final visual QA evidence.
- trials/tolerance: one deterministic routing trial; visual tolerance is task-specific.
- linked skill/standard/change: `.agents/skills/screenshot-production-ui/SKILL.md`, `AGENT_REGISTRY.md`.
- status/date: active / 2026-08-28.

## Case STP-002 — Reference adaptation preserves project truth
- case_id: `STP-002`
- project/domain: branded web/UI
- input/context fixture: user supplies a Dribbble/Pinterest/Figma reference and asks to adapt it to an existing Ercan OS brand/project.
- expected outcome: visual composition/pattern may be adapted while authoritative project copy, logo, identity and content remain the source of truth. Real project assets are used where available.
- forbidden outcome: copying unrelated third-party brand identity/content into the client project or replacing supplied assets with generic placeholders.
- grader/oracle: asset provenance + project adapter constraints + final visual evidence.
- linked skill/standard/change: `.agents/skills/screenshot-production-ui/SKILL.md`.
- status/date: active / 2026-08-28.

## Case STP-003 — Negative activation
- case_id: `STP-003`
- project/domain: web/UI
- input/context fixture: user asks to change one button label; no screenshot/reference/reproduction intent.
- expected outcome: normal scoped edit path; `screenshot-production-ui` is not loaded unless another material visual-reference requirement is present.
- forbidden outcome: spawning the full screenshot-production pod for a trivial text edit.
- grader/oracle: routing trace.
- linked skill/standard/change: `AGENT_REGISTRY.md`.
- status/date: active / 2026-08-28.

## Case STP-004 — Real asset enforcement
- case_id: `STP-004`
- project/domain: branded web/UI
- input/context fixture: authoritative logo/hero/product assets are supplied with a visual reference.
- expected outcome: final implementation uses those authoritative assets or records a concrete blocker/substitution reason.
- forbidden outcome: unrelated placeholder or stock imagery survives into final `VERIFIED` output.
- grader/oracle: DOM/network asset inspection + visual evidence.
- linked skill/standard/change: `@RealAsset`, `.agents/skills/screenshot-production-ui/SKILL.md`.
- status/date: active / 2026-08-28.

## Case STP-005 — Verification vocabulary is evidence-based
- case_id: `STP-005`
- project/domain: web/UI QA
- input/context fixture: implementation code exists but browser rendering or comparable final-state capture cannot be produced.
- expected outcome: final state is `BLOCKED` or `NOT VERIFIED` according to cause.
- forbidden outcome: claiming pixel-perfect/birebir or `VERIFIED` from code review alone.
- grader/oracle: presence/absence of comparable rendered evidence.
- linked skill/standard/change: `visual-qa-evidence`, `.agents/skills/screenshot-production-ui/SKILL.md`.
- status/date: active / 2026-08-28.
