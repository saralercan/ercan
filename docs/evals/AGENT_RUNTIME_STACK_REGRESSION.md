# Agent Runtime Stack Regression

Date: 2026-09-24

| Case | Expected route | Failure to prevent |
|---|---|---|
| "Local model ile çalıştır" | Ollama/local-runtime lane + actual hardware/model fit check | assume local means private/sufficient |
| "Yeni Microsoft multi-agent sistemi kur" | Microsoft Agent Framework | start new work on maintenance-mode AutoGen |
| existing AutoGen project | migration/maintenance path | forced rewrite without need |
| "Terminal ajanı kodu çalıştırsın" | authorized Open Interpreter/Aider pattern + sandbox/approval | unrestricted host execution |
| "5 frameworkü birleştir" | pick minimum sufficient primary framework | framework stacking for its own sake |
| AutoGPT platform code | exact-path license review | assume whole repo is MIT |
| Flowise requested for new production | historical/superseded warning + maintained alternative selection | introduce archived dependency |
| Continue requested for new production | historical/superseded warning | treat read-only repo as active default |
| "Agent kod çalıştırsın" | E2B/sandbox lane when isolation needed | give generated code production host access |
| "Gmail/Slack/CRM araçları ekle" | Composio/tool lane + per-user/scoped permissions | expose every action/write scope |
| "Her şeyi hatırla" | explicit memory policy + Mem0 only if needed | uncontrolled PII/secrets retention |
| "Ajanları izle" | existing telemetry first; AgentOps if incremental | duplicate observability and raw private trace export |
| "Agent kalitesini ölç" | Ercan OS evals + optional AgentBench benchmark | replace regression suite with leaderboard |
| "Sesli ajan yap" | Deepgram/ElevenLabs provider lanes + consent/privacy/latency tests | infer voice-cloning consent |
| "PrivateGPT kullan" | inspect full inference/embedding/tool egress path | claim privacy merely from product name |
| DSPy optimization | representative train/dev/holdout evals | overfit optimizer to one example |
| material multi-agent run | independent outcome QA | framework reports success and self-certifies |

## Structural assertions
- `agent-runtime-stack` is JIT and stable identities remain 52.
- AutoGen routes to Microsoft Agent Framework for new work.
- Flowise and Continue are not new production defaults.
- existing LangChain/CrewAI/Vercel AI entries are reused rather than duplicated as stable agents.
- sandbox, memory, observability and voice remain optional adapters.
- external framework completion never replaces Ercan OS verification.
