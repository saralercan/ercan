"""Fail-closed historical Gmail SENT suppression migration checks."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SQL = ROOT / "supabase" / "outreach-gmail-sent-evidence-20261009.sql"

class GmailSentEvidencePolicy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sql = SQL.read_text(encoding="utf-8").lower()

    def test_private_schema(self):
        self.assertIn("vinterro_internal.outreach_gmail_sent_evidence", self.sql)
        self.assertIn("enable row level security", self.sql)
        self.assertIn("revoke all on vinterro_internal.outreach_gmail_sent_evidence from public, anon, authenticated",self.sql)
        self.assertIn("grant select on vinterro_internal.outreach_gmail_sent_evidence to service_role",self.sql)

    def test_never_claim_delivery(self):
        self.assertIn("not evidence of delivery",self.sql)
        self.assertIn("gmail_message_id text primary key",self.sql)
        self.assertIn("recipient_email text not null",self.sql)
        self.assertIn("sent_at timestamptz not null",self.sql)

    def test_atomic_gate_stays_closed(self):
        self.assertIn("first_touch_release_gate_blocked",self.sql)
        self.assertIn("pg_advisory_xact_lock",self.sql)
        self.assertIn("historical_gmail_sent_suppressed",self.sql)

    def test_suppression_precedes_claim(self):
        lock=self.sql.index("perform pg_catalog.pg_advisory_xact_lock")
        guard=self.sql.index("historical_gmail_sent_suppressed")
        lookup=self.sql.index("into v_existing")
        self.assertLess(lock,guard)
        self.assertLess(guard,lookup)

    def test_all_alias_emails_checked(self):
        self.assertIn("e.recipient_email = v_email",self.sql)
        self.assertIn("e.recipient_email = any(v_emails)",self.sql)

if __name__=="__main__":
    unittest.main()
