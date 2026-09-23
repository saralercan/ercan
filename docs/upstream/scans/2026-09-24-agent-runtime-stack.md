# Upstream Scan — Agent Runtime Stack

Date: 2026-09-24

## UI skill delta

The supplied UI list mostly matches the already integrated Design Quality Engine. A new canonical source was resolved for item 10:

### wshobson/agents — interaction-design
Path: `plugins/ui-design/skills/interaction-design/SKILL.md`.
Observed: purposeful motion, microinteractions, feedback, loading states, transitions, gestures and reduced-motion/accessibility considerations.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Action: replace the previous synthesized-only Interaction Design lane with this reviewed upstream while preserving Ercan OS/Emil/Impeccable/platform/accessibility rules as higher-level constraints.

Items 1–9 were already integrated in `design-quality-engine` and are not duplicated.

## Agent runtime sources

### ollama/ollama
Observed: local/open model runtime and API with coding/agent integrations.
License: MIT.
Decision: ADOPT_WHEN_NEEDED.

### langchain-ai/langchain
Already present in Ercan OS upstream catalog.
Decision: reuse existing ADOPT_WHEN_NEEDED status.

### openinterpreter/openinterpreter
Canonical current repository resolved from the older social link.
Observed: low-cost-model coding harness, commands, sandboxing, shared Agent Skills/MCP/ACP/Codex protocol support and computer-use QA.
License: Apache-2.0.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED with explicit execution/permission boundaries.

### microsoft/autogen
Observed: repository explicitly in maintenance mode; directs new users to Microsoft Agent Framework.
Decision: SUPERSEDED_FOR_NEW_WORK.

### microsoft/agent-framework
Observed: active production-grade multi-language agent/workflow framework with graph workflows, checkpointing, human-in-the-loop, middleware, provider flexibility and observability.
License: MIT.
Decision: ADOPT_WHEN_NEEDED / preferred successor for new Microsoft-oriented work.

### Aider-AI/aider
Observed: terminal pair-programming agent, repo map, Git integration, lint/test loops and provider flexibility.
License: Apache-2.0.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

### Significant-Gravitas/AutoGPT
Observed: current workflow/agent platform plus classic components.
License: mixed: `autogpt_platform` PolyForm Shield; other/classic portions MIT.
Decision: ADOPT_PATTERN_ONLY / WATCHLIST; exact-path license review required.

### FoundationAgents/MetaGPT
Observed: SOP/role-oriented software-company multi-agent framework.
License: MIT.
Decision: ADOPT_PATTERN_ONLY.

### crewAIInc/crewAI
Already present in Ercan OS catalog.
Decision: reuse existing ADOPT_WHEN_NEEDED status.

### stanfordnlp/dspy
Observed: modular LM programming and prompt/weight optimization against evaluation objectives.
License: MIT.
Decision: ADOPT_WHEN_NEEDED.

### camel-ai/camel
Observed: multi-agent research framework focused on statefulness, scaling, simulation, data generation and benchmark/research workflows.
License: Apache-2.0.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

### FlowiseAI/Flowise
Observed through current GitHub metadata: repository archived.
Decision: SUPERSEDED/HISTORICAL for new Ercan OS work.

### continuedev/continue
Observed: README states repository is no longer actively maintained and is read-only, with a final 2.0.0 release.
License: Apache-2.0.
Decision: SUPERSEDED/HISTORICAL.

### vercel/ai
Already present in Ercan OS catalog.
Decision: reuse existing ADOPT_WHEN_NEEDED status.

### e2b-dev/E2B
Observed: isolated cloud sandboxes for AI-generated code, code interpreter and desktop/computer-use surfaces; self-hosting is separately documented.
License: Apache-2.0.
Decision: ADOPT_WHEN_NEEDED.

### ComposioHQ/composio
Observed: agent tool/action SDK with per-user sessions, authentication, triggers, sandbox and hosted MCP/provider adapters.
License: MIT.
Decision: ADOPT_WHEN_NEEDED with strict toolkit/account/action scoping.

### zylon-ai/private-gpt
Observed: local/private AI API/RAG layer over OpenAI-compatible inference servers with files/retrieval/tools/MCP/database integrations.
License: Apache-2.0.
Decision: ADOPT_WHEN_NEEDED. Privacy depends on the entire configured provider/tool/egress path.

### mem0ai/mem0
Observed: application memory layer with user/session/agent memories, managed/self-hosted modes and benchmark claims that differ between managed/open-source capabilities.
License: Apache-2.0.
Decision: ADOPT_WHEN_NEEDED with explicit privacy/provenance/retention rules.

### AgentOps-AI/agentops
Observed: agent observability, session replay, cost/runtime analysis, framework integrations and self-hosting.
License: MIT.
Decision: ADOPT_WHEN_NEEDED when incremental over existing telemetry.

### THUDM/AgentBench
Observed: benchmark environments including current function-calling/containerized tasks; resource-heavy environments and benchmark-specific metrics.
License: Apache-2.0.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED_FOR_BENCHMARKING.

### elevenlabs/elevenlabs-python
Observed: official Python SDK for TTS/voice and realtime conversational agent interfaces.
License: MIT.
Decision: ADOPT_WHEN_NEEDED / provider adapter. Voice cloning needs rights/consent.

### deepgram/deepgram-python-sdk
Observed: official Python SDK for STT, TTS, text intelligence and realtime voice-agent APIs.
License: MIT.
Decision: ADOPT_WHEN_NEEDED / provider adapter.

## Architecture decision

Create one JIT `agent-runtime-stack` capability under existing Ercan OS owners. Do not create 20 stable agents and do not install all frameworks. Promote maintained/current components only where a real project need exists, mark archived/maintenance-mode tools correctly, and preserve the 52 stable routing identities.
