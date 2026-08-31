#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

REQUIRED = ("instance_id", "model_name_or_path", "model_patch")
MAX_BYTES = 50 * 1024 * 1024


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate SWE-bench predictions JSONL before external evaluation")
    parser.add_argument("path", type=Path)
    parser.add_argument("--max-instances", type=int, default=500)
    args = parser.parse_args()

    path = args.path.resolve()
    if not path.is_file():
        raise SystemExit(f"predictions file not found: {path}")
    size = path.stat().st_size
    if size <= 0 or size > MAX_BYTES:
        raise SystemExit(f"invalid predictions file size: {size} bytes")

    seen: set[str] = set()
    count = 0
    with path.open("r", encoding="utf-8") as handle:
        for line_no, raw in enumerate(handle, 1):
            if not raw.strip():
                continue
            try:
                row = json.loads(raw)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"line {line_no}: invalid JSON: {exc}") from exc
            if not isinstance(row, dict):
                raise SystemExit(f"line {line_no}: expected JSON object")
            missing = [key for key in REQUIRED if key not in row]
            if missing:
                raise SystemExit(f"line {line_no}: missing fields: {', '.join(missing)}")
            instance_id = row["instance_id"]
            model_name = row["model_name_or_path"]
            patch = row["model_patch"]
            if not isinstance(instance_id, str) or not instance_id.strip():
                raise SystemExit(f"line {line_no}: invalid instance_id")
            if instance_id in seen:
                raise SystemExit(f"line {line_no}: duplicate instance_id: {instance_id}")
            if not isinstance(model_name, str) or not model_name.strip():
                raise SystemExit(f"line {line_no}: invalid model_name_or_path")
            if not isinstance(patch, str):
                raise SystemExit(f"line {line_no}: model_patch must be a string")
            seen.add(instance_id)
            count += 1
            if count > args.max_instances:
                raise SystemExit(f"too many instances: {count} > {args.max_instances}")

    if count == 0:
        raise SystemExit("predictions file contains no instances")

    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(json.dumps({"instances": count, "bytes": size, "sha256": digest}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
