#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json"
ENGINE = ROOT / "docs/standards/AGENT_CONTINUAL_EXPERTISE_ENGINE.md"
PACK = ROOT / "docs/standards/ACADEMIC_RESEARCH_SOURCE_PACK.md"
CATALOG = ROOT / "docs/research/ACADEMIC_SOURCE_CATALOG_2026-09-29.md"
AGENTS = ROOT / "AGENTS.md"

REQUIRED_DISCOVERY = {
    "https://api.openalex.org/",
    "https://api.crossref.org/",
    "https://graph.openaire.eu/",
    "https://core.ac.uk/",
    "https://oatd.org/",
    "https://www.opendoar.org/",
}
REQUIRED_THESIS = {
    "https://dspace.mit.edu/communities/6fc02cc2-0d14-4023-8a6f-d9900d0c4302",
    "https://library.stanford.edu/sdr-stanford-digital-repository",
    "https://dash.harvard.edu/",
    "https://repository.tudelft.nl/",
    "https://aaltodoc.aalto.fi/",
    "https://www.research-collection.ethz.ch/",
    "https://tez.yok.gov.tr/UlusalTezMerkezi/",
}
REQUIRED_GITHUB = {
    "openai/openai-agents-python",
    "microsoft/autogen",
    "All-Hands-AI/OpenHands",
    "langchain-ai/langgraph",
    "stanfordnlp/dspy",
    "princeton-nlp/SWE-agent",
    "SWE-bench/SWE-bench",
    "web-arena-x/webarena",
    "xlang-ai/OSWorld",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []
    for path in (MATRIX, ENGINE, PACK, CATALOG, AGENTS):
        if not path.is_file():
            fail(f"missing required academic expertise file: {path.relative_to(ROOT)}", failures)
    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    profiles = matrix.get("profiles") or []
    count = matrix.get("agent_count")
    coverage = matrix.get("coverage_contract") or {}

    if not isinstance(count, int) or count < 103:
        fail(f"agent_count must preserve synchronized live floor >=103, got {count!r}", failures)
    if len(profiles) != count:
        fail(f"profile count drift: {len(profiles)} != {count}", failures)
    if coverage.get("profiles") != len(profiles):
        fail(f"coverage_contract.profiles drift: {coverage.get('profiles')} != {len(profiles)}", failures)

    academic = (matrix.get("source_pack_catalog") or {}).get("academic_research") or {}
    primary = set(academic.get("primary") or [])
    github = set(academic.get("github") or [])
    for uri in sorted(REQUIRED_DISCOVERY | REQUIRED_THESIS):
        if uri not in primary:
            fail(f"academic_research missing source: {uri}", failures)
    for name in sorted(REQUIRED_GITHUB):
        if name not in github:
            fail(f"academic_research missing canonical GitHub research source: {name}", failures)

    for profile in profiles:
        name = profile.get("name", "<unknown>")
        if "academic_research" not in (profile.get("source_packs") or []):
            fail(f"{name}: academic_research not loaded", failures)
        if len(profile.get("academic_queries") or []) < 2:
            fail(f"{name}: needs >=2 academic_queries", failures)
        if len(profile.get("thesis_queries") or []) < 2:
            fail(f"{name}: needs >=2 thesis_queries", failures)
        policy = profile.get("academic_ingestion") or {}
        if policy.get("preserve_limitations") is not True:
            fail(f"{name}: academic_ingestion must preserve limitations", failures)
        if policy.get("require_original_source_for_material_claims") is not True:
            fail(f"{name}: material academic claims must require original-source inspection", failures)

    engine = ENGINE.read_text(encoding="utf-8")
    pack = PACK.read_text(encoding="utf-8")
    agents = AGENTS.read_text(encoding="utf-8")

    for needle in (
        "Academic, thesis and external evidence lane",
        "ACADEMIC_RESEARCH_SOURCE_PACK.md",
        "A thesis/dissertation is **Tier 3 academic evidence**",
    ):
        if needle not in engine:
            fail(f"continual expertise engine missing academic rule: {needle}", failures)

    for needle in (
        "OpenAlex",
        "Crossref",
        "OpenAIRE",
        "CORE",
        "OATD",
        "MIT Open Scholarship",
        "TU Delft Repository",
        "YÖK Ulusal Tez Merkezi",
        "Research-to-learning gate",
        "Do not permanently ingest or redistribute full copyrighted",
    ):
        if needle not in pack:
            fail(f"academic source pack missing contract/source: {needle}", failures)

    if "ACADEMIC_RESEARCH_SOURCE_PACK.md" not in agents:
        fail("AGENTS.md does not route scholarly research through academic source pack", failures)

    if failures:
        print("Academic expertise validator: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("Academic expertise validator: PASS")
    print(f"Runtime expertise profiles: {len(profiles)}")
    print("Academic research source pack: present")
    print("Academic/thesis queries: present for every profile")
    print("Original-source + copyright + limitations gates: present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
