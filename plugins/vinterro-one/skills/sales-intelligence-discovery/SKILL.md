---
name: sales-intelligence-discovery
description: Discover and enrich company-level Vinterro Digital prospects from public business evidence. Use for prospect discovery, Vinterro Keşif sales scans, broken/missing website prospecting, company enrichment, market scans and qualified lead-pool building. Does not send outreach.
---

# Sales Intelligence Discovery

Owner: `Sales Intelligence Agent / Satış İstihbarat Ajanı`.

## Purpose

Find businesses with a concrete, evidence-backed Vinterro Digital opportunity and return company-level intelligence that can survive independent QA.

Use this skill for:
- new prospect discovery;
- "web sitesi olmayan / bozuk işletmeleri bul";
- Vinterro Keşif -> Vinterro Digital prospecting;
- market/region/category scans;
- company-level firmographic/technographic enrichment;
- public-business contact verification;
- trigger/signal scans that support a sales hypothesis.

Do not use it to send email, DM, ads, CRM mutations or autonomous follow-ups.

## Mandatory load order

1. repository root `AGENTS.md`
2. `docs/standards/VINTERRO_SALES_INTELLIGENCE_AGENT.md`
3. this skill
4. `.agents/skills/website-opportunity-audit/SKILL.md` when website condition is material
5. `.agents/skills/sales-lead-qualification/SKILL.md`
6. current Vinterro One / AutoGTM / Gmail history evidence when dedupe is needed
7. independent reviewer for material shortlist claims

## Discovery hierarchy

Prefer, in order:
1. official business website / owned domain;
2. official business social/profile;
3. official tourism/chamber/municipality/association/business directories;
4. connected Vinterro Keşif / AutoGTM / CRM records;
5. reputable booking/marketplace/profile pages for public business facts;
6. broad web search only to close a specific evidence gap.

Do not treat scraped directories, lead farms or SEO spam pages as identity authority.

## Identity resolution

Normalize the account before qualification:
- canonical business/brand name;
- city/region/country;
- current and old/redirected domains;
- official social handles;
- public business emails;
- booking/store URLs;
- aliases and transliterations.

A different email or domain does not automatically create a new account.

## Contact rules

Allowed:
- public business email explicitly published for the business;
- public role/team email;
- public business phone/social channel when email is unavailable.

Forbidden:
- guessed `info@`, `hello@`, first-name or pattern-generated emails;
- hidden/private personal data;
- credit-consuming personal-contact enrichment without prior explicit user approval;
- treating a third-party email as the business email without identity evidence.

## Discovery output

Every candidate must retain:
- business name;
- location;
- category;
- official source(s);
- owned website/domain state;
- public contact + provenance;
- opportunity hypothesis;
- duplicate/contact-history state;
- confidence;
- next skill/handoff.

A candidate may remain `SOCIAL_ONLY` or `CONTACT_UNRESOLVED`; never fabricate data to fill quota.

## Coverage honesty

A bounded scan is never "all businesses" unless the source itself is a complete bounded registry and every row was processed. State the scan boundary and unresolved gaps.
