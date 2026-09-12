# Upstream review — Website Downloader adoption

Date: 2026-09-12
Decision: `ADOPT_WHEN_NEEDED`
Domain: web / migration / archival-reference capture / asset inventory
Stable identity decision: **NO NEW STABLE AGENT**. The repository is a JIT engine behind the existing web pod and `.agents/skills/site-mirror/SKILL.md`.

## Candidate

- Repository: `AhmadIbrahiim/Website-downloader`
- Reviewed branch: `master`
- Reviewed head: `130ad63d7163c19df64322556ca9c260eef353be`
- Latest reviewed head date: 2026-08-12
- License: MIT for the downloader software
- Runtime: Node.js + system `wget`; archive delivery over the app/socket flow

## Why it is useful

The project provides a compact full-site capture primitive that can support owner-authorized migration, offline reference/evidence capture, route/content/asset inventory and archival. It complements screenshot/reference tooling because it can collect HTML/CSS/JS/images and linked requisites rather than only rendered pixels.

It is intentionally not promoted as a permanent agent identity. Ercan OS stable identities remain function-first and replaceable-engine neutral; this engine is loaded only when mirroring materially helps a real task.

## Code/security review

Current upstream hardening observed in the reviewed code:
- uses `execFile` instead of interpolating the target into a shell command;
- accepts only HTTP(S) URLs with a hostname;
- creates a unique per-request working directory;
- scopes cleanup under the download root;
- supports a download quota (`100m` default) and wall-clock timeout (`300000` ms default);
- reports download failures instead of treating empty archives as success.

Residual production risk:
- protocol/hostname validation is **not** a complete SSRF boundary;
- a hosted/multi-user mirror must block loopback, RFC1918/private, link-local, multicast, unspecified and cloud-metadata destinations after DNS resolution;
- redirects must be revalidated and DNS rebinding must be defended against;
- ambient credentials/cookies/Authorization headers must not leak to arbitrary targets;
- mirrored HTML/JS/SVG/archives are untrusted input and must not be executed during ingestion;
- output paths and archives must remain traversal-safe and isolated.

## Rights/provenance boundary

The upstream downloader being MIT-licensed does not license the sites it can fetch. Captured third-party source, text, imagery, fonts and media retain their own copyright/license/contract constraints. Ercan OS may use legitimate public/authorized captures as evidence/reference, but does not infer republication rights from technical accessibility.

## Routing

When mirroring is justified:
`@Orchestrator → existing web/platform owner → web-production-specialist → site-mirror JIT → rebuild/migration implementation as needed → independent Browser/Accessibility/Performance/Production QA`.

Use `@UpstreamIntelligence` when the upstream must be refreshed/replaced or a current vulnerability/license/maintenance check is material.

## Adoption result

`ADOPT_WHEN_NEEDED` with mandatory network-safety, provenance and rights guardrails. Do not globally install or invoke for ordinary website work. Do not use it to bypass authentication/access controls or reach internal/private network resources.
