# Upstream Scan — free-claude-code Reassessment

Date: 2026-09-24

Repository: `Alishahryar1/free-claude-code`

## Current shape

The repository has evolved beyond a simple free-provider catalog into a Python local proxy/router application with:
- multiple coding-harness launchers;
- shared provider/model catalog;
- ordered fallback models;
- local Admin UI;
- optional proxy authentication;
- provider/account integrations;
- browser-hosted coding sessions;
- optional voice/messaging integrations;
- diagnostics and smoke/contract tests.

License observed: MIT.

## Positive implementation signals

### Admin boundary
`src/free_claude_code/api/admin_security.py` enforces loopback Admin access using:
- client address;
- Host authority;
- Origin validation.

### Proxy authentication
`src/free_claude_code/api/dependencies.py` implements bearer-token authentication, with Anthropic-compatible `x-api-key` handling on messages routes, and constant-time token comparison.

Tests cover missing/invalid credentials and model/root endpoint behavior.

### Secret/config handling
Reviewed code includes:
- secret metadata/masking in Admin;
- managed config atomic persistence;
- Unix owner-only `0o600` config/credential modes;
- `0o700` sensitive directories;
- diagnostics redaction patterns for authorization/API-key/token/secret/password fields.

### Routing/fallback
The Admin manifest explicitly documents ordered fallback models and warns that one failed request may consume usage from multiple providers.

## Critical default-security finding

Current settings source defines:
- `HOST=0.0.0.0` by default;
- `PROXY_AUTH_ENABLED=false` by default.

Therefore Ercan OS must not adopt upstream defaults.

Safe local Ercan OS baseline:
- bind `127.0.0.1`;
- enable proxy authentication;
- use a generated non-empty token;
- retain Admin loopback-only;
- use an explicit provider allowlist.

## Installer finding

The shell installer can download/install/configure multiple third-party coding agents and helper tools from external URLs. This is convenient but materially increases the installation trust surface.

Decision:
- no direct remote-pipe installation as an Ercan OS default;
- inspect exact installer/release first;
- install only requested/required clients;
- prefer isolated first evaluation;
- retain rollback/uninstall path.

## Provider claims

README claims about provider count, free tokens and ToS-friendliness are upstream-maintainer claims and are volatile.

Every selected provider needs independent current verification from official provider docs/terms.

## Updated Ercan OS decision

Previous:
`WATCHLIST / ADOPT_PATTERN_ONLY`.

New:
`ADOPT_WHEN_NEEDED / CONDITIONAL_PROVIDER_ROUTER`.

This is a JIT runtime capability, not a stable agent identity and not a global dependency.

Promotion is based on the architecture/tests/security mechanisms now present, with mandatory Ercan OS hardening overriding unsafe-for-general-network defaults.
