#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    if not MANIFEST_PATH.exists():
        print(f"Missing manifest: {MANIFEST_PATH.relative_to(ROOT)}", file=sys.stderr)
        return 2

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    required_top_level = [
        "routing_standard",
        "registry",
        "qualified_routing",
        "catalog",
        "current_index",
        "adoption_ledger",
        "regression_eval",
        "evidence_scan",
        "router_skill",
        "domains",
        "invariants",
    ]
    for key in required_top_level:
        if key not in manifest:
            fail(f"manifest missing top-level key: {key}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    referenced_files = [
        manifest["routing_standard"],
        manifest["registry"],
        manifest["qualified_routing"],
        manifest["catalog"],
        manifest["current_index"],
        manifest["adoption_ledger"],
        manifest["regression_eval"],
        manifest["evidence_scan"],
        manifest["router_skill"],
    ]

    for domain, config in manifest["domains"].items():
        referenced_files.append(config["skill"])
        referenced_files.extend(config.get("additional_skills", []))

    for path in sorted(set(referenced_files)):
        if not (ROOT / path).is_file():
            fail(f"referenced file does not exist: {path}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    registry = read(manifest["registry"])
    routing = read(manifest["qualified_routing"])
    expansion = read(manifest["routing_standard"])
    catalog = read(manifest["catalog"])
    current = read(manifest["current_index"])
    ledger = read(manifest["adoption_ledger"])
    regression = read(manifest["regression_eval"])
    root_agents = read("AGENTS.md")

    all_agents: list[str] = []
    all_upstreams: list[tuple[str, str, str]] = []

    allowed_decisions = {
        "ADOPT",
        "ADOPT_WHEN_NEEDED",
        "ADOPT_PATTERN_ONLY",
        "WATCHLIST",
        "SUPERSEDED",
        "HISTORICAL_ARCHIVED",
    }

    for domain, config in manifest["domains"].items():
        agents = config.get("agents", [])
        if not agents:
            fail(f"domain has no agents: {domain}", failures)

        if len(set(agents)) != len(agents):
            fail(f"duplicate agent inside domain {domain}", failures)

        for agent in agents:
            all_agents.append(agent)
            if agent not in registry:
                fail(f"agent missing from registry: {agent}", failures)
            if agent not in expansion:
                fail(f"agent missing from expansion standard: {agent}", failures)

        for upstream in config.get("upstreams", []):
            repo = upstream.get("repo", "")
            decision = upstream.get("decision", "")
            if not repo or "/" not in repo:
                fail(f"invalid upstream repo in {domain}: {repo!r}", failures)
            if decision not in allowed_decisions:
                fail(f"invalid upstream decision for {repo}: {decision}", failures)
            all_upstreams.append((domain, repo, decision))

    if len(set(all_agents)) != len(all_agents):
        seen: set[str] = set()
        dupes: set[str] = set()
        for agent in all_agents:
            if agent in seen:
                dupes.add(agent)
            seen.add(agent)
        fail(f"stable agent identity duplicated across domains: {sorted(dupes)}", failures)

    upstream_repo_names = {repo.lower() for _, repo, _ in all_upstreams}
    for agent in all_agents:
        normalized = agent.lstrip("@").lower()
        if normalized in upstream_repo_names:
            fail(f"agent identity incorrectly equals upstream repo: {agent}", failures)

    for _, repo, _ in all_upstreams:
        if repo not in catalog and repo not in current and repo not in ledger:
            fail(f"upstream missing from catalog/current/ledger surfaces: {repo}", failures)

    required_root_refs = [
        "GITHUB_SPECIALIST_EXPANSION_V3.md",
        "github-specialist-router/SKILL.md",
    ]
    for ref in required_root_refs:
        if ref not in root_agents:
            fail(f"root AGENTS.md missing v3 reference: {ref}", failures)

    if "GITHUB_SPECIALIST_EXPANSION_V3.md" not in routing:
        fail("qualified routing does not reference v3 expansion", failures)

    if "GITHUB_SPECIALIST_ROUTING_V3.md" not in expansion and "GITHUB_SPECIALIST_ROUTING_V3.md" not in root_agents:
        fail("v3 regression eval is not linked from governing surfaces", failures)

    invariants = manifest["invariants"]
    for key, value in invariants.items():
        if value is not True:
            fail(f"manifest invariant must be true: {key}", failures)

    invariant_evidence = {
        "stable_agent_identity_is_not_upstream_repo": ["replaceable", "agent identit"],
        "qualified_routing_not_literal_full_fanout": ["must not fan out", "minimum sufficient"],
        "implementation_does_not_self_certify": ["independent", "self-cert"],
        "meta_attribution_is_not_incrementality": ["causal", "ROAS"],
        "publishing_requires_authenticated_surface": ["authenticated", "publishing"],
        "archived_upstreams_not_primary_production_dependency": ["archived", "primary"],
    }
    combined_governance = "\n".join([expansion, routing, catalog, ledger, regression]).lower()
    for key, needles in invariant_evidence.items():
        for needle in needles:
            if needle.lower() not in combined_governance:
                fail(f"invariant lacks governance evidence ({key}): {needle}", failures)

    archived_brand = [
        (repo, decision)
        for _, repo, decision in all_upstreams
        if repo.lower() == "scty-inc/brand.md"
    ]
    if archived_brand != [("SCTY-Inc/brand.md", "HISTORICAL_ARCHIVED")]:
        fail("SCTY-Inc/brand.md must remain HISTORICAL_ARCHIVED", failures)

    meta_required = {
        "facebookexperimental/Robyn": "ADOPT_WHEN_NEEDED",
        "facebookincubator/GeoLift": "ADOPT_WHEN_NEEDED",
    }
    meta_decisions = {repo: decision for domain, repo, decision in all_upstreams if domain == "meta_ads"}
    for repo, expected in meta_required.items():
        if meta_decisions.get(repo) != expected:
            fail(f"Meta science decision drift: {repo} must be {expected}", failures)

    if failures:
        print("GitHub Specialist v3 doctor: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("GitHub Specialist v3 doctor: PASS")
    print(f"Domains: {len(manifest['domains'])}")
    print(f"Stable agents: {len(all_agents)}")
    print(f"Upstream references: {len(all_upstreams)}")
    print(f"Referenced files: {len(set(referenced_files))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
