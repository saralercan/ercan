# Ercan OS — Managed Agent Deployment

Status: active
Date: 2026-09-24

## Purpose

Define how Ercan OS may use managed agent platforms as external execution/deployment surfaces without surrendering project governance, source-of-truth rules, approvals or independent verification.

Execution skill: `.agents/skills/managed-agent-deployment/SKILL.md`.

Primary reviewed provider: Rerun (`https://rerun.build/`).

Stable routing identities remain **52**.

## Rerun decision

`ADOPT_WHEN_NEEDED / MANAGED_AGENT_DEPLOYMENT_PROVIDER / CLOSED_SOURCE_SAAS`

### Why it is useful

Current public product materials describe:
- recurring/event-triggered autonomous agents;
- one private cloud machine per workspace, with Boxes used to organize agents;
- human approval before sensitive actions;
- live run visibility;
- broad app integration plus MCP/API support;
- bring-your-own AI/subscription/API/local-model options;
- agent/skill templates;
- client/expert distribution workflows.

This fills a deployment/operations gap rather than an orchestration-theory gap.

### Why it is not Ercan OS itself

Rerun is a closed-source managed platform. Ercan OS keeps:
- project policy;
- agent routing;
- reusable skills/standards;
- source-controlled business rules;
- QA/eval;
- completion authority;
- cross-provider architecture.

Rerun is a replaceable runtime/deployment provider.

## Deployment route

`Ercan OS task/project policy -> managed-agent-deployment decision -> Rerun agent/Box/connector configuration -> approval gates -> scheduled/triggered execution -> live evidence -> independent Ercan OS verification`

## Provider constraints

### Connector scope
A connector is approved per capability, not per brand name. Verify current permissions and write scope.

### Gmail
Current privacy documentation states Gmail access is sending-only. Do not assume mailbox read/search/list capabilities from marketing examples.

### Outreach
Current AUP prohibits bulk unsolicited email/message/call campaigns. Do not use Rerun as Vinterro's bulk cold-outreach sender.

### Data processing
Current Privacy Policy/DPA describe Reunit SA as processor for Cloud Mode customer content and EU core infrastructure. Current technical docs define one private machine per workspace and explicitly say Boxes are not an isolation wall; current DPA Annex II still says one dedicated VM per Box. This is a `PROVIDER_STATE_CONFLICT`, not a resolved isolation guarantee. Self-hosted availability and subprocessor details remain runtime-verified facts.

### Approvals
Use Rerun approvals to implement the Ercan OS risk classification, not to redefine it.

### Pricing
Current marketing/pricing details are volatile. Verify immediately before purchase/proposal. Never hard-code commercial assumptions into project economics.

## Project/client isolation

Current docs make the **workspace** the machine/security boundary and Boxes organizational.

Use separate workspaces or another separately isolated deployment when:
- clients have separate credentials;
- confidentiality boundaries matter;
- filesystem/shared-database state must not be shared;
- ownership/accountability should be separable.

Do not treat Boxes as tenant isolation and do not place all Vinterro clients into one shared workspace merely to reduce cost.

## API bridge
For programmatic Ercan OS ↔ Rerun synchronization, load `RERUN_API_BRIDGE.md` + `.agents/skills/rerun-api-bridge/SKILL.md`. The current Rerun docs expose workspace-scoped MCP/API tools for agents, skills, schedules, triggers, runs/messages, databases, connectors, share links and templates.

## Source of truth

Business logic that materially affects client delivery should remain reproducible outside a single SaaS UI where practical:
- versioned skill/instruction docs;
- schemas;
- templates;
- prompts;
- approval rules;
- integration contracts;
- eval cases.

Managed-platform-only state must be documented sufficiently for migration or disaster recovery.

## Fit examples

### Good fit
- recurring client reporting;
- weekly SEO diagnostic/search-visibility monitoring when paired with `WEEKLY_SEO_DIAGNOSTIC.md`;
- competitor creative monitoring and public Meta Ad Library research when paired with `COMPETITOR_CREATIVE_INTELLIGENCE.md`;
- competitor/SEO signal briefs;
- support/admin workflows with explicit approvals;
- monitoring and summarization;
- client-facing operations that benefit from a readable dashboard;
- agent templates delivered to non-technical clients.

### Poor fit
- one-off coding changes better handled by Codex/GitHub;
- deterministic workflows better served by simple automation;
- bulk unsolicited outreach;
- deeply custom low-level runtimes where source-level control is essential;
- high-impact decisioning without human review.

## Expert/marketplace route

The current Expert Program may be evaluated as a Vinterro Digital distribution channel.

Before business adoption:
- verify current eligibility;
- marketplace terms;
- revenue share;
- client ownership;
- template IP rights;
- support obligations;
- payout/Stripe availability;
- customer relationship and data-controller responsibilities.

No revenue forecast is based solely on current marketing terms.

## Completion contract

Managed deployment is VERIFIED only after real execution and external side-effect checks. A dashboard status or agent self-report alone is insufficient.
