#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import urllib.parse
import urllib.request

DATASETS = {
    "lite": "SWE-bench/SWE-bench_Lite",
    "verified": "SWE-bench/SWE-bench_Verified",
}
INSTANCE_RE = re.compile(r"^[A-Za-z0-9_.-]+__[A-Za-z0-9_.-]+$")
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
COMMIT_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch a sanitized SWE-bench case without gold/test patches")
    parser.add_argument("--dataset", choices=sorted(DATASETS), required=True)
    parser.add_argument("--instance-id", required=True)
    args = parser.parse_args()

    instance_id = args.instance_id.strip()
    if not INSTANCE_RE.fullmatch(instance_id):
        raise SystemExit("invalid SWE-bench instance_id")

    where = f'"instance_id"=\'{instance_id.replace(chr(39), chr(39) * 2)}\''
    params = urllib.parse.urlencode(
        {
            "dataset": DATASETS[args.dataset],
            "config": "default",
            "split": "test",
            "where": where,
            "offset": 0,
            "length": 2,
        }
    )
    url = f"https://datasets-server.huggingface.co/filter?{params}"
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Ercan-OS-Benchmark-Harness/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)

    rows = payload.get("rows")
    if not isinstance(rows, list) or len(rows) != 1:
        raise SystemExit(f"expected exactly one row for {instance_id}, got {0 if not isinstance(rows, list) else len(rows)}")
    row = rows[0].get("row") if isinstance(rows[0], dict) else None
    if not isinstance(row, dict):
        raise SystemExit("dataset API returned invalid row")

    repo = row.get("repo")
    base_commit = row.get("base_commit")
    problem_statement = row.get("problem_statement")
    if not isinstance(repo, str) or not REPO_RE.fullmatch(repo):
        raise SystemExit("invalid repo in dataset row")
    if not isinstance(base_commit, str) or not COMMIT_RE.fullmatch(base_commit):
        raise SystemExit("invalid base_commit in dataset row")
    if not isinstance(problem_statement, str) or not problem_statement.strip():
        raise SystemExit("missing problem_statement in dataset row")

    # Gold patch, test patch, hints and evaluator fields are intentionally omitted.
    sanitized = {
        "instance_id": instance_id,
        "repo": repo,
        "base_commit": base_commit,
        "problem_statement": problem_statement,
        "dataset": DATASETS[args.dataset],
    }
    print(json.dumps(sanitized, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
