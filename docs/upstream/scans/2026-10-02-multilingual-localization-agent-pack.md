# 2026-10-02 — Multilingual Localization Agent Pack Research Scan

Scope: English, Bulgarian, Spanish, Greek, German and French localization agents for Vinterro One.

## Research method

High-recall discovery was performed across current official language/style resources, ACL/WMT peer-reviewed research, university theses/dissertations and canonical GitHub repositories. Sources were reduced to an operational curriculum rather than copied into prompts.

This is deliberately **not** an unbounded claim that every internet page or thesis was read. Vinterro One's expertise policy requires broad discovery followed by authority-weighted, task-relevant ingestion and verification.

## High-value academic evidence

- Guerreiro et al. (TACL 2024), **xCOMET: Transparent Machine Translation Evaluation through Fine-grained Error Detection** — sentence-level evaluation plus categorized error spans and stress tests for critical errors/hallucinations. https://aclanthology.org/2024.tacl-1.54/
- Kocmi et al. (WMT 2025), **Findings of the WMT25 General Machine Translation Shared Task: Time to Stop Evaluating on Easy Test Sets** — harder professional test sets, ESA/MQM human evaluation and increasing document-level translation. https://aclanthology.org/2025.wmt-1.22/
- Havaldar et al. (ACL 2025), **Towards Style Alignment in Cross-Cultural Translation** — cultural/style misalignment and politeness loss; motivates an explicit pragmatic/style QA pass. https://aclanthology.org/2025.acl-long.1550/
- Yao et al. (EMNLP 2024 Findings), **Benchmarking Machine Translation with Cultural Awareness** — pragmatic quality for culture-specific items; motivates culture-aware evaluation separate from grammar. https://aclanthology.org/2024.findings-emnlp.765/
- University of Surrey PhD (2026), **Quality Estimation for Machine Translation in Low-Resource Settings** — multilingual transfer, QE and limits of zero-shot/in-context LLM quality estimation. https://openresearch.surrey.ac.uk/esploro/outputs/doctoral/Quality-Estimation-for-Machine-Translation-in/991146796302346
- Current academic source discovery also included thesis/dissertation repositories in the Vinterro `academic_research` pack (OpenAlex, Crossref, OpenAIRE, CORE, OATD, MIT, Stanford, Harvard, TU Delft, Aalto, ETH, YÖK).

## Current language/locale authority sources

Common:
- EU Interinstitutional Style Guide — https://style-guide.europa.eu/
- IATE EU terminology — https://iate.europa.eu/
- W3C Internationalization — https://www.w3.org/International/
- Unicode CLDR — https://cldr.unicode.org/
- Microsoft Globalization — https://learn.microsoft.com/globalization/

Language-specific:
- English: EU style guidance + target-project UK/US conventions.
- Bulgarian: Institute for Bulgarian Language, Bulgarian Academy of Sciences — https://ibl.bas.bg/ ; EU/IATE terminology.
- Spanish: Real Academia Española / ASALE — https://www.rae.es/ and https://www.rae.es/dpd/
- Greek: Centre for the Greek Language — https://www.greek-language.gr/
- German: Rat für deutsche Rechtschreibung, 2024 official rules — https://www.rechtschreibrat.com/DOX/RfdR_Amtliches-Regelwerk_2024.pdf
- French: FranceTerme — https://www.culture.fr/franceterme ; Dictionnaire de l’Académie française — https://www.dictionnaire-academie.fr/

## Canonical GitHub evidence checked

- Unbabel/COMET — active neural MT evaluation framework.
- google-research/mt-metrics-eval — active WMT metric-evaluation tooling.
- mjpost/sacrebleu — active reproducible MT evaluation tooling.
- Helsinki-NLP/OPUS-MT-train — active open MT training pipeline.
- unicode-org/cldr — active locale-data repository.
- w3c/i18n-drafts — active W3C internationalization drafts repository.
- facebookresearch/flores was checked and is archived; it may remain historical benchmark evidence but is not current implementation authority.

## Operational lessons promoted into the agent standard

1. Evaluate error spans/categories, not only one aggregate “quality” score.
2. Use document/thread context for professional translation.
3. Separate semantic accuracy, terminology, style/register and cultural/pragmatic alignment.
4. Preserve factual invariants before stylistic adaptation.
5. Resolve locale and forms of address explicitly.
6. Maintain project/client terminology and test terminology consistency.
7. Require an independent linguistic QA identity for material output.
8. Escalate high-stakes certified translation to qualified human/domain review.
9. Treat archived benchmarks as historical evidence, not maintained implementation guidance.
10. Re-check volatile language/style/terminology sources on task entry and periodic refresh.
