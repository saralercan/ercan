# Upstream Scan — Adaptive Capability Pack

Date: 2026-09-24
Scope: five GitHub skill repositories supplied for Ercan OS capability expansion.

## Findings

### bevibing/tutor-skills
Observed: document/codebase learning modes, StudyVault generation, active-recall quiz flow, concept-level progress and weak-area drilling.
License observed: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Reason: useful teaching architecture; Claude/Obsidian-specific UX and storage must remain optional.

Note: the README references `RoundTable02/tutor-skills` in install examples while the reviewed accessible repository path is `bevibing/tutor-skills`. Treat canonical ownership as a runtime re-check before vendoring.

### ZeroPointRepo/youtube-skills
Observed: `youtube-full` skill for transcripts, video/channel search, channel feeds, playlists and related read-only research through TranscriptAPI.
License observed: MIT.
Dependency: `TRANSCRIPT_API_KEY` and network access.
Decision: ADOPT_WHEN_NEEDED as a read-only intelligence provider under the existing YouTube Growth Engine.
Do not treat as publishing/account management.

### ehmo/platform-design-skills
Observed: platform-specific rules for iOS, iPadOS, macOS, watchOS, visionOS, tvOS, Android and Web; sources include Apple HIG, Material Design 3, WCAG 2.2 and MDN.
License observed: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Reason: strong routing/checklist value, but distilled rules can lag normative guidance; official current platform docs remain authority.

### GanyuanRan/Aegis
Observed: method pack with fast-path discipline, goal framing, systematic debugging, canonical-owner repair, minimality and verification-before-completion patterns.
License observed: MIT.
Decision: ADOPT_PATTERN_ONLY as Execution Governance.
Reason: aligns with Ercan OS evidence/QA philosophy; must not become a second policy authority or mandatory ceremony layer.

### ognjengt/founder-skills
Observed: SOP, CRO, hooks, lead magnets, strategic planning, GTM, outreach, competitor intelligence, copy, pricing, PRD and marketing-idea workflows.
License observed: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Reason: broad founder workflow coverage overlaps existing Ercan OS roles; route through existing owners rather than create duplicate stable agents. Promotional outcome claims are not adopted.

## Architecture decision
Create five JIT skills and one shared Adaptive Capability Pack standard. Preserve the 52 stable routing identities. Add YouTube retrieval as an optional provider beneath the existing YouTube Growth Engine, not a replacement engine.

## Security / supply chain
No upstream repository is installed or executed by this integration. Only reviewed workflow patterns and provider boundaries are represented in Ercan OS instructions. Runtime installation requires separate provenance, permission, network/secrets and maintenance review.
