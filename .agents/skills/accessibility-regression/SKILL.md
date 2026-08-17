---
name: accessibility-regression
description: Run risk-appropriate accessibility regression review for web/UI changes using automated detection plus manual keyboard/focus/semantic checks. Use after material UI changes, component refactors, forms, menus, dialogs, account/cart flows or design-system changes.
---

# Accessibility Regression

## Principle
Automated scans detect a subset of accessibility problems. Never convert a clean axe result into “accessible” without the task-relevant manual checks.

## Procedure
1. Identify critical routes/components/states changed.
2. Run available automated scanner (axe-core or equivalent) in real browser states.
3. Review violations and `incomplete`/needs-review findings; do not suppress without evidence.
4. Keyboard test: tab order, skip/navigation, menus/dialogs, focus trap/return, escape/close, actionable controls.
5. Focus visibility: ensure current focus is visually clear and not hidden by sticky UI.
6. Semantics: headings/landmarks, names/roles/values, button-vs-link intent, form labels/descriptions/errors.
7. Visual: contrast/readability, zoom/reflow, text clipping and non-color status cues where relevant.
8. Dynamic UI: loading/error/validation/live updates have understandable state changes where needed.
9. Record automated and manual evidence separately.

## Output
- routes/states tested
- automated findings
- manual keyboard/focus findings
- semantic/form findings
- unresolved blockers
- VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED

## Never
- waive a failure because the design matches a screenshot
- remove keyboard/focus behavior to satisfy a visual baseline
- hide axe rules globally without a documented false-positive rationale
- claim WCAG conformance from automation alone