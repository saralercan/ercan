#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPECTED_SCHEMA = 2
COUNT_FIELDS = (
    "total_instances",
    "submitted_instances",
    "completed_instances",
    "resolved_instances",
    "unresolved_instances",
    "empty_patch_instances",
    "error_instances",
)
LIST_FIELDS = (
    "completed_ids",
    "incomplete_ids",
    "empty_patch_ids",
    "submitted_ids",
    "resolved_ids",
    "unresolved_ids",
    "error_ids",
)


def require_int(report: dict, key: str) -> int:
    value = report.get(key)
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{key} must be a non-negative integer")
    return value


def require_list(report: dict, key: str) -> list[str]:
    value = report.get(key)
    if not isinstance(value, list) or any(not isinstance(item, str) or not item for item in value):
        raise ValueError(f"{key} must be a list of non-empty strings")
    if len(value) != len(set(value)):
        raise ValueError(f"{key} contains duplicates")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize a canonical SWE-bench schema-v2 run report")
    parser.add_argument("report", type=Path)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--agent-harness-id", required=True)
    parser.add_argument("--ercan-os-commit", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    raw = args.report.read_bytes()
    report = json.loads(raw)
    if not isinstance(report, dict):
        raise SystemExit("report root must be a JSON object")
    if report.get("schema_version") != EXPECTED_SCHEMA:
        raise SystemExit(f"unsupported SWE-bench report schema: {report.get('schema_version')!r}")

    try:
        counts = {key: require_int(report, key) for key in COUNT_FIELDS}
        ids = {key: require_list(report, key) for key in LIST_FIELDS}
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc

    expected_lengths = {
        "completed_ids": counts["completed_instances"],
        "submitted_ids": counts["submitted_instances"],
        "resolved_ids": counts["resolved_instances"],
        "unresolved_ids": counts["unresolved_instances"],
        "empty_patch_ids": counts["empty_patch_instances"],
        "error_ids": counts["error_instances"],
    }
    for key, expected in expected_lengths.items():
        if len(ids[key]) != expected:
            raise SystemExit(f"{key} length {len(ids[key])} != declared count {expected}")

    submitted = set(ids["submitted_ids"])
    completed = set(ids["completed_ids"])
    resolved = set(ids["resolved_ids"])
    unresolved = set(ids["unresolved_ids"])
    empty = set(ids["empty_patch_ids"])
    errors = set(ids["error_ids"])

    if not resolved.issubset(completed) or not unresolved.issubset(completed):
        raise SystemExit("resolved/unresolved IDs must be completed IDs")
    if resolved & unresolved:
        raise SystemExit("resolved_ids and unresolved_ids overlap")
    if not completed.issubset(submitted):
        raise SystemExit("completed_ids must be submitted_ids")
    if not empty.issubset(submitted) or not errors.issubset(submitted):
        raise SystemExit("empty/error IDs must be submitted_ids")
    if counts["resolved_instances"] + counts["unresolved_instances"] > counts["completed_instances"]:
        raise SystemExit("resolved + unresolved exceeds completed")
    if counts["submitted_instances"] > counts["total_instances"]:
        raise SystemExit("submitted_instances exceeds total_instances")

    if counts["submitted_instances"] == 0:
        evidence_state = "NO_BEHAVIORAL_RESULT"
    elif counts["error_instances"] > 0 or counts["empty_patch_instances"] > 0:
        evidence_state = "EVIDENCE_REVIEW_REQUIRED"
    elif counts["completed_instances"] == 0:
        evidence_state = "NO_BEHAVIORAL_RESULT"
    else:
        evidence_state = "VALID_BEHAVIORAL_EVIDENCE"

    resolution_rate_submitted = (
        counts["resolved_instances"] / counts["submitted_instances"]
        if counts["submitted_instances"]
        else None
    )
    resolution_rate_completed = (
        counts["resolved_instances"] / counts["completed_instances"]
        if counts["completed_instances"]
        else None
    )

    normalized = {
        "schema_version": 1,
        "source": "swe-bench",
        "source_report_schema": EXPECTED_SCHEMA,
        "dataset": args.dataset,
        "run_id": args.run_id,
        "agent_harness_id": args.agent_harness_id,
        "ercan_os_commit": args.ercan_os_commit,
        "source_report_sha256": hashlib.sha256(raw).hexdigest(),
        "evidence_state": evidence_state,
        "promotion_decision": "NO_AUTOMATIC_PROMOTION",
        "recertification_decision": "REVIEW_REQUIRED" if evidence_state == "EVIDENCE_REVIEW_REQUIRED" else "NO_AUTOMATIC_DEMOTION",
        "counts": counts,
        "resolution_rate_submitted": resolution_rate_submitted,
        "resolution_rate_completed": resolution_rate_completed,
        "ids": ids,
        "interpretation": {
            "smoke_subset_is_not_full_benchmark": counts["submitted_instances"] < counts["total_instances"],
            "unresolved_is_behavioral_failure_for_instance_not_global_hard_fail": True,
            "error_requires_attribution_review": counts["error_instances"] > 0,
            "empty_patch_requires_review": counts["empty_patch_instances"] > 0,
        },
    }

    text = json.dumps(normalized, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
