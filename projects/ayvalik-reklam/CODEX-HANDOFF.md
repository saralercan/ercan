# Ayvalık Reklam — Codex Recovery Handoff (2026-10-02)

## Canonical baseline

This branch exists to preserve the recovered state of the Ayvalık Reklam WordPress work after the previous Codex session hit usage limits.

Verified from the recovered session log:

- Site: `hotpink-hamster-833576.hostingersite.com`
- WordPress installation: `30279926`
- Main plugin: `ayvalik-reklam`
- Live version after the last successful Codex deploy: `2.5.1`
- Deploy completed: 45/45 plugin files
- Customer panel canonical route: `admin.php?page=ayvalik-reklam-content`
- The earlier bare route `/wp-admin/ayvalik-reklam-content` was fixed.
- Codex then reproduced a WordPress critical error while rendering the panel's “İletişim ve temel site ayarları” section on PHP 8.3.
- Codex was hardening malformed/corrupt stored values and preparing a diagnostic runtime build when usage limits stopped the session.

## Important integrity boundary

The exact final 2.5.1 PHP source tree, final Codex ZIP and live PHP stack trace are not present in the recovered Library/GitHub materials. Do **not** reconstruct them from guesswork and do not treat the later 2.6.x prototype packages as the Codex baseline.

## Continued recovery work

A companion recovery candidate was built from the verified 2.5.1 behavioral state:

- Artifact: `ayvalik-reklam-codex-recovery-2.5.2.zip`
- SHA-256: `e8c04e48441274de9662290cced1ed56526e840d1f1a1b4a3c523c2c7dba9658`
- ChatGPT Library path: `/Ayvalik Reklam Mac Dosyalari/ayvalik-reklam-codex-recovery-2.5.2.zip`
- Library file id: `libfile_8f6edb6c9db48191ba00c3b643a0fc3f`

The recovery package is intentionally additive/companion-style and does not claim to be the missing original 2.5.1 source.

### Recovery behavior

- Reuses the canonical admin slug `ayvalik-reklam-content`.
- Removes/normalizes stale submenu entries and explicitly renders `admin.php?page=ayvalik-reklam-content`.
- Takes ownership of the page hook late in `admin_menu` so a stale 2.5.1 renderer cannot execute on the same hook.
- Normalizes malformed nested option shapes before render/save.
- Wraps the admin renderer in `Throwable` recovery and logs the exact exception to the WordPress error log.
- Keeps frontend changes opt-in per section.
- Adds sectioned management for Header, Hero, Banner, Services, Projects/Gallery, About, Contact, Footer and Settings.
- Services: 20 initial repeatable rows, max 50.
- Projects/Gallery: 20 initial repeatable rows, max 50.

## Strong root-cause hypothesis — not yet a confirmed stack trace

The recovered Codex notes say the fatal occurs in “İletişim ve temel site ayarları” and that malformed/corrupt stored values were being hardened. A nested option expected to be an array but saved as a scalar/string/null is therefore a strong PHP 8.3 TypeError candidate.

The recovery package normalizes exactly this failure mode. It must still be confirmed against the live error log before calling the root cause definitive.

## Recovered frontend DOM contract

The real stored Ayvalık Reklam preview confirms these targets:

- `.ar-hdr`
- `#ar-top`, `#ar-hero-kicker`, `#ar-hero-title-main`, `#ar-hero-title-accent`
- `.ar-hero-slide`, `.ar-hero-acts`
- `.ar-strip > .ar-strip-track`
- `#ar-hizmetler .ar-svc .ar-svc-row`
- `#ar-isler .ar-works .ar-work .ar-work-cap`
- `#ar-standart .ar-lead-line`
- `#ar-teklif .ar-quote-side`
- `.ar-ftr`

Observed in the recovered preview: 6 service rows and 9 project cards.

## QA completed on recovery candidate

PASS:
- PHP syntax
- admin JS syntax
- frontend JS syntax
- root scalar option -> safe defaults
- nested contact scalar -> normalized array
- nested footer null -> normalized array
- invalid repeatable row discarded
- services padded to 20
- projects padded to 20
- canonical menu URL restored
- legacy bare submenu slug removed
- legacy page hook replaced by recovery renderer
- real-preview selector/structure audit
- ZIP integrity

Review fixes:
- New project cards preserve the real `.ar-work-cap > div > h3/p + .ar-yr` markup.
- Contact updates are scoped to `#ar-teklif` and no longer mutate Footer while Footer management is disabled.
- A configured Hero image updates every hero slide so rotation cannot immediately restore an old image.

## QA still required before customer final delivery

Not verified in the current runtime:

1. Live wp-admin execution with the actual `ayvalik-reklam 2.5.1` plugin.
2. Exact PHP 8.3 stack trace/error log.
3. Panel open -> edit -> save -> reload -> persistence.
4. Media picker upload/change/remove.
5. Section enable/disable behavior against live HTML.
6. 390/430 px mobile render and desktop browser regression.
7. Every service page and contact/form flow.

Release status: **RECOVERY CANDIDATE — STATIC/STRUCTURAL QA PASS. NOT YET CUSTOMER FINAL.**
