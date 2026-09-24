#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE_PATH = ROOT / "docs/standards/STABLE_AGENT_CORE.md"
SPECIALIST_PATH = ROOT / "docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json"
EXCELLENCE_PATH = ROOT / "docs/standards/AGENT_EXCELLENCE_MANIFEST.json"
RUNTIME_PATH = ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
EXPERTISE_MATRIX_PATH = ROOT / "docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json"
CONTINUAL_ENGINE_PATH = ROOT / "docs/standards/AGENT_CONTINUAL_EXPERTISE_ENGINE.md"
AUDIT_PATH = ROOT / "docs/evals/AGENT_EXCELLENCE_AUDIT_2026-09-24.md"
SUITE_PATH = ROOT / "docs/evals/AGENT_CHAMPIONSHIP_SUITE_V2.md"
CORE_SOURCES_PATH = ROOT / "docs/research/AGENT_SOURCE_PACKS.md"
SPECIALIST_SOURCES_PATH = ROOT / "docs/research/SPECIALIST_EXCELLENCE_SOURCE_PACKS.md"

REQUIRED_PROFILE_FIELDS = [
    "id", "agent", "tier", "domain", "principal_mandate",
    "source_authority_route", "gap_before_remediation", "remediation",
    "hard_fail", "championship_gate", "independent_verification_owner",
    "structural_state", "behavioral_state", "external_comparative_state",
]

def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")

def fail(message: str, failures: list[str]) -> None:
    failures.append(message)

def core_agents() -> list[str]:
    text = read(CORE_PATH)
    section = text.split("## Stable Core — 21 identities", 1)[1].split(
        "## GitHub Specialist v3 Extension", 1
    )[0]
    return re.findall(r"(?m)^\d+\.\s+\x60(@[^\x60]+)\x60\s*$", section)

def specialist_agents() -> list[str]:
    manifest = json.loads(read(SPECIALIST_PATH))
    agents: list[str] = []
    for config in manifest["domains"].values():
        agents.extend(config.get("agents", []))
    return agents

def main() -> int:
    failures: list[str] = []

    required_files = [
        CORE_PATH, SPECIALIST_PATH, EXCELLENCE_PATH, RUNTIME_PATH,
        EXPERTISE_MATRIX_PATH, CONTINUAL_ENGINE_PATH, AUDIT_PATH, SUITE_PATH,
        CORE_SOURCES_PATH, SPECIALIST_SOURCES_PATH,
        ROOT / "docs/standards/AGENCY_EXCELLENCE_STANDARD.md",
        ROOT / "docs/standards/WORLD_CLASS_AGENT_RESEARCH.md",
        ROOT / "docs/standards/PORTABLE_AGENT_RUNTIME.md",
        ROOT / ".agents/skills/agency-excellence-audit/SKILL.md",
        ROOT / ".agents/skills/portable-agent-router/SKILL.md",
        ROOT / ".agents/skills/continual-expertise-engine/SKILL.md",
    ]
    for path in required_files:
        if not path.is_file():
            fail(f"missing required excellence file: {path.relative_to(ROOT)}", failures)

    if failures:
        for item in failures:
            print(f"AGENCY_EXCELLENCE_FAIL: {item}", file=sys.stderr)
        return 2

    # Architectural stable layer: 21 + 31 = 52
    core = core_agents()
    specialists = specialist_agents()
    canonical = core + specialists

    if len(core) != 21:
        fail(f"Stable Core count drift: expected 21, got {len(core)}", failures)
    if len(specialists) != 31:
        fail(f"Specialist v3 count drift: expected 31, got {len(specialists)}", failures)
    if len(canonical) != 52 or len(set(canonical)) != 52:
        fail(
            f"combined stable identity invariant failed: count={len(canonical)}, unique={len(set(canonical))}",
            failures,
        )

    excellence = json.loads(read(EXCELLENCE_PATH))
    profiles = excellence.get("profiles", [])
    if excellence.get("stable_identity_count") != 52:
        fail("AGENT_EXCELLENCE_MANIFEST stable_identity_count must be 52", failures)
    if len(profiles) != 52:
        fail(f"stable excellence profile count must be 52, got {len(profiles)}", failures)
    if excellence.get("required_profile_fields") != REQUIRED_PROFILE_FIELDS:
        fail("required_profile_fields drift from canonical validator contract", failures)

    profile_agents = [p.get("agent") for p in profiles]
    profile_ids = [p.get("id") for p in profiles]
    if profile_agents != canonical:
        missing = [a for a in canonical if a not in profile_agents]
        extra = [a for a in profile_agents if a not in canonical]
        fail(
            "stable excellence profile order must match Stable Core 1-21 + Specialist v3 22-52; "
            f"missing={missing}, extra={extra}",
            failures,
        )
    if profile_ids != list(range(1, 53)):
        fail("stable excellence profile IDs must be exactly 1..52", failures)

    for idx, p in enumerate(profiles, start=1):
        agent = p.get("agent", f"<profile-{idx}>")
        for field in REQUIRED_PROFILE_FIELDS:
            value = p.get(field)
            if value is None or value == "" or value == []:
                fail(f"{agent}: missing/empty excellence field {field}", failures)
        expected_tier = "core" if idx <= 21 else "specialist"
        if p.get("tier") != expected_tier:
            fail(f"{agent}: tier drift; expected {expected_tier}, got {p.get('tier')!r}", failures)
        if p.get("structural_state") != "STRUCTURALLY_READY":
            fail(f"{agent}: structural_state must be STRUCTURALLY_READY", failures)
        if p.get("behavioral_state") not in {"NOT_RUN", "TASK_VERIFIED", "PRODUCTION_VERIFIED"}:
            fail(f"{agent}: invalid behavioral_state {p.get('behavioral_state')!r}", failures)
        if p.get("external_comparative_state") not in {
            "NOT_RUN", "BENCHMARKED_FRONTIER_CANDIDATE", "WORLD_CLASS_COMPARATIVE_EVIDENCE"
        }:
            fail(f"{agent}: invalid external_comparative_state {p.get('external_comparative_state')!r}", failures)

    audit = read(AUDIT_PATH)
    suite = read(SUITE_PATH)
    core_sources = read(CORE_SOURCES_PATH)
    specialist_sources = read(SPECIALIST_SOURCES_PATH)

    for idx, agent in enumerate(canonical, start=1):
        heading = f"### {idx}. {agent}"
        if heading not in audit:
            fail(f"audit missing numbered stable profile: {heading}", failures)
        if heading not in suite:
            fail(f"championship suite missing numbered stable gate: {heading}", failures)
        source_heading = f"# {idx}. {agent}"
        source_text = core_sources if idx <= 21 else specialist_sources
        if source_heading not in source_text:
            fail(f"stable source pack missing numbered authority profile: {source_heading}", failures)

    # Production runtime layer: 89 agents
    runtime = json.loads(read(RUNTIME_PATH))
    runtime_agents = runtime.get("agents", [])
    runtime_names = [a.get("name") for a in runtime_agents]
    if runtime.get("runtime_agent_count") != 89:
        fail(f"runtime_agent_count must be 89, got {runtime.get('runtime_agent_count')!r}", failures)
    if len(runtime_agents) != 89 or len(set(runtime_names)) != 89:
        fail(f"runtime inventory must contain 89 unique agents; count={len(runtime_agents)}, unique={len(set(runtime_names))}", failures)
    if [a.get("id") for a in runtime_agents] != list(range(1, 90)):
        fail("runtime agent IDs must be exactly 1..89", failures)

    activation = runtime.get("activation_contract", {})
    if activation.get("default_state") != "STANDBY":
        fail("runtime activation default_state must be STANDBY", failures)
    if activation.get("never_broadcast_all") is not True:
        fail("runtime master trigger must never broadcast all agents", failures)

    compat = runtime.get("runtime_compatibility", {})
    for surface in ("openai_codex", "claude_code", "vinterro_one"):
        if not compat.get(surface, {}).get("supported"):
            fail(f"runtime compatibility missing/disabled: {surface}", failures)

    required_runtime = {"Finance Expert Agent", "E-commerce Expert Agent", "Shopify Agent", "Orchestrator"}
    missing_runtime = sorted(required_runtime - set(runtime_names))
    if missing_runtime:
        fail(f"runtime missing required agents: {missing_runtime}", failures)

    # Every runtime agent must have a source/expertise profile.
    expertise = json.loads(read(EXPERTISE_MATRIX_PATH))
    source_profiles = expertise.get("profiles", [])
    source_names = [p.get("name") for p in source_profiles]
    if expertise.get("agent_count") != 89:
        fail(f"expertise matrix agent_count must be 89, got {expertise.get('agent_count')!r}", failures)
    if len(source_profiles) != 89 or len(set(source_names)) != 89:
        fail(f"expertise source matrix must contain 89 unique profiles; count={len(source_profiles)}, unique={len(set(source_names))}", failures)
    if source_names != runtime_names:
        missing = [n for n in runtime_names if n not in source_names]
        extra = [n for n in source_names if n not in runtime_names]
        fail(f"expertise matrix must exactly follow runtime inventory order; missing={missing}, extra={extra}", failures)

    for p in source_profiles:
        name = p.get("name", "<unknown>")
        tiers = p.get("source_tiers", {})
        if not tiers.get("primary"):
            fail(f"{name}: missing primary source tier", failures)
        if "canonical_github" not in tiers:
            fail(f"{name}: missing canonical_github source tier", failures)
        if not p.get("research_topics"):
            fail(f"{name}: missing research_topics", failures)
        if not p.get("continual_queries"):
            fail(f"{name}: missing continual_queries", failures)
        if not p.get("ingestion_rules"):
            fail(f"{name}: missing ingestion_rules", failures)
        refresh = p.get("refresh_policy", {})
        if not refresh.get("scheduled_days") or not refresh.get("event_triggers"):
            fail(f"{name}: incomplete refresh policy", failures)
        if not p.get("mastery_gate"):
            fail(f"{name}: missing mastery_gate", failures)

    by_name = {p["name"]: p for p in source_profiles}
    shopify = by_name.get("Shopify Agent", {})
    shopify_sources = " ".join(shopify.get("source_tiers", {}).get("primary", []) + shopify.get("source_tiers", {}).get("canonical_github", []))
    for needle in ("shopify.dev", "Shopify/dawn", "Shopify/cli", "Shopify/hydrogen", "Shopify/theme-tools", "Shopify/agent-skills"):
        if needle not in shopify_sources:
            fail(f"Shopify Agent expertise profile missing mandatory upstream: {needle}", failures)

    governance = {
        "AGENTS.md": read(ROOT / "AGENTS.md"),
        "AGENT_REGISTRY.md": read(ROOT / "docs/standards/AGENT_REGISTRY.md"),
        ".codex/config.toml": read(ROOT / ".codex/config.toml"),
        "STABLE_AGENT_CORE.md": read(CORE_PATH),
        "QUALIFIED_AGENT_ROUTING.md": read(ROOT / "docs/standards/QUALIFIED_AGENT_ROUTING.md"),
        "AGENT_ENGINEERING.md": read(ROOT / "docs/standards/AGENT_ENGINEERING.md"),
        "WORLD_CLASS_AGENT_RESEARCH.md": read(ROOT / "docs/standards/WORLD_CLASS_AGENT_RESEARCH.md"),
        "GITHUB_SPECIALIST_EXPANSION_V3.md": read(ROOT / "docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md"),
        "AGENT_SCOREBOARD.md": read(ROOT / "docs/evals/AGENT_SCOREBOARD.md"),
        "GITHUB_SPECIALIST_SCOREBOARD_V3.md": read(ROOT / "docs/evals/GITHUB_SPECIALIST_SCOREBOARD_V3.md"),
        "AGENCY_EXCELLENCE_STANDARD.md": read(ROOT / "docs/standards/AGENCY_EXCELLENCE_STANDARD.md"),
        "PORTABLE_AGENT_RUNTIME.md": read(ROOT / "docs/standards/PORTABLE_AGENT_RUNTIME.md"),
        "AGENT_CONTINUAL_EXPERTISE_ENGINE.md": read(CONTINUAL_ENGINE_PATH),
    }

    required_refs = {
        "AGENTS.md": ["AGENCY_EXCELLENCE_STANDARD.md", "AGENT_CONTINUAL_EXPERTISE_ENGINE.md", "AGENT_EXPERTISE_SOURCE_MATRIX.json", "validate_agency_excellence.py"],
        "AGENT_REGISTRY.md": ["AGENCY_EXCELLENCE_STANDARD.md", "AGENT_EXPERTISE_SOURCE_MATRIX.json"],
        ".codex/config.toml": ["AGENCY_EXCELLENCE_STANDARD.md", "SPECIALIST_EXCELLENCE_SOURCE_PACKS.md", "AGENT_EXCELLENCE_MANIFEST.json"],
        "STABLE_AGENT_CORE.md": ["AGENCY_EXCELLENCE_STANDARD.md", "AGENT_EXCELLENCE_MANIFEST"],
        "QUALIFIED_AGENT_ROUTING.md": ["AGENCY_EXCELLENCE_STANDARD.md", "Agency excellence qualification overlay"],
        "AGENT_ENGINEERING.md": ["AGENCY_EXCELLENCE_STANDARD.md", "Principal-level operating bar"],
        "WORLD_CLASS_AGENT_RESEARCH.md": ["SPECIALIST_EXCELLENCE_SOURCE_PACKS.md", "AGENT_EXCELLENCE_MANIFEST"],
        "GITHUB_SPECIALIST_EXPANSION_V3.md": ["AGENCY_EXCELLENCE_STANDARD.md", "AGENT_CHAMPIONSHIP_SUITE_V2.md"],
        "AGENT_SCOREBOARD.md": ["AGENT_EXCELLENCE_MANIFEST.json"],
        "GITHUB_SPECIALIST_SCOREBOARD_V3.md": ["AGENT_EXCELLENCE_MANIFEST.json"],
        "AGENCY_EXCELLENCE_STANDARD.md": ["world-class agency target", "Vinterro One 89-agent runtime contract"],
        "PORTABLE_AGENT_RUNTIME.md": ["89 active agents", "STANDBY", "AGENT_EXPERTISE_SOURCE_MATRIX.json"],
        "AGENT_CONTINUAL_EXPERTISE_ENGINE.md": ["all 89 Vinterro One runtime agents", "Shopify deep-specialist requirement", "ercan_os_agent_expertise_profiles", "record_agent_learning"],
    }
    for surface, needles in required_refs.items():
        text = governance[surface]
        for needle in needles:
            if needle not in text:
                fail(f"{surface} missing agency/expertise reference: {needle}", failures)

    if failures:
        for item in failures:
            print(f"AGENCY_EXCELLENCE_FAIL: {item}", file=sys.stderr)
        return 2

    print("Agency Excellence coverage: PASS")
    print("Stable architectural identities: 52/52")
    print("Vinterro One runtime agents: 89/89")
    print("Runtime source/expertise profiles: 89/89")
    print("Portable adapters: Codex + Claude + Vinterro One")
    print("Finance Expert: present")
    print("E-commerce Expert: present")
    print("ACTIVE/STANDBY anti-broadcast contract: enforced")
    print("Behavioral and comparative mastery states remain evidence-driven.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
