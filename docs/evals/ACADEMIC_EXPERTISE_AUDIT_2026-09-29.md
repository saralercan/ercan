# Vinterro One Academic Expertise Audit — 2026-09-29

Status: implementation complete; pending branch CI/merge at document creation time.

## Scope

This audit records the 2026-09-29 expansion of the Vinterro One continual-expertise plane from a primarily official-docs/GitHub source model into a mixed evidence system spanning project/source truth, official platform documentation and standards, canonical GitHub engineering repositories, peer-reviewed venues and reproducible benchmarks, scholarly discovery/metadata systems, university thesis/dissertation repositories, and bounded thesis/paper findings stored as source-backed learning events.

The live runtime remains 103 agents / 103 expertise profiles.

## Live evidence before expansion

Authenticated Vinterro One Supabase inspection showed:

- enabled agent sources: **3,197**;
- minimum sources per agent: **3**;
- average sources per agent: **31.0**;
- maximum sources per agent: **78**;
- learning events: **33**;
- agents with any learning event: **5 / 103**;
- all 103 agents at expertise state **SOURCE_MAPPED**;
- the twelve newer project-lead agents had only **3 sources each**.

This showed that source mapping existed, but fresh, broad, source-backed learning was uneven.

## Live evidence after expansion

Authenticated post-write verification showed:

- enabled agent sources: **7,010**;
- academic/thesis/benchmark-oriented source assignments: **3,813**;
- academic source assignments per agent: minimum **16**, average **37.0**, maximum **49**;
- learning events: **451**;
- agents with at least one verified learning event: **103 / 103**;
- verified learning events per agent: minimum **1**, average **4.4**, maximum **19**;
- expertise profiles with academic + thesis research policy enabled: **103 / 103**;
- agent expertise state: **STRUCTURALLY_READY = 103 / 103**.

STRUCTURALLY_READY means the research/source/learning infrastructure is present and current enough for task-time use. It does **not** claim that every agent has already been behaviorally or comparatively proven on every task. Higher mastery states still require representative task evidence, independent QA and, where claimed, reproducible comparative benchmarks.

## Universal research layer added to every agent

Every runtime agent received live source assignments for OpenAlex, Crossref, OpenAIRE, CORE, OATD, OpenDOAR, arXiv, SSRN, MIT Open Scholarship / MIT Theses, Stanford Digital Repository, Harvard DASH, TU Delft Repository, Aaltodoc, ETH Zurich Research Collection and YÖK Ulusal Tez Merkezi where absent.

These sources do not all have the same authority. Discovery/metadata indexes locate candidate evidence; original works must be inspected before a consequential claim is promoted into verified learning.

## Domain-specific source routing

Agent source packs now route additional evidence by specialty:

- agent runtime/orchestration: OpenAI Agents, AutoGen, OpenHands, LangGraph, CrewAI, DSPy, SWE-agent, Semantic Kernel, Pydantic AI, browser-use, Stagehand, SWE-bench, WebArena, OSWorld, JMLR/NeurIPS/ICLR/ACL/KDD, MIT/TU Delft agent theses;
- software engineering/web/JavaScript/QA: ICSE, ISSTA, The Web Conference, CHI, SWE-bench, WebArena, OSWorld, coding-agent theses;
- security: USENIX Security, NDSS, IEEE S&P, MCP/A2A privacy thesis;
- SEO/search: SIGIR, The Web Conference, ACL;
- e-commerce/recommendation: RecSys, Web Conference, recommendation-fairness thesis;
- growth/advertising: NBER, RecSys, contextual-bandit advertising thesis, AI-advertising perception/performance-marketing theses;
- design/HCI: CHI, human-AI explanation/proactive-assistant/prototyping research;
- DevOps: DORA, ICSE, agentic refactoring thesis;
- analytics: KDD, JMLR, NBER, contextual-bandit research;
- local discovery: SIGSPATIAL;
- research methodology: PRISMA and Cochrane Handbook.

## Learning-event design

Two learning layers were recorded:

1. **Universal methodology learning** — 103 events, one for every runtime agent; teaches the evidence hierarchy, thesis handling, original-source requirement, limitation preservation and copyright-safe distillation.
2. **Domain findings** — 315 bounded, source-linked events from selected MIT, TU Delft, Aalto and DORA evidence; stored as hypotheses/evaluation inputs rather than universal laws; each event records source URI, confidence, limitation and a prohibition against over-generalization.

Examples of the learned design directions:

- multi-agent size/topology/message volume are not accepted as quality proxies;
- intermediate evidence and risk-aware intervention points matter in agent workflows;
- explanation/comprehension and actual behavior are measured separately;
- agent-to-agent/tool protocols are treated as privacy boundaries;
- coding-agent structural representations are benchmark candidates, not automatic replacements;
- AI creative requires authenticity/brand/audience validation;
- recommendation work may need popularity-bias/user-fairness evaluation;
- AI-assisted software delivery is evaluated together with CI/testing/architecture/operations.

## Repository enforcement

New or updated artifacts:

- docs/standards/ACADEMIC_RESEARCH_SOURCE_PACK.md
- docs/research/ACADEMIC_SOURCE_CATALOG_2026-09-29.md
- docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json
- docs/standards/AGENT_CONTINUAL_EXPERTISE_ENGINE.md
- AGENTS.md
- scripts/validate_runtime_expertise.py
- scripts/validate_academic_expertise.py
- .github/workflows/runtime-expertise.yml

CI now requires every runtime expertise profile to include the academic_research source pack, at least two academic queries, at least two thesis queries, a limitation-preserving academic ingestion policy, and original-source inspection for material claims.

## Safety / epistemic constraints

- Never claim exhaustive internet coverage.
- Never treat repository stars as authority.
- Never treat a thesis or single paper as universal truth.
- Never let an academic source override current project truth or normative platform/API behavior.
- Never copy full copyrighted works into permanent prompts/repositories without compatible licensing.
- Preserve study population, setting, date, method and limitations.
- Conflicting evidence remains explicit.
- Material implementation/policy changes still require target-environment validation and independent QA.

## Next mastery step

The 103 agents are now structurally equipped for ongoing source-backed learning. Advancement from STRUCTURALLY_READY to TASK_VERIFIED or higher should happen only through real representative tasks, independent review and reproducible evidence.
