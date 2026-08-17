# Map Engineering Standard

Status: shared Ercan OS standard for web/mobile/local-guide maps, POI discovery, geocoding, clustering, route/location UX and map-data QA.

## Core rule
Do not choose a map library by popularity alone. Select the smallest maintained stack that fits the actual product surface, data scale, styling, offline, licensing, hosting and mobile requirements.

Default decision order:
1. define the product problem and data contract;
2. choose rendering engine;
3. choose tile/basemap source and hosting model;
4. choose geocoding/search provider;
5. add clustering/routing/offline only when required;
6. validate attribution/licensing/privacy;
7. run real map/browser/mobile QA.

## Rendering-engine selection
### MapLibre GL JS — default modern web candidate
Use for new interactive web maps that benefit from GPU-accelerated vector tiles, rich styling, heatmaps, data layers, 3D/terrain/buildings or larger POI datasets. It is vendor-neutral/open source and can use self-hosted or third-party vector tiles.

### Leaflet — simple/legacy/lightweight web candidate
Use for relatively simple maps, raster/tile overlays, small-to-medium marker sets, WordPress embeds/plugins or existing Leaflet systems where its small footprint and plugin ecosystem are more valuable than vector-tile styling. Do not force a MapLibre migration if the current Leaflet implementation is healthy and requirements are simple.

### Mapbox GL JS — commercial/provider-specific candidate
Use only when Mapbox-specific services/features and current commercial terms materially justify it. Licensing, tokens, pricing and API behavior are runtime facts and must be checked before adoption. Do not choose it merely because old examples use it.

### Mobile
- Flutter: `maplibre/flutter-maplibre-gl` is the preferred vendor-neutral candidate when vector tiles/style portability/offline-capable architecture matter. Current feature matrix/platform support must be checked at runtime.
- React Native: `react-native-maps/react-native-maps` is a mature native-map abstraction for iOS/Android and supports markers, overlays, GeoJSON and local/URL tiles. Evaluate provider/offline/style requirements before selection.
- Native iOS/Android or shared engines: MapLibre Native is the reference open-source engine when a deeper native integration is required.

## Tile / basemap architecture
Separate rendering engine from tile/data source. The map renderer must not silently become the data vendor.

Possible models:
- hosted vector/raster tile provider;
- self-hosted tiles;
- PMTiles/static object storage for bounded datasets/regions;
- offline packaged tiles for mobile/local-guide use cases.

Do not hotlink a public community tile endpoint at production scale without checking its usage policy. Keep attribution and source licensing visible and correct.

### PMTiles / Protomaps
PMTiles/static-hosted tile archives are useful when a bounded region can be served cheaply from object/static storage and operational simplicity matters. New projects should prefer MapLibre-compatible PMTiles flows rather than starting on `protomaps-leaflet`, which is maintenance-mode/legacy-oriented.

## Geocoding and place search
### Nominatim
`osm-search/Nominatim` is the canonical open-source reference for OpenStreetMap name/address search and reverse geocoding.

Rules:
- geocoding search and map rendering are separate services;
- public shared Nominatim instances have usage policies/rate limits and must not be treated as unlimited production APIs;
- high-volume/commercial use may require a hosted provider or self-hosted instance;
- cache only when policy/licensing permits;
- search results must preserve source attribution and be reconciled with project-owned canonical business/POI records.

For Vinterro Keşif / Ayvalık projects, external geocoder output is discovery evidence, not authoritative business truth. Website, phone, category, opening hours and business status need separate source verification.

## POI data model
Use stable canonical IDs independent of marker rendering. Recommended conceptual fields:
- `id`
- `name`
- `category_ids[]`
- `lat`, `lng`
- `address`
- `website`, `instagram`, `phone`, `email`
- `source_refs[]`
- `verification_state`
- `last_verified_at`
- `status` (active/closed/unknown)
- optional editorial/ranking metadata.

Map pins are a view over records, not the source of truth.

## Clustering
For hundreds/thousands of points, avoid rendering one expensive custom DOM/native marker per record at all zoom levels.

`mapbox/supercluster` is the canonical JS reference for fast GeoJSON point clustering and cluster expansion/aggregation. Use clustering when density makes individual pins unreadable or costly.

Rules:
- cluster by viewport/zoom, not arbitrary pagination alone;
- clicking a cluster should zoom/expand predictably;
- list and map must stay synchronized by canonical record ID;
- selection state must survive clustering/unclustering transitions;
- test dense regions and low-end mobile performance.

## Map + list synchronization
For local-guide/lead-map products, the map and list are two views of one query state.

Shared state should cover:
- viewport/bounds;
- search text;
- category/filter set;
- selected POI;
- hovered/focused POI when relevant;
- sort/ranking mode;
- pagination/infinite-load state;
- URL/shareable query state when product value warrants it.

Map movement must not create request storms; use debouncing/cancellation and stale-response protection.

## Search / filtering
Prefer server-side or indexed filtering when datasets grow. Do not push entire national datasets into the browser just because clustering can render them.

Use spatial bounding-box/radius queries plus category/text filters. Cache and pagination strategies must preserve deterministic record identity.

## Routing / directions
Routing is a separate capability from rendering. Do not implement straight-line distance as driving/walking time.

When routing is required, choose a maintained routing engine/provider based on mode coverage, Turkey data quality, licensing, traffic needs, self-hosting cost and SLA. Treat routing ETAs as volatile external results.

## WordPress integration
For WordPress local-guide projects:
- map/business records that are site-critical belong in structured plugin/custom-post-type/custom-table/application logic, not hardcoded theme JS;
- enqueue map assets only where needed;
- expose data through a stable REST/API contract rather than embedding huge inline JSON blobs;
- keep editor/admin workflows for location/category verification;
- use staging for material map migrations;
- preserve accessibility fallback: meaningful list/details must remain usable even if map JS fails.

## Mobile / offline
Offline support is a product requirement, not a checkbox.

Define:
- offline geographic region;
- tile/data package size;
- update strategy;
- POI freshness behavior;
- user-location privacy;
- network fallback;
- storage eviction/versioning.

Do not promise offline navigation merely because offline tiles render.

## Privacy and permissions
- Request precise location only when the feature needs it and explain the value.
- Support map browsing without location permission where practical.
- Do not retain user coordinates unnecessarily.
- Third-party map/geocoder providers may receive IP/location/query data; privacy disclosures and provider terms apply.

## Accessibility
A map cannot be the only way to access critical information.
- provide accessible list/detail equivalents;
- keyboard/focus behavior for map controls when supported;
- visible focus and readable labels/callouts;
- sufficient contrast for custom markers and overlays;
- do not encode category/status by color alone.

## Performance
Test real datasets and real devices.
Watch for:
- excessive custom DOM/native markers;
- repeated map reinitialization;
- unbounded GeoJSON payloads;
- oversized icons/images;
- request storms on pan/zoom;
- expensive style expressions/layers;
- unnecessary tile/detail fetches;
- memory leaks after route/page transitions.

## Map QA evidence
For material map changes capture task-relevant evidence:
- target URL/app build and dataset version;
- viewport/device;
- initial center/zoom/bounds;
- selected filters/category/search;
- expected marker/cluster count when deterministic;
- list ↔ pin synchronization;
- marker click/callout/detail destination;
- dense-area clustering behavior;
- pan/zoom/search cancellation behavior;
- mobile gestures and overlays;
- console/network errors;
- permission-denied/no-location fallback;
- attribution visibility;
- screenshot/video evidence for visual regressions.

Completion states remain `VERIFIED`, `PARTIAL`, `BLOCKED`, `NOT VERIFIED`.

## Upstream references
Verify current maintenance/docs/license at runtime before adoption:
- `maplibre/maplibre-gl-js` — modern open-source vector map renderer for web.
- `maplibre/maplibre-native` — native engine.
- `maplibre/flutter-maplibre-gl` — Flutter Android/iOS/Web binding, vendor-neutral.
- `Leaflet/Leaflet` — lightweight interactive web maps.
- `react-native-maps/react-native-maps` — iOS/Android React Native maps.
- `osm-search/Nominatim` — OSM geocoding/reverse geocoding.
- `mapbox/supercluster` — high-performance point clustering.
- Protomaps/PMTiles ecosystem — static/offline-friendly vector tile distribution; check the current maintained MapLibre integration path.

## Adoption policy
Map engine migrations are architectural changes. Do not rewrite an existing working map solely because another library is newer. Compare current requirements, bundle/runtime cost, styling needs, provider lock-in, migration risk and test coverage first.
