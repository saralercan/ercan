#!/usr/bin/env python3
"""Structural regression gate for Vinterro One multilingual localization agents."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
MATRIX = ROOT / "docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json"
STANDARD = ROOT / "docs/standards/MULTILINGUAL_LOCALIZATION_AGENT_STANDARD.md"
SKILL = ROOT / ".agents/skills/multilingual-localization-specialists/SKILL.md"
EVAL = ROOT / "docs/evals/MULTILINGUAL_LOCALIZATION_REGRESSION.md"

SPECIALISTS = [
    "English Language & Localization Specialist",
    "Bulgarian Language & Localization Specialist",
    "Spanish Language & Localization Specialist",
    "Greek Language & Localization Specialist",
    "German Language & Localization Specialist",
    "French Language & Localization Specialist",
]
QA = "Multilingual Localization QA Auditor"
ALL = SPECIALISTS + [QA]
ADAPTERS = ("codex", "claude", "vinterro_one", "chatgpt", "openai")


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    manifest = json.loads(MANIFEST.read_text())
    matrix = json.loads(MATRIX.read_text())

    if manifest.get("runtime_agent_count") != len(manifest.get("agents", [])):
        fail("runtime_agent_count does not match manifest agents")
    if matrix.get("agent_count") != len(matrix.get("profiles", [])):
        fail("agent_count does not match expertise profiles")
    if manifest.get("runtime_agent_count", 0) < 112:
        fail("runtime registry regressed below multilingual baseline 112")
    if matrix.get("agent_count") != manifest.get("runtime_agent_count"):
        fail("runtime/expertise counts diverge")

    agents = {a["name"]: a for a in manifest["agents"]}
    profiles = {p["name"]: p for p in matrix["profiles"]}

    for name in ALL:
        if name not in agents:
            fail(f"missing runtime agent: {name}")
        if name not in profiles:
            fail(f"missing expertise profile: {name}")

        agent = agents[name]
        profile = profiles[name]

        if agent.get("family") != "language_localization":
            fail(f"{name}: wrong runtime family")
        if profile.get("family") != "language_localization":
            fail(f"{name}: wrong profile family")
        if agent.get("activation") != "jit" or agent.get("default_state") != "STANDBY":
            fail(f"{name}: must be JIT/STANDBY")
        for adapter in ADAPTERS:
            if agent.get("adapters", {}).get(adapter) is not True:
                fail(f"{name}: missing adapter {adapter}")
        packs = set(profile.get("source_packs", []))
        for required in ("language_localization", "academic_research"):
            if required not in packs:
                fail(f"{name}: missing source pack {required}")
        tiers = profile.get("source_tiers", {})
        if len(tiers.get("primary", [])) < 5:
            fail(f"{name}: insufficient primary authority sources")
        if len(tiers.get("canonical_github", [])) < 4:
            fail(f"{name}: insufficient canonical GitHub sources")
        if not profile.get("academic_queries") or not profile.get("thesis_queries"):
            fail(f"{name}: academic/thesis discovery missing")

    for name in SPECIALISTS:
        if QA not in agents[name].get("handoffs", []):
            fail(f"{name}: independent multilingual QA handoff missing")

    if agents[QA].get("role") != "multilingual_localization_qa":
        fail("multilingual QA role mismatch")

    for coordinator in ("Orchestrator", "Content Agent"):
        missing = set(ALL) - set(agents[coordinator].get("handoffs", []))
        if missing:
            fail(f"{coordinator}: multilingual handoffs missing: {sorted(missing)}")

    lf = agents.get("Language Freshness Agent", {})
    if "HUMAN-LANGUAGE ROUTING CLARIFICATION" not in lf.get("instructions", ""):
        fail("Language Freshness Agent human-language routing clarification missing")

    pack = matrix.get("source_pack_catalog", {}).get("language_localization")
    if not pack:
        fail("language_localization source pack missing")
    expected_repos = {
        "Unbabel/COMET",
        "google-research/mt-metrics-eval",
        "mjpost/sacrebleu",
        "Helsinki-NLP/OPUS-MT-train",
        "unicode-org/cldr",
        "w3c/i18n-drafts",
    }
    if not expected_repos.issubset(set(pack.get("github", []))):
        fail("language_localization canonical GitHub set incomplete")
    if "facebookresearch/flores" in set(pack.get("github", [])):
        fail("archived FLORES repo must not be current canonical implementation authority")

    for path in (STANDARD, SKILL, EVAL):
        if not path.exists() or not path.read_text().strip():
            fail(f"required multilingual contract missing: {path}")

    standard = STANDARD.read_text()
    for token in ("Source-intent freeze", "Independent QA", "CRITICAL", "Spanish", "Bulgarian", "Greek", "German", "French", "English"):
        if token not in standard:
            fail(f"standard missing required rule/token: {token}")

    print(
        "PASS: multilingual localization pod structurally verified "
        f"({manifest['runtime_agent_count']} runtime agents / {matrix['agent_count']} expertise profiles)"
    )


if __name__ == "__main__":
    main()
