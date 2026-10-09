#!/usr/bin/env python3
"""Build a bounded, auditable workflow PLAN for Vinterro One Reklam Ajansı.

No network, database, account access, model calls, paid execution, emails or
live campaign mutations. Outputs are proposed tasks with NOT_STARTED states,
not real run records or a claim of independent QA.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from route_reklam_ajansi_subskills import route

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json"

# Do not infer a user explicitly authorized live spend just because the task
# mentions a budget, conversion event, publish button, or campaign account.
SENSITIVE_DATA_TERMS = (
    "müşteri listesi", "müşteri e-post", "telefon listesi", "customer list",
    "email list", "lookalike audience", "custom audience", "müşteri verisi",
    "kişisel veri", "audience upload", "kitle yükle",
)

WRITE_ACTION_TERMS = (
    "aktif et", "aktifleştir", "yayına al", "yayınla", "başlat",
    "duraklat", "durdur", "devre dışı bırak", "sil", "silin",
    "bütçe değiştir", "bütçeyi değiştir", "bütçeyi artır",
    "bütçe artır", "harcama yap", "teklif değiştir", "teklifi yükselt",
    "hedeflemeyi değiştir", "hedef kitle yükle", "kitle yükle",
    "pixel kur", "etiket kur", "publish", "unpause", "pause",
    "enable campaign", "disable campaign", "launch campaign",
    "delete campaign", "update budget", "change bidding",
    "upload audience", "add payment method", "change targeting",
)

OUTPUTS_BY_SKILL = {
    "google-ads": ("campaign_and_keyword_plan", "search_negatives", "merchant_readiness"),
    "meta-ads": ("campaign_adset_plan", "purchase_pixel_capi_audit", "placement_brief"),
    "paid-social-video": ("channel_native_storyboard", "placement_checks", "test_hypotheses"),
    "creative-studio": ("creative_concepts", "channel_copy_variants", "creative_qa_checklist"),
    "analytics-attribution": ("event_flow_matrix", "reconciliation_gaps", "causal_claims_review"),
    "growth-budget": ("unit_economics", "budget_scenarios", "spend_change_risks"),
    "compliance-privacy": ("platform_policy_audit", "privacy_risk_register", "restricted_claims"),
    "global-market-research": ("original_language_source_matrix", "eligibility_gaps", "localization_risks"),
    "retail-marketplaces": ("catalog_feed_audit", "seller_eligibility", "product_ad_taxonomy"),
}


def _matches_any(task: str, terms: tuple[str, ...]) -> bool:
    # Using the existing router's token-boundary semantics avoids matching 'sil'
    # within unrelated terms such as 'silüet' or 'silindir'.
    from route_reklam_ajansi_subskills import _contains
    return any(_contains(task, term) for term in terms)


def plan(task: str) -> dict:
    if not isinstance(task, str) or not task.strip():
        raise ValueError("Task must be a nonempty instruction")

    chosen = route(task)
    manifest = json.loads(REGISTRY.read_text(encoding="utf-8"))
    ids = {s["id"] for s in manifest["skills"]}
    selected = chosen["selected"]
    if any(item["id"] not in ids for item in selected):
        raise ValueError("Unregistered skill selected")
    if len(selected) > 3 and not chosen["global_invocation"]:
        raise ValueError("More than three scopes: split the task")
    if chosen["global_invocation"] and len(selected) != 9:
        raise ValueError("Global Vinterro One dispatch must include all nine skills")

    requested_write = chosen["requested_live_mutation"] or _matches_any(task, WRITE_ACTION_TERMS)
    sensitive_data = _matches_any(task, SENSITIVE_DATA_TERMS)
    manual_review_required = bool(requested_write or sensitive_data)
    skill_stages = []

    for i, item in enumerate(selected):
        skill = next(s for s in manifest["skills"] if s["id"] == item["id"])
        skill_stages.append({
            "id": f"research-{i+1}-{item['id']}",
            "type": "skill_workstream",
            "owner": manifest["canonical_agent_name"],
            "skill_id": item["id"],
            "skill_file": skill["path"],
            "depends_on": ["intake"],
            "status": "NOT_STARTED",
            "participation": item["participation"],
            "scope_assessment_only": item["participation"] == "SCOPE_CHECK_ONLY",
            "can_be_parallelized_after_verified_worker_connection": True,
            "evidence_required": [
                "Cited, dated official or primary sources, refreshed for task market",
                "Actual client account/report evidence OR explicitly mark unavailable",
                "Assumptions, unknowns, contradictions and decision limits",
            ],
            "deliverable_keys": list(OUTPUTS_BY_SKILL[item["id"]]),
            "reviewer_candidates": skill["independent_reviewer_candidates"],
            "actual_model_receipt": None,
            "source_certification_claim": False,
        })

    if not skill_stages:
        skill_stages.append({
            "id": "parent-scoping",
            "type": "parent_intake",
            "owner": manifest["canonical_agent_name"],
            "skill_id": None,
            "depends_on": ["intake"],
            "status": "NOT_STARTED",
            "deliverable_keys": ["scope_and_account_requirements"],
            "actual_model_receipt": None,
        })

    assemble_deps = [s["id"] for s in skill_stages]
    stages = [
        {
            "id": "intake",
            "type": "scope_and_authority_check",
            "status": "NOT_STARTED",
            "depends_on": [],
            "fields_required": [
                "Client identity and task-specific delegated scope",
                "Country, language, currency, period and business objective",
                "Read-only account data provenance or explicit no-access flag",
                "Consent, catalog, inventory and policy constraints where relevant",
            ],
            "account_access_verified": False,
        },
        *skill_stages,
        {
            "id": "synthesis",
            "type": "evidence_merge",
            "status": "BLOCKED_PENDING_UPSTREAM",
            "depends_on": assemble_deps,
            "rules": [
                "One Reklam Ajansı report; no synthetic account metrics",
                "Keep conflicts/unknowns rather than overriding contradictory sources",
                "Observed Shopify orders, platform attribution and causal lift are distinct",
                "Mark unaddressed subskills as deferred, not silently completed",
            ],
            "output_contract": {
                "observation": None,
                "primary_sources": [],
                "assumptions": [],
                "unresolved_blockers": [],
                "proposed_experiments": [],
                "proposed_account_mutations": [],
                "source_execution_receipt_ids": [],
            },
        },
        {
            "id": "independent-qa",
            "type": "independent_external_review",
            "status": "NOT_PERFORMED",
            "depends_on": ["synthesis"],
            "reviewer_must_differ_from_producer": True,
            "reviewer_candidates": sorted({
                candidate for item in selected
                for candidate in item["reviewer_candidates"]
            } | {"QA Agent"}),
            "requirements": [
                "Access actual cited primary sources and task artifacts",
                "Review measurement, creative, policy, budget and provenance risks",
                "Escalate reviewer disagreement to independent arbitration",
                "An offline structural check is never a real model examination",
            ],
            "verdict": "PENDING",
            "review_receipt": None,
        },
    ]
    if manual_review_required:
        stages.append({
            "id": "human-approval",
            "type": "explicit_scope_bound_approval",
            "status": "NOT_REQUESTED",
            "depends_on": ["independent-qa"],
            "required_for": [
                x for x, is_on in (
                    ("LIVE_AD_ACCOUNT_MUTATION", requested_write),
                    ("CUSTOMER_DATA_PROCESSING_OR_UPLOAD", sensitive_data),
                ) if is_on
            ],
            "authorization": None,
            "notes": "A user request alone does not prove technical access, legal basis, or final release approval",
        })

    # The contract ends at a proposal. There is deliberately NO action to
    # submit a live advertising change, email, billing change or fake receipt.
    return {
        "schema_version": "1.0.0",
        "canonical_agent": manifest["canonical_agent_name"],
        "canonical_agent_id": manifest["canonical_agent_id"],
        "task": task,
        "mode": "PLAN_ONLY_NO_REMOTE_EFFECTS",
        "global_invocation": chosen["global_invocation"],
        "global_inclusion_contract": chosen["global_inclusion_contract"],
        "parent_agent_included": chosen["parent_agent_included"],
        "workstreams": len(skill_stages),
        "scope_check_only_skills": [
            item["id"] for item in selected
            if item["participation"] == "SCOPE_CHECK_ONLY"
        ],
        "material_skill_ids": [
            item["id"] for item in selected
            if item["participation"] == "MATERIAL_WORKSTREAM"
        ],
        "selected_skill_ids": [s["id"] for s in selected],
        "deferred_skill_ids": [s["id"] for s in chosen.get("deferred_matches", [])],
        "scope_split_recommended": bool(chosen.get("deferred_matches")),
        "parallel_model_work_executed": False,
        "campaign_data_read_from_accounts": False,
        "provider_receipt_verified": False,
        "requested_live_mutation": requested_write,
        "sensitive_customer_data_requested": sensitive_data,
        "human_approval_required": manual_review_required,
        "independent_qa_done": False,
        "gates": {
            "ads_account_write": "BLOCKED",
            "model_worker": "NOT_VERIFIED",
            "first_touch_email": "BLOCKED",
            "production_release": "BLOCKED",
        },
        "stages": stages,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare a read-only Reklam Ajansı evidence workflow")
    parser.add_argument("task")
    args = parser.parse_args(argv)
    try:
        result = plan(args.task)
    except ValueError as exc:
        parser.error(str(exc))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
