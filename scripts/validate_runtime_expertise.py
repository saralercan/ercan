#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RUNTIME = ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
MATRIX = ROOT / "docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json"
ENGINE = ROOT / "docs/standards/AGENT_CONTINUAL_EXPERTISE_ENGINE.md"
PORTABLE = ROOT / "docs/standards/PORTABLE_AGENT_RUNTIME.md"
SHOPIFY_PACK = ROOT / "docs/standards/SHOPIFY_EXPERT_SOURCE_PACK.md"
ROOT_AGENTS = ROOT / "AGENTS.md"

REQUIRED_PROFILE_KEYS = {
    "id",
    "name",
    "role",
    "family",
    "source_tiers",
    "research_topics",
    "continual_queries",
    "refresh_policy",
    "mastery_gate",
    "source_packs",
    "depth_contract",
    "required_evidence",
}

SHOPIFY_REQUIRED_PRIMARY = {
    "https://shopify.dev/docs",
    "https://shopify.dev/changelog",
    "https://shopify.dev/docs/api/liquid",
    "https://shopify.dev/docs/storefronts/themes/architecture",
    "https://shopify.dev/docs/api/admin-graphql/latest",
}
SHOPIFY_REQUIRED_GITHUB = {
    "Shopify/dawn",
    "Shopify/cli",
    "Shopify/hydrogen",
    "Shopify/theme-tools",
    "Shopify/agent-skills",
}


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(msg: str, failures: list[str]):
    failures.append(msg)


def main() -> int:
    failures: list[str] = []
    for path in [RUNTIME, MATRIX, ENGINE, PORTABLE, SHOPIFY_PACK, ROOT_AGENTS]:
        if not path.is_file():
            fail(f"missing required file: {path.relative_to(ROOT)}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    runtime = read_json(RUNTIME)
    matrix = read_json(MATRIX)

    agents = runtime.get("agents", [])
    profiles = matrix.get("profiles", [])

    runtime_count = runtime.get("runtime_agent_count")
    if not isinstance(runtime_count, int) or runtime_count < 1:
        fail(f"runtime_agent_count must be a positive integer, got {runtime_count!r}", failures)
        runtime_count = len(agents)
    if len(agents) != runtime_count:
        fail(f"runtime manifest count mismatch: declared={runtime_count}, actual={len(agents)}", failures)
    if matrix.get("agent_count") != runtime_count:
        fail(f"expertise matrix agent_count must match runtime count {runtime_count}, got {matrix.get('agent_count')}", failures)
    if len(profiles) != runtime_count:
        fail(f"expertise matrix profile count must match runtime count {runtime_count}, got {len(profiles)}", failures)

    runtime_names = [a.get("name") for a in agents]
    profile_names = [p.get("name") for p in profiles]
    if len(set(runtime_names)) != runtime_count:
        fail("runtime agent names are not unique", failures)
    if len(set(profile_names)) != runtime_count:
        fail("expertise profile names are not unique", failures)
    if runtime_names != profile_names:
        missing = [n for n in runtime_names if n not in profile_names]
        extra = [n for n in profile_names if n not in runtime_names]
        fail(f"runtime/expertise order or membership drift; missing={missing}, extra={extra}", failures)

    expected_ids = list(range(1, runtime_count + 1))
    if [a.get("id") for a in agents] != expected_ids:
        fail(f"runtime manifest IDs must be exactly 1..{runtime_count}", failures)
    if [p.get("id") for p in profiles] != expected_ids:
        fail(f"expertise profile IDs must be exactly 1..{runtime_count}", failures)

    runtime_name_set = set(runtime_names)
    for agent in agents:
        name = agent.get("name", "<unknown>")
        adapters = agent.get("adapters") or {}
        if not all(adapters.get(k) is True for k in ("codex", "claude", "vinterro_one")):
            fail(f"{name}: all three runtime adapters must be true", failures)
        if agent.get("default_state") != "STANDBY":
            fail(f"{name}: default_state must be STANDBY", failures)
        if agent.get("activation") != "jit":
            fail(f"{name}: activation must be jit", failures)
        for target in agent.get("handoffs") or []:
            if target not in runtime_name_set:
                fail(f"{name}: broken handoff -> {target}", failures)

    for profile in profiles:
        name = profile.get("name", "<unknown>")
        missing_keys = sorted(k for k in REQUIRED_PROFILE_KEYS if k not in profile)
        if missing_keys:
            fail(f"{name}: missing expertise keys {missing_keys}", failures)
            continue

        source_tiers = profile.get("source_tiers") or {}
        primary = source_tiers.get("primary") or []
        canonical = source_tiers.get("canonical_github") or []
        secondary = source_tiers.get("reviewed_secondary") or []
        if len(primary) < 2:
            fail(f"{name}: needs at least 2 primary/official sources", failures)
        if not canonical and not secondary:
            fail(f"{name}: needs canonical GitHub or reviewed secondary evidence", failures)
        if len(profile.get("research_topics") or []) < 2:
            fail(f"{name}: research_topics too shallow", failures)
        if len(profile.get("continual_queries") or []) < 2:
            fail(f"{name}: continual_queries too shallow", failures)
        if not profile.get("source_packs"):
            fail(f"{name}: missing source_packs", failures)

        refresh = profile.get("refresh_policy") or {}
        scheduled = int(refresh.get("scheduled_days") or 0)
        stale = int(refresh.get("stale_after_days") or 0)
        if scheduled < 1:
            fail(f"{name}: scheduled_days must be >= 1", failures)
        if stale < scheduled:
            fail(f"{name}: stale_after_days must be >= scheduled_days", failures)

        depth = profile.get("depth_contract") or {}
        for key in ("discovery", "ingestion", "freshness", "verification"):
            if not depth.get(key):
                fail(f"{name}: depth_contract missing {key}", failures)

        if len(profile.get("required_evidence") or []) < 4:
            fail(f"{name}: required_evidence is too shallow", failures)

    by_name = {p.get("name"): p for p in profiles}
    for name in ("Finance Expert Agent", "E-commerce Expert Agent"):
        if name not in by_name:
            fail(f"missing required specialist: {name}", failures)

    shopify = by_name.get("Shopify Agent") or {}
    shop_primary = set((shopify.get("source_tiers") or {}).get("primary") or [])
    shop_github = set((shopify.get("source_tiers") or {}).get("canonical_github") or [])
    for src in sorted(SHOPIFY_REQUIRED_PRIMARY - shop_primary):
        fail(f"Shopify Agent missing primary source: {src}", failures)
    for src in sorted(SHOPIFY_REQUIRED_GITHUB - shop_github):
        fail(f"Shopify Agent missing canonical GitHub: {src}", failures)
    shopify_pack = SHOPIFY_PACK.read_text(encoding="utf-8")
    if "Shopify/agent-skills" not in shopify_pack:
        fail("Shopify source pack missing official agent-skills", failures)
    if "Storefront MCP" not in shopify_pack or "WebMCP" not in shopify_pack:
        fail("Shopify source pack missing agentic-commerce coverage", failures)
    shop_refresh = int((shopify.get("refresh_policy") or {}).get("scheduled_days") or 999)
    if shop_refresh > 1:
        fail(f"Shopify Agent scheduled refresh must be <= 1 day, got {shop_refresh}", failures)
    if len(shopify.get("research_topics") or []) < 15:
        fail("Shopify Agent research curriculum is not deep enough", failures)

    packs = matrix.get("source_pack_catalog") or {}
    for pack in ("shopify", "wordpress", "web_engineering", "javascript", "security", "qa", "seo", "ecommerce", "finance", "growth_ads", "content_editorial", "design", "agent_runtime", "local_discovery", "devops", "analytics", "research"):
        if pack not in packs:
            fail(f"missing source pack catalog entry: {pack}", failures)

    engine = ENGINE.read_text(encoding="utf-8")
    portable = PORTABLE.read_text(encoding="utf-8")
    agents_contract = ROOT_AGENTS.read_text(encoding="utf-8")

    for needle in (
        "Scope: all Vinterro One runtime agents",
        "Research the whole internet",
        "Shopify deep-specialist requirement",
        "Source authority tiers",
    ):
        if needle not in engine:
            fail(f"continual expertise engine missing contract: {needle}", failures)

    for needle in (
        "AGENT_CONTINUAL_EXPERTISE_ENGINE.md",
        "AGENT_EXPERTISE_SOURCE_MATRIX.json",
        "Production runtime count is read from the live",
        "STANDBY",
    ):
        if needle not in portable:
            fail(f"portable runtime missing expertise reference: {needle}", failures)

    for needle in (
        "AGENT_CONTINUAL_EXPERTISE_ENGINE.md",
        "AGENT_EXPERTISE_SOURCE_MATRIX.json",
        "PORTABLE_AGENT_RUNTIME.md",
    ):
        if needle not in agents_contract:
            fail(f"AGENTS.md missing mandatory expertise load: {needle}", failures)

    if failures:
        print("Runtime expertise validator: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("Runtime expertise validator: PASS")
    print(f"Runtime agents: {runtime_count}/{runtime_count}")
    print(f"Expertise profiles: {runtime_count}/{runtime_count}")
    print("Portable adapters: Codex + Claude + Vinterro One")
    print("Handoffs: valid")
    print("Source packs: deep domain coverage present")
    print("Shopify deep-specialist gate: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
