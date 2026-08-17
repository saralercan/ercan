---
name: upstream-adoption-audit
description: Evaluate a GitHub repo, CLI, library, Agent Skill or infrastructure tool before Ercan OS adoption. Use when research finds a promising project or when replacing/upgrading an existing dependency.
---

# Upstream Adoption Audit

Load `UPSTREAM_TOOLCHAIN.md` and `DISCOVERY_ADOPTION_LEDGER.md` first.

## Audit
1. Identity: official/verified owner, fork status, successor/history.
2. Status: archived/deprecated, latest activity/releases, current docs, material unresolved issues.
3. License: SPDX/current license, commercial/AGPL/custom constraints.
4. Security: security policy/advisories, install hooks, shell/network/credential requirements, dependency/supply-chain surface.
5. Fit: exact problem solved, overlap with existing capability, migration/lock-in/ops burden.
6. Integration shape: dependency vs provider adapter vs JIT skill vs pattern-only reference.
7. Verification: current API/CLI/model/version behavior from authoritative upstream.
8. Exit: rollback/replacement strategy if the tool disappears or changes licensing/API.

## Decision
Return exactly one primary decision:
- `ADOPT`
- `ADOPT_PATTERN_ONLY`
- `WATCHLIST`
- `REJECT`
- `SUPERSEDED`

Also return:
- authoritative upstream
- useful pattern/capability
- risks/license/security
- files/standards/skills that should change if adopted
- regression/eval requirements

## Guardrails
- Stars/followers are not fitness evidence.
- Do not add an unused dependency merely because a repo is impressive.
- Prefer official platform docs/samples over community wrappers for volatile APIs.
- If a maintained successor exists, do not standardize on the archived predecessor.
- Broad Agent Skills/extensions that request unnecessary credentials/session/shell access require explicit justification.