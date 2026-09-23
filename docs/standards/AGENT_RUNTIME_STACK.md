# Ercan OS — Agent Runtime Stack

Status: active
Date: 2026-09-24

## Purpose

Define how Ercan OS selects and composes modern AI-agent runtimes without turning every popular framework into a dependency or stable agent identity.

Execution skill: `.agents/skills/agent-runtime-stack/SKILL.md`.

Stable routing identities remain **21 Stable Core + 31 GitHub Specialist v3 Extension = 52**.

## Canonical lifecycle

`idea/spec -> model/runtime -> orchestration -> tools/actions -> sandbox -> memory/context -> observability/evals -> delivery/voice -> QA/deploy`

Each stage is optional. Product requirements determine which stages exist.

## Adoption map

| Source | Ercan OS role | Decision |
|---|---|---|
| `ollama/ollama` | local/open-model runtime | ADOPT_WHEN_NEEDED |
| `langchain-ai/langchain` | application/agent framework | existing ADOPT_WHEN_NEEDED |
| `openinterpreter/openinterpreter` | coding/computer-use harness | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |
| `microsoft/autogen` | legacy Microsoft multi-agent framework | SUPERSEDED_FOR_NEW_WORK |
| `microsoft/agent-framework` | current Microsoft production agent/workflow framework | ADOPT_WHEN_NEEDED / preferred AutoGen successor |
| `Aider-AI/aider` | Git-aware coding-agent patterns | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |
| `Alishahryar1/free-claude-code` | shared coding-model/provider proxy + fallback across multiple harnesses | ADOPT_WHEN_NEEDED / CONDITIONAL_PROVIDER_ROUTER |
| `Significant-Gravitas/AutoGPT` | autonomous workflow/platform patterns | ADOPT_PATTERN_ONLY / WATCHLIST; mixed license |
| `FoundationAgents/MetaGPT` | SOP/role decomposition | ADOPT_PATTERN_ONLY |
| `crewAIInc/crewAI` | crew/flow runtime | existing ADOPT_WHEN_NEEDED |
| `stanfordnlp/dspy` | LM program optimization | ADOPT_WHEN_NEEDED |
| `camel-ai/camel` | multi-agent research/simulation/data generation | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |
| `FlowiseAI/Flowise` | historical visual agent workflow | SUPERSEDED/HISTORICAL; repo archived |
| `continuedev/continue` | historical IDE/coding-agent patterns | SUPERSEDED/HISTORICAL; repo read-only |
| `vercel/ai` | AI application SDK/UI/streaming/tool calling | existing ADOPT_WHEN_NEEDED |
| `e2b-dev/E2B` | isolated sandbox/computer execution | ADOPT_WHEN_NEEDED |
| `ComposioHQ/composio` | authenticated external tools/actions | ADOPT_WHEN_NEEDED |
| `zylon-ai/private-gpt` | private/local AI API + RAG/application layer | ADOPT_WHEN_NEEDED |
| `mem0ai/mem0` | application-level long-term memory | ADOPT_WHEN_NEEDED |
| `AgentOps-AI/agentops` | agent observability/session tracing | ADOPT_WHEN_NEEDED |
| `THUDM/AgentBench` | agent benchmark environments | ADOPT_PATTERN_ONLY / WHEN_NEEDED_FOR_BENCHMARKING |
| `elevenlabs/elevenlabs-python` | speech/TTS/voice provider adapter | ADOPT_WHEN_NEEDED |
| `deepgram/deepgram-python-sdk` | STT/TTS/voice provider adapter | ADOPT_WHEN_NEEDED |
| `https://rerun.build/` | managed recurring-agent deployment/client handoff/approvals/live visibility | ADOPT_WHEN_NEEDED / MANAGED_AGENT_DEPLOYMENT_PROVIDER |

## Coding provider routing

Use `CODING_PROVIDER_ROUTER.md` when a coding system needs shared provider/model routing across multiple harnesses. The reviewed FCC implementation is conditional because its current upstream defaults bind the proxy to `0.0.0.0` and leave proxy authentication disabled. Ercan OS local use overrides this to loopback + authentication and installs only explicitly required clients/providers.

## Managed deployment providers

Use `MANAGED_AGENT_DEPLOYMENT.md` when an agent needs to live outside the developer control plane as a managed recurring business operation. Rerun is a reviewed managed provider for this role. Ercan OS retains policy/routing/eval authority; Rerun supplies execution, Boxes, integrations, approvals and operator/client visibility.

## Current-status corrections

### AutoGen
The reviewed `microsoft/autogen` repository is in maintenance mode and directs new projects to `microsoft/agent-framework`. New Microsoft-oriented runtime work must evaluate Agent Framework first.

### Flowise
The reviewed canonical `FlowiseAI/Flowise` repository is archived. Do not introduce it as a new default production dependency.

### Continue
The reviewed `continuedev/continue` README states that the repository is no longer actively maintained and is read-only. Preserve it as a historical/pattern reference only.

### AutoGPT
Licensing is path-sensitive. `autogpt_platform` uses PolyForm Shield while classic/outside-platform portions are MIT. Review exact files before any reuse.

## Architecture rules

### One orchestrator, many adapters
An application normally chooses one orchestration/runtime framework. Tool providers, memory, sandbox, observability and voice are adapters around it.

### Ercan OS stays above framework runtimes
Ercan OS controls project routing, permissions, evidence, quality gates and final completion. CrewAI/MAF/LangChain/MetaGPT/CAMEL/AutoGPT workflows are replaceable execution engines.

### Local model is not a security boundary
Ollama/local inference improves locality only when model serving, embeddings, retrieval, tools and network egress are also configured locally/securely.

### Sandbox is an execution boundary
When untrusted/generated code must run, prefer isolated sandboxing. Sandbox credentials/network/filesystem must be explicitly scoped.

### Tools/actions require identity and approvals
Per-user tool sessions must map to real user/account authorization. Read and write scopes should be separable, with meaningful approvals for irreversible/high-impact actions.

### Memory is data architecture
External memory stores need schema/scope, tenancy, provenance, retention/deletion, privacy and conflict rules. Model-generated memory must not silently become source-of-truth.

### Observability is sensitive
Agent traces can contain source code, prompts, credentials, personal data and tool results. Redact/filter before export and define retention.

### Evaluation is independent
Framework demos and provider benchmarks do not certify Ercan OS behavior. Project acceptance tests, regression suites and independent evaluators remain required.

## Selection preference

For a new system:
1. define requirements before selecting framework;
2. prefer existing Ercan OS/native provider tooling if sufficient;
3. choose one maintained orchestration runtime;
4. add sandbox only when code/computer execution requires isolation;
5. add external action tooling only for real integration breadth;
6. add memory only for a demonstrated cross-session requirement;
7. instrument with existing telemetry first, adding AgentOps only if it provides incremental value;
8. use AgentBench only for benchmark questions, not routine regression;
9. add voice adapters only when the product actually has a voice surface.

## Security

Never:
- expose host shell/filesystem broadly to an agent because Open Interpreter/Aider can use it;
- send production secrets into E2B or other sandboxes without explicit scoped need;
- expose every Composio/tool integration to every agent;
- store unreviewed PII/secrets in Mem0/agent memory;
- export raw private traces to observability providers by default;
- use cloned voices without rights/consent;
- keep archived frameworks as implicit defaults.

## Completion contract

A runtime-stack decision is VERIFIED only when the selected components are current, licensed appropriately for the exact use, secrets/permissions are scoped, failure/fallback behavior is known, representative evals pass and production state is independently checked.
