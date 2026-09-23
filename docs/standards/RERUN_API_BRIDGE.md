# Ercan OS — Rerun API Bridge

Status: active
Date: 2026-09-24

## Purpose

Define the integration contract between Ercan OS and Rerun's current workspace-scoped MCP/API.

Execution skill: `.agents/skills/rerun-api-bridge/SKILL.md`.

Stable routing identities remain **52**.

## Current reviewed API capabilities

Rerun's current official documentation index exposes tools for:
- agents;
- skills;
- schedules;
- triggers/webhooks;
- runs/messages;
- private/shared databases;
- apps/connectors;
- share links;
- templates.

The API can be connected from Codex, Claude Code, Cursor, other MCP clients or Rerun agents.

## Control-plane split

### Ercan OS owns
- policy
- source-controlled standards/skills
- project constraints
- approval policy
- routing
- QA/evals
- completion

### Rerun owns
- managed runtime execution
- workspace machine
- deployed agent state
- schedules/triggers
- connector plumbing
- runtime databases
- run logs/dashboard
- marketplace/share delivery surfaces

## Workspace / Box model

Current technical docs define:
- one private machine per workspace;
- all agents in that workspace share the same machine;
- Boxes group agents by team/client/project;
- Boxes are **not security isolation**;
- agents in different Boxes share the workspace folder and shared database.

Therefore the Ercan OS client-isolation rule is:
**separate workspace (or another isolated deployment) for confidentiality/credential tenant boundaries.**

Do not use separate Boxes alone as proof of client isolation.

## Official-source conflict policy

When current official Rerun sources materially disagree, mark `PROVIDER_STATE_CONFLICT` until target-workspace behavior or provider clarification resolves the difference.

Current official sources are internally inconsistent on some points.

### Box isolation
- current technical docs: one machine per workspace; Boxes are organizational and share machine/data;
- current DPA Annex II: says one dedicated VM per Box.

Runtime architecture must follow current technical behavior unless contract/support confirms otherwise. Contractual claims remain a legal review item.

### Gmail
- Privacy Policy: Gmail OAuth is sending-only and cannot read/search/list mailbox;
- homepage: shows inbox sorting and new-email-trigger examples.

Do not route Gmail read/search/list through Rerun until the exact current connector/trigger mechanism and OAuth scope are observed in the target workspace.

### Pricing/package
Current live pricing page (2026-09-24) shows a newer offer than some recently indexed comparison/search pages. Commercial values are always runtime-verified before proposal/purchase.

## Deployment pattern

`Ercan OS source -> workspace target -> API diff -> skills/agent sync -> connector declaration -> schedule/trigger -> safe smoke run -> approval -> destination verification -> evidence ledger`

## Drift

Runtime edits may create drift between repository definitions and Rerun.

For material agents:
- define field ownership;
- read before write;
- record deployed revision;
- compare runtime state periodically;
- never overwrite operator changes blindly;
- maintain export/rebuild path.

## Security

- workspace API keys are secrets;
- one workspace key must never be reused as a cross-client global credential;
- connectors remain least-privilege;
- public webhook secrets are rotated after exposure;
- shared workspace database is not a tenant boundary;
- share links/templates require data/secret review;
- Rerun AUP continues to prohibit bulk unsolicited outreach.

## Commercial/channel opportunity

The API + template marketplace + Expert Program make Rerun a potential Vinterro Digital productization channel:
- build a verified agent once;
- package as reusable template;
- deploy per client workspace;
- retain Ercan OS source/eval package;
- maintain/update versioned template;
- optionally participate in marketplace/expert distribution.

Current published Expert Program percentages are treated as volatile commercial terms.

## Completion contract

A Rerun API deployment is VERIFIED only after runtime state, actual scheduled/triggered execution and material external side effects are independently checked.
