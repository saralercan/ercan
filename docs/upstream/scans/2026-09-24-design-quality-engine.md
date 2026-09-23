# Upstream Scan — Design Quality Engine

Date: 2026-09-24

## anthropics/skills — frontend-design
Observed: official Anthropic frontend design skill focused on intentional, product-specific visual direction, typography, layout and self-critique rather than generic AI aesthetics.
License observed for this skill: Apache-2.0.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

## emilkowalski/skills — apple-design
Observed: web-oriented translation of Apple fluid-interface and motion principles including response, direct manipulation, interruptibility, momentum and spatial consistency.
Repository license: MIT.
Decision: ADOPT_PATTERN_ONLY. Current Apple HIG remains platform authority.

## MengTo/Skills — beautiful-shadows
Observed: focused Tailwind-oriented layered neutral shadow patterns.
Repository license: MIT.
Decision: ADOPT_PATTERN_ONLY. Do not hard-code one global shadow recipe into every design.

## addyosmani/web-quality-skills — accessibility
Observed: evidence-led WCAG 2.2-oriented accessibility audit workflow combining Lighthouse/axe-style automation, accessibility tree and manual keyboard checks.
Repository license: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED beneath existing `@AccessibilityQA`.

## Superfuture/design-review
Observed: ranked design critique across hierarchy, type, spacing, color/contrast, motion, states, responsiveness, accessibility, content and brand. Skill includes anonymous telemetry and an optional license-gated server-backed Pro workflow.
README says MIT, but no standalone LICENSE file was found in the reviewed root/plugin paths.
Decision: ADOPT_PATTERN_ONLY. Do not import telemetry, Pro licensing/service calls or unverifiable license-sensitive implementation content.

## emilkowalski/skills — emil-design-eng
Observed: design engineering craft patterns covering motion choice, UI responsiveness, popover/origin behavior, state transitions and micro-polish.
Repository license: MIT.
Decision: ADOPT_PATTERN_ONLY.

## shadcn-ui/ui — shadcn
Observed: canonical project-aware skill for current shadcn CLI, component discovery/composition, presets, semantic tokens, forms, component structure and docs lookup.
Repository license: MIT.
Decision: ADOPT_WHEN_NEEDED / CANONICAL for shadcn projects.

## pbakaus/impeccable — adapt
Observed: responsive/adaptive workflow emphasizing context, input method, content priority, content-driven breakpoints, touch behavior and real-device verification. Repository consolidates older standalone interaction/responsive references into a broader skill.
Repository license: Apache-2.0.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

## jakubkrehel/skills — better-interface
Observed: orchestrated interface review across accessibility, layout, writing, typography, color and UI polish; evidence-first findings and root-cause consolidation.
Repository license: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

## interaction-design
The supplied item did not contain a resolvable canonical repository link. Current reviewed sources already cover interaction design via Emil motion/interaction patterns and Impeccable's consolidated animation/adaptation references.
Decision: SYNTHESIZED_LANE / NO_NEW_UPSTREAM_IDENTITY.

## Alishahryar1/free-claude-code
Observed separately from the design pack: MIT-licensed coding-agent/model router/proxy with multiple provider adapters, fallback routing and installer scripts. README claims ToS-friendly free-provider support, but individual provider free tiers/terms are volatile.
Decision: WATCHLIST / ADOPT_PATTERN_ONLY under developer-resource/provider discovery. Do not auto-install or route credentials through it without provider-by-provider current terms, security, privacy and local-proxy review.

## Architecture decision
Create one JIT `design-quality-engine` under existing frontend/design/accessibility/browser specialists. Do not add ten stable agents. Keep `free-claude-code` separate as a provider-router watchlist entry.
