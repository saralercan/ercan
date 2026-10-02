# Multilingual Localization Regression Contract

Date: 2026-10-02
Status: active

This contract protects the six-language localization pod and independent linguistic QA.

## Structural checks

The runtime and expertise matrix must contain exactly one active global specialist for each target language plus the multilingual QA auditor. All must be JIT/STANDBY and portable to ChatGPT/OpenAI, Codex, Claude and Vinterro One.

Required names:
- English Language & Localization Specialist
- Bulgarian Language & Localization Specialist
- Spanish Language & Localization Specialist
- Greek Language & Localization Specialist
- German Language & Localization Specialist
- French Language & Localization Specialist
- Multilingual Localization QA Auditor

Every language specialist must hand off to Multilingual Localization QA Auditor. The QA auditor must be a distinct identity.

## Behavioral regression cases

1. **Factual freeze**: prices, dates, numbers, URLs, product names, negation and offer conditions survive translation unchanged.
2. **No invented claim**: source contains no “award-winning” claim; target must not add one.
3. **Document context**: pronouns/terms remain consistent across paragraphs.
4. **Terminology**: supplied glossary term is used consistently in all occurrences.
5. **English locale**: UK vs US spelling/date convention follows explicit project locale.
6. **Bulgarian**: formal business address and Cyrillic are preserved; transliteration occurs only when required.
7. **Spanish**: Spain/LatAm locale and tú/usted/vos are resolved from audience, not guessed from language alone.
8. **Greek**: Modern Greek business register and monotonic orthography remain natural; no needless transliteration.
9. **German**: Sie/du register is consistent; current official orthography is respected.
10. **French**: vous/tu and locale-appropriate typography are consistent.
11. **Markup safety**: HTML tags, liquid/handlebars placeholders, variables, SKUs and tracking URLs remain valid.
12. **Cross-cultural style**: politeness/directness is preserved without literal calques or cultural stereotyping.
13. **Independent QA**: producer cannot issue its own final linguistic PASS.
14. **Error span reporting**: QA can identify category + severity + offending span for seeded errors.
15. **High-stakes escalation**: legal/medical/regulated binding content triggers qualified-human/domain-review warning rather than unsupported certification.

## Pass rule

A material sample passes only with zero unresolved CRITICAL and zero unresolved MAJOR findings. Structural readiness alone is not evidence of native-quality behavioral mastery.
