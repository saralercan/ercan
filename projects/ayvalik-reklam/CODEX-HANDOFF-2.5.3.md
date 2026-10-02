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
SHA-256: d302ccb9a782c3d8e6ea1a36006956b80452eb9422385e7f0894688080a851b0

Stable WordPress plugin folder:
- ayvalik-reklam-codex-recovery

## 2.5.3 safety hardening
- Zero-touch activation gate: when all managed sections are disabled (default), no frontend recovery JS is enqueued.
- Activation alone therefore does not patch Header, Hero, Banner, Services, Projects, About, Contact or Footer.
- Existing site content remains the source of truth until an administrator explicitly enables a section.
- Malformed nested option values are normalized instead of reaching the renderer as scalar/null values.
- PHP 8.3 missing collection-mode warning fixed.
- Recovery now claims both hidden admin_page and legacy parent page hooks for ayvalik-reklam-content, without touching global admin hooks.
- Admin renderer is wrapped in Throwable recovery and logs exact exception details.

## Existing-content import and safe sync
- “Mevcut içeriği içe aktar” reads the current homepage from the same WordPress origin.
- It only populates the form: it does not save, enable sections, or alter the public site.
- Imported Service and Project/Gallery rows are enabled inside the form, while their parent sections remain disabled.
- Default collection mode is sync:
  - update existing cards by stable row index,
  - append new rows after existing cards,
  - do not delete unmatched existing cards.
- Inactive intermediate rows do not shift later rows onto the wrong existing card.
- Replace mode remains available but is not the safe default.

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
- live-content import button
- client JS max: 50 rows
- server sanitizer hard cap: 50 rows
- mobile admin breakpoints: 960 px and 720 px

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
- legacy parent page hook claimed
- hidden admin page hook claimed
- global admin hooks untouched
- bare submenu slug removed
- canonical submenu URL restored
- rendered admin section/navigation contract
- recovered frontend selector contract

## Important remaining gate
This candidate is NOT customer-final yet because this ChatGPT session does not expose the Hostinger WordPress/Hosting MCP actions. The explicitly selected Hostinger connector skill is loaded, but scoped tools such as hosting_listWebsitesV1 and WordPress management/deploy actions are absent from the active tool surface.

Before any Hostinger write:
1. read current live state,
2. identify the exact site/account/resource from Hostinger list calls,
3. preserve a rollback point,
4. ask for one explicit confirmation naming the exact recovery-plugin write,
5. deploy only the recovery plugin,
6. verify wp-admin panel open/import/save/reload,
7. verify public desktop/mobile rendering and all main service/contact flows,
8. purge caches only after validation.

Do not call the work final until those live checks pass.
