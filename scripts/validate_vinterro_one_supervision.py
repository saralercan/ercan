#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / "docs/standards/VINTERRO_ONE_SUPERVISION_MANIFEST.json"
standard_path = ROOT / "docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md"
skill_path = ROOT / ".agents/skills/vinterro-one-agent-supervision/SKILL.md"
regression_path = ROOT / "docs/evals/VINTERRO_ONE_SUPERVISION_REGRESSION.md"

required_files = [manifest_path, standard_path, skill_path, regression_path]
missing = [str(p.relative_to(ROOT)) for p in required_files if not p.exists()]
if missing:
    raise SystemExit("Missing supervision files: " + ", ".join(missing))

m = json.loads(manifest_path.read_text(encoding="utf-8"))
assert m["product_name"] == "Vinterro One"
assert m["status"] == "active"

inv = m["invariants"]
required_invariants = [
    "material_creator_cannot_self_certify",
    "completion_claim_is_not_evidence",
    "independent_review_required_for_material_work",
    "disagreement_uses_arbiter_not_majority_vote",
    "stale_pass_invalid_after_material_change",
    "critical_external_effect_requires_release_gate",
    "reviewer_and_supervisor_are_auditable",
    "repeated_failure_requires_root_cause_escalation",
    "missing_evidence_cannot_be_reported_as_verified",
]
for key in required_invariants:
    assert inv.get(key) is True, f"invariant must be true: {key}"

for level in ("R1", "R2", "R3", "R4"):
    assert level in m["risk_classes"]

assert "independent_reviewer" in m["risk_classes"]["R1"]["minimum"]
assert "release_gate" in m["risk_classes"]["R3"]["minimum"]
assert "meta_auditor" in m["risk_classes"]["R4"]["minimum"]

states = set(m["verdicts"]["completion"])
assert states == {"VERIFIED", "PARTIAL", "BLOCKED", "NOT_VERIFIED"}

assert "@AgentRuntimeSupervisor" in m["domain_supervisor_capabilities"]
assert "false_pass_rate" in m["reliability_signals"]

print("Vinterro One supervision manifest: PASS")
