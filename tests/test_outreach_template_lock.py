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

    def test_real_approved_mime_paragraph_format_is_allowed(self):
        variables = {
            **VINTERRO,
            "BODY_HTML": (
                '<p style="margin:0 0 20px 0;">Merhaba <strong>Marka</strong> ekibi,</p>'
                '<p style="margin:0 0 20px 0;">'
                'Siteniz hakkında iki somut nokta:<br> birinci<br /> ikinci.'
                '</p>'
            ),
        }
        html = render_exact("vinterro", variables)
        verify_exact("vinterro", variables, html)
        self.assertIn("Merhaba <strong>Marka</strong>", html)

    def test_unsafe_html_cannot_break_approved_outer_shell(self):
        bad_bodies = [
            "<p>Merhaba</p></td></tr><table><tr><td>injection</td></tr></table>",
            "<p>Merhaba</p><script>alert(1)</script>",
            '<p style="width:2000px;">Geniş</p>',
            "<p>Merhaba</p><img src='https://example.org/pixel'>",
            "<p>Merhaba</p><style>table{display:none}</style>",
            '<p onclick="alert(1)">Merhaba</p>',
            "<p>Merhaba</p><iframe src='https://example.org'></iframe>",
            "<p>Merhaba",
            "<p>Merhaba</p><!-- hide content -->",
            '<p>Merhaba</p><p><p>Nested</p></p>',
            "<div>Başka bir şablon</div>",
            '<p>Merhaba</p><a href="javascript:alert(1)">Tıkla</a>',
            '<p>Merhaba</p><a href="https://test.example" style="font-size:30px">Tıkla</a>',
        ]
        for bad in bad_bodies:
            with self.subTest(body=bad), self.assertRaises(OutreachTemplateBlocked):
                render_exact("vinterro", {**VINTERRO, "BODY_HTML": bad})

    def test_approved_mailto_and_unsafe_encoded_subjects(self):
        for good in ("Firsatlari%20konusalim", "Teklif%20i%C3%A7in%20yan%C4%B1t"):
            with self.subTest(approved=good):
                html = render_exact(
                    "vinterro", {**VINTERRO, "MAILTO_SUBJECT_ENCODED": good}
                )
                self.assertIn(good, html)
        for bad in ("%0D%0ABcc%3Aevil%40example.org", "%", "%GG", "%00",
                    "%C3%28", "%7F"):
            with self.subTest(blocked=bad), self.assertRaises(OutreachTemplateBlocked):
                render_exact(
                    "vinterro", {**VINTERRO, "MAILTO_SUBJECT_ENCODED": bad}
                )

    def test_http_mailto_body_links_without_attributes_allowed(self):
        body = (
            '<p>Detaylar için <a href="https://vinterro.digital/" target="_blank">'
            'web sitesini</a> ziyaret edin ya da '
            '<a href="mailto:info@vinterro.digital">bize yanıt verin</a>.</p>'
        )
        html = render_exact("vinterro", {**VINTERRO, "BODY_HTML": body})
        self.assertIn(body, html)

    def test_missing_source_fails_closed(self):
        with self.assertRaises(OutreachTemplateBlocked):
            locked_source("vinterro", ROOT / "nonexistent-directory")


    def test_rpc_release_gate_and_serialized_claim_are_preserved(self):
        path = ROOT / "supabase" / "outreach-first-touch-prepare-transaction-lock.sql"
        source = path.read_text(encoding="utf-8")
        self.assertIn("first_touch_release_gate_blocked", source)
        self.assertIn("pg_advisory_xact_lock", source)
        self.assertIn("vinterro_outreach_account_claims", source)
        self.assertIn("send_attempt_token", source)
        self.assertIn("return jsonb_build_object('allowed',false", source)
        gate_pos = source.index("first_touch_release_gate_blocked")
        lock_pos = source.index("pg_advisory_xact_lock")
        lookup_pos = source.index("into v_existing")
        self.assertLess(gate_pos, lock_pos)
        self.assertLess(lock_pos, lookup_pos)

if __name__ == "__main__":
    unittest.main()
