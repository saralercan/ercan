# Vinterro One — Portable Agent Runtime

Status: active
Version: 1.0
Date: 2026-09-24
Canonical runtime inventory: `VINTERRO_RUNTIME_AGENT_MANIFEST.json`
Production runtime count: **89 active agents**

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
2. Select the **smallest sufficient expert pod**.
3. Mark only those specialists **ACTIVE** for the current task.
4. Keep every other agent **STANDBY**.
5. If the work reveals a new domain, risk, evidence gap or implementation dependency, consult/activate the relevant standby specialist.
6. Independent QA/reviewer roles may join later even if they were not part of the initial producer pod.
7. Never broadcast a normal task to all 89 agents merely because the user used the master trigger.

This rule applies equally to Codex, Claude and Vinterro One.

## Provider adapters

### OpenAI / GPT / Codex

Use:
- root `AGENTS.md`;
- `.agents/skills/portable-agent-router/SKILL.md`;
- the canonical runtime manifest;
- task-relevant domain skills only.

OpenAI Agent Skills use `SKILL.md` bundles and are intended for reusable workflows. Keep the 89-agent inventory JIT behind one router instead of eagerly injecting 89 long prompts into every session.

For managed/SDK agent runtimes, map selected agent records into agent instructions/tools/handoffs at runtime. Use multi-agent orchestration only when work can genuinely benefit from separate context or independent execution.

### Claude Code

Use:
- root `CLAUDE.md`;
- `.claude/agents/vinterro-router.md`;
- the canonical runtime manifest.

Claude Code supports project subagents under `.claude/agents/` and automatically delegates when a task matches a subagent description. The Vinterro router deliberately keeps one short discoverable subagent definition and performs JIT role selection from the 89-agent manifest to avoid loading dozens of descriptions into every Claude session.

When separate contexts materially help, the router may spawn general-purpose/research subagents with the selected Vinterro role's exact mandate and constraints. Do not spawn subagents for trivial single-file or sequential work.

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

All portable runtimes must preserve the same learning contract. Before material work, the selected ACTIVE specialist loads its profile from `AGENT_EXPERTISE_SOURCE_MATRIX.json` and applies `AGENT_CONTINUAL_EXPERTISE_ENGINE.md`. Provider/model differences may change search/tool mechanics but may not lower source authority, freshness, provenance, ingestion or verification standards.

New verified knowledge is converted into durable rules/evals/source notes rather than copied raw into prompts. Non-selected STANDBY agents do not research unnecessarily.

## Verification

A task is complete only after the relevant producer + independent QA evidence exists. Routing metadata must expose at minimum:
- primary agent;
- active pod;
- standby count;
- master-mode flag;
- routing reason.

Provider/model success is not proof of task correctness.
