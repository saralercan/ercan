"""Audit complete corporate-domain candidate suppression before production release."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
P=ROOT / "supabase/vinterro-first-touch-domain-review-complete-20261009.sql"
SRC=P.read_text(encoding="utf-8").lower()

class CompleteDomainReview(unittest.TestCase):
    def test_all_candidate_mailboxes_included(self):
        self.assertIn("from unnest(v_emails) as addr",SRC)
        self.assertIn("select v_domain as domain_name",SRC)
        self.assertIn("v_review_domains := array",SRC)
        self.assertIn("from unnest(v_review_domains) as candidate_domain",SRC)
        self.assertNotIn("v_review_domain text :=",SRC)

    def test_review_after_exact_history_check(self):
        self.assertLess(SRC.index("historical_gmail_sent_suppressed"),SRC.index("historical_corporate_domain_manual_review_required"))

    def test_existing_transaction_and_release_security_preserved(self):
        self.assertLess(SRC.index("first_touch_release_gate_blocked"),SRC.index("pg_advisory_xact_lock"))
        self.assertLess(SRC.index("pg_advisory_xact_lock"),SRC.index("historical_corporate_domain_manual_review_required"))
        self.assertIn("select 1 from vinterro_internal.outreach_gmail_sent_evidence",SRC)

    def test_review_only_never_automatic_merge_or_send(self):
        self.assertIn("'allowed',false",SRC)
        self.assertIn("'reason','historical_corporate_domain_manual_review_required'",SRC)
        self.assertIn("'review_domains',v_review_domains",SRC)
        self.assertNotIn("gmail.send",SRC)
        self.assertNotIn("delete from",SRC)

    def test_consumer_provider_exclusions(self):
        for d in ("gmail.com","hotmail.com","outlook.com","icloud.com","yahoo.com","booking.com","airbnb.com","proton.me"):
            self.assertIn("'"+d+"'",SRC)

if __name__=="__main__":
    unittest.main()
