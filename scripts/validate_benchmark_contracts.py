#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "benchmarks/manifest.json"
STABLE = ROOT / "docs/standards/STABLE_AGENT_CORE.md"
DISPATCH = ROOT / ".github/workflows/behavioral-benchmark-dispatch.yml"
SWEBENCH_DISPATCH = ROOT / ".github/workflows/swebench-modal-dispatch.yml"
CODEX_PREDICTIONS = ROOT / ".github/workflows/codex-swebench-predictions.yml"
COMPUTE_POLICY = ROOT / "docs/evals/BENCHMARK_COMPUTE_POLICY.md"
PREDICTIONS_VALIDATOR = ROOT / "scripts/validate_swebench_predictions.py"
CASE_FETCHER = ROOT / "scripts/fetch_swebench_case.py"
REQUIRED = {
    "bfcl-v4",
    "inspect-bfcl-v1-v3-baseline",
    "swe-bench-verified",
    "codex-swebench-prediction-harness",
    "swe-bench-multimodal",
    "inspect-runtime",
    "mcp-2026-07-28",
    "security-normative",
}
ALLOWED_STATUS = {
    "NOT_RUN",
    "ADOPT_WHEN_NEEDED",
    "SCENARIOS_DEFINED",
    "RUN_FAILED",
    "BEHAVIORAL_BASELINE",
    "PRODUCTION_VERIFIED",
    "BENCHMARKED_FRONTIER_CANDIDATE",
    "STALE_COMPARISON",
}
CODEX_ACTION_COMMIT = "86365089eb2b84e0a8fb0717b304f8bdcb13b20e"
CODEX_VERSION = "0.151.0"


def stable_agents() -> set[str]:
    text = STABLE.read_text(encoding="utf-8")
    return set(re.findall(r"`(@[^`]+)`", text))


def fail(errors: list[str]) -> int:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1


def must_contain(text: str, fragments: dict[str, str], prefix: str, errors: list[str]) -> None:
    for label, fragment in fragments.items():
        if fragment not in text:
            errors.append(f"{prefix} missing {label}")


def validate_dispatch(errors: list[str]) -> None:
    if not DISPATCH.exists():
        errors.append("behavioral benchmark dispatch workflow missing")
        return
    text = DISPATCH.read_text(encoding="utf-8")
    must_contain(
        text,
        {
            "manual-only trigger": "workflow_dispatch:",
            "explicit RUN approval": "inputs.confirmation == 'RUN'",
            "OpenAI secret boundary": "secrets.OPENAI_API_KEY",
            "top-level wheel provenance": "verify_benchmark_artifacts.py",
            "Inspect BFCL internal baseline": "inspect eval inspect_evals/bfcl",
            "sensitive trace suppression": "OPENAI_AGENTS_TRACE_INCLUDE_SENSITIVE_DATA",
            "reproducibility evidence": "behavioral-run-metadata.json",
        },
        "behavioral dispatch",
        errors,
    )
    if re.search(r"(?m)^\s*schedule\s*:", text):
        errors.append("behavioral benchmark dispatch must not be scheduled automatically")
    if "bfcl-v4" in text.lower() or "bfcl_v4" in text.lower():
        errors.append("behavioral Inspect dispatch must not expose BFCL V4; use official Berkeley harness separately")


def validate_codex_predictions(errors: list[str]) -> None:
    if not CASE_FETCHER.exists():
        errors.append("gold-safe SWE-bench case fetcher missing")
    if not CODEX_PREDICTIONS.exists():
        errors.append("Codex SWE-bench prediction workflow missing")
        return
    text = CODEX_PREDICTIONS.read_text(encoding="utf-8")
    must_contain(
        text,
        {
            "manual trigger": "workflow_dispatch:",
            "RUN authorization": "confirm must equal RUN",
            "master-only generation": "refs/heads/master",
            "maximum three instances": "1..3 items",
            "OpenAI secret through action": "openai-api-key: ${{ secrets.OPENAI_API_KEY }}",
            "pinned official Codex action": f"openai/codex-action@{CODEX_ACTION_COMMIT}",
            "pinned Codex CLI": f'codex-version: "{CODEX_VERSION}"',
            "workspace permission profile": 'permission-profile: ":workspace"',
            "drop-sudo safety": 'safety-strategy: "drop-sudo"',
            "ephemeral session": '"--ephemeral"',
            "user config isolation": '"--ignore-user-config"',
            "repo rule isolation": '"--ignore-rules"',
            "project docs disabled": '"project_doc_max_bytes=0"',
            "sanitized case fetch": "fetch_swebench_case.py",
            "gold field leak check": "gold/evaluator fields leaked",
            "prediction validation": "validate_swebench_predictions.py",
            "separate unscored state": "PREDICTIONS_GENERATED_NOT_SCORED",
            "immutable artifacts": "actions/upload-artifact@v7",
        },
        "Codex prediction workflow",
        errors,
    )
    if re.search(r"(?m)^\s*schedule\s*:", text):
        errors.append("Codex prediction generation must not be scheduled automatically")
    if "--modal" in text or "swebench eval" in text:
        errors.append("prediction generation and SWE-bench scoring must remain separate workflows")


def validate_swebench_dispatch(errors: list[str]) -> None:
    if not COMPUTE_POLICY.exists():
        errors.append("benchmark compute policy missing")
    if not PREDICTIONS_VALIDATOR.exists():
        errors.append("SWE-bench predictions validator missing")
    if not SWEBENCH_DISPATCH.exists():
        errors.append("SWE-bench Modal dispatch workflow missing")
        return
    text = SWEBENCH_DISPATCH.read_text(encoding="utf-8")
    must_contain(
        text,
        {
            "manual-only trigger": "workflow_dispatch:",
            "explicit RUN confirmation": "inputs.confirm",
            "master-only paid execution": "refs/heads/master",
            "Modal token ID boundary": "secrets.MODAL_TOKEN_ID",
            "Modal token secret boundary": "secrets.MODAL_TOKEN_SECRET",
            "artifact source selector": "predictions_source",
            "generator provenance check": "Ercan OS Codex SWE-bench Predictions",
            "successful generator requirement": '"conclusion": "success"',
            "artifact download": "actions/download-artifact@v8",
            "actions read permission": "actions: read",
            "predictions path confinement": "benchmarks/predictions",
            "predictions validator": "validate_swebench_predictions.py",
            "official SWE-bench CLI": "swebench eval",
            "Modal cloud flag": "--modal",
            "unique run ID input": "inputs.run_id",
            "wheel hash gate": "SWE_BENCH_WHEEL_SHA256",
            "evidence hashes": "SHA256SUMS.txt",
            "artifact retention": "actions/upload-artifact@v7",
        },
        "SWE-bench dispatch",
        errors,
    )
    if re.search(r"(?m)^\s*schedule\s*:", text):
        errors.append("SWE-bench paid cloud dispatch must not be scheduled automatically")
    if "pull_request:" in text or re.search(r"(?m)^\s*push\s*:", text):
        errors.append("SWE-bench paid cloud dispatch must be workflow_dispatch only")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-freshness", action="store_true")
    args = parser.parse_args()

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []

    if data.get("schema_version") != 1:
        errors.append("manifest schema_version must be 1")
    suites = data.get("suites")
    if not isinstance(suites, list):
        return fail(["manifest suites must be a list"])

    agents = stable_agents()
    ids: set[str] = set()
    today = date.today()

    for suite in suites:
        sid = suite.get("id")
        if not sid or not isinstance(sid, str):
            errors.append("suite missing string id")
            continue
        if sid in ids:
            errors.append(f"duplicate suite id: {sid}")
        ids.add(sid)

        source = suite.get("canonical_source")
        if not isinstance(source, str) or not source.startswith("https://"):
            errors.append(f"{sid}: canonical_source must be https URL")
        pin = suite.get("pin")
        if not isinstance(pin, dict) or not pin:
            errors.append(f"{sid}: non-empty pin object required")
        if suite.get("status") not in ALLOWED_STATUS:
            errors.append(f"{sid}: invalid status {suite.get('status')!r}")

        targets = suite.get("targets")
        if not isinstance(targets, list) or not targets:
            errors.append(f"{sid}: targets must be non-empty")
        else:
            unknown = sorted(set(targets) - agents)
            if unknown:
                errors.append(f"{sid}: unknown stable-agent targets: {', '.join(unknown)}")

        try:
            checked = date.fromisoformat(suite["checked_at"])
            freshness = int(suite["freshness_days"])
            if freshness < 1 or freshness > 90:
                errors.append(f"{sid}: freshness_days must be 1..90")
            stale_on = checked + timedelta(days=freshness)
            if today > stale_on:
                msg = f"{sid}: source pin stale since {stale_on.isoformat()} (checked {checked.isoformat()})"
                if args.strict_freshness:
                    errors.append(msg)
                else:
                    warnings.append(msg)
        except (KeyError, TypeError, ValueError):
            errors.append(f"{sid}: invalid checked_at/freshness_days")

    missing = sorted(REQUIRED - ids)
    if missing:
        errors.append(f"missing required suites: {', '.join(missing)}")

    inspect = next((s for s in suites if s.get("id") == "inspect-runtime"), {})
    ipin = inspect.get("pin", {})
    if ipin.get("inspect-ai") != "0.3.261":
        warnings.append("inspect-ai pin differs from 2026-08-31 reviewed baseline 0.3.261")
    if ipin.get("inspect-evals") != "0.18.0":
        warnings.append("inspect-evals pin differs from 2026-08-31 reviewed baseline 0.18.0")

    swe = next((s for s in suites if s.get("id") == "swe-bench-verified"), {})
    spin = swe.get("pin", {})
    if spin.get("swebench-package") != "5.0.2":
        errors.append("swe-bench-verified must pin reviewed swebench package 5.0.2")
    if spin.get("swebench-wheel-sha256") != "b7f0416a1e686eca22c2f749b5f816685a202835032f6683080e2b53545bbb62":
        errors.append("swe-bench-verified wheel hash differs from reviewed 5.0.2 artifact")
    cloud = spin.get("cloud", [])
    if not isinstance(cloud, list) or "modal" not in cloud:
        errors.append("swe-bench-verified must record official Modal cloud evaluation path")

    codex = next((s for s in suites if s.get("id") == "codex-swebench-prediction-harness"), {})
    cpin = codex.get("pin", {})
    if cpin.get("codex-action-commit") != CODEX_ACTION_COMMIT:
        errors.append("Codex prediction harness action commit differs from reviewed v1 commit")
    if cpin.get("codex-cli") != CODEX_VERSION:
        errors.append("Codex prediction harness CLI differs from reviewed 0.151.0")
    if cpin.get("gold_patch_exposure") != "prohibited":
        errors.append("Codex prediction harness must prohibit gold patch exposure")
    if cpin.get("max_instances_per_generation_run") != 3:
        errors.append("Codex prediction harness must remain capped at three instances per generation run")

    validate_dispatch(errors)
    validate_codex_predictions(errors)
    validate_swebench_dispatch(errors)

    for path in (PREDICTIONS_VALIDATOR, CASE_FETCHER):
        if path.exists():
            try:
                compile(path.read_text(encoding="utf-8"), str(path), "exec")
            except SyntaxError as exc:
                errors.append(f"Python syntax error in {path.name}: {exc}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        return fail(errors)

    print(
        f"Benchmark contracts PASS: {len(suites)} suites; {len(agents)} stable agents known; "
        f"strict_freshness={args.strict_freshness}; behavioral_dispatch=manual-only; "
        "prediction_generation=manual-only; swebench_cloud=manual-only"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
