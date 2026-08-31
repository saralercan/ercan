#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "benchmarks/manifest.json"
DIST = ROOT / "benchmarks/.artifact-check"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(name: str) -> str:
    return re.sub(r"[-_.]+", "_", name).lower()


def main() -> int:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    inspect = next((s for s in data.get("suites", []) if s.get("id") == "inspect-runtime"), None)
    if not inspect:
        print("ERROR: inspect-runtime missing from benchmark manifest", file=sys.stderr)
        return 2

    pin = inspect.get("pin", {})
    expected = {
        ("inspect_ai", str(pin.get("inspect-ai", ""))): str(pin.get("inspect-ai-wheel-sha256", "")),
        ("inspect_evals", str(pin.get("inspect-evals", ""))): str(pin.get("inspect-evals-wheel-sha256", "")),
    }
    errors: list[str] = []

    wheels = list(DIST.glob("*.whl"))
    if not wheels:
        print(f"ERROR: no wheels found in {DIST}", file=sys.stderr)
        return 2

    matched: set[tuple[str, str]] = set()
    for wheel in wheels:
        filename = wheel.name
        parts = filename.split("-")
        if len(parts) < 2:
            continue
        package = norm(parts[0])
        version = parts[1]
        key = (package, version)
        if key not in expected:
            errors.append(f"unexpected wheel: {filename}")
            continue
        actual = sha256(wheel)
        wanted = expected[key]
        if not re.fullmatch(r"[0-9a-f]{64}", wanted):
            errors.append(f"{package}=={version}: missing/invalid reviewed SHA-256 in manifest")
        elif actual != wanted:
            errors.append(f"{package}=={version}: SHA-256 mismatch: expected {wanted}, got {actual}")
        else:
            print(f"PASS {package}=={version} sha256={actual}")
            matched.add(key)

    missing = sorted(set(expected) - matched)
    for package, version in missing:
        errors.append(f"missing verified wheel for {package}=={version}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Benchmark runtime artifact provenance PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
