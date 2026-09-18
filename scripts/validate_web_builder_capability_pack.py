#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKILL = ROOT / ".agents/skills/web-builder-capability-pack/SKILL.md"
SCAN = ROOT / "docs/upstream/scans/2026-09-19-web-builder-capability-expansion.md"

SURFACES = {
    "root": ROOT / "AGENTS.md",
    "web_skill": ROOT / ".agents/skills/web-production-specialist/SKILL.md",
    "router": ROOT / ".agents/skills/github-specialist-router/SKILL.md",
    "registry": ROOT / "docs/standards/AGENT_REGISTRY.md",
    "expansion": ROOT / "docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md",
    "qualified_routing": ROOT / "docs/standards/QUALIFIED_AGENT_ROUTING.md",
}
PROJECTS = [
    ROOT / "projects/dragdrop/AGENTS.md",
    ROOT / "projects/vinterro-digital/AGENTS.md",
    ROOT / "projects/goayvalik/AGENTS.md",
    ROOT / "projects/ayvalik-vibes/AGENTS.md",
]
CATALOG = ROOT / "docs/upstream/UPSTREAM_INTELLIGENCE_CATALOG.md"
CURRENT = ROOT / "docs/upstream/UPSTREAM_INTELLIGENCE_CURRENT.md"
LEDGER = ROOT / "docs/standards/DISCOVERY_ADOPTION_LEDGER.md"
MANIFEST = ROOT / "docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json"

LANES = [
    "AutonomousWebBuilder",
    "InstantAppBuilder",
    "LocalAppBuilder",
    "VisualWebEditor",
    "DesignSystem",
    "ComponentLab",
    "WordPressEngineer",
    "WordPressThemeQA",
    "ShopifyStorefront",
    "HeadlessCommerce",
    "WebOperator",
    "SEOIndexability",
    "LocalizationQA",
    "MediaOptimizer",
    "PWAEngineer",
    "WebSecurity",
    "FrontendHealth",
    "ContentSiteBuilder",
]

NEW_UPSTREAMS = [
    "OpenHands/OpenHands",
    "stackblitz-labs/bolt.diy",
    "dyad-sh/dyad",
    "onlook-dev/onlook",
    "BuilderIO/mitosis",
    "WordPress/theme-check",
    "i18next/i18next",
    "GoogleChrome/workbox",
    "semgrep/semgrep",
    "biomejs/biome",
    "stylelint/stylelint",
    "html-validate/html-validate",
]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    for path in [SKILL, SCAN, CATALOG, CURRENT, LEDGER, MANIFEST, *SURFACES.values(), *PROJECTS]:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}", failures)

    if failures:
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    counts = manifest.get("identity_counts", {})
    if counts.get("stable_core") != 21 or counts.get("specialist_extension") != 31 or counts.get("total_named_stable_routing_identities") != 52:
        fail(f"stable identity accounting drift: {counts}", failures)

    skill = SKILL.read_text(encoding="utf-8")
    if "capability labels" not in skill.lower() or "not new stable" not in skill.lower():
        fail("capability pack must explicitly preserve stable-identity separation", failures)

    for lane in LANES:
        if lane not in skill:
            fail(f"capability lane missing from skill: {lane}", failures)

    # Capability labels must not silently become new stable @ identities.
    governance = "\n".join(p.read_text(encoding="utf-8") for p in [MANIFEST, SURFACES["registry"]])
    for lane in LANES:
        if f"@{lane}" in governance:
            fail(f"capability lane incorrectly promoted to stable identity: @{lane}", failures)

    for name, path in SURFACES.items():
        content = path.read_text(encoding="utf-8")
        if "web-builder-capability-pack" not in content:
            fail(f"{name} missing web-builder-capability-pack reference", failures)

    for path in PROJECTS:
        content = path.read_text(encoding="utf-8")
        if "web-builder-capability-pack" not in content:
            fail(f"project adapter missing capability pack: {path.relative_to(ROOT)}", failures)

    catalog = CATALOG.read_text(encoding="utf-8")
    current = CURRENT.read_text(encoding="utf-8")
    ledger = LEDGER.read_text(encoding="utf-8")
    scan = SCAN.read_text(encoding="utf-8")
    for repo in NEW_UPSTREAMS:
        for label, surface in [("catalog", catalog), ("current", current), ("ledger", ledger), ("scan", scan)]:
            if repo not in surface:
                fail(f"{repo} missing from {label}", failures)

    required_owners = [
        "@WebArchitecture",
        "@FrontendSystem",
        "@ComponentWorkshopQA",
        "@WordPressExpert",
        "@ShopifyExpert",
        "@TechnicalSEO",
        "@SEOScanner",
        "@WebPerformance",
        "@AccessibilityQA",
        "@BrowserQA",
    ]
    for owner in required_owners:
        if owner not in skill:
            fail(f"stable owner missing from capability map: {owner}", failures)

    dragdrop = (ROOT / "projects/dragdrop/AGENTS.md").read_text(encoding="utf-8")
    if "WordPress lanes do not apply to DragDrop" not in dragdrop:
        fail("DragDrop platform-isolation guard missing", failures)

    if failures:
        print("Web Builder Capability Pack validator: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("Web Builder Capability Pack validator: PASS")
    print("Stable identities: 21 core + 31 extension = 52")
    print(f"Capability lanes: {len(LANES)}")
    print(f"New reviewed upstream engines: {len(NEW_UPSTREAMS)}")
    print(f"Project adapters connected: {len(PROJECTS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
