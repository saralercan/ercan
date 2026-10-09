---
name: vinterro-one-router
description: Use Vinterro One from ChatGPT/OpenAI or Codex. Trigger when the user mentions Vinterro One, /agent, ajanları çalıştır, tüm ajanları çalıştır, use all agents, a named Vinterro One agent, or asks GPT/Codex to use the Vinterro One agent system.
---

# Vinterro One Router — ChatGPT/OpenAI + Codex

Use the strongest currently authorized Vinterro One source:
1. live Vinterro One ChatGPT MCP when available;
2. connected Supabase app/plugin and live registry;
3. versioned repository mirror.

Do not pretend a stronger connection exists than the current surface actually provides.

## Reklam Ajansı skill dispatch

Requests for paid advertising, Google Ads, Meta/Instagram Ads, Pinterest/TikTok, creatives, attribution/Purchase, advertising budget, consent compliance, worldwide advertising research or retail media route to the **single** live `Reklam Ajansı` agent. Read `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` and load the relevant `.agents/skills/reklam-ajansi-<id>/SKILL.md` for the task (at most three). Parent: `.agents/skills/reklam-ajansi/SKILL.md`, with master `docs/agents/REKLAM_AJANSI.md`. Do **not** reactivate the five retired specialist identities; they are internal capability lanes. Route planning is read-only and does not start model workers. Account mutation, ad launch, budget change, audience upload, customer data or cold outreach remains approval/verified-execution gated. Independent QA belongs to separate reviewer agents.

### Mandatory Reklam Ajansı for ALL agents / Vinterro One start

The explicit phrases **`tüm ajanları çalıştır`**, **`bütün ajanları çalıştır`**, **`Vinterro One çalıştır`**, **`Vinterro One'ı çalıştır`**, **`run all agents`** and equivalent master invocations automatically include **one Reklam Ajansı parent plus its full nine-subskill roster**, even if the user did not name ads. This is a permanent global exception to the normal 3-skill task selector. Use `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` global_invocation and `scripts/plan_reklam_ajansi_workflow.py`. Every skill must appear: task-matching scopes as MATERIAL_WORKSTREAM; unrelated skills as SCOPE_CHECK_ONLY (no unnecessary remote effects). Other specialists are still task-qualified; do not fan out whole registry. Include independent QA, do not self-certify, never equate a plan with running parallel workers, and never bypass the ads/Gmail release gates.

## Source order

Load only what the task needs.

Prefer live current-state data for status/version/health/project membership, then:
1. repository root `AGENTS.md`;
2. `docs/standards/CHATGPT_VINTERRO_ONE_RUNTIME.md` for ChatGPT/OpenAI;
3. `docs/standards/VINTERRO_PROJECT_REGISTRY.json`;
4. `docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json`;
5. `docs/standards/QUALIFIED_AGENT_ROUTING.md`;
6. the active project's dedicated `projects/<project>/AGENTS.md` when present, otherwise `projects/_runtime/AGENTS.md`;
7. task-relevant skills/standards;
8. `docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md` for material or release-sensitive work.

When canonical repo files are unavailable, use this skill bundle's self-contained references.

Do not eagerly load every agent prompt.

### Drag&Drop mail routing invariant

For any Drag&Drop customer, designer, brand, onboarding or Gmail task:
- activate `Drag&Drop Baş Uzman Ajanı`, `Drag&Drop Müşteri Temsilcisi Ajanı` and `Drag&Drop Mail Ajanı`;
- load `references/DRAGDROP_MAIL_AGENT.md` before drafting or sending;
- use its canonical branded HTML email template, CTA structure, sender/thread approval gates and current commission wording rules;
- include independent MailQA for send-ready or production sends.

### Drag&Drop outreach / tanışma invariant

For cold first-touch designer/brand outreach, alphabetical Excel/list campaigns, outreach example sends or approved cold-outreach batches:
- additionally activate `Drag&Drop Outreach Ajanı`;
- load the plugin skill `dragdrop-outreach-intro`;
- require real product/collection evidence for the personalized opening;
- prohibit unsupported prior-contact language;
- require Gmail SENT dedupe by brand + exact email + domain;
- preserve the Türkiye-based / especially-Europe-active sales positioning, correct recipient commission, B2C+B2B structure and canonical CTA system;
- once a reply/existing conversation is detected, hand off from Outreach to Customer Service + Mail Agent in the same thread.

### Sales intelligence invariant

For sales intelligence, prospect/company discovery or enrichment, Vinterro Keşif-to-sales scans, missing/broken website prospecting, technographic/digital-maturity research, account-level prospect dedupe, qualification/scoring or outreach-ready evidence packets:
- activate `Sales Intelligence Agent` plus the Vinterro Digital project lead when material;
- load plugin skills `sales-intelligence-discovery`, `website-opportunity-audit` when website state matters, `sales-lead-qualification`, and `sales-intelligence-handoff`;
- preserve public-business evidence, passive website checks, no-guessed-contact, no-private-contact and explicit-approval-for-credit-consuming-enrichment rules;
- never let Sales Intelligence send email/DM;
- hand `OUTREACH_READY` accounts to Vinterro Digital Outreach Ajanı + Vinterro Digital Mail Ajanı under canonical dedupe/template/MailQA gates.

## ChatGPT/OpenAI behavior

When a Vinterro One MCP app is connected, call `vinterro_route_task` before substantial project work or a master-trigger request.

When custom MCP is unavailable but the connected Supabase app is authorized:
- read `ercan_os_projects` and `ercan_os_agents`;
- resolve the project from current context/task;
- use the current project lead plus the complete materially relevant specialist pod;
- inspect expertise health/profile state when material;
- preserve the same supervision semantics.

When only GitHub/repository access is available, use the portable registry/manifest and state that the portable contract—not live runtime health—was used.

## Runtime selection

Every agent is STANDBY by default.

When the user says `tüm ajanları çalıştır`, `bütün ajanları çalıştır`, `ajanları çalıştır`, `use all agents`, or equivalent:
- identify the active project;
- activate the current project lead;
- activate the complete non-redundant set of specialists with a distinct material contribution;
- include an independent reviewer/QA lane where verification is material;
- keep unrelated or redundant agents STANDBY;
- do not optimize for fewest agents;
- do not use a fixed 5/8-agent ceiling;
- do not literally fan out to every registered agent.

## /agent behavior

Treat `/agent <name>`, `@<agent>`, or a clear named-agent request as an explicit routing preference.

Resolve the requested identity against the live registry first when available, otherwise the portable manifest. Keep its permissions, project scope, handoffs and QA gates.


Codex compatibility invariant: project coverage **must never be limited to hard-coded examples**. For the master trigger, activate the **complete qualified global specialist/QA/risk pod** together with the current project lead and materially relevant project-scoped specialists. These phrases are part of the shared regression contract and apply equally to ChatGPT/OpenAI.

## Human-language localization

When the task includes translation, localization, multilingual commercial copy, proofreading or terminology work in English, Bulgarian, Spanish, Greek, German or French:
- activate the dedicated Language & Localization Specialist for every required target language;
- activate `Multilingual Localization QA Auditor` for material external-facing output;
- preserve the normal project lead and supervision chain;
- use `MULTILINGUAL_LOCALIZATION_AGENT_STANDARD.md` when the repository/reference bundle is available;
- do not use `Language Freshness Agent` as a substitute; that identity tracks programming/framework language freshness.

The language specialists are global and apply to every project, not only Vinterro Digital.

## Codex native bridge

When running in Codex with native multi-agent support, use the custom roles declared in `.codex/config.toml`
and `.codex/agents/*.toml`. Load `docs/standards/CODEX_NATIVE_AGENT_BRIDGE.md`.

Vinterro One runtime identities are logical expert contracts; Codex native agents are bounded execution threads.
Map the exact selected Vinterro One identity into the most specific native role. Any identity without a more specific
role uses `vinterro_specialist` and the delegated task MUST include the exact runtime agent name.

Do not open the entire runtime registry concurrently. Respect `agents.max_concurrent_threads_per_session`.
If Codex reports an agent/thread limit, treat it as scheduling backpressure: wait for in-flight dependencies,
close completed native agent threads, then continue the remaining qualified pod in the next wave.
Do not conclude that the Vinterro One agents are unavailable merely because a spawn hit the thread ceiling.

If the current Codex surface does not expose native multi-agent execution, follow the selected logical specialist
contracts in the main execution context and state that no independent native subagent execution was evidenced.

## Project lead rule

Project coverage is dynamic. Never limit routing to hard-coded examples.

A dedicated filesystem adapter enriches a project but does not define Vinterro One membership. Active live projects without a dedicated adapter use `projects/_runtime/AGENTS.md`.

## Supervision

Material work preserves:

`producer -> independent reviewer -> correction/retest -> release gate`

A creator cannot self-certify critical work. Security-sensitive work includes Vinterro One Security Director plus independent Security Auditor when the contract requires them.

## External actions

Never claim a send, publish, deploy, database mutation, Shopify mutation, payment, campaign change or other external action happened without current provider evidence and applicable approval.

## Completion

Use evidence-based completion:
- VERIFIED
- PARTIAL
- BLOCKED
- NOT_VERIFIED

Routing success is not the same as real-world execution success.
