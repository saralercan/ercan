# Vinterro One — Codex Native Agent Bridge

Status: active
Date: 2026-10-02
Scope: Codex CLI / IDE multi-agent execution for every Vinterro One runtime identity.

## Why this bridge exists

Vinterro One runtime agents are logical expert contracts stored in the live registry and mirrored in
`docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json`. Codex native agents are execution threads.

The two concepts are intentionally not one-to-one. Creating 112 simultaneous Codex threads would be wasteful,
would hit thread/concurrency limits, and would violate the Vinterro One rule that "tüm ajanları çalıştır" means
all materially relevant specialists rather than literal full-registry fan-out.

Codex therefore uses a bounded native role pool and delegates the exact Vinterro One identity into that role.

## Native role pool

Configured in `.codex/config.toml`:

- `vinterro_orchestrator`
- `vinterro_project_lead`
- `vinterro_specialist`
- `vinterro_researcher`
- `vinterro_implementer`
- `vinterro_reviewer`
- `vinterro_qa`
- `vinterro_security`
- `language_en`
- `language_bg`
- `language_es`
- `language_el`
- `language_de`
- `language_fr`
- `multilingual_qa`

Role config layers live under `.codex/agents/*.toml`.

## Mapping rule

Any active Vinterro One identity can execute in Codex:

1. Project leads -> `vinterro_project_lead`
2. Security identities -> `vinterro_security`
3. QA/reviewer/auditor identities -> `vinterro_reviewer` or `vinterro_qa`
4. Research/intelligence identities -> `vinterro_researcher`
5. Developer/platform/implementation identities -> `vinterro_implementer`
6. Six dedicated human-language specialists -> matching `language_*` role
7. Multilingual Localization QA Auditor -> `multilingual_qa`
8. Every remaining exact runtime identity -> `vinterro_specialist`

For generic bridge roles, the delegated task MUST include the exact Vinterro One agent name. The subagent resolves
that name against the runtime manifest and expertise matrix before acting.

## Concurrency and thread-limit recovery

Project Codex config sets:

`agents.max_concurrent_threads_per_session = 8`

This is a ceiling for open spawned threads, not a target.

The Orchestrator should:
- start independent high-value workstreams first;
- preserve one slot for independent QA/reviewer when practical;
- wait for agents whose output is a dependency;
- close completed agent threads;
- start the next qualified wave;
- never keep finished threads open merely to preserve history.

If Codex reports `agent thread limit reached`, an `agent/thread limit` error, or an equivalent concurrency refusal:
1. a thread-limit condition is not proof that Vinterro One agents are unavailable;
2. inspect current open agent work;
3. wait for in-flight work that should finish;
4. close completed threads;
5. retry only the remaining qualified work in the next wave;
6. if the runtime itself has a lower managed limit than project config, respect the lower limit and continue with smaller waves.

Do not retry-spam a blocked spawn.

## "Tüm ajanları çalıştır"

The phrase means:
- resolve the active project;
- activate its project lead;
- select every materially relevant, non-redundant Vinterro One specialist;
- include independent QA/reviewer/security/release roles when required;
- execute that pod through the native Codex role pool in one or more bounded waves.

It never means 112 simultaneous threads.

## Truthfulness

Loading a Vinterro One contract is not proof a native subagent actually ran.
A native run requires runtime evidence from Codex. If a surface does not expose multi-agent execution,
Codex may still follow the logical specialist contract in the main thread, but must not describe that as an
independently running subagent.

## Official Codex configuration basis

The bridge follows the current Codex configuration model:
- `[agents]` enables multi-agent settings.
- `agents.<name>.description` declares role-selection guidance.
- `agents.<name>.config_file` points to a TOML role config layer.
- `agents.max_concurrent_threads_per_session` bounds concurrently open spawned-agent threads.

See the current OpenAI Codex configuration reference before changing these keys.
