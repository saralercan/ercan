---
name: review-architecture
description: Review a material code change, PR or branch against the target repository's own architecture rules before detailed code review. Use for monorepos, plugins, shared packages, platform adapters, schema/state changes, or when a change may cross ownership/layer boundaries. Do not load for trivial copy-only or isolated styling changes.
---

# Review Architecture

Follow root `AGENTS.md` and `docs/standards/AGENT_ENGINEERING.md`.

## Goal
Find structural violations before downstream symptoms. The target repository's versioned architecture docs are the source of truth; this skill provides the review method, not project-specific package names.

## Procedure
1. Resolve the PR/branch/change scope and list changed files.
2. Load the target repo's architecture/layering/plugin/extension/schema docs that apply to those files.
3. For every new or materially changed file, exported helper/type, store/state field, schema, service, endpoint, component family or dependency edge, classify the owning layer/domain/package.
4. Check dependency direction and forbidden imports. A lower/framework/core layer reaching into a higher/app/plugin-specific layer is blocker-class unless the repo contract explicitly allows it.
5. Check whether new behavior should use an existing registry, capability, hook, extension point, platform API or plugin contract instead of introducing a new parallel dispatch/switch/hard-coded path.
6. For persisted schema/state/data changes, verify compatibility: defaults for additive fields, migrations for rename/removal/retype, and tests using old fixtures where risk warrants.
7. Check public interfaces for narrow contracts, ownership and reversibility; avoid speculative abstractions or hidden cross-layer state.
8. Run architecture-specific lint/structural tests if available.
9. Only after the classification pass, perform conventional correctness/performance/security review.

## Finding format
For each finding return:
- severity: `BLOCKER`, `MAJOR`, `MINOR`
- location
- violated architecture rule/source
- evidence from diff
- impact
- smallest compliant fix

Lead with root architectural violations before downstream symptoms.

## Completion
`PASS` only when no unresolved blocker remains and required structural tests/checks pass. If architecture docs are missing or contradictory, report `PARTIAL` and identify the missing contract instead of inventing one.
