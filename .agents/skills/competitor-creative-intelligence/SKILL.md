---
name: competitor-creative-intelligence
description: Research public competitor ads, extract observable hooks/angles/offers/formats, and turn them into original brand-safe creative briefs without copying protected creative expression or inventing performance claims. Use for Meta Ad Library research, competitor creative monitoring, ad swipe files, recurring creative intelligence, or Rerun-based competitor-ad workflows.
---

# Competitor Creative Intelligence

This is a JIT capability under the existing Meta/brand/social specialists. It does not create a new stable identity.

## Stable-owner mapping
- source collection / Meta Ad Library -> `@AdsCreativeStrategist + @MetaAdsEngineer`
- creative pattern analysis -> `@AdsCreativeStrategist + @BrandSystemArchitect`
- original concept/brief generation -> `@BrandSystemArchitect + @BrandBehavior`
- recurring managed run -> `managed-agent-deployment` when useful
- independent QA -> `@BrandComplianceQA + @MetaMeasurement`

## Core rule

**Observe competitor advertising; do not clone competitor expression.**

Allowed:
- identify recurring hooks, angles, offer structures, formats, CTA patterns, proof styles, landing-page patterns, pacing, framing and category whitespace;
- create an original brief that applies those abstract patterns to the user's own brand/product;
- cite/retain source ad URLs/IDs for research provenance.

Do not:
- reproduce competitor copy verbatim beyond short research excerpts;
- copy logos, trademarks, distinctive layout, photography, video, characters, voice, music, packaging or trade dress into a new ad;
- pass off a derivative as original;
- infer private audience, spend, ROI, conversions or targeting when Meta does not expose them.

## Evidence schema

For each observed ad, record where available:
- advertiser/page name + Page ID
- Meta Ad Library ID / permanent library URL
- observed date and market/country filter
- active/inactive status
- first delivery/start date
- publisher platforms
- format/media type
- visible primary copy/hook
- visible offer/CTA
- landing page/destination
- number of visible variants/collations when actually available
- source screenshot/media reference only when lawful/necessary for analysis
- evidence status: OBSERVED / INFERRED / UNKNOWN

## Performance language

Ad longevity, repeated variants or multiple collations are **signals of persistence**, not proof of profitability.

Never state:
- “winner”
- “profitable”
- “best performing”
- “high ROAS”
unless backed by actual performance data.

Use language such as:
- “long-running”
- “repeated”
- “widely varied”
- “worth testing as a hypothesis”

Meta's public Ad Library exposes ad creative and delivery metadata, but ordinary commercial ads do not generally expose complete spend/ROI/conversion performance.

## Analysis workflow

`competitor set -> market/filter -> public ad collection -> normalize/dedupe -> evidence table -> abstract creative patterns -> whitespace -> original hypotheses -> brand-safe brief -> test plan -> measurement loop`

Analyze across multiple competitors where possible so one brand's idiosyncrasies are not mistaken for category truth.

## Original brief output

The final brief should contain:
- audience/problem state
- original hook
- original angle
- offer/proof structure
- format/placement
- storyboard/layout direction
- CTA
- landing-page match
- what was learned from competitor evidence
- what is deliberately different/original
- test hypothesis
- KPI/decision rule
- IP/brand-policy check

The brief must be usable without reproducing the competitor asset.

## Rerun route

The supplied Rerun template slug `recreate-competitor-ads-meta` is treated as a managed-workflow reference, not a permission to clone ads.

When deployed through Rerun:
- use Rerun for recurring collection, scheduling, Box isolation, approvals and live visibility;
- keep Ercan OS as policy/brief/eval source of truth;
- require approval before consequential publishing/spend actions;
- verify the exact current connector/data-source mechanism because the template page itself may change;
- never publish generated creative automatically merely because research finished.

## Optional Novoads pattern

Reviewed `novoads/agent-skills:spy-competitor-ads` (MIT) is a useful optional vendor pattern for collecting Meta Ad Library evidence. It is not required.

Useful patterns:
- permanent Ad Library URL as durable provenance;
- download expiring media immediately when a paid API returns expiring CDN links;
- estimate cost before paid sweeps;
- distinguish page running the ad from the queried brand;
- zero-result sweep is a valid result;
- do not treat server ranking as performance proof.

Any Novoads use requires current plan/API availability and explicit cost approval.

## Completion

VERIFIED requires:
- public source provenance retained;
- observation vs inference separated;
- no invented performance metrics;
- final concepts materially original;
- brand/product truth preserved;
- Meta/platform policy checked where material;
- test plan defined;
- independent brand/ad QA completed.
