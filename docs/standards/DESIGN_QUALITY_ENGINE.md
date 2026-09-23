# Ercan OS — Design Quality Engine

Status: active
Date: 2026-09-24

## Purpose

Provide a single JIT design-quality layer for premium frontend direction, interaction craft, responsive adaptation, accessibility, component composition and independent interface review.

Execution skill: `.agents/skills/design-quality-engine/SKILL.md`.

The stable routing surface remains **21 Stable Core + 31 GitHub Specialist v3 Extension = 52**. These design lanes are capabilities, not new agents.

## Authority order

1. user/project brief, brand system and do-not-touch constraints
2. current platform/accessibility standards
3. project design system/tokens/components
4. Ercan OS design-quality and QA contracts
5. reviewed third-party design skills/patterns

No third-party design skill may silently replace the project's visual identity.

## Reviewed upstreams

| Source | Use | Decision |
|---|---|---|
| `anthropics/skills:frontend-design` | distinctive frontend direction | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |
| `emilkowalski/skills:apple-design` | fluid/physical interaction reference | ADOPT_PATTERN_ONLY |
| `MengTo/Skills:beautiful-shadows` | surface/elevation patterns | ADOPT_PATTERN_ONLY |
| `addyosmani/web-quality-skills:accessibility` | WCAG-oriented accessibility workflow | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |
| `Superfuture/design-review` | prioritized evidence-led UI critique | ADOPT_PATTERN_ONLY |
| `emilkowalski/skills:emil-design-eng` | design-engineering polish/motion | ADOPT_PATTERN_ONLY |
| `shadcn-ui/ui:shadcn` | canonical shadcn project/component workflow | ADOPT_WHEN_NEEDED / CANONICAL |
| `pbakaus/impeccable:adapt` | responsive/adaptive workflow | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |
| `jakubkrehel/skills:better-interface` | holistic review orchestration | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |
| `wshobson/agents:interaction-design` | microinteractions, feedback, motion and gesture patterns | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED |

Interaction Design now has a reviewed canonical upstream. Ercan OS still combines it with Emil/Impeccable patterns and existing platform/accessibility standards rather than treating any single community skill as universal interaction authority.

## Design implementation flow

`scope -> brief/brand -> thesis/tokens -> component architecture -> implement -> adapt -> interaction/motion -> accessibility -> rendered critique -> browser/visual QA`

### Thesis before code
For material visual work, define what makes this interface specific to the product. A premium result should not be an accumulation of fashionable effects.

### Component discipline
Use existing project components first. In shadcn projects, inspect `components.json`, installed components, project base, Tailwind version and current official docs before adding/updating components.

### Interaction discipline
Feedback should be immediate and state changes understandable. Gesture-driven motion should be interruptible where practical. Reduced-motion behavior must preserve meaning.

### Responsive discipline
Verify the experience at representative content-driven breakpoints, not only preset device sizes. Check pointer/touch/keyboard assumptions separately from viewport width.

### Review discipline
Visual claims require rendered evidence. Code-level claims require source evidence. Rank defects by user impact; do not turn personal stylistic preference into a blocker.

## Completion gate

Material interface work is VERIFIED only when:
- project visual source of truth is identified;
- the rendered result is inspected;
- representative responsive states are checked;
- critical interaction states work;
- accessibility is checked automatically where useful and manually where required;
- no critical console/runtime failure remains;
- relevant performance impact is acceptable;
- independent design/browser QA ran;
- remaining tradeoffs are explicit.
