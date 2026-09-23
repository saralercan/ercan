# Provider Scan — Rerun Platform Refresh

Date: 2026-09-24
Provider: https://rerun.build/
Docs: https://docs.rerun.build/

## Why this refresh exists

A same-day recheck found material changes/conflicts versus the earlier Rerun scan. This refresh supersedes stale operational assumptions while retaining the earlier scan as history.

## Current technical model

Current official Rerun docs state:
- a workspace is the account/team boundary;
- each workspace runs on one private cloud computer;
- all agents in the workspace share that computer;
- a Box is an organizational room for team/client/project;
- Boxes are instant/free and are **not an isolation wall**;
- agents across Boxes share the same machine, folder and workspace database;
- each agent still has its own prompt/model/memory/skills/files/private database.

This means the previous Ercan OS rule "separate Box = separate client isolation" is no longer safe.

Updated rule:
- use separate workspaces or another separately isolated deployment for tenant/confidentiality boundaries;
- use Boxes for organization only.

## API/MCP expansion

Current docs expose a workspace-scoped MCP/API with tools for:
- agents
- skills
- scheduled tasks
- triggers/webhooks
- messages/runs
- private and workspace databases
- connectors
- share links
- templates

Clients include Codex, Claude Code, Cursor, Rerun agents and generic MCP clients.

Decision:
create `rerun-api-bridge` JIT capability.

## Known official-source conflicts

### Box model
Technical docs say one machine per workspace and Boxes are not isolated.
DPA Annex II currently says one dedicated VM per Box.

Decision:
`PROVIDER_STATE_CONFLICT`.
Use current technical docs for runtime architecture; retain DPA discrepancy as contractual issue requiring provider clarification if isolation matters.

### Gmail
Privacy Policy says Gmail is sending-only and cannot read/search/list mailbox.
Homepage shows inbox sorting and "new email" trigger examples.

Decision:
`PROVIDER_STATE_CONFLICT`.
Do not infer mailbox-read OAuth capability. Inspect actual target connector/trigger before production.

### Pricing/package
Live pricing page on this review shows:
- from $49/month
- 5 agents
- 3 seats
- one private workspace machine
- 200+ apps
- unlimited executions
- 3-day trial, no card required

Older recently indexed/compare pages still show:
- $24/month
- 3 agents
- 1 seat/Box
- 7-day trial

Decision:
live pricing page wins for present purchase decisions, but Ercan OS stores no permanent commercial assumption.

## Marketplace / Expert channel

Current Expert Program page advertises:
- directory listing and client matching;
- free expert sandbox;
- 95% of template sales;
- 20% recurring on referred client plans;
- co-marketing/early access.

Marketplace Creator Terms state templates are reviewed before publication; publication is discretionary and not certification of fitness/safety. Sellers must maintain templates and complete Stripe Connect identity/AML requirements.

Decision:
retain as a potential Vinterro Digital distribution/productization channel, not guaranteed revenue.

## Template patterns

Current official templates reveal useful architecture conventions:
- scheduled source collection;
- dedupe against prior runs;
- explicit observed/inferred labels;
- graceful delivery when one source fails;
- source-backed briefs;
- write-back after dedupe;
- human review before public posting in some content templates.

These patterns may be adopted independently of Rerun.

## Updated adoption

Rerun remains:
`ADOPT_WHEN_NEEDED / MANAGED_AGENT_DEPLOYMENT_PROVIDER / CLOSED_SOURCE_SAAS`.

New additional capability:
`rerun-api-bridge` for controlled Ercan OS -> Rerun workspace synchronization.

No stable identity count change.
