# Provider Scan — Rerun

Date: 2026-09-24
Provider: https://rerun.build/
Operator: Reunit SA (Luxembourg), per current Privacy Policy.

## Product shape

Rerun currently presents itself as a managed AI-agent operations platform for recurring business tasks.

Public materials describe:
- natural-language agent setup;
- scheduled/event-triggered execution;
- private cloud "Boxes";
- live dashboard/run visibility;
- human approval before sensitive actions;
- broad app integrations plus MCP/API;
- bring-your-own AI subscription/API/local model;
- agent/skill library;
- client/expert marketplace/distribution options.

Decision:
`ADOPT_WHEN_NEEDED / MANAGED_AGENT_DEPLOYMENT_PROVIDER / CLOSED_SOURCE_SAAS`.

## Architecture fit

Rerun should not replace Ercan OS routing, skill standards, project rules or QA.

Best fit:
`Ercan OS control plane -> Rerun managed execution/deployment -> client/operator dashboard + approvals -> independent Ercan OS verification`.

This is especially relevant for non-technical client handoff and always-on recurring business operations.

## Security / privacy evidence

Current Privacy Policy and DPA state:
- Cloud Mode customer content is processed by Reunit SA as processor;
- core infrastructure is hosted in the EU;
- one dedicated virtual machine per Box is described;
- connected-service secrets/credentials are not stored in Rerun's database;
- Google API access uses narrow scopes;
- self-hosted mode is described for customer infrastructure;
- Enterprise advertises custom infrastructure.

These are provider statements and contractual documents, not independent security certification.

## Gmail scope finding

Current Privacy Policy explicitly states:
- Gmail: sending only;
- Rerun cannot read, search or list the mailbox.

This conflicts with any broad interpretation of marketing phrases such as inbox sorting/reply automation. Therefore Ercan OS must inspect the exact current trigger/connector mechanism before routing inbound Gmail workflows.

## Approval model

The public product surface shows "Allow once / This session / Always / Deny" style approval controls for sensitive actions.

Use this as an execution gate beneath Ercan OS risk policy.

## AUP finding — outreach

Current Acceptable Use Policy prohibits bulk unsolicited email, messages or calls.

Therefore Rerun is not approved as the transport for Vinterro's bulk cold outreach workflow.

It may still be considered for:
- research;
- lead briefs;
- scoring;
- drafting;
- compliant operational/customer communication;
subject to current terms and legal/project rules.

## Pricing / packaging

Current public pricing advertises a base plan from $24/month with agents, one Box, seat, model credit, broad integrations and unlimited executions, plus a 7-day trial.

Treat all quantities/prices/features as volatile and verify before purchase/proposal.

## Expert Program

Current Expert Program marketing advertises:
- directory/client matching;
- a Box for building/demo;
- agent template marketplace;
- creator revenue share;
- recurring referral/client-plan share.

These are commercial terms, not guaranteed income. Before Vinterro Digital uses the channel, review current program/marketplace terms, payout availability, IP terms, support obligations and customer/data responsibilities.

## Adoption boundary

Adopt Rerun as:
- managed deployment/runtime option;
- client handoff surface;
- approvals/live-run visibility layer;
- possible distribution channel.

Do not adopt it as:
- Ercan OS policy authority;
- mandatory dependency;
- default platform for every automation;
- bulk cold-outreach transport;
- proof of task completion;
- substitute for project-level data/connector/legal review.
