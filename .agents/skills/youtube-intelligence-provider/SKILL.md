---
name: youtube-intelligence-provider
description: Retrieve YouTube transcripts, video/channel search results, channel feeds and playlist evidence for research and channel intelligence when an authorized provider is available. Use as an evidence provider under the existing YouTube Growth Engine; never treat it as publishing/account-management capability.
---

# YouTube Intelligence Provider

This JIT provider supplements `.agents/skills/youtube-growth-engine/SKILL.md`. It does not replace strategy, packaging, analytics interpretation, publishing QA or monetization governance.

## Stable-owner mapping
- Research queries -> `@SocialStrategy + @AEO_GEO`
- Channel/competitor evidence -> `@SocialAnalytics + @SocialStrategy`
- Transcript evidence -> task researcher + factual QA
- Topic/format mining -> `@SocialStrategy + @ContentRecycling`
- Provider/auth boundary -> `@Orchestrator`

## Provider model
Reviewed upstream: `ZeroPointRepo/youtube-skills` — MIT.

Its `youtube-full` skill exposes transcript, video search, channel resolution/info/feed/search, playlist and community/section retrieval through TranscriptAPI. It requires network access and a `TRANSCRIPT_API_KEY`.

## Routing rules
1. Load this provider only when YouTube evidence materially improves the task.
2. Prefer official YouTube/Google surfaces when they directly provide the required authoritative fact.
3. Treat TranscriptAPI as a replaceable third-party data provider, not platform authority.
4. Never request, expose or persist API keys in logs/artifacts.
5. If no provider credential is available, fall back to other available public/research tooling and mark unavailable evidence honestly.
6. Transcript availability is not proof of completeness, speaker identity, factual truth or endorsement.
7. Separate observed metrics/metadata from strategic interpretation.
8. This provider is read/research only. It does not authorize upload, edit, comment, monetization, account or channel mutation.
9. Volatile endpoint limits, pricing, credit costs and provider schemas must be checked at runtime rather than frozen into Ercan OS policy.
10. For competitor intelligence, avoid copying creators' scripts or protected expressive content; extract ideas, facts, structures and public signals at an appropriate abstraction level.

## Typical flow
`research question -> search/channel shortlist -> metadata/transcript evidence -> claim/topic extraction -> cross-check -> YouTube Growth Engine strategy/production decision`

## Completion evidence
Record query, provider/source, timestamp when material, selected videos/channels, transcript/metadata coverage, uncertainty, downstream decision and final state.
