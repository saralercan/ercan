---
name: agent-runtime-stack
description: Route production AI-agent systems across local/model runtime, agent framework/orchestration, coding harness, tools/actions, sandbox execution, private/RAG memory, observability/evals and voice interfaces. Use when choosing or composing agent infrastructure such as Ollama, Microsoft Agent Framework, LangChain, CrewAI, DSPy, E2B, Composio, PrivateGPT, Mem0, AgentOps, AgentBench, ElevenLabs or Deepgram. Avoid stacking overlapping frameworks and route archived/superseded projects as pattern-only.
---

# Agent Runtime Stack

This JIT capability organizes agent infrastructure without creating new stable Ercan OS identities.

## Core lifecycle

`idea/spec -> model/runtime -> agent/workflow orchestration -> tools/actions -> sandbox/execution -> memory/context -> observability/evals -> delivery/voice -> independent QA`

Select the smallest sufficient implementation for each stage. Do **not** install one product from every stage by default.

## Stable-owner mapping

- runtime/model selection -> `@Orchestrator` + project implementation owner
- multi-agent/workflow orchestration -> `@Orchestrator` + execution-governance
- coding harness -> repository implementation owner + independent QA
- tools/actions/connectors -> tool integration owner + security/approval gate
- sandbox/computer execution -> authorized execution owner + security reviewer
- memory/RAG -> data/application owner + privacy/security reviewer
- observability/tracing -> runtime/platform owner + QA
- benchmarks/evals -> independent evaluator + `agent-eval-regression`
- speech/voice -> media/application owner + privacy/consent review

## Run & build

### Ollama — `ollama/ollama`
Decision: `ADOPT_WHEN_NEEDED` (MIT).

Use for local/open-model serving when privacy, offline use, latency control, local experimentation or provider independence materially benefits the task.

Rules:
- local execution does not automatically mean private; inspect model downloads, telemetry, remote integrations and exposed API binding;
- bind local APIs narrowly unless network exposure is explicitly required;
- model capability, context size and hardware fit are runtime facts;
- do not assume a local model is sufficient for a task without evaluation.

### LangChain — `langchain-ai/langchain`
Decision: existing `ADOPT_WHEN_NEEDED`.

Use when the inspected application actually benefits from its provider/tool/retrieval/workflow abstractions. Do not wrap simple direct SDK calls merely to standardize on a framework.

### Open Interpreter — `openinterpreter/openinterpreter`
Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` (Apache-2.0).

Canonical reviewed repository is `openinterpreter/openinterpreter`; older social links may point at the previous repository path.

Use for coding-harness, local command and computer-use architecture where explicit execution is required. Current implementation can execute code/commands and operate interfaces, so:
- preserve user authorization;
- use native sandboxing/isolated workspaces;
- require approval for destructive, credential, account, financial or production-impacting operations;
- do not grant broad host access merely because the harness supports it.

### AutoGen — `microsoft/autogen`
Decision: `SUPERSEDED_FOR_NEW_WORK`.

The reviewed repository is in maintenance mode and directs new users to `microsoft/agent-framework`. Existing AutoGen deployments may remain supported/migrated, but new Microsoft-oriented multi-agent systems should evaluate Microsoft Agent Framework first.

### Microsoft Agent Framework — `microsoft/agent-framework`
Decision: `ADOPT_WHEN_NEEDED / PREFERRED_SUCCESSOR_FOR_AUTOGEN` (MIT).

Use for production-oriented Microsoft/.NET/Python/Go agent systems requiring graph workflows, handoffs, checkpointing, human-in-the-loop, middleware, provider flexibility and observability.

### Aider — `Aider-AI/aider`
Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` (Apache-2.0).

Useful patterns:
- repository map/context selection;
- Git-aware reversible edits;
- lint/test feedback after changes;
- provider-flexible coding harness.

It does not replace Ercan OS branch, architecture, independent review or completion evidence.

### Coding provider router
Primary reviewed reference: `Alishahryar1/free-claude-code`.

Decision: `ADOPT_WHEN_NEEDED / CONDITIONAL_PROVIDER_ROUTER` (MIT).

Load `.agents/skills/coding-provider-router/SKILL.md` + `docs/standards/CODING_PROVIDER_ROUTER.md` only when multi-provider coding-model routing/fallback/shared harness configuration materially helps. Ercan OS hardening overrides upstream defaults: local evaluations bind loopback and require proxy authentication. Direct/native provider configuration remains preferred when simpler.

## Coordinate

### AutoGPT — `Significant-Gravitas/AutoGPT`
Decision: `ADOPT_PATTERN_ONLY / WATCHLIST`.

The repository is mixed-license: the `autogpt_platform` directory is PolyForm Shield while classic components outside it are MIT. Treat workflow-builder/agent-platform patterns as references unless the exact code path and commercial-use rights are separately reviewed. Do not copy platform code under an assumed MIT license.

### MetaGPT — `FoundationAgents/MetaGPT`
Decision: `ADOPT_PATTERN_ONLY` (MIT).

Useful for SOP-driven role decomposition and software-company-style multi-agent workflow patterns. Ercan OS already has stable role/routing governance, so MetaGPT does not become a second agent constitution.

### CrewAI — `crewAIInc/crewAI`
Decision: existing `ADOPT_WHEN_NEEDED`.

Use only when a project genuinely benefits from CrewAI's crew/flow runtime. Ercan OS orchestration remains the higher-level project policy and completion authority.

### DSPy — `stanfordnlp/dspy`
Decision: `ADOPT_WHEN_NEEDED` (MIT).

Use for modular LM programs and empirical optimization of prompts/examples/weights where a measurable evaluation objective exists.

Rules:
- optimize against representative evals, not a single demo;
- preserve holdout/regression sets;
- never optimize graders/security checks away;
- record the compiled/optimized artifact and evaluation conditions.

### CAMEL — `camel-ai/camel`
Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` (Apache-2.0).

Strong for research, simulations, multi-agent experiments, stateful agent studies and synthetic data generation. Do not introduce high agent-count orchestration into ordinary product work when a smaller workflow is sufficient.

## Act & execute

### Flowise — `FlowiseAI/Flowise`
Decision: `SUPERSEDED/HISTORICAL`.

The reviewed GitHub repository is archived. Keep only historical low-code/visual-flow architecture patterns unless an active canonical successor is separately verified.

### Continue — `continuedev/continue`
Decision: `SUPERSEDED/HISTORICAL` (Apache-2.0).

The reviewed README states that the repository is no longer actively maintained and is read-only. It may inform coding-agent/IDE patterns, but it is not a new production dependency.

### Vercel AI SDK — `vercel/ai`
Decision: existing `ADOPT_WHEN_NEEDED`.

Use for provider-neutral AI application streaming, tool calling and UI integration in compatible JavaScript/TypeScript stacks. It is an application SDK, not Ercan OS policy authority.

### E2B — `e2b-dev/E2B`
Decision: `ADOPT_WHEN_NEEDED` (Apache-2.0).

Use for isolated cloud sandboxes, code execution or desktop/computer-use environments when external sandbox infrastructure is justified.

Rules:
- least-privilege credentials and network egress;
- per-task sandbox lifecycle and cleanup;
- no implicit access to production secrets;
- outcome verification outside the sandbox when mutations affect external systems;
- self-hosted vs managed deployment is a separate architecture/operations decision.

### Composio — `ComposioHQ/composio`
Decision: `ADOPT_WHEN_NEEDED` (MIT).

Use for authenticated third-party tool/action integrations when it materially reduces custom connector work.

Rules:
- scope sessions to the correct user/account;
- expose only required toolkits/actions;
- separate read from write/action permissions;
- preserve explicit approval for high-impact external actions;
- treat connected-account tokens and hosted MCP endpoints as sensitive credentials;
- do not load hundreds of tool schemas when discovery/meta-tools can keep context narrow.

### Managed agent deployment
Primary reviewed provider: `https://rerun.build/`.

Decision: `ADOPT_WHEN_NEEDED / MANAGED_AGENT_DEPLOYMENT_PROVIDER / CLOSED_SOURCE_SAAS`.

Load `.agents/skills/managed-agent-deployment/SKILL.md` + `docs/standards/MANAGED_AGENT_DEPLOYMENT.md` when recurring business agents need a managed runtime, client/team handoff, isolated project/client execution, connector-backed actions, human approval gates or operator-friendly live run visibility.

Rerun is a deployment/execution surface beneath Ercan OS governance. It must not replace project rules, stable routing, evals or completion authority. Current provider terms, pricing, connector scopes and data-processing arrangements remain runtime-verified facts.

## Memory, evaluation and delivery

### PrivateGPT — `zylon-ai/private-gpt`
Decision: `ADOPT_WHEN_NEEDED` (Apache-2.0).

Use as a private/local AI API/RAG layer over an OpenAI-compatible inference server such as Ollama when data locality is a real requirement.

PrivateGPT does not itself guarantee that every configured model/tool/data source is local. Verify inference, embeddings, web/search tools, MCP connectors, databases and outbound egress independently.

### Mem0 — `mem0ai/mem0`
Decision: `ADOPT_WHEN_NEEDED` (Apache-2.0).

Use for application-level agent/user/session memory where the product needs retrieval across interactions.

Memory contract:
- define tenant/user/session scope;
- classify PII/secrets before storage;
- define write authority, retention/deletion and conflict behavior;
- distinguish observed facts from model-generated summaries/inferences;
- do not let external memory override project source-of-truth artifacts;
- Ercan OS/ChatGPT product memory remains a separate product surface.

### AgentOps — `AgentOps-AI/agentops`
Decision: `ADOPT_WHEN_NEEDED` (MIT).

Use for agent traces, session replay, cost/latency/error analysis and runtime observability when it improves debugging/production operations.

Before external telemetry:
- classify prompt/tool/result content;
- redact secrets/private data;
- define sampling/retention;
- prefer existing OpenTelemetry/runtime observability when sufficient;
- do not duplicate tracing systems with no operational benefit.

### AgentBench — `THUDM/AgentBench`
Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED_FOR_BENCHMARKING` (Apache-2.0).

Use benchmark environments/methodology when a task requires agent capability benchmarking. It is not the default Ercan OS regression suite. Its container/resource requirements and environment-specific metrics must be treated separately from project-level acceptance tests.

### ElevenLabs — `elevenlabs/elevenlabs-python`
Decision: `ADOPT_WHEN_NEEDED / PROVIDER_ADAPTER` (MIT SDK).

Use for speech/voice/TTS/realtime voice-agent functionality only when required. Current models, languages, quotas and prices are runtime provider facts.

Voice cloning requires explicit rights/consent for the supplied voice material. Never infer consent from possession of an audio file.

### Deepgram — `deepgram/deepgram-python-sdk`
Decision: `ADOPT_WHEN_NEEDED / PROVIDER_ADAPTER` (MIT SDK).

Use for STT/TTS/voice-agent and speech intelligence where current provider capabilities fit. Verify language/model/runtime requirements from current official docs.

## Framework selection rules

1. Prefer **one primary orchestration framework** per application.
2. Use direct provider SDKs when a framework adds no material value.
3. Existing Ercan OS routing may orchestrate external framework-based workers; external frameworks do not redefine the stable agent registry.
4. Do not combine LangChain + CrewAI + Microsoft Agent Framework + MetaGPT merely because all are available.
5. Prefer current maintained successors over archived/maintenance-mode predecessors.
6. Sandbox and action providers are selected independently from orchestration frameworks.
7. Memory and observability are optional product capabilities, not mandatory agent-stack layers.
8. Voice providers are I/O adapters, not orchestration engines.

## Recommended Ercan OS stack shapes

### Local/private prototype
`Ollama -> direct SDK or PrivateGPT -> project agent/workflow -> local isolated tools -> project artifacts -> Ercan OS evals`

### Production multi-agent service
`provider/runtime -> Microsoft Agent Framework OR CrewAI/LangChain as justified -> scoped tools/Composio -> E2B or other isolated execution -> optional Mem0 -> OpenTelemetry/AgentOps -> Ercan OS eval/regression -> deploy`

### Coding workflow
`repo rules -> Ercan OS implementation owner -> optional Aider/Open Interpreter patterns -> isolated execution -> lint/test/build -> independent review -> merge/deploy evidence`

### Voice agent
`speech input (Deepgram or compatible) -> application agent/workflow -> scoped tools/memory -> speech output (ElevenLabs/Deepgram or compatible) -> latency/privacy/eval QA`

## Completion evidence

Record:
- selected runtime/framework and why;
- rejected overlapping frameworks;
- tool/action permission scope;
- sandbox boundary;
- memory/telemetry data policy if used;
- eval/benchmark evidence;
- provider costs/limits checked when material;
- deployment/runtime smoke evidence;
- final state: VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED.
