"""Production-safe tests for the 2026-10-08 user-approved HTML source locks."""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_vinterro_outreach_html import (  # noqa: E402
    OutreachTemplateBlocked,
    EXPECTED_TOKENS,
    SOURCES,
    git_blob_sha,
    locked_source,
    render_exact,
    verify_exact,
)


VINTERRO = {
    "BODY_HTML": "<p>Merhaba, doğrulanmış fırsatlara dayanan mesaj.</p>",
    "CTA_LABEL": "E-posta ile devam edelim",
    "MAILTO_SUBJECT_ENCODED": "Firsatlari%20konusalim",
    "COMPLIANCE_TEXT": "İletişim istemiyorsanız yanıtlayabilirsiniz.",
}
DRAGDROP = {
    "BODY_HTML": "<p>Merhaba, tasarımcı iş birliği hakkında.</p>",
    "B2C_CTA_LABEL": "Bize Katılın",
    "B2B_CTA_LABEL": "Kurumsal Siparişler",
    "COMPLIANCE_TEXT": "E-posta almak istemiyorsanız yanıtlayabilirsiniz.",
}


class LockedOutreachTests(unittest.TestCase):
    def test_approved_sources_byte_locked(self):
        for kind, (relative, expected_sha) in SOURCES.items():
            with self.subTest(kind=kind):
                data = (ROOT / relative).read_bytes()
                self.assertEqual(git_blob_sha(data), expected_sha)
                self.assertIn("680px", locked_source(kind))

    def test_approved_token_sets_are_explicit(self):
        self.assertEqual(set(VINTERRO), EXPECTED_TOKENS["vinterro"])
        self.assertEqual(set(DRAGDROP), EXPECTED_TOKENS["dragdrop"])

    def test_render_and_verify_approved_vinterro(self):
        html = render_exact("vinterro", VINTERRO)
        verify_exact("vinterro", VINTERRO, html)
        self.assertIn(">WEB</span>", html)
        self.assertIn("info@vinterro.digital", html)
        self.assertIn("#e31b23", html)
        self.assertIn("max-width:680px", html)

    def test_render_and_verify_approved_dragdrop(self):
        html = render_exact("dragdrop", DRAGDROP)
        verify_exact("dragdrop", DRAGDROP, html)
        self.assertIn(">B2C</span>", html)
        self.assertIn(">B2B</span>", html)
        self.assertIn("info@draganddrop.tr", html)
        self.assertIn("max-width:680px", html)

    def test_spacing_divider_footer_drift_blocked(self):
        html = render_exact("vinterro", VINTERRO)
        for old, new in [
            ("max-width:680px", "max-width:681px"),
            ("background:#e31b23", "background:#000000"),
            ("CREATIVITY GROWTH STUDIO", "GROWTH AGENCY"),
            ("info@vinterro.digital", "test@example.com"),
        ]:
            with self.subTest(change=old):
                self.assertIn(old, html)
                with self.assertRaises(OutreachTemplateBlocked):
                    verify_exact("vinterro", VINTERRO, html.replace(old, new, 1))

    def test_hidden_extra_element_blocked(self):
        html = render_exact("dragdrop", DRAGDROP)
        with self.assertRaises(OutreachTemplateBlocked):
            verify_exact("dragdrop", DRAGDROP, html + "<div>extra footer</div>")

    def test_extra_or_missing_tokens_blocked(self):
        for values in [
            {"BODY_HTML": "<p>Only partial</p>"},
            {**VINTERRO, "SECOND_CTA": "unapproved"},
        ]:
            with self.assertRaises(OutreachTemplateBlocked):
                render_exact("vinterro", values)

    def test_empty_and_markup_label_blocked(self):
        for value in ["", "  ", "<a>click</a>", "hello\nthere"]:
            with self.subTest(value=value), self.assertRaises(OutreachTemplateBlocked):
                render_exact("vinterro", {**VINTERRO, "CTA_LABEL": value})

    def test_invalid_encoded_subject_blocked(self):
        with self.assertRaises(OutreachTemplateBlocked):
            render_exact(
                "vinterro",
                {**VINTERRO, "MAILTO_SUBJECT_ENCODED": "Hello world"},
            )

    def test_missing_source_fails_closed(self):
        with self.assertRaises(OutreachTemplateBlocked):
            locked_source("vinterro", ROOT / "nonexistent-directory")


if __name__ == "__main__":
    unittest.main()
