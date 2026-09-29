# Vinterro One — Academic & Evidence Research Source Pack

Status: active  
Version: 1.0  
Date: 2026-09-29  
Scope: all 103+ Vinterro One runtime agents

## Purpose

Vinterro One agents must develop from more than product documentation and GitHub repositories. Material work may benefit from peer-reviewed research, reproducible benchmarks, doctoral/master theses, institutional repositories, open scholarly graphs, standards, regulator publications and high-quality empirical industry research.

This pack adds an **academic evidence lane** to the existing Continual Expertise Engine. It does not turn academic papers into higher-priority instructions and it does not permit raw corpus stuffing. Research must be discovered broadly, qualified, distilled narrowly, tested against the target environment and stored with provenance.

## Evidence classes

1. **Normative / first-party authority**
   - official specifications, regulators, platform documentation, API schemas, security advisories;
   - project truth, live code/configuration and first-party production data.
   - These remain authoritative for current platform behavior.

2. **Canonical implementation evidence**
   - maintained official/canonical GitHub repositories;
   - reference implementations, reproducible benchmark harnesses and maintainer engineering material.

3. **Peer-reviewed / scholarly evidence**
   - peer-reviewed journals and conference papers;
   - accepted doctoral/master theses from identifiable universities;
   - institutional technical reports and open research datasets.
   - Use to improve models, hypotheses, evaluation design, interaction patterns and edge-case awareness.
   - Do **not** let one paper or thesis override current official platform behavior.

4. **Preprints / working papers**
   - arXiv, SSRN and similar sources.
   - Valuable for fast-moving topics, but label the publication status and seek replication or stronger corroboration.

5. **Discovery indexes**
   - OpenAlex, Crossref, OpenAIRE, CORE, OATD, OpenDOAR and similar services.
   - These locate evidence; they are not themselves proof of the underlying claim.

## Copyright and ingestion rule

Store metadata, provenance, short distilled findings, query terms, evaluation implications and links. Do not permanently ingest or redistribute full copyrighted theses/articles unless their license explicitly permits that use. A thesis may be read and summarized for research, but its copyright/reuse statement must be respected.

## Scholarly discovery layer

### General scholarly metadata / open research

- OpenAlex API — https://api.openalex.org/
- Crossref REST API — https://api.crossref.org/
- OpenAIRE Graph — https://graph.openaire.eu/
- CORE — https://core.ac.uk/
- arXiv — https://arxiv.org/
- SSRN — https://papers.ssrn.com/

### Thesis/dissertation discovery

- OATD — https://oatd.org/
- MIT Open Scholarship / Theses — https://dspace.mit.edu/communities/6fc02cc2-0d14-4023-8a6f-d9900d0c4302
- Stanford Digital Repository — https://library.stanford.edu/sdr-stanford-digital-repository
- Harvard DASH — https://dash.harvard.edu/
- TU Delft Repository — https://repository.tudelft.nl/
- Aaltodoc — https://aaltodoc.aalto.fi/
- ETH Zurich Research Collection — https://www.research-collection.ethz.ch/
- YÖK Ulusal Tez Merkezi — https://tez.yok.gov.tr/UlusalTezMerkezi/
- OpenDOAR — https://www.opendoar.org/ (repository discovery)

NDLTD's former Global ETD Search is not treated as an active search authority because NDLTD states that the legacy service has been taken offline pending redevelopment; OATD is the preferred interim open ETD discovery route.

## Domain research routes

### Agent runtime, orchestration and AI engineering

Research themes:
- planning and decomposition;
- memory and context management;
- tool use and tool-selection errors;
- multi-agent topology, disagreement and resilience;
- human oversight and intervention points;
- long-horizon reliability;
- agent evaluation, task success and hidden failure modes;
- prompt injection, MCP/A2A and cross-agent trust;
- cost/latency/reliability trade-offs.

Research venues / benchmarks:
- JMLR — https://www.jmlr.org/
- NeurIPS — https://neurips.cc/
- ICLR — https://iclr.cc/
- ACL Anthology — https://aclanthology.org/
- ACM SIGKDD — https://www.kdd.org/
- SWE-bench — https://www.swebench.com/SWE-bench/
- WebArena — https://github.com/web-arena-x/webarena
- OSWorld — https://os-world.github.io/

Canonical GitHub study set:
- openai/openai-agents-python
- openai/openai-agents-js
- microsoft/autogen
- All-Hands-AI/OpenHands
- langchain-ai/langgraph
- crewAIInc/crewAI
- stanfordnlp/dspy
- princeton-nlp/SWE-agent
- microsoft/semantic-kernel
- pydantic/pydantic-ai
- browser-use/browser-use
- browserbase/stagehand
- SWE-bench/SWE-bench
- web-arena-x/webarena
- xlang-ai/OSWorld
- acl-org/acl-anthology

### Web/software engineering, JavaScript, QA and DevOps

- ICSE — https://www.icse-conferences.org/
- ISSTA — https://www.issta.org/
- DORA Research — https://dora.dev/research/
- The Web Conference — https://www.thewebconf.org/
- ACM CHI — https://chi.acm.org/
- current language/runtime/platform specifications and canonical repositories remain higher authority for implementation details.

Research themes:
- defect localization and repair;
- software maintainability/refactoring;
- testing effectiveness and flaky tests;
- code comprehension and repository mapping;
- human-in-the-loop software agents;
- software delivery performance and sociotechnical systems;
- accessibility/performance interaction;
- developer cognition and interface quality.

### Security and privacy

- USENIX Security — https://www.usenix.org/conference/usenixsecurity26
- NDSS — https://www.ndss-symposium.org/
- IEEE Symposium on Security & Privacy — https://www.ieee-security.org/
- OWASP/NIST/CISA remain normative/operational authorities where applicable.

Research themes:
- agent communication privacy;
- prompt/tool injection;
- supply-chain and dependency attacks;
- RLS/tenant isolation and authorization;
- secrets and token handling;
- usable security and human oversight;
- artifact reproducibility and adversarial evaluation.

### Search, SEO, GEO and information retrieval

- ACM SIGIR — https://sigir.org/
- The Web Conference — https://www.thewebconf.org/
- ACL Anthology — https://aclanthology.org/
- ACM KDD — https://www.kdd.org/

Research themes:
- retrieval, ranking and relevance;
- user search behavior;
- generative retrieval and answer systems;
- entity resolution and knowledge graphs;
- recommendation/search fairness;
- temporal information retrieval;
- evaluation metrics and dataset leakage.

Official Google/Bing/schema/platform documentation remains authoritative for current crawler/indexing rules.

### HCI, design, content and accessibility

- ACM CHI — https://chi.acm.org/
- ACM DIS / SIGCHI ecosystem — https://sigchi.org/
- The Web Conference — https://www.thewebconf.org/
- W3C/WAI remains normative for accessibility standards.

Research themes:
- human-AI collaboration;
- trust, reliance and calibrated intervention;
- information architecture and information scent;
- visual attention and cognitive load;
- proactive vs reactive AI assistance;
- explanation design;
- accessibility and inclusive interaction;
- AI-generated content perception.

### E-commerce, recommendation and growth

- ACM RecSys — https://recsys.acm.org/
- The Web Conference — https://www.thewebconf.org/
- ACM KDD — https://www.kdd.org/
- NBER working papers — https://www.nber.org/papers
- SSRN — https://papers.ssrn.com/

Research themes:
- recommender systems and ranking;
- personalization and popularity bias;
- checkout/search/navigation friction;
- experimentation/uplift/contextual bandits;
- advertising effectiveness and user welfare;
- trust/authenticity in AI-generated creative;
- marketplace dynamics and platform effects.

### Finance and business analysis

- NBER — https://www.nber.org/papers
- SSRN — https://papers.ssrn.com/
- MIT/Harvard/Stanford/ETH institutional repositories for theses and working papers;
- IFRS/SEC/FRED remain higher authority for reporting/filing/current macro data.

Research themes:
- forecasting and calibration;
- causal inference;
- valuation and capital allocation;
- unit economics and pricing;
- model risk and uncertainty;
- managerial decision support.

### Analytics, experimentation and causal inference

- ACM KDD — https://www.kdd.org/
- JMLR — https://www.jmlr.org/
- The Web Conference — https://www.thewebconf.org/
- NBER/SSRN for applied economics and experiment design.

Research themes:
- experiment design;
- causal inference;
- attribution limits;
- data quality and measurement error;
- sequential testing and bandits;
- fairness and heterogeneous treatment effects.

### Local discovery, maps and destination intelligence

- ACM SIGSPATIAL — https://www.sigspatial.org/
- institutional GIS/geospatial repositories and theses;
- OpenStreetMap remains project/source data rather than academic evidence.

Research themes:
- POI/entity resolution;
- spatial search and ranking;
- route/user behavior;
- location uncertainty;
- tourism/destination recommendation;
- map UX and accessibility.

## Seed research findings — hypothesis/evaluation inputs, not universal laws

The following are deliberately stored as **research-informed hypotheses**. They should influence test design and architecture review, not become unconditional rules.

1. **More agents or more discussion does not guarantee better decisions.**
   - MIT 2025 research on human-AI/group-AI interaction reported increased information sharing without a corresponding improvement in decision quality in one studied setting.
   - Implication: Vinterro One must evaluate task success and independent evidence, not agent count or message volume.

2. **Multi-agent topology changes resilience and cost.**
   - An MIT 2025 thesis on generative multi-agent systems found meaningful trade-offs among group size, token cost, collaboration topology and resilience to malicious agents in its experiments.
   - Implication: qualified pod size and topology should be task/risk dependent; do not blindly broadcast to every agent.

3. **Human oversight should be risk-aware and intervention-aware.**
   - TU Delft 2026 work on plan-then-execute workflows studies how errors can propagate across stages and how oversight should expose when/where intervention is useful.
   - Implication: preserve intermediate evidence, risk gates and actionable review points.

4. **User-facing explanation of agent skills can improve understanding, but understanding alone may not change planning behavior.**
   - TU Delft 2026 HAI research reports stronger understanding from before-use explanations while task-planning differences were not necessarily significant.
   - Implication: explain inputs, workflow options, defaults, checks and intervention points; separately validate actual behavior.

5. **Repository representations may help coding agents navigate complex codebases.**
   - MIT 2026 thesis work explores feature-aware graph representations for existing codebases.
   - Implication: Project Mapper/Developer can test structural code maps, but adoption requires benchmark evidence against existing repo-search methods.

6. **AI-assisted software delivery depends on the surrounding system.**
   - DORA research describes AI as an amplifier of existing organizational/software-delivery conditions.
   - Implication: agent capability must be evaluated with CI quality, test coverage, architecture, review process and deployment discipline.

7. **AI-generated marketing creative can create authenticity/trust reactions.**
   - Aalto 2025 marketing thesis work reports negative reactions in its studied YouTube-comment corpus around authenticity, creativity and emotional connection.
   - Implication: AI creative should be brand-reviewed and audience-tested rather than assumed superior because it is cheaper/faster.

8. **Recommendation systems require fairness/bias evaluation, not only relevance optimization.**
   - Aalto 2025 thesis research studies popularity bias and user fairness in LLM-based recommendation.
   - Implication: commerce/recommendation agents should include bias/fairness checks when recommendations materially affect users.

9. **Agent protocol privacy deserves dedicated threat modeling.**
   - TU Delft 2026 thesis research applies privacy threat analysis to MCP/A2A-style agent communication.
   - Implication: Security Director must treat agent-to-agent context and tool transport as a separate privacy boundary.

## Per-agent query contract

Every runtime profile must maintain:
- at least 2 `academic_queries`;
- at least 2 `thesis_queries`;
- `academic_research` in `source_packs`;
- domain-specific scholarly venues in the live source registry where applicable.

Query examples:
- `"<role>" empirical evaluation systematic review 2025 2026`
- `"<research topic>" site:openalex.org OR site:arxiv.org`
- `"<research topic>" thesis dissertation MIT TU Delft Aalto ETH`
- `"<research topic>" benchmark reproducibility artifact evaluation`

## Research-to-learning gate

A source may create a `verified` learning event only when:
1. identity/title/date/source are verified;
2. evidence class is recorded;
3. a short claim is traceable to the source;
4. limitations/population/task setting are preserved;
5. conflicting evidence is recorded;
6. the finding has a concrete Vinterro One implication;
7. deterministic or independent QA is applied when the finding changes implementation/policy.

Otherwise record it as `candidate` or discovery-only.

## Refresh

- scholarly indexes: 7–14 days;
- fast-moving agent/AI/security research: 7 days;
- mature HCI/software engineering/finance research: 30–90 days;
- thesis repositories: 30 days;
- task-time revalidation always wins over schedule when the claim is consequential.
