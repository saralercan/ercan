---
name: portable-agent-router
description: Route any Vinterro One task to the smallest relevant expert pod across Codex/OpenAI, Claude and the native Vinterro One runtime. Trigger on "ajanları çalıştır", "tüm ajanları çalıştır", multi-domain work, or when a specialist must be selected.
---

# Portable Agent Router

Load the repository's Vinterro runtime manifest, portable-runtime standard and task-relevant domain skills only.

## Required behavior

1. Parse the current task, project, execution surface, risk and required evidence.
2. Treat every runtime agent as STANDBY by default.
3. Select the smallest sufficient ACTIVE pod from the canonical runtime manifest.
4. On the master trigger, **do not run every agent**. It means autonomous relevant-specialist routing.
5. Keep non-selected agents on STANDBY.
6. If a new need appears mid-task, activate/consult only the matching standby specialist.
7. Add independent QA/reviewer agents when the task reaches verification.
8. Respect agent permissions/handoffs and provider/tool availability.
9. Never report an agent/tool/action as executed unless the current runtime actually executed it.

## Selection priorities

Choose specialists by direct domain match, project ownership, source authority, required tools, risk boundary and independent verification need.

Prefer one strong owner plus a few material specialists over a large meeting.

## Finance

Use `Finance Expert Agent` for FP&A, budgeting, cash flow, margin/unit economics, forecasts, financial statements, scenario analysis and financial model review.

## E-commerce

Use `E-commerce Expert Agent` for cross-platform commerce, merchandising, checkout, payments, marketplace/feed, inventory, retention, CRO, analytics and unit-economics work. Add Shopify/WooCommerce/platform specialists only where needed.

## Escalation

When current evidence shows the initial pod is insufficient, record:
`STANDBY -> ACTIVE: <agent>, reason: <new need>`.

Never activate unrelated agents merely to satisfy the phrase "all agents".
