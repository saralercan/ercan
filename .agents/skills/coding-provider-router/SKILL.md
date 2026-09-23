---
name: coding-provider-router
description: Route coding agents through a reviewed provider/model proxy layer with explicit provider allowlists, fallback policy, loopback binding, proxy authentication, credential isolation and per-harness compatibility checks. Use when a coding workflow needs multiple model providers, resilient fallback, provider switching or a shared local proxy across Codex/Claude/Aider/OpenCode-class clients.
---

# Coding Provider Router

This JIT capability is owned by `@Orchestrator` + the task's coding/runtime owner. It does not create a new stable agent identity.

Primary reviewed implementation reference: `Alishahryar1/free-claude-code` (MIT).

## Why this exists

Use a provider router only when one or more of these are true:
- the coding workflow genuinely needs multiple model providers;
- provider outage/quota resilience matters;
- different harnesses should share one model catalog;
- the user explicitly wants provider/model switching without reconfiguring each client;
- local and hosted providers need one compatibility layer.

Do not add a router to a single-provider workflow merely because it is available.

## Ercan OS hardening profile

The reviewed upstream currently defaults to:
- `HOST=0.0.0.0`
- `PROXY_AUTH_ENABLED=false`

Ercan OS **must not use those defaults**.

Minimum safe local profile:
- `HOST=127.0.0.1`
- `PROXY_AUTH_ENABLED=true`
- generate/store a non-empty proxy token outside source control;
- expose only explicitly selected providers;
- do not expose the proxy outside loopback unless a separate network/security review approves it;
- keep Admin local-only;
- preserve restrictive file permissions for managed config/credentials where the platform supports them.

If remote/LAN access is required, treat it as a separate deployment/security decision with TLS, authentication, firewalling, origin policy and audit logging.

## Provider policy

Every provider is independently reviewed for:
- current official terms;
- plan/subscription compatibility;
- API key/account scope;
- data retention/training/privacy;
- regional availability;
- quotas/rate limits;
- billing behavior;
- model availability and context limits.

The router README's aggregate free-token/free-provider claims are discovery data only and may change.

Use an explicit provider allowlist. Do not enable every discovered provider.

## Fallback contract

Fallback is allowed only when:
- the first provider failed before meaningful output/action began;
- the fallback provider is explicitly approved for the same data class;
- model capability is compatible with the task;
- retries/fallbacks cannot silently multiply billable or rate-limited calls beyond the configured policy.

Record which provider/model actually completed the turn.

Never claim a specific model/provider executed unless runtime evidence confirms it.

## Harness compatibility

Reviewed upstream supports launchers for multiple coding clients. Ercan OS should treat every harness integration separately.

Before enabling a harness:
- inspect its current authentication model;
- verify config changes are reversible;
- preserve existing native client settings;
- verify tools/images/thinking/streaming behavior needed by the task;
- run one read-only or low-risk smoke turn first;
- do not assume the proxy preserves every provider-native feature.

## Installer policy

Do **not** execute remote installer pipes directly as an Ercan OS default.

The reviewed upstream installer can download/install multiple external coding agents and tools. Before installation:
1. inspect the current installer at the exact commit/release;
2. choose only the required client(s);
3. use a disposable or isolated environment for first evaluation;
4. prefer pinned releases/checksums/package-manager verification where practical;
5. preserve uninstall/rollback path;
6. never install unrelated coding agents just because the installer offers them.

## Credential handling

- Provider keys/tokens never enter Git history.
- Managed config and auth files should remain owner-readable only where supported.
- Admin/API responses must mask secrets.
- Logs/diagnostics must redact authorization headers, API keys, tokens and passwords.
- Connected-account OAuth/session data is sensitive and provider-specific.
- Never forward one provider's credential to another provider.
- Never expose proxy tokens to generated code unless the harness contract requires it and scope is controlled.

## Browser/code sessions

If using a browser-hosted coding session:
- workspace path must be explicitly selected and scoped;
- default to least-privilege filesystem mode;
- production credentials are not inherited automatically;
- background sessions need lifecycle/termination control;
- changing providers/models mid-session must not change project permissions;
- independent source/test/CI verification still owns completion.

## Routing relationship

This skill sits beneath:
- `agent-runtime-stack` for overall runtime selection;
- `execution-governance` for completion authority;
- `agent-eval-regression` for representative routing/fallback evaluation;
- project/repository AGENTS rules for coding behavior.

It does not replace Ercan OS orchestration or stable agent routing.

## Verification

Before marking a provider-router setup VERIFIED:
- bind address is confirmed;
- proxy auth is enabled and actually rejects unauthenticated requests;
- Admin remains local-only;
- selected provider credentials are stored outside source control;
- provider allowlist matches project need;
- one approved model works for each required harness;
- fallback success/failure paths were tested without unsafe duplicate side effects;
- logs/config previews do not expose secrets;
- the actual completing provider/model can be observed;
- uninstall/rollback path is documented;
- final project tests/QA run outside the router's self-report.

Final state: VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED.
