---
name: portable-agent-router
description: Route Vinterro One tasks to the complete materially relevant expert pod across Codex/OpenAI, Claude and the native Vinterro One runtime. Trigger on "ajanları çalıştır", "tüm ajanları çalıştır", multi-domain work, specialist selection, and Vinterro Digital mail/outreach tasks that require the canonical MailAgent contract.
---

# Portable Agent Router

Load the repository's Vinterro runtime manifest, portable-runtime standard and task-relevant domain skills only.

## Required behavior

1. Parse the current task, project, execution surface, risk and required evidence.
2. Treat every runtime agent as STANDBY by default.
3. Select the complete non-redundant ACTIVE pod of specialists with a distinct material contribution; do not optimize for minimum headcount when broader expert coverage materially improves the task.
4. On the master trigger, **do not run every agent**. It means autonomous relevant-specialist routing.
5. Keep non-selected agents on STANDBY.
6. If a new need appears mid-task, activate/consult only the matching standby specialist.
7. Add independent QA/reviewer agents when the task reaches verification.
8. Respect agent permissions/handoffs and provider/tool availability.
9. Never report an agent/tool/action as executed unless the current runtime actually executed it.

## Selection priorities

Choose specialists by direct domain match, project ownership, source authority, required tools, risk boundary and independent verification need.

Prefer the complete non-redundant specialist pod. Independent workstreams should run in parallel when safe and supported; unrelated agents remain STANDBY.

## Vinterro Digital mail routing hard gate

Before any Vinterro Digital email/outreach/reply/example-mail task, load `.agents/skills/vinterro-mail-agent/SKILL.md` regardless of current working directory. That skill then requires `docs/standards/VINTERRO_MAIL_AGENT.md` and the exact source artifact `docs/standards/VINTERRO_MAIL_CANONICAL_TEMPLATE.html`.

Do not rely on generic `MAIL_ENGINEERING.md` alone for Vinterro Digital commercial mail. Do not reconstruct the HTML shell/signature from memory. If the canonical source artifact cannot be read, stop the render/send path as `BLOCKED`.

Route copy work through the Vinterro Text/Copy lane, delivery/dedupe through MailAgent/Outreach/Gmail, and visual/template compliance through independent MailQA. A draft is not send-ready until canonical template tokens and signature are verified.

## Human-language localization

For English, Bulgarian, Spanish, Greek, German or French translation/localization, load `.agents/skills/multilingual-localization-specialists/SKILL.md` and `docs/standards/MULTILINGUAL_LOCALIZATION_AGENT_STANDARD.md`.

Route each target language to its dedicated Language & Localization Specialist. Material customer-facing/public multilingual output additionally requires `Multilingual Localization QA Auditor` as an independent reviewer. The existing `Language Freshness Agent` is for programming/framework language freshness and does not replace human-language specialists.

For multilingual tasks, activate every target-language specialist materially required by the deliverable; do not collapse all languages into one generic translation lane.

## Finance

Use `Finance Expert Agent` for FP&A, budgeting, cash flow, margin/unit economics, forecasts, financial statements, scenario analysis and financial model review.

## E-commerce

Use `E-commerce Expert Agent` for cross-platform commerce, merchandising, checkout, payments, marketplace/feed, inventory, retention, CRO, analytics and unit-economics work. Add Shopify/WooCommerce/platform specialists only where needed.

## Escalation

When current evidence shows the initial pod is insufficient, record:
`STANDBY -> ACTIVE: <agent>, reason: <new need>`.

Never activate unrelated agents merely to satisfy the phrase "all agents".
