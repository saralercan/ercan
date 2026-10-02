#!/usr/bin/env python3
"""Validate the Vinterro One -> native Codex agent bridge."""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / ".codex/config.toml"
AGENT_DIR = ROOT / ".codex/agents"
MANIFEST = ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
BRIDGE = ROOT / "docs/standards/CODEX_NATIVE_AGENT_BRIDGE.md"
ROUTER = ROOT / "plugins/vinterro-one/skills/vinterro-one-router/SKILL.md"

REQUIRED_ROLES = {
    "vinterro_orchestrator": "agents/vinterro-orchestrator.toml",
    "vinterro_project_lead": "agents/vinterro-project-lead.toml",
    "vinterro_specialist": "agents/vinterro-specialist.toml",
    "vinterro_researcher": "agents/vinterro-researcher.toml",
    "vinterro_implementer": "agents/vinterro-implementer.toml",
    "vinterro_reviewer": "agents/vinterro-reviewer.toml",
    "vinterro_qa": "agents/vinterro-qa.toml",
    "vinterro_security": "agents/vinterro-security.toml",
    "language_en": "agents/language-en.toml",
    "language_bg": "agents/language-bg.toml",
    "language_es": "agents/language-es.toml",
    "language_el": "agents/language-el.toml",
    "language_de": "agents/language-de.toml",
    "language_fr": "agents/language-fr.toml",
    "multilingual_qa": "agents/multilingual-qa.toml",
}

LANGUAGE_RUNTIME_NAMES = (
    "English Language & Localization Specialist",
    "Bulgarian Language & Localization Specialist",
    "Spanish Language & Localization Specialist",
    "Greek Language & Localization Specialist",
    "German Language & Localization Specialist",
    "French Language & Localization Specialist",
    "Multilingual Localization QA Auditor",
)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []

    for path in (CONFIG, MANIFEST, BRIDGE, ROUTER):
        if not path.is_file():
            fail(f"missing required bridge file: {path.relative_to(ROOT)}", failures)

    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    config = tomllib.loads(CONFIG.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    agents_cfg = config.get("agents") or {}

    if agents_cfg.get("enabled") is not True:
        fail("Codex [agents] must be enabled", failures)

    limit = agents_cfg.get("max_concurrent_threads_per_session")
    if not isinstance(limit, int) or not (2 <= limit <= 16):
        fail("max_concurrent_threads_per_session must be an explicit bounded integer 2..16", failures)

    if agents_cfg.get("max_threads") is not None:
        fail("legacy agents.max_threads alias must not be used", failures)

    for role, expected_rel in REQUIRED_ROLES.items():
        role_cfg = agents_cfg.get(role)
        if not isinstance(role_cfg, dict):
            fail(f"missing native Codex role declaration: {role}", failures)
            continue
        if role_cfg.get("config_file") != expected_rel:
            fail(f"{role}: config_file mismatch", failures)
        if not str(role_cfg.get("description") or "").strip():
            fail(f"{role}: description missing", failures)

        config_path = CONFIG.parent / expected_rel
        if not config_path.is_file():
            fail(f"{role}: role config missing: {config_path.relative_to(ROOT)}", failures)
            continue
        try:
            layer = tomllib.loads(config_path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            fail(f"{role}: invalid TOML: {exc}", failures)
            continue
        if not str(layer.get("developer_instructions") or "").strip():
            fail(f"{role}: developer_instructions missing", failures)

    runtime_agents = manifest.get("agents") or []
    if manifest.get("runtime_agent_count") != len(runtime_agents):
        fail("runtime_agent_count mismatch", failures)
    if len(runtime_agents) < 112:
        fail("runtime registry below expected 112-agent baseline", failures)

    for agent in runtime_agents:
        if (agent.get("adapters") or {}).get("codex") is not True:
            fail(f"runtime agent is not Codex-enabled: {agent.get('name')}", failures)

    runtime_names = {a.get("name") for a in runtime_agents}
    for name in LANGUAGE_RUNTIME_NAMES:
        if name not in runtime_names:
            fail(f"missing multilingual runtime identity: {name}", failures)

    config_text = CONFIG.read_text(encoding="utf-8")
    bridge_text = BRIDGE.read_text(encoding="utf-8")
    router_text = ROUTER.read_text(encoding="utf-8")

    for needle in (
        "agent/thread limit",
        "close completed agent threads",
        "next wave",
        "not proof that Vinterro One agents are unavailable",
    ):
        if needle not in bridge_text:
            fail(f"bridge thread-recovery contract missing: {needle}", failures)

    if "A thread-limit condition is scheduling backpressure" not in config_text:
        fail("project Codex config missing thread-limit recovery instruction", failures)

    if "CODEX NATIVE SUBAGENT BRIDGE" not in config_text:
        fail("project Codex config missing native bridge contract", failures)

    if "Codex native bridge" not in router_text:
        fail("Vinterro One router missing native bridge routing section", failures)

    if failures:
        print("Vinterro One Codex native agent bridge: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("Vinterro One Codex native agent bridge: PASS")
    print(f"Runtime identities: {len(runtime_agents)}")
    print(f"Native role archetypes: {len(REQUIRED_ROLES)}")
    print(f"Concurrent spawned-thread ceiling: {limit}")
    print("Any runtime identity can route through an exact manifest contract.")
    print("Thread-limit recovery: bounded-wave scheduling enabled.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
