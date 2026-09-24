#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CORE = [
    "@Orchestrator", "@UpstreamIntelligence", "@ShopifyExpert", "@WordPressExpert", "@WixExpert",
    "@DragDrop", "@VinterroDigital", "@AyvalıkVibes", "@GoAyvalık", "@ScreenshotToCode",
    "@RealAsset", "@PixelMatch", "@UXEnhancement", "@ProductionQA", "@SEOExpert",
    "@SocialMediaExpert", "@CreativeDesignExpert", "@WebAppExpert", "@SecurityExpert",
    "@PerformanceExpert", "@AgentMCPExpert",
]

REQUIRED_PROFILE_FIELDS = {
    "id", "agent", "tier", "domain", "principal_mandate", "gap_before_remediation",
    "remediation", "hard_fail", "championship_gate", "structural_state",
    "behavioral_state", "external_comparative_state",
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def fail(msg: str) -> None:
    print(f"AGENCY_EXCELLENCE_FAIL: {msg}", file=sys.stderr)


def main() -> int:
    errors: list[str] = []

    v3 = json.loads(read("docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json"))
    extension: list[str] = []
    for domain in v3["domains"].values():
        extension.extend(domain["agents"])

    canonical = CORE + extension
    if len(CORE) != 21:
        errors.append(f"core count drift: expected 21, got {len(CORE)}")
    if len(extension) != 31:
        errors.append(f"extension count drift: expected 31, got {len(extension)}")
    if len(canonical) != 52 or len(set(canonical)) != 52:
        errors.append("canonical 52-agent list is not exactly 52 unique identities")

    excellence = json.loads(read("docs/standards/AGENT_EXCELLENCE_MANIFEST.json"))
    profiles = excellence.get("profiles", [])
    if excellence.get("stable_identity_count") != 52:
        errors.append("AGENT_EXCELLENCE_MANIFEST stable_identity_count must be 52")
    if len(profiles) != 52:
        errors.append(f"excellence profile count must be 52, got {len(profiles)}")

    profile_agents = [p.get("agent") for p in profiles]
    profile_ids = [p.get("id") for p in profiles]
    if profile_agents != canonical:
        errors.append("excellence profile agent order does not match Stable Core 1-21 + v3 extension 22-52")
    if profile_ids != list(range(1, 53)):
        errors.append("excellence profile IDs must be exactly 1..52")

    for p in profiles:
        missing = REQUIRED_PROFILE_FIELDS - set(p)
        if missing:
            errors.append(f"{p.get('agent')}: missing fields {sorted(missing)}")
        if p.get("structural_state") != "STRUCTURALLY_READY":
            errors.append(f"{p.get('agent')}: structural_state must be STRUCTURALLY_READY")
        if p.get("behavioral_state") not in {"NOT_RUN", "TASK_VERIFIED", "PRODUCTION_VERIFIED"}:
            errors.append(f"{p.get('agent')}: invalid behavioral_state")
        if p.get("external_comparative_state") not in {"NOT_RUN", "BENCHMARKED_FRONTIER_CANDIDATE", "WORLD_CLASS_COMPARATIVE_EVIDENCE"}:
            errors.append(f"{p.get('agent')}: invalid external_comparative_state")

    audit = read("docs/evals/AGENT_EXCELLENCE_AUDIT_2026-09-24.md")
    suite = read("docs/evals/AGENT_CHAMPIONSHIP_SUITE_V2.md")
    core_sources = read("docs/research/AGENT_SOURCE_PACKS.md")
    specialist_sources = read("docs/research/SPECIALIST_EXCELLENCE_SOURCE_PACKS.md")

    for idx, agent in enumerate(canonical, start=1):
        heading = rf"(?m)^### {idx}\. {re.escape(agent)}(?:\s|$)"
        if not re.search(heading, audit):
            errors.append(f"audit missing numbered heading {idx}. {agent}")
        if not re.search(heading, suite):
            errors.append(f"championship suite missing numbered heading {idx}. {agent}")
        source_heading = rf"(?m)^# {idx}\. {re.escape(agent)}(?:\s|$)"
        source_text = core_sources if idx <= 21 else specialist_sources
        if not re.search(source_heading, source_text):
            errors.append(f"source pack missing numbered heading {idx}. {agent}")

    root_agents = read("AGENTS.md")
    engineering = read("docs/standards/AGENT_ENGINEERING.md")
    stable = read("docs/standards/STABLE_AGENT_CORE.md")
    research = read("docs/standards/WORLD_CLASS_AGENT_RESEARCH.md")
    qualified = read("docs/standards/QUALIFIED_AGENT_ROUTING.md")
    standard = read("docs/standards/AGENCY_EXCELLENCE_STANDARD.md")

    required_refs = {
        "AGENTS.md": (root_agents, "AGENCY_EXCELLENCE_STANDARD.md"),
        "AGENT_ENGINEERING.md": (engineering, "AGENCY_EXCELLENCE_STANDARD.md"),
        "STABLE_AGENT_CORE.md": (stable, "AGENCY_EXCELLENCE_STANDARD.md"),
        "WORLD_CLASS_AGENT_RESEARCH.md": (research, "SPECIALIST_EXCELLENCE_SOURCE_PACKS.md"),
        "QUALIFIED_AGENT_ROUTING.md": (qualified, "Agency excellence qualification overlay"),
        "AGENCY_EXCELLENCE_STANDARD.md": (standard, "principal-level specialist"),
    }
    for name, (text, needle) in required_refs.items():
        if needle not in text:
            errors.append(f"{name} missing agency-excellence reference: {needle}")

    if errors:
        for error in errors:
            fail(error)
        return 2

    print("Agency Excellence coverage: PASS")
    print("Stable Core profiles: 21/21")
    print("GitHub Specialist v3 profiles: 31/31")
    print("Total stable identity excellence coverage: 52/52")
    print("Behavioral and external comparative states remain evidence-driven; NOT_RUN is not auto-promoted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
