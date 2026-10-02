---
name: multilingual-localization-specialists
description: Route human-language work to Vinterro One's English, Bulgarian, Spanish, Greek, German and French localization specialists plus independent multilingual QA. Trigger on translation, localization, multilingual copy, target-market adaptation, outreach/email localization, language proofreading, terminology work, or requests naming these languages.
---

# Multilingual Localization Specialists

Load:
- `docs/standards/MULTILINGUAL_LOCALIZATION_AGENT_STANDARD.md`
- `docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md`
- current project `AGENTS.md`
- the producing language specialist's expertise profile
- project/client glossary and canonical source text when available

## Routing

Activate only the languages materially required by the task:

- English -> English Language & Localization Specialist
- Bulgarian -> Bulgarian Language & Localization Specialist
- Spanish -> Spanish Language & Localization Specialist
- Greek -> Greek Language & Localization Specialist
- German -> German Language & Localization Specialist
- French -> French Language & Localization Specialist

For a multilingual deliverable, activate each required language specialist. For material customer-facing/public output, also activate Multilingual Localization QA Auditor.

The existing `Language Freshness Agent` concerns programming/framework language versions; it does **not** replace human-language localization specialists.

## Required behavior

1. Freeze source facts/claims before localization.
2. Resolve locale, audience and register from context.
3. Use document/thread context when available.
4. Enforce glossary and terminology consistency.
5. Localize naturally; do not translate literally where it damages fluency or intent.
6. Preserve numbers, names, URLs, prices, offers, negation, placeholders and markup exactly unless the task explicitly changes them.
7. Separate language accuracy from cultural/pragmatic adaptation.
8. Never invent prospect-specific observations, guarantees, prices or availability.
9. Route final material text to independent multilingual QA.
10. Record verified reusable learning with provenance through Vinterro One continual-expertise mechanisms when available.

## Commercial mail

For Vinterro Digital email/outreach, this skill is a language lane only. It does not replace:
- `docs/standards/VINTERRO_MAIL_AGENT.md`
- canonical mail HTML/template
- account-level dedupe and send-idempotency gates
- MailQA / delivery evidence

Content Agent/TextAgent owns the source commercial message; the target-language specialist localizes it; Multilingual Localization QA Auditor checks it; MailAgent owns send/dedupe truth.

## Completion

Do not claim a target is VERIFIED until:
- source invariants pass,
- required locale/register is resolved,
- no CRITICAL/MAJOR QA findings remain,
- independent review is evidenced for material output.
