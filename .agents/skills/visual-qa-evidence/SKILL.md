---
name: visual-qa-evidence
description: Produce an inspectable visual QA evidence ledger for UI, screenshot-reference, responsive, branding or social-creative work. Use when visual fidelity or channel rendering is part of acceptance. Do not treat code/tests alone as visual proof.
---

# Visual QA Evidence

Follow root `AGENTS.md` plus `BRAND_SOCIAL.md` and platform/project rules when relevant.

## Required inputs
- authoritative reference or intended visual state
- implementation/creative artifact to inspect
- viewport/device/channel and route/screen/state
- acceptance criteria and do-not-touch constraints

## Evidence procedure
1. Record **Comparison Target**: reference screenshot/design/brand asset and what makes it authoritative.
2. Record **Implementation Evidence**: final screenshot/export/preview and exact build/environment if relevant.
3. Record **Viewport / Channel / State**: width × height, device class, route/screen, menu/cart/modal/hover/selection state, waits/loading prerequisites.
4. State the **Intended State** in observable terms.
5. Compare the **Full View**: hierarchy, layout, density, crop, typography scale, color/token use, composition and overall brand fit.
6. Compare **Focused Regions**: the exact changed components/areas; measure spacing/alignment/crop/type/component-state discrepancies where useful.
7. Log findings with severity and evidence:
   - `P0` blocker — target state cannot be rendered/tested, major broken interaction, severe overlap/clipping, wrong asset/identity, or comparison impossible.
   - `P1` major — material fidelity/usability/channel failure.
   - `P2` polish — non-blocking craft issue.
8. Check fidelity surfaces: typography, spacing/layout rhythm, colors/tokens, imagery/assets, copy/content, responsive/channel crop, interaction state.
9. Record implementation checks actually run: lint/build/tests, browser E2E, console/network, accessibility, visual/export checks.
10. Record unresolved follow-up checks and final state: `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT VERIFIED`.

## Hard rule
If the target state cannot be reproduced and captured in the same meaningful state, visual acceptance is `BLOCKED` even if unit tests, geometry assertions or code review pass. Do not substitute reasoning for rendered evidence.

## Regression use
When possible retain the approved reference, implementation screenshot and manifest so the same state can become a future visual regression fixture.
