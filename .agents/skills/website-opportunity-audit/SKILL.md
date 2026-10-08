---
name: website-opportunity-audit
description: Passively verify whether a prospect has no owned website, an unavailable/broken site, or a weak commercial web journey. Use for sales-intelligence website opportunity classification. No intrusive security testing.
---

# Website Opportunity Audit

Owner: `Sales Intelligence Agent / Satış İstihbarat Ajanı`.

## Goal

Turn "site yok / site bozuk" into a defensible commercial signal, not a guess.

## Classification

Use exactly one primary status:
- `NO_OWNED_SITE_FOUND` — no owned domain found after bounded current-source research; never claim metaphysical certainty that no site exists;
- `DOWN_OR_UNREACHABLE` — owned domain currently fails normal public access;
- `DNS_TLS_OR_REDIRECT_FAILURE` — clear DNS, TLS/certificate, redirect-loop or canonical-host failure;
- `BROKEN_RENDER_OR_CORE_FLOW` — homepage/core navigation/contact/booking flow materially fails in a normal browser;
- `COMMERCIAL_JOURNEY_WEAK` — site works but the relevant conversion path is materially weak or missing;
- `HEALTHY_OR_NO_CLEAR_GAP` — no material web opportunity proven;
- `UNKNOWN` — evidence is ambiguous, blocked by bot protection, temporary provider error or insufficient access.

## Passive checks only

Allowed:
- public DNS/HTTP(S) reachability;
- final URL and redirect behavior;
- TLS/certificate existence as observed by normal browser/request tooling;
- 404/5xx/parked-domain evidence;
- normal desktop/mobile browser rendering;
- navigation, contact, reservation, ecommerce or enquiry journey;
- basic public page metadata/indexability signals when relevant.

Forbidden:
- port scanning;
- vulnerability exploitation;
- brute force;
- authentication bypass;
- hidden endpoint enumeration;
- destructive load/performance tests;
- any intrusive security probe.

Security concerns discovered incidentally are handed to the security lane, not tested further.

## Evidence rules

For `DOWN_OR_UNREACHABLE` or `DNS_TLS_OR_REDIRECT_FAILURE`, prefer two current modalities when practical (for example browser + HTTP/search evidence).

A bot/WAF challenge, geo block or tool-specific 403 is `UNKNOWN` unless normal-user failure is independently verified.

A visually old site is not automatically broken. Separate:
- technical failure;
- usability/conversion weakness;
- aesthetic preference.

## Commercial opportunity evidence

Examples:
- no owned web presence while business is visibly active;
- broken booking/contact/enquiry flow;
- domain parked/expired or wrong destination;
- mobile navigation makes core action unusable;
- no clear reservation/sales/contact path for a high-intent business;
- major language/locale mismatch for an international-demand business.

Never invent analytics, traffic, conversion rate, revenue loss or SEO penalties.

## Freshness

Website-state evidence used for production outreach should be rechecked within 24 hours of send. A previously broken site that is now healthy must not be described as broken.
