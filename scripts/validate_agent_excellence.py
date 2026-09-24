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
AUDIT_PATH = ROOT / "docs/evals/AGENT_EXCELLENCE_AUDIT_2026-09-24.md"
SUITE_PATH = ROOT / "docs/evals/AGENT_CHAMPIONSHIP_SUITE_V2.md"

REQUIRED_PROFILE_FIELDS = [
    "id",
    "agent",
    "tier",
    "domain",
    "principal_mandate",
    "source_authority_route",
    "gap_before_remediation",
    "remediation",
    "hard_fail",
    "championship_gate",
    "independent_verification_owner",
    "structural_state",
    "behavioral_state",
    "external_comparative_state",
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
        CORE_PATH,
        SPECIALIST_PATH,
        EXCELLENCE_PATH,
        AUDIT_PATH,
        SUITE_PATH,
        ROOT / "docs/standards/AGENCY_EXCELLENCE_STANDARD.md",
        ROOT / ".agents/skills/agency-excellence-audit/SKILL.md",
    ]
    for path in required_files:
        if not path.is_file():
            fail(f"missing required excellence file: {path.relative_to(ROOT)}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    core = core_agents()
    specialists = specialist_agents()
    expected = core + specialists

    if len(core) != 21:
        fail(f"Stable Core count drift: expected 21, got {len(core)}", failures)
    if len(specialists) != 31:
        fail(f"Specialist v3 count drift: expected 31, got {len(specialists)}", failures)
    if len(expected) != 52 or len(set(expected)) != 52:
        fail(
            f"Combined identity invariant failed: count={len(expected)}, unique={len(set(expected))}",
            failures,
        )

    manifest = json.loads(read(EXCELLENCE_PATH))
    profiles = manifest.get("profiles", [])
    if manifest.get("stable_identity_count") != 52:
        fail("excellence manifest stable_identity_count must be 52", failures)
    if len(profiles) != 52:
        fail(f"excellence profile count drift: expected 52, got {len(profiles)}", failures)

    declared_fields = manifest.get("required_profile_fields", [])
    if declared_fields != REQUIRED_PROFILE_FIELDS:
        fail("required_profile_fields drift from validator contract", failures)

    ids = [p.get("id") for p in profiles]
    if ids != list(range(1, 53)):
        fail(f"excellence profile ids must be exactly 1..52, got {ids}", failures)

    manifest_agents = [p.get("agent") for p in profiles]
    if manifest_agents != expected:
        missing = [a for a in expected if a not in manifest_agents]
        extra = [a for a in manifest_agents if a not in expected]
        fail(
            "excellence manifest must follow canonical Stable Core 1–21 then Specialist v3 22–52 order; "
            f"missing={missing}, extra={extra}",
            failures,
        )

    for idx, profile in enumerate(profiles, start=1):
        agent = profile.get("agent", f"<profile-{idx}>")
        for field in REQUIRED_PROFILE_FIELDS:
            value = profile.get(field)
            if value is None or value == "" or value == []:
                fail(f"{agent} missing excellence field: {field}", failures)

        expected_tier = "core" if idx <= 21 else "specialist"
        if profile.get("tier") != expected_tier:
            fail(
                f"{agent} tier drift: expected {expected_tier}, got {profile.get('tier')!r}",
                failures,
            )

        if profile.get("structural_state") != "STRUCTURALLY_READY":
            fail(f"{agent} structural_state must be STRUCTURALLY_READY", failures)

        if profile.get("behavioral_state") not in {
            "NOT_RUN",
            "TASK_VERIFIED",
            "PRODUCTION_VERIFIED",
        }:
            fail(
                f"{agent} invalid behavioral_state: {profile.get('behavioral_state')!r}",
                failures,
            )
        if profile.get("external_comparative_state") not in {
            "NOT_RUN",
            "BENCHMARKED_FRONTIER_CANDIDATE",
            "WORLD_CLASS_COMPARATIVE_EVIDENCE",
        }:
            fail(
                f"{agent} invalid external_comparative_state: "
                f"{profile.get('external_comparative_state')!r}",
                failures,
            )

    audit = read(AUDIT_PATH)
    suite = read(SUITE_PATH)
    for idx, agent in enumerate(expected, start=1):
        heading = f"### {idx}. {agent}"
        if heading not in audit:
            fail(f"audit missing numbered profile: {heading}", failures)
        if heading not in suite:
            fail(f"championship suite missing numbered gate: {heading}", failures)

    governance = {
        "AGENTS.md": read(ROOT / "AGENTS.md"),
        "STABLE_AGENT_CORE.md": read(CORE_PATH),
        "QUALIFIED_AGENT_ROUTING.md": read(ROOT / "docs/standards/QUALIFIED_AGENT_ROUTING.md"),
        "AGENT_ENGINEERING.md": read(ROOT / "docs/standards/AGENT_ENGINEERING.md"),
        "GITHUB_SPECIALIST_EXPANSION_V3.md": read(
            ROOT / "docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md"
        ),
        "AGENT_SCOREBOARD.md": read(ROOT / "docs/evals/AGENT_SCOREBOARD.md"),
        "GITHUB_SPECIALIST_SCOREBOARD_V3.md": read(
            ROOT / "docs/evals/GITHUB_SPECIALIST_SCOREBOARD_V3.md"
        ),
    }
    required_refs = {
        "AGENTS.md": ["AGENCY_EXCELLENCE_STANDARD.md", "validate_agent_excellence.py"],
        "STABLE_AGENT_CORE.md": ["AGENCY_EXCELLENCE_STANDARD.md", "AGENT_EXCELLENCE_MANIFEST"],
        "QUALIFIED_AGENT_ROUTING.md": ["AGENCY_EXCELLENCE_STANDARD.md", "excellence fit"],
        "AGENT_ENGINEERING.md": ["AGENCY_EXCELLENCE_STANDARD.md", "Principal-level operating bar"],
        "GITHUB_SPECIALIST_EXPANSION_V3.md": [
            "AGENCY_EXCELLENCE_STANDARD.md",
            "AGENT_CHAMPIONSHIP_SUITE_V2.md",
        ],
        "AGENT_SCOREBOARD.md": ["AGENT_EXCELLENCE_MANIFEST.json"],
        "GITHUB_SPECIALIST_SCOREBOARD_V3.md": ["AGENT_EXCELLENCE_MANIFEST.json"],
    }
    for surface, needles in required_refs.items():
        text = governance[surface]
        for needle in needles:
            if needle not in text:
                fail(f"{surface} missing excellence governance reference: {needle}", failures)

    if failures:
        print("Agent Excellence validator: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("Agent Excellence validator: PASS")
    print("Stable Core: 21/21 covered")
    print("GitHub Specialist v3: 31/31 covered")
    print("Total stable identities: 52/52 covered")
    print("Numbered audit: 1..52 present")
    print("Championship gates: 52/52 present")
    print("Behavioral/comparative statuses remain evidence-gated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
