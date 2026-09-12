---
name: site-mirror
description: Capture an authorized or public website into a local/offline reference package for migration, redesign evidence, asset inventory or archival. Use only when source mirroring materially helps the web task; never use it to bypass authentication, access controls or private-network boundaries.
---

# Site Mirror

Load `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`, `.agents/skills/web-production-specialist/SKILL.md`, and the active project/platform adapter. The reviewed upstream engine is `AhmadIbrahiim/Website-downloader`, classified `ADOPT_WHEN_NEEDED`.

## Stable routing owners
This is a JIT capability, not a new stable agent identity. Route through the existing web specialists that own the actual task:
- `@WebArchitecture` for migration/capture architecture and boundaries.
- `@ScreenshotToCode` only when the mirror is reference material for a rebuild or redesign.
- `@FrontendSystem` when captured structure/assets inform reusable UI implementation.
- `@BrowserQA`, `@AccessibilityQA`, and `@WebPerformance` for the rebuilt target as materially required.
- `@UpstreamIntelligence` when the upstream engine itself must be re-verified or replaced.

## Allowed uses
- Owner-authorized migration or disaster-recovery reference capture.
- Public-site offline snapshot for redesign/reference evidence.
- HTML/CSS/JS/image/font asset inventory before a rebuild.
- Link/route/content-structure discovery that does not bypass access controls.
- Archival of content the user is entitled to retain.

## Hard security boundaries
1. Accept only `http:` and `https:` targets.
2. Resolve DNS before the request and block loopback, RFC1918/private, link-local, multicast, unspecified and cloud-metadata destinations.
3. Re-resolve and re-validate every redirect target; protect against DNS rebinding.
4. Never forward ambient credentials, cookies, Authorization headers or internal proxy credentials to the mirrored target unless the user explicitly owns the target and the approved workflow requires those credentials.
5. Do not bypass authentication, paywalls, robots/access controls or anti-bot protections.
6. Preserve strict download quota, wall-clock timeout, per-job isolation and bounded concurrency.
7. Treat mirrored HTML, JavaScript, SVG, archives and other assets as untrusted input. Do not execute captured scripts as part of ingestion.
8. Sanitize archive paths and output names; prevent path traversal and writes outside the job directory.
9. Do not republish third-party code, copy or media merely because it was technically downloadable. Verify ownership/license/permission first.

## Upstream review baseline — 2026-09-12
- Repository: `AhmadIbrahiim/Website-downloader`.
- Reviewed master head: `130ad63d7163c19df64322556ca9c260eef353be`.
- License: MIT for the downloader software; mirrored site content retains its own rights.
- Current implementation already uses `execFile` rather than shell interpolation, validates HTTP(S), isolates request directories, scopes cleanup, and supports quota/timeout controls.
- Residual production concern: URL protocol validation alone is not sufficient SSRF protection for hosted/multi-user use; private-network/DNS/redirect enforcement remains mandatory in Ercan OS.

## Procedure
1. Confirm target ownership/authorization or that the requested capture is limited to legitimately public content.
2. Decide whether a full mirror is actually necessary; prefer a narrower page/reference capture when sufficient.
3. Re-verify upstream status/license/security when a production task depends on it.
4. Apply network guardrails before running any mirror engine.
5. Capture into a disposable isolated workspace with quota and timeout.
6. Inventory routes/assets/content and record provenance.
7. Feed only required evidence into the rebuild/migration flow; do not blindly deploy captured third-party code.
8. Rebuild using the active platform’s native architecture, then run independent browser/accessibility/performance QA.

## Completion evidence
Report target authorization basis, capture scope, upstream revision, network-safety checks, quota/timeout, inventory result, any blocked/skipped resources, provenance/rights notes, and final `VERIFIED/PARTIAL/BLOCKED/NOT VERIFIED` state. A successful mirror is not proof that the rebuilt site is production-ready.