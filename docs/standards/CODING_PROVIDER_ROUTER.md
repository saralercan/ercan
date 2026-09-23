# Ercan OS — Coding Provider Router

Status: active
Date: 2026-09-24

## Purpose

Define safe use of multi-provider coding-model routers across Codex/Claude/Aider/OpenCode-class harnesses.

Execution skill: `.agents/skills/coding-provider-router/SKILL.md`.

Primary reviewed implementation reference: `Alishahryar1/free-claude-code`.

Stable routing identities remain **52**.

## Adoption decision

`Alishahryar1/free-claude-code`:
**ADOPT_WHEN_NEEDED / CONDITIONAL_PROVIDER_ROUTER / MIT**

Reason for promotion from watchlist:
- maintained typed Python application rather than only a provider list;
- shared model/provider catalog across multiple coding harnesses;
- explicit fallback routing;
- local Admin surface;
- proxy bearer authentication support;
- provider/account adapters;
- smoke/contract tests;
- owner-restricted config/credential file permissions on supported Unix platforms;
- diagnostics secret-redaction patterns.

Reason it is not a global/default dependency:
- provider terms/quotas/models are volatile;
- the upstream server currently defaults to `0.0.0.0`;
- proxy authentication currently defaults to disabled;
- installer can install multiple external coding agents/tools;
- one router increases the blast radius of credential/configuration mistakes;
- compatibility can differ per harness/provider/model.

## Mandatory Ercan OS override

For local development, use:
`HOST=127.0.0.1`
and:
`PROXY_AUTH_ENABLED=true`.

A non-empty proxy token is mandatory.

Do not expose the API on LAN/public interfaces unless a separate security architecture is approved.

## Trust boundaries

### Admin
Reviewed upstream enforces loopback-only Admin access using client address, Host and Origin checks. Preserve this boundary.

### Proxy API
Proxy auth is optional upstream but mandatory in Ercan OS. Verify unauthenticated API requests fail before adding real credentials.

### Credentials
Provider tokens, connected-account credentials and router auth tokens are secrets. They belong in managed secret/config storage outside source control.

### Installer
The convenience installer is not a trust boundary. It downloads/configures external clients. Ercan OS first-use evaluation must inspect the exact installer and select only required clients.

## Model routing

A model catalog is discovery/configuration state, not capability proof.

Before routing a coding task:
- confirm model still exists;
- verify provider/account entitlement;
- match context/tool/image/reasoning requirements;
- respect project privacy constraints;
- check current cost/quota when material.

Fallback routes are explicit and ordered. The final trace should record the provider/model that actually completed the request.

## Provider independence

The router may normalize protocols, but provider-specific behavior still exists:
- tool-call schemas;
- streaming;
- reasoning controls;
- images/multimodal input;
- rate limits;
- model aliases;
- subscription/API account restrictions;
- terms governing third-party clients.

Do not assume protocol compatibility means policy/capability equivalence.

## Integration with Ercan OS

`intent -> coding requirement -> agent-runtime-stack -> coding-provider-router? -> approved provider allowlist -> hardened local proxy -> harness smoke -> task execution -> independent repo QA -> completion`

The router is skipped when direct provider/native client configuration is simpler and sufficient.

## Update gate

Before upgrading:
- review changelog/diff;
- provider catalog changes;
- authentication/bind defaults;
- installer changes;
- dependency changes;
- migrations/config ownership;
- harness launchers;
- routing/fallback changes;
- tests/CI.

A new upstream release never auto-upgrades production Ercan OS environments solely because it is available.
