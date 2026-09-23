# Provider/Pattern Scan — Rerun Competitor Meta Ads

Date: 2026-09-24
Input URL: https://rerun.build/templates/recreate-competitor-ads-meta

## Retrieval status
The exact supplied template URL was not directly retrievable through the current web fetch path during review, and search indexing did not expose the full template body. Therefore no unobserved template details are asserted.

The slug indicates a Meta competitor-ad recreation workflow. Ercan OS treats that as discovery input and verifies the underlying public-data and policy boundaries independently.

## Verified primary facts
Meta Ad Library publicly supports searching ads by advertiser/keyword and exposes current ads; official Meta Ad Library/API documentation exposes creative, Page identity, delivery dates and platforms, with additional transparency data for political/social-issue and EU/UK ads.

Rerun is already adopted conditionally as a managed agent deployment provider with scheduling, Boxes, approvals and connectors.

Rerun AUP prohibits IP infringement, so a competitor-ad workflow must not copy protected creative expression.

## Supporting open-source pattern
Reviewed `novoads/agent-skills:skills/spy-competitor-ads`:
- MIT;
- collects live competitor ad evidence;
- preserves permanent Ad Library URLs;
- distinguishes mechanical ranking from actual performance judgment;
- explicitly notes page-running-ad can differ from queried brand;
- uses paid API sweeps with cost estimation/approval.

Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` for collection mechanics, not as a mandatory dependency.

## Ercan OS decision
Create `competitor-creative-intelligence` JIT capability.

Use Rerun only as optional recurring execution/deployment surface.
Use Meta Ad Library as the primary evidence source.
Convert observed competitor patterns into original brand-owned creative briefs.
Do not use public persistence signals as proof of profitability.
