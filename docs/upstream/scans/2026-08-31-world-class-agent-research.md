# Research Scan — 2026-08-31 World-Class Agent Program

Status: reviewed evidence record
Scope: upgrade all 21 stable Ercan OS agents with current GitHub, official standards/platform documentation, university/lab benchmarks, peer-reviewed research methodology and continuous re-certification.

No third-party community code was installed or executed. No production credentials were used.

## Core finding

The best way to improve agent quality is not to copy an unbounded amount of internet text into prompts. High-quality agent systems require current primary-source retrieval, narrow JIT context, outcome-based evaluation, adversarial regression tests, reproducible benchmarks and a feedback loop from real failures.

## Academic / university benchmark evidence

### SWE-bench / Princeton-origin software engineering benchmark
- Real-world GitHub issue resolution benchmark; ICLR 2024 publication and maintained evaluation harness.
- SWE-bench Verified adds curated/verified tasks; Multimodal extends evaluation to visual software domains.
- Operational lesson: coding expertise should be measured by repository outcome/tests, not plausible code generation.
- Sources: https://www.swebench.com/ ; https://github.com/SWE-bench/SWE-bench ; https://openreview.net/forum?id=VTF8yNQM66

### Berkeley Function Calling Leaderboard (UC Berkeley)
- Evaluates function/tool calling across single, parallel, multi-turn and agentic settings, including relevance/irrelevance and web-search/memory dimensions.
- Operational lesson: Ercan OS must test correct tool selection/arguments/abstention and multi-turn recovery, not merely answer quality.
- Source: https://gorilla.cs.berkeley.edu/leaderboard.html

### Stanford CRFM HELM / HEIM
- HELM emphasizes holistic, reproducible and transparent evaluation across multiple metrics rather than a single score.
- HEIM applies multi-dimensional evaluation to text-to-image systems and reports that automated metrics correlate weakly with several human-rated aesthetic/photorealism dimensions.
- Operational lesson: creative-agent quality requires structured human review; agent quality needs multi-dimensional evaluation.
- Sources: https://crfm.stanford.edu/helm/ ; https://github.com/stanford-crfm/helm ; https://crfm.stanford.edu/helm/heim/latest/

### Browser/GUI research family
- WebArena/Mind2Web/ScreenSpot/BrowserGym-class research provides useful methodology for realistic web navigation and GUI-grounding evaluation.
- Operational lesson: screenshot/browser agents need outcome/state checks and visual/interaction evaluation, not screenshot generation alone.
- Decision: research/benchmark reference; pin canonical versions before any executable adoption.

## Standards and public-interest engineering evidence

### W3C WCAG 2.2
- W3C Recommendation with testable accessibility criteria.
- Operational lesson: accessibility is a cross-agent production requirement for web/UI work and requires manual plus automated verification.
- Source: https://www.w3.org/TR/WCAG22/

### W3C Design Tokens Community Group 2025.10 stable specification
- Stable vendor-neutral token format with theming, aliases and cross-tool/platform goals.
- Operational lesson: Creative/Design System experts should prefer interoperable token sources of truth over ad hoc duplicated values.
- Sources: https://www.w3.org/community/design-tokens/ ; https://www.designtokens.org/

### NIST SSDF
- Secure Software Development Framework for integrating secure-development practices into SDLC.
- Operational lesson: security and upstream adoption should include process/provenance controls, not only vulnerability scanning.
- Source: https://csrc.nist.gov/Projects/ssdf

### OWASP ASVS / WSTG
- Application security verification and web security testing frameworks.
- Operational lesson: SecurityExpert/ProductionQA need requirement-mapped security checks and authorized testing methodology.
- Sources: https://owasp.org/www-project-application-security-verification-standard/ ; https://owasp.org/www-project-web-security-testing-guide/

### OpenSSF / SLSA
- Open-source security posture and software-artifact provenance/build-integrity guidance.
- Operational lesson: UpstreamIntelligence should assess repository/build provenance and supply-chain controls in addition to popularity/maintenance.
- Sources: https://scorecard.dev/ ; https://slsa.dev/

## Current platform/agent evidence retained

### Shopify
- `Shopify/Shopify-AI-Toolkit` is the canonical agent-training/developer context source; provides docs/schema lookup and validation.
- Source: https://github.com/Shopify/Shopify-AI-Toolkit

### WordPress
- `WordPress/agent-skills` explicitly targets common AI assistant failures such as outdated pre-Gutenberg patterns and missed security concerns, and includes an eval harness.
- Source: https://github.com/WordPress/agent-skills

### Wix
- `wix/skills` remains official experimental Agent Skills; current dev.wix.com docs remain runtime authority.
- Source: https://github.com/wix/skills

### MCP
- MCP 2026-07-28 introduces a stateless core, header routing, cacheable lists, authorization hardening, extensions and updated SDKs.
- Operational lesson: AgentMCPExpert must re-check current protocol/version and deprecations rather than use old session assumptions.
- Sources: https://blog.modelcontextprotocol.io/posts/2026-07-28/ ; https://github.com/modelcontextprotocol/modelcontextprotocol

## Search / performance / UX evidence

### Google / Core Web Vitals
- Current Core Web Vitals focus on LCP, INP and CLS and emphasize p75 field measurement; lab measurements are diagnostic and do not replace field data.
- Operational lesson: PerformanceExpert must distinguish field and lab evidence.
- Source: https://web.dev/articles/vitals

### Search
- Google Search Central/Search Essentials and Schema.org remain primary sources for search eligibility/structured data; rankings are not guaranteed by compliance.
- Sources: https://developers.google.com/search/docs/essentials ; https://schema.org/

### UX
- Nielsen Norman Group usability heuristics/research methods are useful high-quality practitioner evidence, but real user research remains stronger for a specific product population.
- Source: https://www.nngroup.com/articles/

## New Ercan OS artifacts created

- `docs/standards/WORLD_CLASS_AGENT_RESEARCH.md`
- `docs/research/AGENT_SOURCE_PACKS.md`
- `docs/evals/WORLD_CLASS_AGENT_BENCHMARK_SUITE.md`
- `.agents/skills/expert-research-refresh/SKILL.md`
- stable-core and Codex routing integration

## Final decision

**ADOPT AS CORE OPERATING SYSTEM LAYER.**

World-class is a target demonstrated by evidence, not a permanent label. The stable core must continuously refresh evidence and re-certify after material failures/platform changes. Do not promise perfection or completeness of the entire internet; instead maintain broad discovery + narrow authoritative JIT research + reproducible evaluation.
