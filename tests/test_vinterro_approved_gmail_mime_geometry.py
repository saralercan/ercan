"""Compare canonical Vinterro outreach against frozen actual approved Gmail MIME geometry.

Source: SENT message 1a11c21c960cc646, its decoded text/html MIME part.
Only non-personal fixed CSS is snapshotted, never recipient body content.
"""
import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SNAPSHOT=ROOT/"tests/fixtures/vinterro_outreach_approved_real_mime_styles.json"
CANONICAL=ROOT/"docs/standards/VINTERRO_OUTREACH_CANONICAL_TEMPLATE.html"

class ApprovedGmailMimeGeometry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.snapshot=json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        src=CANONICAL.read_text(encoding="utf-8")
        src=re.sub(r"<!--[\\s\\S]*?-->","",src)
        cls.styles=re.findall(r'\\bstyle="([^"]*)"',src)

    def test_approved_gmail_message_provenance(self):
        self.assertEqual(self.snapshot["reference_gmail_message_id"],"1a11c21c960cc646")
        self.assertEqual(self.snapshot["reference_html_style_count"],27)
        self.assertEqual(self.snapshot["dynamic_body_style_count"],6)

    def test_exact_head_geometry_from_real_mime(self):
        self.assertEqual(self.styles[:9],self.snapshot["header_style_sequence"])

    def test_exact_cta_compliance_dividers_footer_geometry(self):
        self.assertEqual(self.styles[9:],self.snapshot["cta_footer_style_sequence"])
        self.assertEqual(len(self.styles),21)

    def test_no_approved_body_content_snapshotted(self):
        s=SNAPSHOT.read_text(encoding="utf-8")
        self.assertNotIn("BODY_HTML",s)
        self.assertNotIn("COMPLIANCE_TEXT",s)
        self.assertNotIn("mailto:info@vinterro.digital",s)

    def test_template_keeps_approved_dynamic_slots(self):
        s=CANONICAL.read_text(encoding="utf-8")
        for token in ("{{BODY_HTML}}","{{CTA_LABEL}}","{{MAILTO_SUBJECT_ENCODED}}","{{COMPLIANCE_TEXT}}"):
            self.assertIn(token,s)

if __name__=="__main__":
    unittest.main()
