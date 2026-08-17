---
name: creative-export-pipeline
description: Build or audit deterministic export pipelines for social/brand images, video compositions and SVG assets. Use for batch feed/story/ad variants, exact resize/crop, Remotion video templates, Sharp raster exports, SVGO optimization or export manifests.
---

# Creative Export Pipeline

Load `BRAND_SOCIAL.md`; load provider-specific creative standards only if generation is actually used.

## Pipeline
`editable/master source → approved composition → deterministic renderer/exporter → manifest → visual/channel QA → delivery`.

## Procedure
1. Define approved master and protected elements: copy, logo, product geometry, colors/tokens, safe zones.
2. Define target channels/aspect ratios/dimensions from current platform requirements.
3. Choose deterministic tooling by need:
   - Sharp-class raster processing for resize/crop/composite/format/ICC-alpha work.
   - SVGO-class optimization for SVG only after geometry/mask/gradient/accessibility regression checks.
   - Remotion-class composition for repeatable code-driven video when licensing/terms fit.
4. Keep generated/provider imagery separate from exact typography/layout layer.
5. Produce an export manifest with source version, target, dimensions/aspect, format, file size/checksum when useful, renderer/tool version and asset version.
6. Render representative edge cases: longest copy, missing optional field, alternate product/image crop, light/dark background where relevant.
7. Run channel preview and visual QA; verify no clipping, unsafe crop, wrong logo/text, alpha/ICC issues or stretched imagery.
8. Re-run the same build to confirm deterministic naming/output expectations where required.

## Rules
- Do not hand-edit generated exports as new masters.
- Do not use one resize for all placements when hierarchy/crop needs recomposition.
- Verify Remotion/current tool license and runtime requirements before commercial production.
- Optimization must not change brand geometry or accessibility behavior.

## Output
- source/master
- target matrix
- tool choice/rationale
- manifest location/content
- QA evidence
- final status