# Upstream Scan — Discovery Source Expansion

Date: 2026-09-24

## Purpose

Review five supplied high-recall GitHub sources and decide whether Ercan OS should treat them as production dependencies, task-scoped discovery indexes, research-only references or reject them.

Stable routing identities remain **21 Stable Core + 31 GitHub Specialist v3 Extension = 52**.

## 1. punkpeye/awesome-mcp-servers

Observed:
- public, non-archived repository;
- curated multilingual index of Model Context Protocol servers;
- entries span browsers, databases, SaaS APIs, local tools, cloud services, security tooling and many other capability areas;
- repository license observed: MIT.

Decision: **DISCOVERY_SOURCE / MCP_CATALOG**.

Use:
- discover candidate MCP servers when a project has a concrete integration gap;
- follow each candidate to its own canonical repository/docs;
- independently verify maintenance, publisher identity, transport, auth, permissions, network access, local command execution, package/install scripts and license.

Do not:
- install MCP servers directly from the catalog merely because they are listed;
- connect credentials before server audit;
- treat a remote MCP server as trustworthy because it appears in an awesome list;
- expose broad filesystem/shell/database write access without least-privilege review.

## 2. Shubhamsaboo/awesome-llm-apps

Observed:
- public, non-archived repository;
- collection of open-source agent, skill, RAG, voice and multi-agent application examples;
- README includes quick-install/clone-and-run examples;
- repository license observed: Apache-2.0;
- examples span low-risk demos and potentially sensitive/high-stakes domains.

Decision: **DISCOVERY_SOURCE / APP_PATTERN_LIBRARY**.

Use:
- discover implementation patterns, example application architecture, agent-skill patterns and RAG/voice/multi-agent reference projects;
- audit only the specific subproject needed.

Do not:
- clone/run the whole repository as a trusted bundle;
- inherit model/provider/API-key choices without current review;
- reuse high-stakes medical/financial/security behavior without domain-specific validation;
- treat project claims or screenshots as production evidence.

## 3. x1xhlol/system-prompts-and-models-of-ai-tools

Observed:
- public, non-archived repository;
- README explicitly presents a collection of exposed/leaked AI system prompts and related material;
- no root LICENSE file was observed in review;
- provenance/authorization for individual prompt/model artifacts is not established by the repository itself.

Decision: **RESEARCH_REFERENCE_ONLY / DO_NOT_COPY / DO_NOT_EXECUTE**.

Permitted use:
- defensive prompt-leakage awareness;
- threat-modeling system-prompt extraction and prompt-injection risks;
- high-level comparative research based on independently lawful/public facts.

Prohibited Ercan OS adoption:
- copying leaked/proprietary prompts into Ercan OS;
- treating leaked instructions as authoritative product documentation;
- executing scripts/artifacts from the repository merely to reproduce another vendor's hidden behavior;
- redistributing substantial unlicensed prompt/model content.

For current behavior of Cursor, Devin, v0, Claude Code, Codex or other products, use official/current product documentation and observable public behavior instead.

## 4. composio-community/awesome-codex-skills

Observed:
- current GitHub repository resolves to **composio-community/awesome-codex-skills** rather than the older ComposioHQ path shown in some README/install examples;
- public, non-archived repository;
- curated Codex skills grouped across development, productivity, communication, data and utilities;
- no root LICENSE file was found;
- many individual skills contain their own LICENSE.txt and license metadata, so licensing is per-skill/path rather than safely inferred for the whole collection.

Decision: **DISCOVERY_SOURCE_ONLY / PER_SKILL_AUDIT_REQUIRED**.

Use:
- discover candidate Codex/Agent Skills;
- resolve each skill to its actual source and exact path;
- inspect SKILL.md, scripts, allowed-tools, network/credential behavior and exact license before adoption.

Do not:
- clone/install the entire catalog into Ercan OS;
- infer the whole repository is Apache/MIT because some included skills are;
- trust README owner/path examples over current canonical GitHub identity.

## 5. sindresorhus/awesome

Observed:
- public, non-archived meta-index of curated awesome lists;
- root license observed: CC0-1.0.

Decision: **DISCOVERY_SOURCE / ROOT_RECURSIVE_INDEX**.

Use only when narrower Ercan OS catalogs do not already provide a better source. Route:
`requirement -> relevant awesome sub-list -> original candidate repository -> upstream audit -> adoption decision`.

Do not:
- recursively ingest every list into persistent context;
- treat awesome-list inclusion or star count as a trust score;
- bypass candidate-level provenance/license/security review.

## Architecture decision

No new stable identity and no new production dependency.

Extend the existing `developer-resource-discovery` JIT capability with:
- MCPServerDiscovery;
- LLMAppPatternDiscovery;
- CodexSkillDiscovery;
- RootAwesomeDiscovery;
- PromptLeakResearch boundary.

The system continues to follow:
**discover broadly -> resolve original source -> audit narrowly -> adopt the smallest useful unit -> independently verify**.
