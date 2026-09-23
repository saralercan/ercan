---
name: managed-agent-deployment
description: Select and govern managed agent deployment surfaces for recurring business operations, client delivery, approvals, connectors, isolated workspaces and live run visibility. Use when Ercan OS needs to hand off a persistent agent to a team/client without turning the managed platform into the Ercan OS control plane.
---

# Managed Agent Deployment

This JIT capability covers external managed execution/deployment platforms. It does **not** create a new stable Ercan OS identity.

Primary reviewed provider: `https://rerun.build/`.

Current Ercan OS decision for Rerun:
`ADOPT_WHEN_NEEDED / MANAGED_AGENT_DEPLOYMENT_PROVIDER / CLOSED_SOURCE_SAAS`.

## Role in Ercan OS

Ercan OS remains the source of:
- project rules;
- stable routing identities;
- skills/standards;
- approval policy;
- evaluation and completion contracts;
- source-controlled agent definitions where applicable.

Rerun may be used as:
- a managed execution surface for recurring business agents;
- an isolated client/project Box;
- a connector/MCP/API access layer;
- a human-approval surface for risky actions;
- a live run/visibility surface for non-technical operators;
- a client handoff/deployment channel.

Rerun must never silently become the authoritative project memory, policy source, or completion authority.

## Best-fit use cases

Use Rerun when the task benefits from:
- always-on scheduled or event-triggered business agents;
- operator-friendly deployment without terminal maintenance;
- client/team access to run status and approvals;
- isolated per-client/project execution environments;
- managed integrations across SaaS tools;
- bringing an existing model subscription/API/local model into a managed business-ops runtime;
- packaging repeatable client agents/templates.

Examples:
- competitor monitoring;
- competitor creative monitoring / Meta Ad Library evidence collection, when paired with `competitor-creative-intelligence`;
- reporting and digest generation;
- invoice/admin follow-up with approval gates;
- support triage where the connector permissions fit;
- SEO/content research pipelines;
- account research and sales briefs;
- client-specific operational agents.

## Poor-fit / prohibited default use

Do not select Rerun merely because it has many connectors.

Avoid or escalate when:
- deterministic automation is simpler and sufficient;
- source-code-level orchestration/control is required;
- the workflow depends on unsupported connector permissions;
- bulk unsolicited email/message/call outreach is the goal;
- legal/high-impact decisions would be made without meaningful human review;
- the project requires guarantees or infrastructure controls not covered by the selected Rerun plan;
- current pricing/limits/connector behavior have not been reverified.

## Governance model

Ercan OS maps actions into three classes:

### Read / low-impact
May run automatically if the connected account scope is appropriate.

### Reversible / moderate
May run automatically only if the project explicitly permits it and there is a reliable audit/rollback path.

### High-impact / irreversible
Requires human approval before execution, including when material:
- sending external client/customer communications;
- creating/deleting production records;
- payments/refunds;
- publishing;
- destructive file/database changes;
- account/permission changes;
- high-impact external side effects.

Use the platform's approval feature as an execution gate, but preserve the Ercan OS approval rule as the policy source.

## Boxes / isolation

Treat one Rerun Box as an execution environment, not as proof of complete security.

For client/project isolation:
- use separate Boxes when credentials/data/projects should not share a machine;
- scope files and connectors to the minimum required;
- avoid placing unrelated client data in the same Box;
- define retention/deletion/export behavior before handoff;
- verify backup/export/termination behavior if business-critical state lives there.

## Connectors and credentials

Rerun currently advertises a broad connector library plus MCP/API support. Every connection still needs separate least-privilege review.

Rules:
- verify the exact OAuth/API scope currently requested;
- never infer read access from send access or vice versa;
- restrict write/action connectors independently;
- do not use one client's credentials in another client's Box;
- connected third-party terms remain binding;
- MCP servers remain independently audited under Ercan OS MCP discovery/security rules.

## Gmail boundary

Current Rerun Privacy Policy states its Google Gmail access is **sending only** and cannot read, search or list the mailbox.

Therefore:
- do not route mailbox search/reading workflows to the Gmail connector unless Rerun's current official connector documentation explicitly shows a different authorized mechanism;
- for outbound sends, still require appropriate user/project approval and recipient policy;
- for inbound email automation, resolve the actual trigger/source mechanism rather than assuming Gmail mailbox read access.

## Outreach boundary

Rerun's current Acceptable Use Policy prohibits bulk unsolicited email, message or call campaigns.

Therefore:
- do not use Rerun for bulk cold outreach;
- do not route Vinterro's scaled outbound prospecting through Rerun unless the specific workflow is compliant with Rerun's current AUP and recipient/legal requirements;
- research/brief preparation can be separated from sending;
- user-authorized one-to-one or operational communications remain subject to the current service terms and connector permissions.

## Data / privacy

Rerun currently states:
- Cloud Mode customer content is processed by Reunit SA as processor under its DPA;
- core infrastructure is EU-hosted;
- a dedicated virtual machine is used per Box in cloud mode;
- connected-service secrets are not stored in Rerun's database;
- self-hosted mode is described for customer infrastructure, with Enterprise/custom infrastructure references.

Before client production use:
- inspect current Privacy Policy + DPA + subprocessor list;
- classify personal/sensitive data;
- establish controller/processor roles;
- verify retention/deletion;
- verify whether Cloud, dedicated or self-hosted deployment is actually available under the selected contract;
- avoid special-category personal data unless there is a clear lawful basis and explicit project approval.

## Commercial / client delivery

Rerun currently advertises an Expert Program and template marketplace.

Treat current revenue-share, marketplace, pricing and expert benefits as volatile commercial terms. Reverify them before:
- client proposals;
- recurring-revenue calculations;
- marketplace publication;
- margin/pricing commitments.

Rerun is a potential deployment and distribution channel for Vinterro Digital, not an assumed revenue source.

## Completion / verification

A Rerun deployment is VERIFIED only when:
- the exact agent mission/instructions are versioned or otherwise recoverable;
- connector scopes were inspected;
- approvals match the Ercan OS risk policy;
- scheduled/triggered run actually fired;
- action/output evidence was inspected;
- client/project isolation is correct;
- sensitive data handling is documented;
- external side effects were independently confirmed;
- fallback/retry behavior is understood;
- current service terms/pricing/limits were checked when material;
- handoff and rollback/export path are documented.

Final state: VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED.
