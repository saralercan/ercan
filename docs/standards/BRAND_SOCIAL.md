# Brand, Graphic Design & Instagram Operating Standard

## Brand source of truth
Brand = strategy + positioning + personality + voice + messaging + logo system + color roles + typography roles + imagery + iconography + layout/grid + motion + channel behavior.

Recommended source structure: `brand/{strategy,logos,colors,typography,imagery,icons,voice,templates,examples/good,examples/bad,export-specs}`.
Approved assets are authoritative; deprecated assets are not reused.

## Design system
- Use semantic design tokens for color/type/spacing/radius/border/shadow/motion where useful.
- Map design roles across Figma/code/Shopify/WordPress/social instead of maintaining unrelated palettes.
- Preserve editable masters; exports are derivatives, not source masters.
- Logo rules: approved variants, clear space, minimum size, background suitability; no arbitrary recolor/stretch/skew/shadow/3D/rotation/crop.
- If the brief says logosuz, do not invent a replacement mark or leave a fake logo placeholder.

## Art direction and anti-template quality
- Establish focal point, reading order, grid/alignment, whitespace rhythm and controlled repetition.
- Generic AI/template patterns are failure signals when distinctive agency work is required: purposeless gradients/glows, generic glass cards, random blobs, fake premium stock people, meaningless brush/grain, repeated prompt-art compositions.
- A design should still feel brand-owned when the logo is mentally removed.
- Imagery must share coherent lighting/crop/perspective/color treatment; generated humans/products require anatomy, geometry, label/material and shadow QA.

## Creative provider routing
Generative providers are optional production tools, not a replacement for the brand system or art direction.
- Load `LUMA_CREATIVE_PROVIDER.md` only when multi-reference generation/editing or generative video materially benefits the task.
- Prefer approved project references over open-web inspiration for final brand production.
- Exact typography, logo geometry, layout, tokenized color/type and deterministic exports should remain in Figma/Canva/code/graphics tooling when precision matters.
- A generated image/video is a candidate artifact until independent evaluator + channel QA pass.
- Provider choice should follow task fit, not novelty. Keep the creative system provider-agnostic so another model can replace Luma without changing the brand contract.

## Design evaluator
Separate generator and evaluator where material. Evaluate:
1. Brand fit
2. Hierarchy
3. Originality
4. Craft (spacing, alignment, type, crop, contrast)
5. Message clarity
6. Channel fit
7. Accessibility/readability
8. Asset integrity
9. Campaign cohesion
10. Production/export readiness
Evaluator returns actionable findings; it does not replace browser/interaction QA.

For generative output also evaluate reference fidelity, product/person integrity, unintended layout/logo/text drift and whether a concept/mockup is being misrepresented as a real product/customer asset.

## Visual QA evidence ledger
Material UI/graphic/reference-matching work should leave an inspectable QA artifact, not only a chat claim. Recommended evidence fields:
- **Comparison target:** authoritative reference screenshot(s), approved design or brand source.
- **Implementation evidence:** final screenshot/export/preview path or URL.
- **Viewport / channel / state:** exact viewport, device class, route/screen, interaction state and any wait/loading condition required to reproduce the comparison.
- **Intended state:** what should be visually/functionally true.
- **Full-view comparison:** hierarchy, overall layout, crop, density, composition and brand feel.
- **Focused-region comparison:** precise areas changed, spacing/alignment/type/crop/component-state differences.
- **Findings with severity:** P0 blocker / P1 major / P2 polish where useful; include location, evidence, impact and fix.
- **Required fidelity surfaces:** typography, spacing/layout rhythm, colors/tokens, imagery/assets, copy/content, interaction state.
- **Implementation evidence:** tests/build/lint/browser/console/network/a11y/visual results actually run.
- **Follow-up checklist:** unresolved visual/interaction checks.
- **Final result:** `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT VERIFIED`.

If the target state cannot be rendered or captured in the same meaningful state, visual acceptance is **blocked** even when unit tests or geometry/code assertions pass. Do not substitute implementation reasoning for browser/channel evidence.

For user-provided screenshot matching, preserve source and implementation screenshots side-by-side or in a comparison manifest when tooling allows. A passing design QA artifact should be reusable as regression evidence for later changes.

## Instagram operating model
Instagram work is a system: profile identity → content pillars → feed → static/carousel → Reels → Stories → copy → calendar → paid creative → Insights → learning loop.
Exact current dimensions, limits, eligibility, safe zones, scheduling and ad policy are runtime facts verified from Meta/Instagram.

### Profile
- Avatar must survive small circular crop; use an approved symbol/monogram/social variant rather than crushing a horizontal wordmark.
- Test optical centering, light/dark visibility and small-size legibility.
- Bio communicates who/for whom/value/CTA succinctly.
- Highlights/pinned content support navigation and brand story, not decorative clutter.

### Feed
- Feed consistency ≠ repeating one template.
- Evaluate scroll/grid rhythm, color distribution, typography density, imagery/text balance, whitespace, motifs and content-pillar balance.
- Assets must work at profile/feed preview size, not only after tapping open.
- Text-heavy content should often move to carousel rather than squeezing paragraphs onto one card.

### Carousel
Card 1 hook/promise/tension → middle cards one idea each with narrative progression → final synthesis/proof/CTA. Maintain continuity with grid/type/numbering/imagery. Sequential paid carousels must account for automatic card-order behavior.

### Reels
Vertical-first; storyboard hook → context/problem → value/proof → payoff → CTA. Avoid long logo intros. Keep text within current safe zones. Design covers for profile/grid recognition. Organic trend mimicry is not a brand strategy.

### Stories
Tap-speed, one dominant idea/frame, safe-zone-aware text/logo/CTA, purposeful native interactions. Organic-story features are not automatically ad-eligible.

### Copy
Caption extends visual meaning rather than repeating it. Strong opening, brand voice, one realistic CTA, no jargon/emoji/hashtag spam. Claims, testimonials and scarcity must be real and source-backed.

## Paid Instagram / Meta creative
Paid creative is separate from organic. Brief includes objective, audience/problem awareness, offer, destination, hook/angle, proof, CTA, placements and KPI.
Test genuinely different angles (problem, outcome, demo, proof, comparison, objection, founder, lifestyle, education, offer), not recolors of one template.
Evaluate hook, offer clarity, relevance, brand recognition, proof, hierarchy, CTA, placement-native composition, safe zone, landing-page match, policy risk, testable hypothesis and differentiation.
A/B tests should isolate the main variable where practical; judge by objective-relevant downstream metrics, not CTR alone.

Generative-provider variants must still preserve brand/product truth and be distinguishable by creative hypothesis, not just random visual drift.

## Measurement loop
`publish/run → collect Insights/reporting → segment by format/pillar/angle → diagnose winners/losers → hypothesis → variant → test → update playbook`.
Store learnings as audience/offer/angle/format/KPI relationships, not “this design looked nice.” Treat small samples and estimated metrics with uncertainty.

## Logo design workflow
brief → brand/audience/competitor research → positioning/personality → references/mood → genuinely different rough concepts → black/white test → type/geometry/optical refinement → small-size/scalability → monochrome/reversed/background tests → social/web/print mockups → evaluator → vector master → responsive variants → clear-space/min-size/usage guide → export kit.
First generated mark is never automatically final. Check obvious competitor similarity, generic stock/icon marks, meaningless geometry and licensing/trademark risk; design review is not legal clearance.

Generative models may assist concept exploration, but final logo geometry, typography and vector master require deterministic refinement and uniqueness/originality review.

## Programmatic creative production
For scalable campaigns, templates may be code-driven (e.g. Remotion-class video, Sharp-class raster pipeline, SVGO-class SVG optimization) but templates never replace art direction. Generated outputs must pass channel-specific visual/export QA.

Generative and deterministic pipelines are complementary: use a generative provider for concept/reference-guided imagery or motion, then deterministic tooling for exact type, CTA, brand-token layout, resize/crop, export manifest and repeatable delivery.

## Social publishing QA
Before publish where relevant: current aspect/export spec, profile/feed/Reel/Story preview, mobile readability, avatar/logo integrity, crop/safe zone, spelling, CTA/destination, tags/partner permissions, audio/ad eligibility, policy, schedule/account, correct asset/version, high-quality upload and duplicate/stale asset check.

## Agency-quality completion
Do not claim agency-level completion unless brand fit, originality, craft, clarity, channel/mobile preview, asset correctness, readability/accessibility, export QA and campaign cohesion have no unresolved critical findings.
