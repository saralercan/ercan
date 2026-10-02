# Ayvalık Reklam — Codex Recovery 2.5.3 Handoff

Date: 2026-10-02
Branch: ayvalik-reklam-codex-recovery-2026-10-02

## Verified Codex baseline
- Live target: hotpink-hamster-833576.hostingersite.com
- WordPress installation previously identified by Hostinger: 30279926
- Main live plugin after the last successful Codex deploy: ayvalik-reklam 2.5.1
- Last successful deploy: 45/45 plugin files
- Canonical customer-panel route: admin.php?page=ayvalik-reklam-content
- The earlier bare /wp-admin/ayvalik-reklam-content route problem was fixed.
- Remaining Codex blocker: PHP 8.3 critical error while rendering “İletişim ve temel site ayarları”.
- Exact final live 2.5.1 source tree and stack trace are still not recovered. Do not invent them.

## Current recovery candidate
Artifact: ayvalik-reklam-codex-recovery-2.5.3.zip
Library: /Ayvalik Reklam Mac Dosyalari/ayvalik-reklam-codex-recovery-2.5.3.zip
Library id: libfile_b046168c08c08191bfeb0b383702b4ff
SHA-256: 2d490bb29e9fd1158786d382d069a499c01215e093fcaeda125498f348b77772

Stable WordPress plugin folder:
- ayvalik-reklam-codex-recovery

## 2.5.3 safety hardening
- Zero-touch activation gate: when all managed sections are disabled (default), no frontend recovery JS is enqueued.
- Activation alone therefore does not patch Header, Hero, Banner, Services, Projects, About, Contact or Footer.
- Existing site content remains the source of truth until an administrator explicitly enables a section.
- Default collection mode is append, not replace.
- PHP 8.3 missing mode warning fixed.
- Malformed nested option values are normalized instead of reaching the renderer as scalar/null values.
- Admin renderer is wrapped in Throwable recovery and logs exact exception details.

## Customer panel contract rendered and verified
Navigation/sections:
1. Genel
2. Header
3. Hero
4. Banner
5. Hizmetler
6. Projeler / Galeri
7. Hakkımızda
8. İletişim
9. Footer
10. Ayarlar

Rendered default panel:
- 20 service rows
- 20 project/gallery rows
- 45 media-picker controls
- 48 textarea/description fields
- two “add new record” workflows
- client JS max: 50 rows
- server sanitizer hard cap: 50 rows
- mobile admin breakpoint: 960 px

## Recovered public DOM contract
Verified against the stored real Ayvalık Reklam preview:
- .ar-hdr
- #ar-top
- .ar-strip-track
- #ar-hizmetler .ar-svc
- #ar-isler .ar-works
- #ar-standart
- #ar-teklif .ar-quote-side
- .ar-ftr
- 6 existing service rows
- 9 existing project cards
- 3 hero slides
- 3 about-title lines

## Local QA PASS
- PHP syntax
- admin JS syntax
- frontend JS syntax
- ZIP integrity
- all enqueued asset files exist
- default activation enqueues no frontend patch
- enabling one section enqueues exactly one frontend patch
- malformed contact scalar -> safe array
- null footer -> safe array
- service collection padded to 20
- valid rows preserved
- service sanitizer caps at 50
- rendered admin section/navigation contract
- recovered frontend selector contract

## Important remaining gate
This candidate has NOT yet been declared customer-final because the current ChatGPT session does not expose the Hostinger WordPress/Hosting MCP tools. The selected Hostinger connector currently exposes no scoped hosting_listWebsitesV1 / WordPress management actions here.

Before any Hostinger write:
1. read current live state,
2. name the exact site/account/resource,
3. get one explicit confirmation for the write,
4. preserve a rollback point,
5. deploy only the recovery plugin,
6. verify wp-admin panel open/save/reload,
7. verify public desktop/mobile rendering and all main service/contact flows,
8. purge caches only after validation.

Do not call the work final until those live checks pass.
