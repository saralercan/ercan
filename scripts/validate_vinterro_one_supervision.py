#!/usr/bin/env python3
"""Structural validator for the Vinterro One Agent Supervision Mesh."""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

MANIFEST = ROOT / "docs/standards/VINTERRO_ONE_SUPERVISION_MANIFEST.json"
STANDARD = ROOT / "docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md"
SKILL = ROOT / ".agents/skills/vinterro-one-agent-supervision/SKILL.md"
REGRESSION = ROOT / "docs/evals/VINTERRO_ONE_AGENT_SUPERVISION_REGRESSION.md"
ROOT_AGENTS = ROOT / "AGENTS.md"

REQUIRED_TIERS = {"R0", "R1", "R2", "R3", "R4"}
REQUIRED_TERMINAL = {"VERIFIED", "PARTIAL", "BLOCKED", "NOT_VERIFIED"}
REQUIRED_DOMAINS = {
    "web_ui",
    "commerce",
    "mail_outreach",
    "security",
    "seo_aeo_geo",
    "brand_creative",
    "social",
    "meta_measurement",
    "mobile",
    "performance",
    "agent_runtime",
    "research_upstream",
    "deployment_release",
    "finance_operations",
    "general",
}
REQUIRED_TRIGGERS = {
    "tool_error",
    "test_failure",
    "unsupported_completion_claim",
    "user_reports_issue_persists",
    "agent_disagreement",
    "production_regression",
    "post_review_material_change",
}


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    raise SystemExit(1)


def require_file(path: Path) -> str:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def main() -> int:
    standard = require_file(STANDARD)
    skill = require_file(SKILL)
    regression = require_file(REGRESSION)
    root_agents = require_file(ROOT_AGENTS)
    raw = require_file(MANIFEST)

    try:
        manifest = json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(f"manifest JSON invalid: {exc}")

    if manifest.get("system_name") != "Vinterro One":
        fail("canonical system_name must be Vinterro One")

    inv = manifest.get("invariants", {})
    required_invariants = {
        "producer_cannot_final_verify_own_material_work",
        "completion_claim_is_not_verification",
        "deterministic_evidence_outranks_semantic_vote",
        "material_change_invalidates_stale_pass",
        "critical_blocker_cannot_be_overridden_by_quorum",
        "project_human_approval_rules_remain_authoritative",
    }
    for key in required_invariants:
        if inv.get(key) is not True:
            fail(f"required invariant not enabled: {key}")

    tiers = set(manifest.get("risk_tiers", {}))
    if tiers != REQUIRED_TIERS:
        fail(f"risk tiers must be exactly {sorted(REQUIRED_TIERS)}; got {sorted(tiers)}")

    terminal = set(manifest.get("terminal_states", []))
    if terminal != REQUIRED_TERMINAL:
        fail(f"terminal states must be exactly {sorted(REQUIRED_TERMINAL)}; got {sorted(terminal)}")

    domains = set(manifest.get("domain_supervisors", {}))
    missing_domains = REQUIRED_DOMAINS - domains
    if missing_domains:
        fail(f"missing domain supervisors: {sorted(missing_domains)}")

    if not manifest["domain_supervisors"].get("general"):
        fail("general fallback supervisor must be non-empty")

    triggers = set(manifest.get("watchdog_triggers", []))
    missing_triggers = REQUIRED_TRIGGERS - triggers
    if missing_triggers:
        fail(f"missing watchdog triggers: {sorted(missing_triggers)}")

    inventory = manifest.get("inventory", {})
    if inventory.get("hardcode_count_for_enforcement") is not False:
        fail("supervision enforcement must use dynamic inventory, not a hardcoded count")
    if "general_supervisor" not in inventory.get("unknown_agent_policy", ""):
        fail("unknown-agent policy must route to general supervisor")

    retry = manifest.get("retry_policy", {})
    if retry.get("allow_third_attempt_with_identical_hypothesis") is not False:
        fail("third identical failed hypothesis must be forbidden")
    if retry.get("repeated_failure_requires_alternate_owner_or_architecture_review") is not True:
        fail("repeated failure escalation missing")

    expected_paths = {
        "canonical_standard": "docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md",
        "skill": ".agents/skills/vinterro-one-agent-supervision/SKILL.md",
        "regression_suite": "docs/evals/VINTERRO_ONE_AGENT_SUPERVISION_REGRESSION.md",
        "validator": "scripts/validate_vinterro_one_supervision.py",
    }
    for key, value in expected_paths.items():
        if manifest.get(key) != value:
            fail(f"manifest {key} mismatch")

    text_checks = [
        (standard, "producer != final verifier", "standard self-verification invariant"),
        (standard, "@MetaAuditor", "meta auditor"),
        (standard, "@Arbiter", "arbiter"),
        (standard, "@ReleaseGate", "release gate"),
        (skill, "material producer cannot be the final verifier", "skill separation rule"),
        (regression, "SUP-001", "core regression case"),
        (root_agents, "Vinterro One supervision hard gate", "root hard gate"),
    ]
    for haystack, needle, label in text_checks:
        if needle.lower() not in haystack.lower():
            fail(f"missing {label}: {needle}")

    print("PASS: Vinterro One Agent Supervision Mesh structural contract is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
