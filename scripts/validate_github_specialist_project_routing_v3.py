#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json"


def main() -> int:
    failures: list[str] = []
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    domains = manifest.get("domains", {})
    projects = manifest.get("project_routing", {})

    if not projects:
        failures.append("manifest missing project_routing map")

    extension_agents = {
        agent
        for domain in domains.values()
        for agent in domain.get("agents", [])
    }

    expected_projects = {
        "dragdrop": ("@DragDrop", "@ShopifyExpert"),
        "vinterro-digital": ("@VinterroDigital", "@WordPressExpert"),
        "goayvalik": ("@GoAyvalık", "@WordPressExpert"),
        "ayvalik-vibes": ("@AyvalıkVibes", "@WordPressExpert"),
    }

    if set(projects) != set(expected_projects):
        failures.append(
            f"project_routing keys drift: expected {sorted(expected_projects)}, got {sorted(projects)}"
        )

    routed_agents: set[str] = set()

    for slug, (expected_owner, expected_platform) in expected_projects.items():
        cfg = projects.get(slug)
        if not cfg:
            continue

        adapter_path = cfg.get("adapter", "")
        if not adapter_path or not (ROOT / adapter_path).is_file():
            failures.append(f"{slug}: adapter missing: {adapter_path!r}")
            continue

        adapter = (ROOT / adapter_path).read_text(encoding="utf-8")
        owner = cfg.get("core_owner")
        platform = cfg.get("platform_expert")
        if owner != expected_owner:
            failures.append(f"{slug}: core_owner drift: {owner!r} != {expected_owner!r}")
        if platform != expected_platform:
            failures.append(f"{slug}: platform_expert drift: {platform!r} != {expected_platform!r}")
        if expected_owner not in adapter:
            failures.append(f"{slug}: adapter does not reference core owner {expected_owner}")
        if expected_platform not in adapter:
            failures.append(f"{slug}: adapter does not reference platform expert {expected_platform}")

        if "GITHUB_SPECIALIST_EXPANSION_V3.md" not in adapter:
            failures.append(f"{slug}: adapter missing GITHUB_SPECIALIST_EXPANSION_V3.md")
        if "github-specialist-router" not in adapter:
            failures.append(f"{slug}: adapter missing github-specialist-router")
        if "candidate" not in adapter.lower():
            failures.append(f"{slug}: adapter must describe routes as candidate pods")

        routes = cfg.get("routes", {})
        if not routes:
            failures.append(f"{slug}: no project routes defined")

        for route_name, agents in routes.items():
            if not agents:
                failures.append(f"{slug}.{route_name}: empty route")
            if len(agents) != len(set(agents)):
                failures.append(f"{slug}.{route_name}: duplicate agents")
            for agent in agents:
                routed_agents.add(agent)
                if agent not in extension_agents:
                    failures.append(
                        f"{slug}.{route_name}: non-v3 or unknown specialist in project route: {agent}"
                    )
                if agent not in adapter:
                    failures.append(
                        f"{slug}.{route_name}: manifest specialist missing from adapter text: {agent}"
                    )

    # Platform isolation gates.
    dragdrop = projects.get("dragdrop", {})
    if dragdrop.get("platform_expert") == "@WordPressExpert":
        failures.append("dragdrop must never default to @WordPressExpert")
    for slug in ("vinterro-digital", "goayvalik", "ayvalik-vibes"):
        if projects.get(slug, {}).get("platform_expert") == "@ShopifyExpert":
            failures.append(f"{slug} must not default to @ShopifyExpert")

    # GoAyvalık's known mobile route is Flutter, but source inspection remains mandatory.
    go_mobile = projects.get("goayvalik", {}).get("routes", {}).get("mobile_app", [])
    if "@MobileArchitect" not in go_mobile or "@FlutterSpecialist" not in go_mobile or "@MobileQA" not in go_mobile:
        failures.append("goayvalik.mobile_app missing MobileArchitect/FlutterSpecialist/MobileQA candidate chain")
    if "@ReactNativeSpecialist" in go_mobile:
        failures.append("goayvalik.mobile_app must not default-route React Native without verified stack change")
    go_adapter_path = projects.get("goayvalik", {}).get("adapter")
    if go_adapter_path and (ROOT / go_adapter_path).is_file():
        go_adapter = (ROOT / go_adapter_path).read_text(encoding="utf-8").lower()
        if "verified as flutter" not in go_adapter and "source stack" not in go_adapter:
            failures.append("goayvalik adapter lacks source-stack verification guard for Flutter routing")

    # Meta routes must preserve measurement-only vs campaign mutation separation.
    for slug in ("dragdrop", "vinterro-digital"):
        meta = projects.get(slug, {}).get("routes", {}).get("meta_ads", [])
        if meta:
            for required in ("@MetaMeasurement", "@MetaAdsEngineer"):
                if required not in meta:
                    failures.append(f"{slug}.meta_ads missing {required} candidate")
            adapter_path = projects.get(slug, {}).get("adapter")
            adapter = (ROOT / adapter_path).read_text(encoding="utf-8").lower()
            if "measurement-only" not in adapter and "measurement only" not in adapter:
                failures.append(f"{slug}: Meta route lacks measurement-only no-mutation guard")

    # At least one project should exercise every major specialist domain except stack alternatives,
    # but project maps need not include every one of the 31 identities.
    required_routed = {
        "@FrontendSystem",
        "@BrowserQA",
        "@WebPerformance",
        "@AccessibilityQA",
        "@TechnicalSEO",
        "@SEOScanner",
        "@AEO_GEO",
        "@SocialStrategy",
        "@SocialAnalytics",
        "@BrandSystemArchitect",
        "@BrandComplianceQA",
        "@MetaMeasurement",
        "@MetaAdsEngineer",
        "@MobileArchitect",
        "@FlutterSpecialist",
        "@MobileQA",
    }
    missing_coverage = required_routed - routed_agents
    if missing_coverage:
        failures.append(f"project routing lacks cross-domain coverage: {sorted(missing_coverage)}")

    if failures:
        print("GitHub Specialist v3 project routing: FAIL", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1

    print("GitHub Specialist v3 project routing: PASS")
    print(f"Projects: {len(projects)}")
    print(f"Project route specialist references: {len(routed_agents)} unique v3 identities")
    print("Qualified routing remains material-contribution based; project routes are candidate pods.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
