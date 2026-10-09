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
from html.parser import HTMLParser
from urllib.parse import unquote_to_bytes, urlsplit

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


class _AllowedBodyParser(HTMLParser):
    """Only inline, structurally safe copy inside the immutable 680px shell.

    This accepts the approved Gmail reference's paragraph-margin style and
    simple emphasis/links, not arbitrary tables, wrappers, CSS or scripts.
    """

    ALLOWED = frozenset({"p", "strong", "b", "em", "i", "br", "a"})
    P_STYLES = frozenset({"margin:0 0 20px 0;", "margin:0 0 22px 0;"})

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.paragraphs = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in self.ALLOWED:
            raise OutreachTemplateBlocked(f"unapproved BODY_HTML element: {tag}")
        names = [name for name, _ in attrs]
        if len(names) != len(set(names)):
            raise OutreachTemplateBlocked("duplicate BODY_HTML attribute")
        if tag == "p":
            if self.stack:
                raise OutreachTemplateBlocked("nested BODY_HTML paragraphs")
            if attrs not in ([], [("style", "margin:0 0 20px 0;")],
                             [("style", "margin:0 0 22px 0;")]):
                raise OutreachTemplateBlocked("unapproved paragraph geometry")
            self.paragraphs += 1
        elif tag == "a":
            attr = dict(attrs)
            if not attr.get("href") or set(attr) - {"href", "target"}:
                raise OutreachTemplateBlocked("unapproved link attributes")
            if "target" in attr and attr["target"] != "_blank":
                raise OutreachTemplateBlocked("unapproved link target")
            uri = attr["href"].strip()
            scheme = urlsplit(uri).scheme.lower()
            try:
                decoded_uri = unquote_to_bytes(uri).decode("utf-8", errors="strict")
            except UnicodeError as exc:
                raise OutreachTemplateBlocked("non-UTF8 BODY_HTML link") from exc
            if scheme not in ("https", "http", "mailto") or any(
                ord(char) < 32 or ord(char) == 127 for char in decoded_uri
            ):
                raise OutreachTemplateBlocked("unsafe BODY_HTML link")
            if scheme in ("https", "http") and not urlsplit(uri).netloc:
                raise OutreachTemplateBlocked("invalid BODY_HTML web link")
        elif attrs:
            raise OutreachTemplateBlocked("unapproved BODY_HTML attributes")
        if tag != "br":
            self.stack.append(tag)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "br":
            raise OutreachTemplateBlocked("unapproved self-closing BODY_HTML element")
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if not self.stack or self.stack.pop() != tag:
            raise OutreachTemplateBlocked("unbalanced BODY_HTML structure")

    def handle_comment(self, data: str) -> None:
        raise OutreachTemplateBlocked("BODY_HTML comment not permitted")

    def handle_decl(self, decl: str) -> None:
        raise OutreachTemplateBlocked("BODY_HTML declaration not permitted")

    def handle_pi(self, data: str) -> None:
        raise OutreachTemplateBlocked("BODY_HTML processing instruction not permitted")


def validate_body_html(body: str) -> None:
    if len(body) > 12_000:
        raise OutreachTemplateBlocked("BODY_HTML exceeds reviewed length")
    if body.rfind(chr(60)) > body.rfind(chr(62)):
        raise OutreachTemplateBlocked("incomplete trailing BODY_HTML tag")
    parser = _AllowedBodyParser()
    try:
        parser.feed(body)
        parser.close()
    except (ValueError, TypeError) as exc:
        raise OutreachTemplateBlocked("invalid BODY_HTML") from exc
    if parser.stack or not parser.paragraphs or parser.rawdata.strip():
        raise OutreachTemplateBlocked("missing paragraphs or unbalanced BODY_HTML")


def validate_mailto_subject(value: str) -> None:
    # A percent sign must be followed by two hex digits. Decoded CR/LF and
    # control characters must not enter the Gmail recipient's mailto URL.
    if re.search(r"%(?![0-9A-Fa-f]{2})", value):
        raise OutreachTemplateBlocked("malformed percent-encoded mailto subject")
    try:
        decoded = unquote_to_bytes(value).decode("utf-8", errors="strict")
    except UnicodeError as exc:
        raise OutreachTemplateBlocked("non-UTF8 mailto subject") from exc
    if not decoded.strip() or any(ord(c) < 32 or ord(c) == 127 for c in decoded):
        raise OutreachTemplateBlocked("unsafe mailto subject control character")


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

    validate_body_html(variables["BODY_HTML"])
    if kind == "vinterro":
        validate_mailto_subject(variables["MAILTO_SUBJECT_ENCODED"])

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
