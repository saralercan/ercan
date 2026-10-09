# Vinterro One repository extraction — 2026-10-09

Status: **PREPARATION ONLY / NOT DEPLOYED**.

## Decision
- Keep `saralercan/ercan` as the shared, cross-project agent/CI standards control plane.
- Establish a distinct **private** `saralercan/vinterro-one` product repository after provisioning.
- Never delete or relocate working source code from the central repository until verified cutover, smoke/regression QA and rollback readiness.

## Source inventory (verified on `master`)
| Domain | Current location | Planned target |
| --- | --- | --- |
| Vinterro One plugin + router | `plugins/vinterro-one/` | Same path in target |
| Agent orchestration / paid media skills | `.agents/skills/reklam-ajansi*`, `.codex/agents/vinterro-*` | Product-specific selected agents/skills |
| Sales worker, supervision | `services/vinterro-sales-worker/`, `services/vinterro-supervision/` | `services/` |
| Supabase edge functions | `supabase/functions/ercan-os-api/`, `supabase/functions/vinterro-one-chatgpt-mcp/`, `supabase/functions/vinterro-one-supervision/` | `supabase/functions/` |
| Runtime project adapters | `projects/_runtime/` | `projects/_runtime/` |
| Agent manifests and CI | `docs/standards/VINTERRO_*`, `.github/workflows/vinterro-*`, scripts/tests | Selective, dependency-reviewed import |
| Application web frontend | **Not located in the current central Git tree** | Locate actual Git remote/Vercel source before import |

## Current required invariants
1. One canonical Reklam Ajansı, nine subskills and global dispatch triggers remain intact.
2. Shared `AGENTS.md` and cross-project CI contracts continue to live in the control plane; target repo pins audited refs instead of copying all global policy.
3. Secrets remain in managed secret stores; no database keys, Railway worker tokens or OAuth secrets committed.
4. No production Git remote changes, app deployments, SQL replay, live ads, budget changes, Gmail first-contact or external writes during import.
5. Use execution receipts and independent reviewer / release-gate evidence before moving any live service.

## Safe staging order
1. Create and confirm **private** `saralercan/vinterro-one` (GitHub repository provisioning is not currently exposed through the connected GitHub action interface).
2. Import product files on an unpublished branch, preserve folder paths while resolving dependencies.
3. Identify real Vinterro One web frontend source and which Railway/Vercel/Supabase services follow which repositories.
4. Run CI + security + routing + worker/supervision + browser QA.
5. Perform an explicit, reversible, one-service-at-a-time deployment cutover only with reviewed evidence.
6. Keep `saralercan/ercan` available as the rollback source until new repository operation is proven.

## Blocking facts
- The new `vinterro-one` remote does not yet exist / was not verified.
- Web application source and live deployments are not yet mapped to an exact Git commit.
- Passing a GitHub PR alone does not prove running Vinterro One agents, worker or marketing integrations.
