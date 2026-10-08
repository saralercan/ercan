#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    ".agents/skills/sales-intelligence-discovery/SKILL.md",
    ".agents/skills/website-opportunity-audit/SKILL.md",
    ".agents/skills/sales-lead-qualification/SKILL.md",
    ".agents/skills/sales-intelligence-handoff/SKILL.md",
    "plugins/vinterro-one/skills/sales-intelligence-discovery/SKILL.md",
    "plugins/vinterro-one/skills/website-opportunity-audit/SKILL.md",
    "plugins/vinterro-one/skills/sales-lead-qualification/SKILL.md",
    "plugins/vinterro-one/skills/sales-intelligence-handoff/SKILL.md",
    "docs/standards/VINTERRO_SALES_INTELLIGENCE_AGENT.md",
    "docs/evals/VINTERRO_SALES_INTELLIGENCE_REGRESSION.md",
    ".codex/agents/sales-intelligence.toml",
    ".claude/agents/sales-intelligence.md",
]
missing = [p for p in required if not (ROOT / p).exists()]
assert not missing, f"missing Sales Intelligence files: {missing}"

manifest = json.loads((ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json").read_text())
assert manifest["runtime_agent_count"] >= 116
agents = {a["name"]: a for a in manifest["agents"]}
assert "Sales Intelligence Agent" in agents
agent = agents["Sales Intelligence Agent"]
assert agent["role"] == "sales_intelligence"
assert agent["permissions"]["production_send"] is False
assert agent["permissions"]["website_checks"] == "passive_normal_user_only"
assert agent["permissions"]["account_level_dedupe_required"] is True
assert "Vinterro Digital Outreach Ajanı" in agent["handoffs"]
assert "Vinterro Digital Mail Ajanı" in agent["handoffs"]

matrix = json.loads((ROOT / "docs/standards/AGENT_EXPERTISE_SOURCE_MATRIX.json").read_text())
assert matrix["agent_count"] >= 116
profiles = {p["name"]: p for p in matrix["profiles"]}
assert "Sales Intelligence Agent" in profiles
assert "Vinterro Digital Outreach Ajanı" in profiles
assert "Vinterro Digital Mail Ajanı" in profiles

plugin_manifest = json.loads((ROOT / "plugins/vinterro-one/skills/vinterro-one-router/references/VINTERRO_RUNTIME_AGENT_MANIFEST.json").read_text())
assert plugin_manifest["runtime_agent_count"] == manifest["runtime_agent_count"]
assert {a["name"] for a in plugin_manifest["agents"]} == set(agents)

root_agents = (ROOT / "AGENTS.md").read_text()
assert "## Sales Intelligence hard route" in root_agents
assert "VINTERRO_SALES_INTELLIGENCE_AGENT.md" in root_agents

codex = (ROOT / ".codex/config.toml").read_text()
assert "[agents.sales_intelligence]" in codex
assert 'config_file = "agents/sales-intelligence.toml"' in codex

claude = (ROOT / "CLAUDE.md").read_text()
assert ".claude/agents/sales-intelligence.md" in claude

print("Sales Intelligence Agent contract: PASS")
