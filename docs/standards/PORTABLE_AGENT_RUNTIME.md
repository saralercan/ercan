# Vinterro One — Portable Agent Runtime

Status: active
Version: 1.1
Date: 2026-09-29
Canonical runtime inventory: `VINTERRO_RUNTIME_AGENT_MANIFEST.json`
Production runtime count is read from the live `ercan_os_agents` registry at runtime; do not hardcode routing behavior to an older snapshot.

**Mirror/live count drift:** the versioned manifest is a portable mirror, not the live count authority. If the live registry count differs from the repo mirror (for example, the operator reports 103 while the mirror still contains 89), routing must use the live registry when available and the mirror must be flagged for resync; never fabricate missing agent records merely to match a count.

## Goal

Every Vinterro One agent must be usable from:
- OpenAI / GPT / Codex-compatible agent harnesses;
- Claude Code / Anthropic-compatible subagent orchestration;
- Vinterro One's native Supabase + Edge control plane.

Agent expertise is provider-neutral. Model/provider adapters may change syntax, tools or invocation mechanics, but must not silently change the agent's mandate, safety boundary, source truth or QA contract.

## One source of truth

Use the runtime manifest as the canonical portable inventory. Do not maintain separate divergent name/role lists for Codex, Claude and Vinterro One.

Each agent record provides:
- name and role;
- principal instructions;
- tools/capability labels;
- permissions;
- allowed handoffs;
- step/retry/cost limits;
- JIT activation state;
- runtime adapters.

Vinterro One's live `ercan_os_agents` table remains the production execution registry. The repo manifest is the portable/versioned mirror and must be resynced after registry changes.

## ACTIVE / STANDBY orchestration

Default state for a specialist is **STANDBY**.

The phrases:
- `tüm ajanları çalıştır`
- `bütün ajanları çalıştır`
- `ajanları çalıştır`
- `run agents`
- `run the agents`

mean:

1. Understand the current task, project, risk and required evidence.
2. Build the **complete non-redundant pod of every specialist with a distinct material contribution** to the current task.
3. Activate the project lead plus all materially relevant domain specialists and independent QA/reviewer roles; do not optimize for minimum headcount.
4. Run independent workstreams in parallel when the provider/runtime supports it; keep dependency-bound work ordered.
5. Three, five, eight or more specialists may be ACTIVE simultaneously when the task genuinely spans that many capabilities.
6. Keep only unrelated or redundant agents **STANDBY**.
7. If the work reveals a new domain, risk, evidence gap or implementation dependency, activate the matching standby specialist immediately.
8. Never broadcast a task to every registered agent merely because of the phrase; the trigger means **all relevant experts for this task**, not literal full-registry fan-out.

This rule applies **identically** to ChatGPT/OpenAI, Codex, Claude and Vinterro One. Provider adapters may change mechanics, but they may not reduce the selected expert coverage or reinterpret the master trigger as a minimum-team shortcut.

## Connector availability and portable fallback

The absence of a live Vinterro One/Supabase connector in a provider session does **not** make Vinterro One agent contracts unavailable when the repository is accessible.

When the live control-plane connector is unavailable:
- load routing/agent/project/skill/standard contracts from the versioned repository mirror;
- preserve the exact same specialist selection semantics, project rules, mail/template contracts, safety boundaries and QA requirements;
- use whatever provider connectors are actually available (for example Gmail) only for their real external evidence/actions;
- never claim that a live Vinterro One runtime agent executed unless current runtime evidence proves it;
- say `repo contract loaded` / `portable specialist route applied` rather than falsely claiming live agent execution.

When the live connector is available, live registry/state may refine the repo snapshot for current health/status/version, but it must not silently weaken project standards.

## Provider adapters

### OpenAI / GPT / Codex

Use:
- root `AGENTS.md`;
- `.agents/skills/portable-agent-router/SKILL.md`;
- the canonical runtime manifest;
- task-relevant domain skills only.

OpenAI Agent Skills use `SKILL.md` bundles and are intended for reusable workflows. Keep the runtime inventory JIT behind one router instead of eagerly injecting every long prompt into every session. On the master trigger, the router must still activate every materially relevant expert for the task.

For managed/SDK agent runtimes, map selected agent records into agent instructions/tools/handoffs at runtime. Use multi-agent orchestration only when work can genuinely benefit from separate context or independent execution.

### Claude Code

Use:
- root `CLAUDE.md`;
- `.claude/agents/vinterro-router.md`;
- the canonical runtime manifest.

Claude Code supports project subagents under `.claude/agents/` and automatically delegates when a task matches a subagent description. The Vinterro router deliberately keeps one short discoverable subagent definition and performs JIT role selection from the current versioned runtime manifest to avoid loading dozens of descriptions into every Claude session.

When separate contexts materially help, the router should spawn/activate the selected specialist contexts with each Vinterro role's exact mandate and constraints. Independent specialist workstreams should run concurrently when supported. Do not spawn unrelated subagents merely to inflate agent count.

### Vinterro One native

Native routing uses:
- live `ercan_os_agents` registry;
- `ercan-os-api` `resolve_specialists` and `start_ai_run`;
- runtime policy/Human Approval;
- active pod + standby pool.

The production control plane is authoritative for current active/paused health state.

## Model portability

Do not encode agent identity around one model name.

A portable agent may run on:
- an OpenAI model through Codex/Agents/Responses/AI Gateway;
- an Anthropic Claude model through Claude Code/AI Gateway;
- another approved provider added later.

Provider-specific capabilities are adapters. If a capability is absent in a provider, mark it unavailable or route through an approved tool/connector; do not pretend it executed.

## Tool portability

Agent `tools` in the manifest are semantic capability labels, not a promise that every runtime exposes a tool with the same literal name.

Adapter mapping must resolve labels such as:
- `web` / research;
- GitHub;
- browser QA;
- filesystem/code edit;
- Shopify / WordPress;
- analytics / spreadsheet;
- policy / approval;
- sandbox/runtime.

If a required capability cannot be mapped in the current runtime, the agent stays partially blocked and the Orchestrator may escalate to another runtime or specialist.

## Handoff contract

Every handoff carries:
- task objective;
- project/context;
- authoritative inputs;
- completed findings;
- unresolved question;
- permission/risk boundary;
- requested output;
- acceptance criteria.

A standby agent is activated only when its contribution is material.

## Finance Expert Agent

`Finance Expert Agent` is a principal finance specialist covering:
- FP&A and budgeting;
- cash-flow planning;
- financial statement interpretation;
- pricing/margin and unit economics;
- KPI/forecast design;
- scenario/sensitivity analysis;
- business-case and financial-model review.

It must separate actuals, assumptions and forecasts; reverify current accounting/reporting requirements when material; and never invent financial figures. It does not execute banking, payments, investment or trading actions. Tax/legal certainty and regulated financial advice remain outside its authority without appropriate qualified review.

## E-commerce Expert Agent

`E-commerce Expert Agent` is the cross-platform commerce owner covering:
- catalog and merchandising;
- PDP/PLP and navigation;
- pricing/promotions;
- inventory;
- cart/checkout/payments;
- shipping/returns;
- marketplaces and product feeds;
- Merchant Center;
- CRO and retention/lifecycle;
- analytics, SEO and attribution;
- unit economics and operational handoffs.

It coordinates Shopify, WordPress/WooCommerce, CRO, SEO, paid media, analytics, compliance and finance specialists rather than replacing them.

## Continual expertise

All portable runtimes must preserve the same learning contract. Before material work, the selected ACTIVE specialist loads its profile from `AGENT_EXPERTISE_SOURCE_MATRIX.json` and applies `AGENT_CONTINUAL_EXPERTISE_ENGINE.md`. In Vinterro One native runtime, `ercan_os_agent_expertise_health` is authoritative for freshness: any ACTIVE agent whose state is not `CURRENT` is `research_required` and must refresh current authority before material decisions. Provider/model differences may change search/tool mechanics but may not lower source authority, freshness, provenance, ingestion or verification standards.

New verified knowledge is converted into durable rules/evals/source notes rather than copied raw into prompts. Non-selected STANDBY agents do not research unnecessarily.

## Verification

A task is complete only after the relevant producer + independent QA evidence exists. Routing metadata must expose at minimum:
- primary agent;
- active pod;
- standby count;
- master-mode flag;
- routing reason.

Provider/model success is not proof of task correctness.
