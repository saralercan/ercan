#!/usr/bin/env python3
"""Deterministic, READ-ONLY planning router for ONE Vinterro Reklam Ajansı agent.

Does not run agents, invoke paid model endpoints, connect to ad accounts,
approve campaigns or claim successful work. The output is only a task plan.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json"


def _contains(text: str, phrase: str) -> bool:
    needle = re.escape(phrase.casefold().strip())
    return bool(re.search(r"(?<!\w)" + needle + r"(?!\w)", text.casefold()))


def route(task: str, *, max_skills: int | None = None) -> dict:
    manifest = json.loads(REGISTRY.read_text(encoding="utf-8"))
    global_contract = manifest["global_invocation"]
    global_invocation = bool(global_contract["enabled"] and any(
        _contains(task, phrase) for phrase in global_contract["phrases"]
    ))
    limit = int(manifest["orchestration"]["select_max"])
    if max_skills is not None:
        limit = min(limit, max(1, max_skills))
    matches = []
    for skill in manifest["skills"]:
        strong = [s for s in skill["signals"]["strong"] if _contains(task, s)]
        context = [s for s in skill["signals"]["context"] if _contains(task, s)]
        score = 6 * len(strong) + 2 * len(context)
        if score > 0:
            matches.append({"id": skill["id"], "label": skill["label"],
                            "path": skill["path"], "score": score,
                            "evidence": {"strong": strong, "context": context},
                            "_priority": skill["priority"],
                            "reviewer_candidates": skill["independent_reviewer_candidates"]})
    matches.sort(key=lambda x: (-x["score"], x["_priority"], x["id"]))
    if global_invocation:
        # The user's GLOBAL invocation specifically asks to include Reklam Ajansı
        # AND its entire nine-skill capability roster. Normal tasks stay capped.
        # Nonmatching skills are explicit SCOPE_CHECK_ONLY, not pretend execution.
        by_id = {item["id"]: item for item in matches}
        chosen = []
        for skill in sorted(manifest["skills"], key=lambda x: x["priority"]):
            item = by_id.get(skill["id"])
            if item is None:
                item = {
                    "id": skill["id"], "label": skill["label"],
                    "path": skill["path"], "score": 0,
                    "evidence": {"strong": [], "context": []},
                    "_priority": skill["priority"],
                    "reviewer_candidates": skill["independent_reviewer_candidates"],
                }
            item["participation"] = (
                "MATERIAL_WORKSTREAM" if item["score"] > 0 else "SCOPE_CHECK_ONLY"
            )
            chosen.append(item)
        deferred = []
    else:
        chosen = matches[:limit]
        for item in chosen:
            item["participation"] = "MATERIAL_WORKSTREAM"
        # Preserve every matching but unselected expertise as a visible gap.
        deferred = [{"id": x["id"], "score": x["score"]} for x in matches[limit:]]
    for item in chosen:
        item.pop("_priority", None)
    requested_mutation = any(_contains(task, term) for term in (
        "yayınla", "yayına al", "reklamları aç", "reklam başlat",
        "bütçeyi artır", "bütçe değiştir", "müşteri listesini yükle",
        "enable campaign", "publish", "spend", "launch campaign",
        "unpause", "resume ads", "faturalandırma değiştir"
    ))
    return {
        "canonical_agent": manifest["canonical_agent_name"],
        "agent_id": manifest["canonical_agent_id"],
        "task": task,
        "selected": chosen,
        "deferred_matches": deferred,
        "global_invocation": global_invocation,
        "global_inclusion_contract": (
            "ALL_NINE_IN_PLAN_ONE_CANONICAL_AGENT" if global_invocation
            else "TASK_QUALIFIED_MAX_THREE"
        ),
        "parent_agent_included": global_invocation,
        "fallback_parent_skill": "reklam-ajansi" if not chosen else None,
        "execution_state": "NOT_EXECUTED_PLANNING_ONLY",
        "real_parallel_workers_verified": False,
        "independent_qa_state": "REQUIRED_NOT_PERFORMED",
        "can_mutate_ad_accounts": False,
        "requested_live_mutation": requested_mutation,
        "mutation_gate": "BLOCKED_REQUIRES_HUMAN_APPROVAL_AND_VERIFIED_RUNTIME",
        "first_touch_email_gate": "BLOCKED",
        "reasons": ["Skill selection is not a model execution",
                    "Each source needs task-time verification",
                    "Human permission and real provider execution proof are separate"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only Reklam Ajansı subskill selection")
    parser.add_argument("task", help="Turkish or multilingual advertising task")
    parser.add_argument("--max-skills", type=int, default=None)
    args = parser.parse_args(argv)
    print(json.dumps(route(args.task, max_skills=args.max_skills), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
