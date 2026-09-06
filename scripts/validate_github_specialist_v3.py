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
        "identity_counts",
        "routing_standard",
        "registry",
        "qualified_routing",
        "catalog",
        "current_index",
        "adoption_ledger",
        "regression_eval",
        "extension_scoreboard",
        "extension_certification",
        "evidence_scan",
        "latest_refresh_scan",
        "router_skill",
        "upstream_aliases",
        "archived_rejections",
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
        manifest["extension_scoreboard"],
        manifest["extension_certification"],
        manifest["evidence_scan"],
        manifest["latest_refresh_scan"],
        manifest["router_skill"],
        "docs/standards/STABLE_AGENT_CORE.md",
        "docs/standards/DOMAIN_EXPERT_REGISTRY.md",
        "docs/evals/AGENT_SCOREBOARD.md",
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
    scoreboard = read(manifest["extension_scoreboard"])
    certification = read(manifest["extension_certification"])
    refresh_scan = read(manifest["latest_refresh_scan"])
    stable_core = read("docs/standards/STABLE_AGENT_CORE.md")
    domain_registry = read("docs/standards/DOMAIN_EXPERT_REGISTRY.md")
    core_scoreboard = read("docs/evals/AGENT_SCOREBOARD.md")
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
            if agent not in scoreboard:
                fail(f"agent missing from v3 extension scoreboard: {agent}", failures)
            if agent not in certification:
                fail(f"agent missing from v3 behavioral certification contract: {agent}", failures)

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

    counts = manifest["identity_counts"]
    expected_core = counts.get("stable_core")
    expected_extension = counts.get("specialist_extension")
    expected_total = counts.get("total_named_stable_routing_identities")

    if expected_core != 21:
        fail(f"stable core count drift: expected manifest stable_core=21, got {expected_core!r}", failures)
    if expected_extension != len(all_agents):
        fail(
            f"specialist extension count drift: manifest={expected_extension!r}, actual={len(all_agents)}",
            failures,
        )
    if expected_total != expected_core + expected_extension:
        fail(
            f"total identity count drift: total={expected_total!r}, core+extension={expected_core + expected_extension}",
            failures,
        )
    if expected_extension != 31 or expected_total != 52:
        fail(
            f"v3 accounting invariant drift: expected 21 core + 31 extension = 52 total, got "
            f"{expected_core}+{expected_extension}={expected_total}",
            failures,
        )

    upstream_repo_names = {repo.lower() for _, repo, _ in all_upstreams}
    for agent in all_agents:
        normalized = agent.lstrip("@").lower()
        if normalized in upstream_repo_names:
            fail(f"agent identity incorrectly equals upstream repo: {agent}", failures)

    for _, repo, _ in all_upstreams:
        if repo not in catalog and repo not in current and repo not in ledger:
            fail(f"upstream missing from catalog/current/ledger surfaces: {repo}", failures)

    # Canonical repository aliases: aliases must never re-enter the active domain upstream lists.
    aliases = manifest.get("upstream_aliases", [])
    if not isinstance(aliases, list) or not aliases:
        fail("upstream_aliases must be a non-empty list", failures)
    alias_names: set[str] = set()
    canonical_names: set[str] = set()
    active_repos = {repo for _, repo, _ in all_upstreams}
    for item in aliases:
        alias = item.get("alias", "")
        canonical = item.get("canonical", "")
        status = item.get("status", "")
        if not alias or "/" not in alias:
            fail(f"invalid upstream alias: {alias!r}", failures)
        if not canonical or "/" not in canonical:
            fail(f"invalid canonical repo for alias {alias!r}: {canonical!r}", failures)
        if alias == canonical:
            fail(f"alias equals canonical repo: {alias}", failures)
        if status != "SUPERSEDED_RENAMED":
            fail(f"alias status drift for {alias}: expected SUPERSEDED_RENAMED, got {status!r}", failures)
        if alias in active_repos:
            fail(f"superseded alias reintroduced as active upstream: {alias}", failures)
        if canonical not in active_repos:
            fail(f"canonical target missing from active upstreams: {canonical}", failures)
        alias_names.add(alias)
        canonical_names.add(canonical)
        for surface_name, surface in [
            ("catalog", catalog),
            ("current", current),
            ("ledger", ledger),
            ("refresh_scan", refresh_scan),
        ]:
            if alias not in surface or canonical not in surface:
                fail(
                    f"canonical rename evidence missing in {surface_name}: {alias} -> {canonical}",
                    failures,
                )

    required_aliases = {
        "amzn/style-dictionary": "style-dictionary/style-dictionary",
        "Nuraveda-Labs/ai-seo-agent": "Meshpilot-AGI/ai-seo-agent",
    }
    alias_map = {item.get("alias"): item.get("canonical") for item in aliases}
    for alias, canonical in required_aliases.items():
        if alias_map.get(alias) != canonical:
            fail(f"required canonical alias drift: {alias} must map to {canonical}", failures)

    # Archived candidates are explicit non-promotions and must not enter active upstreams.
    archived_rejections = manifest.get("archived_rejections", [])
    if not isinstance(archived_rejections, list):
        fail("archived_rejections must be a list", failures)
        archived_rejections = []
    required_archived = {
        "lost-pixel/lost-pixel",
        "Shopify/react-native-performance",
    }
    if not required_archived.issubset(set(archived_rejections)):
        fail(
            f"required archived rejections missing: {sorted(required_archived - set(archived_rejections))}",
            failures,
        )
    for repo in archived_rejections:
        if repo in active_repos:
            fail(f"archived rejection reintroduced as active upstream: {repo}", failures)
        if repo not in current or repo not in ledger or repo not in refresh_scan:
            fail(f"archived rejection lacks current/ledger/scan evidence: {repo}", failures)

    # Explicit canonical decisions that must remain stable unless a future reviewed status change updates this doctor.
    seo_decisions = {repo: decision for domain, repo, decision in all_upstreams if domain == "seo"}
    if seo_decisions.get("Meshpilot-AGI/ai-seo-agent") != "ADOPT_PATTERN_ONLY":
        fail("Meshpilot-AGI/ai-seo-agent must remain ADOPT_PATTERN_ONLY in active SEO upstreams", failures)
    branding_decisions = {repo: decision for domain, repo, decision in all_upstreams if domain == "branding"}
    if branding_decisions.get("style-dictionary/style-dictionary") != "ADOPT_PATTERN_ONLY":
        fail("style-dictionary/style-dictionary must remain ADOPT_PATTERN_ONLY in active branding upstreams", failures)

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

    core_count_needles = [
        "Canonical stable core count: **21**",
        "GitHub Specialist v3 extension count: **31**",
        "Total named stable routing identities: **52**",
    ]
    for needle in core_count_needles:
        if needle not in stable_core:
            fail(f"stable-core accounting surface missing: {needle}", failures)

    if "Combined named stable routing surface: **52 identities**" not in domain_registry:
        fail("domain expert registry does not acknowledge 21+31=52 stable routing surface", failures)

    if "Specialist-extension structural readiness: **31/31 PASS**" not in scoreboard:
        fail("v3 extension scoreboard missing 31/31 PASS structural summary", failures)
    if "Total named stable routing identities: **52**" not in scoreboard:
        fail("v3 extension scoreboard missing 52-identity accounting", failures)
    if "Behavioral specialist certification: **NOT_RUN**" not in scoreboard:
        fail("v3 extension scoreboard must keep behavioral certification NOT_RUN", failures)

    if "Stable identities checked: **21**" not in core_scoreboard:
        fail("core scoreboard must remain scoped to 21 Stable Core identities", failures)
    if "Structural readiness: **21/21 PASS**" not in core_scoreboard:
        fail("core scoreboard 21/21 structural summary drift", failures)

    certification_needles = [
        "PRODUCTION_VERIFIED",
        "85/100",
        "zero hard fails",
        "behavioral status remains `NOT_RUN`",
    ]
    certification_lower = certification.lower()
    for needle in certification_needles:
        if needle.lower() not in certification_lower:
            fail(f"v3 behavioral certification contract missing: {needle}", failures)

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
        "canonical_repo_redirects_are_normalized": ["canonical", "redirect"],
    }
    combined_governance = "\n".join(
        [expansion, routing, catalog, ledger, regression, scoreboard, certification, stable_core, refresh_scan]
    ).lower()
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
    print(f"Stable Core identities: {expected_core}")
    print(f"Specialist extension identities: {len(all_agents)}")
    print(f"Total named stable routing identities: {expected_total}")
    print(f"Upstream references: {len(all_upstreams)}")
    print(f"Canonical aliases guarded: {len(aliases)}")
    print(f"Archived rejections guarded: {len(archived_rejections)}")
    print(f"Referenced files: {len(set(referenced_files))}")
    print("Behavioral specialist certification: NOT_RUN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
