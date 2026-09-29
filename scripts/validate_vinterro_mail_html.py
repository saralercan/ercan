#!/usr/bin/env python3
"""Validate rendered Vinterro Digital mail HTML against the locked canonical contract."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

REQUIRED = [
    ('container width', 'width="770"'),
    ('container max width', 'max-width:770px'),
    ('outer padding', 'padding:32px 18px'),
    ('body font', 'font-family:Arial,Helvetica,sans-serif'),
    ('body size', 'font-size:16px'),
    ('body line-height', 'line-height:1.72'),
    ('body color', 'color:#191919'),
    ('left alignment', 'text-align:left'),
    ('divider height', 'height:1px'),
    ('divider red', 'background:#e31b23'),
    ('divider spacing', 'margin:0 0 18px 0'),
    ('signature brand', '>Vinterro Digital</div>'),
    ('signature tagline size', 'font-size:12px;line-height:1.5;letter-spacing:1.4px'),
    ('signature contact size', 'font-size:14px;line-height:1.55'),
    ('signature services size', 'font-size:13px;line-height:1.55;color:#9a9a9a'),
    ('mailto link', 'href="mailto:info@vinterro.digital"'),
    ('site link', 'href="https://vinterro.digital/"'),
    ('service line', 'Strategy &amp; Brand · Digital Products &amp; Web · Commerce · Growth · Automation'),
]

FORBIDDEN = [
    ('760px near-match', 'max-width:760px'),
    ('780px near-match', 'max-width:780px'),
    ('centered body', 'text-align:center'),
    ('old 15px signature brand token', 'font-size:15px'),
    ('old 11px tagline token', 'font-size:11px'),
]


def validate(html: str) -> list[str]:
    errors: list[str] = []
    for label, token in REQUIRED:
        if token not in html:
            errors.append(f"missing {label}: {token}")
    for label, token in FORBIDDEN:
        if token in html:
            errors.append(f"forbidden {label}: {token}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Rendered HTML file to validate")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.is_file():
        print(f"BLOCKED: file not found: {path}", file=sys.stderr)
        return 2

    html = path.read_text(encoding="utf-8")
    errors = validate(html)
    if errors:
        print("BLOCKED: Vinterro canonical mail validation failed", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("VERIFIED: Vinterro canonical mail HTML tokens match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
