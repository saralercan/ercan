#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
AUTHORITY = ROOT / "docs/standards/AGENT_SOURCE_AUTHORITY_89.json"
PORTABLE = ROOT / "docs/standards/PORTABLE_AGENT_RUNTIME.md"
EXPERTISE = ROOT / "docs/standards/CONTINUOUS_EXPERTISE_ENGINE.md"
SHOPIFY = ROOT / "docs/standards/SHOPIFY_EXPERT_SOURCE_PACK.md"
CODEX_ROUTER = ROOT / ".agents/skills/portable-agent-router/SKILL.md"
CLAUDE_ROUTER = ROOT / ".claude/agents/vinterro-router.md"

def fail(msg: str, failures: list[str]) -> None:
    failures.append(msg)

def main() -> int:
    failures: list[str] = []
    for p in [RUNTIME, AUTHORITY, PORTABLE, EXPERTISE, SHOPIFY, CODEX_ROUTER, CLAUDE_ROUTER]:
        if not p.is_file():
            fail(f"missing required runtime expertise artifact: {p.relative_to(ROOT)}", failures)
    if failures:
        for x in failures:
            print(f"FAIL: {x}", file=sys.stderr)
        return 2

    runtime = json.loads(RUNTIME.read_text(encoding="utf-8"))
    authority = json.loads(AUTHORITY.read_text(encoding="utf-8"))
    agents = runtime.get("agents", [])
    source_agents = authority.get("agents", [])

    if runtime.get("runtime_agent_count") != 89:
        fail(f"runtime_agent_count must be 89, got {runtime.get('runtime_agent_count')}", failures)
    if len(agents) != 89:
        fail(f"runtime manifest must contain 89 agents, got {len(agents)}", failures)
    if authority.get("agent_count") != 89 or len(source_agents) != 89:
        fail("authority map must contain 89 agents", failures)

    ids = [a.get("id") for a in agents]
    if ids != list(range(1, 90)):
        fail("runtime IDs must be exactly 1..89", failures)

    names = [a.get("name") for a in agents]
    if len(set(names)) != 89:
        fail("runtime agent names must be unique", failures)

    authority_names = [a.get("name") for a in source_agents]
    if authority_names != names:
        fail("authority map must match runtime manifest name/order exactly", failures)

    name_set = set(names)
    for a in agents:
        name = a.get("name", "<unknown>")
        if a.get("status") != "active":
            fail(f"{name}: expected active production registry state", failures)
        if a.get("activation") != "jit":
            fail(f"{name}: activation must be jit", failures)
        if a.get("default_state") != "STANDBY":
            fail(f"{name}: default_state must be STANDBY", failures)
        adapters = a.get("adapters") or {}
        for key in ("codex", "claude", "vinterro_one"):
            if adapters.get(key) is not True:
                fail(f"{name}: adapter {key} must be true", failures)
        instructions = a.get("instructions") or ""
        if "CONTINUOUS EXPERTISE PROTOCOL (2026-09-24)" not in instructions:
            fail(f"{name}: missing continuous expertise protocol", failures)
        if not a.get("excellence_standard"):
            fail(f"{name}: missing excellence_standard", failures)
        if not a.get("authority_map"):
            fail(f"{name}: missing authority_map", failures)
        for target in a.get("handoffs") or []:
            if target not in name_set:
                fail(f"{name}: broken handoff target {target}", failures)

    for a in source_agents:
        name = a.get("name", "<unknown>")
        if not a.get("primary_sources"):
            fail(f"{name}: missing primary_sources", failures)
        if not a.get("deep_scan_topics"):
            fail(f"{name}: missing deep_scan_topics", failures)
        if not isinstance(a.get("freshness_days"), int) or a.get("freshness_days") < 1:
            fail(f"{name}: invalid freshness_days", failures)
        if a.get("knowledge_state") != "JIT_REFRESH_REQUIRED":
            fail(f"{name}: knowledge_state must be JIT_REFRESH_REQUIRED", failures)
        if not a.get("ingestion"):
            fail(f"{name}: missing ingestion contract", failures)
        rules = " ".join(a.get("hard_rules") or []).lower()
        if "claim research" not in rules and "claim" not in rules:
            fail(f"{name}: missing anti-fabrication research rule", failures)

    finance = next((a for a in agents if a.get("name") == "Finance Expert Agent"), None)
    ecommerce = next((a for a in agents if a.get("name") == "E-commerce Expert Agent"), None)
    shopify = next((a for a in agents if a.get("name") == "Shopify Agent"), None)
    theme = next((a for a in agents if a.get("name") == "Shopify Theme Developer"), None)
    for label, item in [("Finance Expert Agent", finance), ("E-commerce Expert Agent", ecommerce), ("Shopify Agent", shopify), ("Shopify Theme Developer", theme)]:
        if item is None:
            fail(f"missing required specialist: {label}", failures)

    if shopify and "Shopify/agent-skills" not in SHOPIFY.read_text(encoding="utf-8"):
        fail("Shopify source pack missing official agent-skills source", failures)
    if shopify and "Storefront MCP" not in SHOPIFY.read_text(encoding="utf-8"):
        fail("Shopify source pack missing Storefront MCP/UCP coverage", failures)

    portable = PORTABLE.read_text(encoding="utf-8")
    if "smallest sufficient expert pod" not in portable:
        fail("portable runtime missing qualified pod contract", failures)
    if "STANDBY" not in portable or "89 active agents" not in portable:
        fail("portable runtime missing 89-agent ACTIVE/STANDBY contract", failures)

    if failures:
        print("Runtime Agent Expertise validator: FAIL", file=sys.stderr)
        for x in failures:
            print(f"  - {x}", file=sys.stderr)
        return 1

    print("Runtime Agent Expertise validator: PASS")
    print("Vinterro One runtime agents: 89/89")
    print("Codex adapters: 89/89")
    print("Claude adapters: 89/89")
    print("Vinterro One adapters: 89/89")
    print("Continuous expertise protocol: 89/89")
    print("Authority maps: 89/89")
    print("Handoff integrity: PASS")
    print("Master routing: ACTIVE pod + STANDBY pool")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
