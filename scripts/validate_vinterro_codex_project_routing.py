#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT_REGISTRY = ROOT / "docs/standards/VINTERRO_PROJECT_REGISTRY.json"
RUNTIME_MANIFEST = ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
BUNDLED_PROJECT_REGISTRY = ROOT / "plugins/vinterro-one/skills/vinterro-one-router/references/VINTERRO_PROJECT_REGISTRY.json"
BUNDLED_RUNTIME_MANIFEST = ROOT / "plugins/vinterro-one/skills/vinterro-one-router/references/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
ROUTER = ROOT / "plugins/vinterro-one/skills/vinterro-one-router/SKILL.md"
CODEX_CONFIG = ROOT / ".codex/config.toml"
ROOT_AGENTS = ROOT / "AGENTS.md"
FALLBACK_AGENTS = ROOT / "projects/_runtime/AGENTS.md"
FALLBACK_PROJECT = ROOT / "projects/_runtime/PROJECT.md"

REQUIRED_FILES = (
    PROJECT_REGISTRY,
    RUNTIME_MANIFEST,
    BUNDLED_PROJECT_REGISTRY,
    BUNDLED_RUNTIME_MANIFEST,
    ROUTER,
    CODEX_CONFIG,
    ROOT_AGENTS,
    FALLBACK_AGENTS,
    FALLBACK_PROJECT,
)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            fail(f"missing required Codex routing file: {path.relative_to(ROOT)}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    registry = read_json(PROJECT_REGISTRY)
    bundled_registry = read_json(BUNDLED_PROJECT_REGISTRY)
    runtime = read_json(RUNTIME_MANIFEST)
    bundled_runtime = read_json(BUNDLED_RUNTIME_MANIFEST)

    projects = registry.get("projects") or []
    agents = runtime.get("agents") or []
    routing = registry.get("routing_contract") or {}

    if not projects:
        fail("project registry must contain at least one active project", failures)

    if routing.get("all_active_projects_supported") is not True:
        fail("project registry must declare all_active_projects_supported=true", failures)

    if routing.get("fallback_adapter") != "projects/_runtime":
        fail("project registry fallback_adapter must be projects/_runtime", failures)

    runtime_slugs = [p.get("runtime_slug") for p in projects]
    canonical_slugs = [p.get("canonical_slug") for p in projects]
    if any(not slug for slug in runtime_slugs) or len(runtime_slugs) != len(set(runtime_slugs)):
        fail("project runtime_slug values must be present and unique", failures)
    if any(not slug for slug in canonical_slugs) or len(canonical_slugs) != len(set(canonical_slugs)):
        fail("project canonical_slug values must be present and unique", failures)

    agents_by_name = {a.get("name"): a for a in agents if a.get("name")}
    for project in projects:
        name = project.get("name") or "<unnamed project>"
        lead = project.get("lead_agent")
        adapter = project.get("adapter")
        adapter_type = project.get("adapter_type")

        if not lead or lead not in agents_by_name:
            fail(f"{name}: lead agent missing from runtime manifest: {lead!r}", failures)
        else:
            lead_agent = agents_by_name[lead]
            if lead_agent.get("status") != "active":
                fail(f"{name}: project lead is not active: {lead}", failures)
            adapters = lead_agent.get("adapters") or {}
            if adapters.get("codex") is not True:
                fail(f"{name}: project lead is not Codex-enabled: {lead}", failures)

        if adapter_type not in {"dedicated", "runtime_fallback"}:
            fail(f"{name}: invalid adapter_type {adapter_type!r}", failures)

        if not adapter:
            fail(f"{name}: adapter path is required", failures)
            continue

        adapter_root = ROOT / adapter
        if not (adapter_root / "AGENTS.md").is_file():
            fail(f"{name}: adapter AGENTS.md missing at {adapter}/AGENTS.md", failures)
        if not (adapter_root / "PROJECT.md").is_file():
            fail(f"{name}: adapter PROJECT.md missing at {adapter}/PROJECT.md", failures)

        if adapter_type == "runtime_fallback" and adapter != "projects/_runtime":
            fail(f"{name}: runtime_fallback must use projects/_runtime", failures)

    if registry != bundled_registry:
        fail("bundled Codex project registry drifted from canonical project registry", failures)

    if runtime != bundled_runtime:
        fail("bundled Codex runtime manifest drifted from canonical runtime manifest", failures)

    router = ROUTER.read_text(encoding="utf-8")
    codex = CODEX_CONFIG.read_text(encoding="utf-8")
    root_agents = ROOT_AGENTS.read_text(encoding="utf-8")
    fallback = FALLBACK_AGENTS.read_text(encoding="utf-8")

    router_needles = (
        "VINTERRO_PROJECT_REGISTRY.json",
        "projects/_runtime/AGENTS.md",
        "must never be limited to hard-coded examples",
        "complete qualified global specialist/QA/risk pod",
    )
    for needle in router_needles:
        if needle not in router:
            fail(f"Codex router missing all-project rule: {needle}", failures)

    codex_needles = (
        "Project coverage is dynamic.",
        "VINTERRO_PROJECT_REGISTRY.json",
        "projects/_runtime/AGENTS.md",
        "Never restrict Codex routing to a hard-coded subset of projects.",
    )
    for needle in codex_needles:
        if needle not in codex:
            fail(f".codex/config.toml missing all-project rule: {needle}", failures)

    root_needles = (
        "Dynamic all-project Codex coverage",
        "VINTERRO_PROJECT_REGISTRY.json",
        "projects/_runtime/AGENTS.md",
        "New active projects in the live registry inherit Vinterro One routing immediately.",
    )
    for needle in root_needles:
        if needle not in root_agents:
            fail(f"AGENTS.md missing dynamic project coverage rule: {needle}", failures)

    fallback_needles = (
        "project Baş Uzman Ajanı",
        "complete materially relevant ACTIVE pod",
        "independent reviewer/QA",
        "Release Gate",
        "Never claim",
    )
    for needle in fallback_needles:
        if needle not in fallback:
            fail(f"runtime project fallback missing supervision/routing rule: {needle}", failures)

    if failures:
        print("Vinterro One Codex project routing validator: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("Vinterro One Codex project routing validator: PASS")
    print(f"Projects covered: {len(projects)}")
    print(f"Runtime agents available: {len(agents)}")
    print("All project leads: active + Codex-enabled")
    print("Dedicated and runtime-fallback adapters: valid")
    print("Canonical/plugin project registry: synchronized")
    print("Canonical/plugin runtime manifest: synchronized")
    print("Dynamic all-project + qualified-agent routing contract: present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
