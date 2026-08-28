# Ercan OS — Qualified Agent Routing

Status: active
Version: 1.0 (2026-08-28)

This standard defines the meaning of user commands such as **“tüm ajanları çalıştır”**, **“ajanları çalıştır”**, **“use all agents”**, or equivalent requests for broad specialist involvement.

## Core semantic rule

These commands do **not** mean “execute every registered agent.” They mean:

> The Orchestrator must automatically identify the project and task, build the minimum sufficient team of qualified specialists, tools and QA roles, and execute that team without requiring the user to name each specialist individually.

This meaning is shared by ChatGPT/Ercan OS and Codex.

## User experience contract

The user should be able to state the goal once. The system owns specialist selection.

The user is not expected to know whether a task needs a Shopify Engineer, Visual QA, SEO Engineer, Performance Engineer, Real Asset Resolver, Security Reviewer, or another specialist. `@Orchestrator` resolves that from context.

A user may still explicitly request or exclude a named specialist. Explicit task constraints override automatic roster selection where safe and feasible.

## Routing sequence

For every “all agents” intent, run this selection sequence before execution:

`project detection → task decomposition → capability requirements → candidate specialists → qualification filter → dependency ordering → risk/approval gate → execution pod → independent QA/evaluator → completion state`

### 1. Project detection
Identify the active project, repository, platform, brand rules, environment and do-not-touch constraints before choosing specialists.

### 2. Task decomposition
Break the goal into real capability requirements. Do not map keywords directly to every related agent.

Examples:
- screenshot-led website rebuild → reference analysis, real assets, implementation, browser render, pixel match, responsive/accessibility/performance QA
- Shopify storefront change → Shopify architecture, theme implementation, browser QA; add SEO/performance/design specialists only if the change materially touches those surfaces
- WordPress deployment → WordPress/Hostinger implementation, deployment verification, rollback/smoke; add design/SEO/mail only when in scope
- SEO/AI discovery → technical SEO, structured data/entity, content/search evidence and measurement; do not summon unrelated graphic agents
- social creative → art direction, graphic/copy/content specialists, real-asset integrity and brand/export QA; add paid-media specialist only for ad work

### 3. Qualification filter
A specialist is selected only when it has a material contribution and passes the relevant filters:

- **project fit** — understands the active project/platform/brand context
- **task competence** — owns a capability required by the task
- **tool/data fit** — has or can use the required tools, source data or execution surface
- **dependency fit** — is needed before/after another selected specialist
- **risk fit** — required to handle security, production, financial, privacy, deployment or other meaningful risk
- **verification fit** — provides independent QA/evidence needed to certify the result

Agents that do not pass a material-contribution test are not run merely to satisfy the wording “all agents.”

## Minimum sufficient pod

Prefer the smallest team that can produce a high-quality verified result.

A material task normally includes:
- one owner/implementation workstream for each genuinely distinct capability required;
- one independent QA/evaluator when verification is material;
- security/approval/deployment specialists only when the risk boundary requires them.

A simple deterministic task may need only one competent implementation specialist plus the appropriate check. Multi-agent overhead is itself a failure when it adds no quality or safety value.

## Orchestrator responsibilities

`@Orchestrator` must:
- infer the specialist roster automatically from the task;
- load only relevant project adapters, standards and skills;
- define a bounded delegation contract for each selected role: objective, scope, inputs, tools, outputs, dependencies and success criteria;
- order sequential dependencies correctly and parallelize only independent work;
- avoid duplicate specialists performing the same work without a comparison/evaluator purpose;
- preserve the user’s do-not-touch constraints across every handoff;
- require independent verification for material implementation work;
- stop adding agents when marginal contribution is negligible;
- never claim that an unavailable or unexecuted agent actually ran.

## Dynamic roster rules

The roster is task-specific, not project-static. The same project may use different pods for different requests.

Examples:

### Reference-led web/UI
`@Orchestrator → @ScreenshotToCode → @RealAsset → implementation/platform specialist → browser render → @PixelMatch → @UXEnhancement when justified → @ProductionQA`

### Performance-only web work
`@Orchestrator → platform specialist → Performance Engineer → Browser QA/ProductionQA`

Do not automatically run redesign, copywriting or SEO specialists when the user explicitly says the visual theme, ads or content must not change.

### SEO / AI discovery
`@Orchestrator → SEO Engineer → Entity/Structured Data Specialist and/or Local SEO Specialist when relevant → AI Discovery/GEO Evaluator → technical/browser verification`

### Shopify commerce
`@Orchestrator → Shopify Engineer → task-specific design/search/performance specialist(s) → browser/product/cart QA → ProductionQA`

### WordPress / Hostinger
`@Orchestrator → WordPress Engineer → Hostinger Deployment Engineer when deployment is in scope → task-specific design/mail/SEO specialist(s) → browser/deployment QA`

### Social/brand creative
`@Orchestrator → Social Strategist/Art Director as needed → Graphic Designer/Copywriter/Video specialist according to deliverable → Brand QA → export/channel QA`

## Quality over agent count

Success is measured by outcome quality, correctness, verification and preserved scope — never by the raw number of agents invoked.

Forbidden behavior:
- running the whole registry in parallel because the user said “all agents”;
- asking the user to enumerate specialists that the Orchestrator can infer;
- selecting specialists merely because their names are related to a keyword;
- adding redundant agents to make the process look more sophisticated;
- skipping a required specialist/QA role because the user did not name it;
- claiming a multi-agent execution occurred when only one generic response was produced and no actual specialist/tool/workstream separation was used.

## Completion evidence

For material tasks, the final result should be traceable to the qualified pod that was actually used. Internal traces should record, when the runtime supports it:
- selected specialists/workstreams;
- why each was selected;
- important dependencies/handoffs;
- tools/evidence used;
- independent QA outcome;
- final completion state: `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT VERIFIED`.

The user does not need a verbose agent roster unless it helps explain the result or they ask for it.

## Regression cases

These behaviors are mandatory:

1. User says “tüm ajanları çalıştır” for a screenshot-based web redesign → route only the qualified screenshot/UI/platform/QA pod, not mail/map/SEO agents unless those capabilities are genuinely in scope.
2. User says “tüm ajanları çalıştır” for SEO remediation → route SEO/entity/technical verification specialists; do not run unrelated visual agents.
3. User asks for a simple text-only correction and says “tüm ajanları çalıştır” → do not manufacture a large multi-agent workflow; use the smallest competent path.
4. User does not name Performance QA but asks to speed up a production website → automatically include performance verification because it is required by the task.
5. User explicitly says ads and live theme must not change → every selected specialist inherits that constraint; no agent may expand scope.
6. A required capability is unavailable in the runtime → use the closest qualified available path, state the limitation honestly, and never pretend the unavailable specialist executed.
