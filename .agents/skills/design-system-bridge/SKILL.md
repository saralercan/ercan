---
name: design-system-bridge
description: Audit or implement the bridge between brand tokens, Figma design-system assets and production UI code. Use for token migrations, Figma/code drift, Code Connect, Storybook/component-system work, Shopify/WordPress shared foundations, or design-system refactors.
---

# Design System Bridge

Load `docs/standards/DESIGN_SYSTEM_ENGINEERING.md` and the project brand/platform standards.

## Procedure
1. Identify authoritative sources: brand/token source, Figma/library references, code component package, generated outputs and product consumers.
2. Inventory semantic tokens and component variants/states; flag raw/off-system values and duplicate concepts.
3. Determine KEEP / MAP / MIGRATE / DEPRECATE for each relevant token/component contract.
4. If Figma Code Connect is in use, verify the current official supported integration path before editing mappings.
5. Generate platform outputs from source tokens; never patch generated files as source.
6. Verify representative component states in Storybook/workshop or equivalent isolated harness when present.
7. Run visual + interaction + accessibility checks on affected states and representative product pages.
8. Produce migration notes for renamed/removed tokens or component variants.

## Output
Return:
- source-of-truth map
- token/component drift findings
- planned changes and migration risks
- generated outputs/tests run
- unresolved design/code mismatches
- completion state: VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED

## Reject patterns
- copying Figma SDS component names as project architecture
- creating a second token source because it is convenient
- updating screenshot baselines merely to hide drift
- treating Code Connect as runtime behavior authority
- hand-editing generated token artifacts