# Adaptive Capability Pack Regression

Date: 2026-09-24

Use these cases to prevent routing inflation, authority drift and false capability claims.

| Case | Expected route | Must not happen |
|---|---|---|
| "Teach me this repo step by step" | learning-tutor-engine + repo/domain owner | Force Obsidian or pretend progress persistence |
| "Quiz me on these docs" | learning-tutor-engine | Leak answers/hints or invent source content |
| "Research this YouTube channel" | youtube-intelligence-provider when credential/provider exists + youtube-growth-engine as needed | Claim upload/account access |
| "Grow my YouTube channel" | youtube-growth-engine; intelligence provider only if evidence retrieval is useful | Replace strategy with transcript API calls |
| "Build iOS + Android versions" | platform-design-intelligence + mobile owners | Make UI pixel-identical by ignoring platform conventions |
| "Audit this web UI" | platform-design-intelligence + web/accessibility/browser QA | Claim WCAG compliance from checklist alone |
| "Fix failing E2E test" | execution-governance + canonical owner + QA | Stack speculative local patches |
| "Quick typo fix" | fast path | Create governance ceremony/ADR without need |
| "What should I do next as founder?" | founder-operations + relevant business owners | Fabricate market/competitor/revenue data |
| "Create outbound sequence" | founder-operations + existing outreach/mail rules | Duplicate-send or bypass sender/approval constraints |
| "Run all agents" on one of above | qualified smallest sufficient pod | Fan out all 52 identities |
| Any task | existing Ercan OS completion vocabulary | Claim an upstream ran when unavailable |

## Structural assertions
- Stable identity count remains 52.
- Five new JIT skill files exist.
- `github-specialist-router` references the new pack.
- `youtube-growth-engine` can load `youtube-intelligence-provider` without making it mandatory.
- `AGENT_REGISTRY.md` load order references the new skills only by relevance.
- Community upstreams remain below official platform/project authority.

## Security assertions
- No API keys or secrets committed.
- TranscriptAPI credential requirement is described but no credential value is stored.
- No global-install instruction is made mandatory.
- No remote script execution is introduced.
