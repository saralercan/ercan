---
name: learning-tutor-engine
description: Turn documents or codebases into a structured learning path, then teach interactively with diagnostics, active recall, weak-area drilling and progress evidence. Use when the user asks to learn, be taught step-by-step, onboard into a codebase, create a study vault/guide, or be quizzed. Route through existing Ercan OS identities; this is a JIT capability, not a new stable agent.
---

# Learning & Tutor Engine

This JIT capability adapts the useful patterns from `bevibing/tutor-skills` without making Obsidian, Claude-specific UI primitives, or any single storage layout mandatory.

## Stable-owner mapping
- LearningPlan -> `@Orchestrator`
- SourceGrounding -> task-domain specialist + `@UpstreamIntelligence` only when current external sources are materially required
- CodebaseOnboarding -> `@WebArchitecture` / platform expert / repository owner specialist as appropriate
- KnowledgeStructure -> `@Orchestrator` + domain specialist
- QuizAndActiveRecall -> bounded Tutor role under `@Orchestrator`
- ProgressReview -> `@Orchestrator` with evidence from prior sessions/artifacts
- IndependentQA -> task-domain QA specialist when generated learning material makes technical or factual claims

## Modes

### Document learning
`source discovery -> topic/dependency map -> concise concept notes -> practice questions -> diagnostic -> weak-area drill -> progress update`

### Codebase onboarding
`repo baseline -> architecture/module map -> request/data flow -> key interfaces/config -> exercises -> diagnostic -> weak-area drill`

## Rules
1. Teach from authoritative user/project sources first; do not invent missing architecture or facts.
2. Prefer progressive disclosure: concept map first, then detail on demand.
3. Use active recall, spaced revisiting and error-focused rephrasing rather than repeating the same question verbatim.
4. Track progress by concept when persistence is available; otherwise summarize progress in-chat without pretending durable storage exists.
5. Do not require Obsidian. A StudyVault-style folder is optional and only created when requested or materially useful.
6. Do not require exactly four questions; adapt round size to user intent and interface constraints.
7. Never leak answers through option wording, hints or ordering when running a diagnostic.
8. Codebase onboarding must distinguish observed source truth from inferred explanation.
9. Learning content inherits current project rules, terminology and do-not-touch constraints.
10. Completion means the learner-facing artifact/session is usable and grounded, not merely generated.

## Reviewed upstream
- `bevibing/tutor-skills` — MIT — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
- Useful upstream concepts: document/codebase mode split, StudyVault structure, concept-level progress, diagnostics, weak-area drilling, self-review.
- Do not copy host-specific `AskUserQuestion`, Claude-only commands or storage assumptions into Ercan OS core contracts.

## Completion evidence
Record source set, target learner goal, covered concepts, unanswered/weak concepts, generated exercises, progress evidence if any, factual/technical QA and final state: VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED.
