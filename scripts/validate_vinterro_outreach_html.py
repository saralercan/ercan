#!/usr/bin/env python3
"""Fail-closed, byte-for-byte renderer/validator for locked outreach HTML.

This is a QA primitive, NOT a mail sender. Actual Gmail first touch still
requires account-level history checks, atomic claim, and SENT reconciliation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Git blob hashes of the user-approved files at the 2026-10-08 lock.
# Changing a locked source requires explicit approval and a deliberate
# update of these hashes; do not silently update both in a template PR.
SOURCES = {
    "vinterro": (
        "docs/standards/VINTERRO_OUTREACH_CANONICAL_TEMPLATE.html",
        "716f9fa7b1e11fd292c9801162db551bb3f77113",
    ),
    "dragdrop": (
        "docs/standards/DRAGDROP_OUTREACH_CANONICAL_TEMPLATE.html",
        "32afb7c66698d749037e4ea08e37eb90de7042e9",
    ),
}

TEMPLATE_TOKEN = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")
EXPECTED_TOKENS = {
    "vinterro": {
        "BODY_HTML", "CTA_LABEL", "MAILTO_SUBJECT_ENCODED", "COMPLIANCE_TEXT"
    },
    "dragdrop": {
        "BODY_HTML", "B2C_CTA_LABEL", "B2B_CTA_LABEL", "COMPLIANCE_TEXT"
    },
}


class OutreachTemplateBlocked(ValueError):
    """Do not create or send the candidate outreach message."""


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(
        b"blob " + str(len(data)).encode("ascii") + b"\0" + data
    ).hexdigest()


def locked_source(kind: str, root: Path = ROOT) -> str:
    if kind not in SOURCES:
        raise OutreachTemplateBlocked("unsupported template kind")
    relative, expected_sha = SOURCES[kind]
    path = root / relative
    try:
        raw = path.read_bytes()
        source = raw.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise OutreachTemplateBlocked("approved template unavailable") from exc

    if git_blob_sha(raw) != expected_sha:
        raise OutreachTemplateBlocked("locked source changed: user approval required")
    if set(TEMPLATE_TOKEN.findall(source)) != EXPECTED_TOKENS[kind]:
        raise OutreachTemplateBlocked("locked template token contract changed")
    return source


def render_exact(kind: str, variables: dict[str, str], root: Path = ROOT) -> str:
    source = locked_source(kind, root)
    if not isinstance(variables, dict) or set(variables) != EXPECTED_TOKENS[kind]:
        raise OutreachTemplateBlocked("missing or unapproved substitution token")

    for token, value in variables.items():
        if not isinstance(value, str) or not value.strip():
            raise OutreachTemplateBlocked(f"empty or invalid value for {token}")
        if token != "BODY_HTML" and ("<" in value or ">" in value):
            raise OutreachTemplateBlocked(f"markup in visible text token: {token}")
        if token != "BODY_HTML" and ("\r" in value or "\n" in value):
            raise OutreachTemplateBlocked(f"newline in visible text token: {token}")

    if "MAILTO_SUBJECT_ENCODED" in variables and not re.fullmatch(
        r"[A-Za-z0-9._~%+-]+", variables["MAILTO_SUBJECT_ENCODED"]
    ):
        raise OutreachTemplateBlocked("mail-to subject must be URL encoded")

    # The only permitted changes to the HTML bytes are explicit token values.
    return TEMPLATE_TOKEN.sub(lambda m: variables[m.group(1)], source)


def verify_exact(
    kind: str, variables: dict[str, str], candidate: str, root: Path = ROOT
) -> None:
    expected = render_exact(kind, variables, root)
    if candidate != expected:
        mismatch = next(
            (i for i, (actual, wanted) in enumerate(zip(candidate, expected))
             if actual != wanted),
            min(len(candidate), len(expected)),
        )
        raise OutreachTemplateBlocked(
            f"outreach HTML drift at character {mismatch}; do not send"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kind", choices=sorted(SOURCES), required=True)
    parser.add_argument("--variables", type=Path, required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--render", type=Path)
    group.add_argument("--verify", type=Path)
    args = parser.parse_args()
    try:
        variables = json.loads(args.variables.read_text(encoding="utf-8"))
        if args.render is not None:
            result = render_exact(args.kind, variables)
            args.render.write_text(result, encoding="utf-8")
            print("PASS: locked outreach HTML rendered; no email was sent")
        else:
            candidate = args.verify.read_text(encoding="utf-8")
            verify_exact(args.kind, variables, candidate)
            print("PASS: byte-for-byte locked outreach geometry")
        return 0
    except (OutreachTemplateBlocked, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"BLOCKED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
