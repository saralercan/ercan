# Ercan OS — Adaptive Capability Pack

Status: active
Date: 2026-09-24

Purpose: integrate five reviewed GitHub skill sources into Ercan OS as narrow JIT capabilities without increasing the stable routing identity count.

## Stable identity rule
The stable routing surface remains **21 Stable Core + 31 GitHub Specialist v3 Extension = 52 named stable routing identities**. The capabilities in this pack are JIT lanes/providers only.

## Included capabilities

| Capability | Ercan OS skill | Reviewed upstream | Adoption |
|---|---|---|---|
| Learning / tutoring | `learning-tutor-engine` | `bevibing/tutor-skills` | ADOPT_PATTERN_ONLY / WHEN_NEEDED |
| YouTube intelligence | `youtube-intelligence-provider` | `ZeroPointRepo/youtube-skills` | ADOPT_WHEN_NEEDED |
| Platform design | `platform-design-intelligence` | `ehmo/platform-design-skills` | ADOPT_PATTERN_ONLY / WHEN_NEEDED |
| Execution governance | `execution-governance` | `GanyuanRan/Aegis` | ADOPT_PATTERN_ONLY |
| Founder operations | `founder-operations` | `ognjengt/founder-skills` | ADOPT_PATTERN_ONLY / WHEN_NEEDED |

All five reviewed repositories exposed MIT licensing at review time. License status, maintenance and canonical ownership remain runtime-verifiable upstream facts.

## Cross-capability routing

### "Teach me this"
`@Orchestrator -> learning-tutor-engine -> domain specialist -> diagnostic/active recall -> progress evidence`

### YouTube research/growth
`youtube-intelligence-provider (when available) -> youtube-growth-engine -> @SocialStrategy/@SocialAnalytics/@AEO_GEO -> publishing/measurement owners as needed`

### Platform-specific UI
`platform-design-intelligence -> web/mobile implementation owner -> accessibility/performance -> browser/mobile QA`

### Bug/regression/risky implementation
`execution-governance -> canonical implementation owner -> proportional tests -> independent QA -> retirement/cleanup evidence`

### Founder operating request
`founder-operations -> existing sales/marketing/product/research owners -> artifact/action -> metric/review trigger`

## Authority boundaries
- Community repositories are references/providers, never Ercan OS policy authority.
- User/project rules, root `AGENTS.md`, platform standards and project adapters outrank these packs.
- Official current platform documentation outranks distilled platform-design rules.
- TranscriptAPI is a replaceable third-party read provider and requires explicit runtime credential availability.
- Aegis patterns may improve engineering discipline but do not replace Ercan OS completion authority.
- Founder marketing language is treated as workflow inspiration, not performance guarantee.
- Tutor host-specific UX/storage assumptions are not imported as mandatory Ercan OS behavior.

## Supply-chain rules
1. Do not globally install or execute upstream code merely because a repository is listed here.
2. Review scripts, permissions, network behavior and secrets before any runtime installation.
3. Keep API credentials out of logs, artifacts, prompts committed to Git and user-visible exports.
4. Re-check license/canonical repo/maintenance before vendoring code.
5. Prefer narrow reimplementation of patterns over copying large host-specific instruction sets.

## Completion state
Use VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED. A capability being listed or routed does not mean its upstream engine actually ran.
