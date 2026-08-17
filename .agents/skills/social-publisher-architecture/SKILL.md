---
name: social-publisher-architecture
description: Design or review a multi-channel social publishing/scheduling service with provider adapters, media state, retries, idempotency and metrics sync. Use for Instagram/Meta publishing automation, scheduler backends or Postiz-class architecture work.
---

# Social Publisher Architecture

Load `BRAND_SOCIAL.md` and current official provider API docs/samples for every provider in scope.

## Canonical model
`channel/integration → credential reference → media assets → content → provider settings → schedule/publish job → provider state → external post ID/permalink → metrics sync`.

## Procedure
1. List target channels and official provider capabilities; do not assume feature parity.
2. Define provider-neutral internal entities and provider-specific adapter boundaries.
3. Model explicit job states such as draft/scheduled/queued/uploading/processing/publishing/published/failed/cancelled where required by provider semantics.
4. Define idempotency key/duplicate prevention for publish actions.
5. Separate media upload/container creation from final publish when provider APIs require multi-step flows.
6. Add rate-limit handling, bounded retries/backoff, permanent-failure classification and reconciliation after ambiguous responses.
7. Persist external post IDs/permalinks and enough provider metadata to edit/delete/sync when supported.
8. Keep credentials/tokens out of model prompts/logs; provider access is least-privilege and refresh/revocation aware.
9. Use official Meta Business SDK/samples/docs as authority for Instagram/Meta; Postiz-class repos are architecture references only.
10. Define metrics sync separately from publish success and store metric timestamp/source.

## QA
- duplicate publish test
- retry after transient failure
- ambiguous-success reconciliation
- invalid/expired media handling
- rate-limit behavior
- scheduled time/timezone behavior
- edit/delete capability discovery
- wrong-account prevention
- permissions/token expiry
- provider webhook/event replay when used

## Output
Architecture diagram/model, provider capability matrix, state transitions, failure/retry rules, security notes, tests and completion state.