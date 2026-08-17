---
name: map-platform-selection
description: Select or review a web/mobile mapping stack for Ercan OS projects. Use for map, POI, geocoding, clustering, offline tiles, route/location UX, map performance or map-provider migration tasks. Do not trigger for metaphorical maps/mind maps/data mapping.
---

# Map Platform Selection

Load `docs/standards/MAP_ENGINEERING.md` and the matching project adapter first.

## Input
A map/location task or an existing map implementation.

## Procedure
1. Identify the actual product surface: web, WordPress, Flutter, React Native, native app, internal dashboard.
2. Inspect the current renderer, tile/basemap source, geocoder/search source, POI data model, clustering and routing dependencies before proposing a migration.
3. Classify requirements:
   - simple markers/raster overlays vs vector-tile styling/data layers;
   - dataset size/density;
   - list-map synchronization;
   - offline requirement;
   - custom styling/3D/heatmap;
   - geocoding/search volume;
   - routing/navigation;
   - mobile/location permissions;
   - hosting/vendor-lock-in constraints.
4. Select the smallest maintained stack that meets those requirements. Prefer MapLibre for new rich vector web maps, Leaflet for simple/legacy lightweight web maps, and platform-specific maintained mobile bindings when appropriate.
5. Add Supercluster only when point density needs clustering. Add Nominatim/another geocoder as a separate service; do not conflate renderer and search provider.
6. Verify current upstream maintenance, license, pricing/terms, provider limits and attribution requirements.
7. Produce migration/no-migration recommendation with risks, data-contract impact and QA plan.

## Output contract
Return:
- current_stack
- requirements
- recommended_renderer
- tile/basemap_strategy
- geocoder/search_strategy
- clustering_strategy
- routing_strategy if needed
- offline_strategy if needed
- licensing/privacy/attribution notes
- migration decision (`KEEP`, `ADAPT`, `MIGRATE`, `WATCHLIST`)
- acceptance/QA checklist

## Guardrails
- Never migrate a working map solely for novelty.
- Never treat public OSM/Nominatim/tile endpoints as unlimited production infrastructure without policy review.
- Never invent POI/business facts from geocoder output.
- Map pins are a view over canonical records, not the source of truth.
