---
name: verify-social-claim
description: Verify technical/product/repository claims found in X/Twitter or other social posts before adopting them into Ercan OS. Use after a social post is resolved or when a user asks whether a viral AI/tool claim is real or useful. Decompose claims, trace official upstream evidence, classify confidence, and recommend ADOPT/WATCHLIST/REJECT without hype.
---

# Verify Social Claim

Follow `docs/standards/SOCIAL_RESEARCH.md` and `docs/standards/UPSTREAM_TOOLCHAIN.md`.

## Procedure
1. Receive exact post text/links when available. If the originating post is unresolved, preserve that limitation.
2. Split the post into atomic factual claims and opinions.
3. For each factual claim identify the highest-authority upstream: official docs/release notes, verified GitHub repo, official sample, primary paper/spec.
4. Check current status: feature availability, version, deprecation, license, install requirements, maintenance and material security implications.
5. Compare with existing Ercan OS capabilities to avoid duplicate skills/adapters.
6. Classify each claim: `CONFIRMED`, `PARTIAL`, `UNVERIFIED`, `CONTRADICTED`, or `OPINION`.
7. End with one system decision: `ADOPT`, `ADOPT_PATTERN_ONLY`, `WATCHLIST`, or `REJECT`.
8. If adoption is requested, implement the smallest provider-neutral skill/standard/adapter and preserve authoritative upstream references.

## Output contract
- source social URL/post ID
- atomic claims
- primary evidence per claim
- claim status
- security/license/maintenance notes
- overlap with existing Ercan OS
- practical value by domain
- adoption decision
- exact files/standards changed if implementation occurred

## Anti-hype rule
Follower count, likes, reposts, star count or confident wording are not verification. A social post is discovery input, not authority.
