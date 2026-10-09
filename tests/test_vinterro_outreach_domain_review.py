"""Static regression checks for conservative same-domain first-touch review."""
from pathlib import Path
import unittest

SQL=(Path(__file__).resolve().parents[1]/"supabase/vinterro-first-touch-domain-review-20261009.sql").read_text(encoding="utf-8").lower()

class HistoricalDomainReview(unittest.TestCase):
    def test_existing_release_gate_precedes_domain_check(self):
        self.assertLess(SQL.index("first_touch_release_gate_blocked"),SQL.index("historical_corporate_domain_manual_review_required"))

    def test_transactional_serialization_precedes_review(self):
        self.assertLess(SQL.index("pg_advisory_xact_lock"),SQL.index("historical_corporate_domain_manual_review_required"))

    def test_exact_known_email_checked_first(self):
        self.assertLess(SQL.index("historical_gmail_sent_suppressed"),SQL.index("historical_corporate_domain_manual_review_required"))

    def test_review_is_not_auto_claim(self):
        self.assertIn("'allowed',false", SQL)
        self.assertIn("manual_review_required",SQL)
        self.assertIn("never an automatic",SQL)
        self.assertIn("review_domain",SQL)

    def test_shared_email_providers_not_assumed_same_business(self):
        for domain in ("gmail.com","outlook.com","hotmail.com","yahoo.com","icloud.com","booking.com","qq.com"):
            self.assertIn("'"+domain+"'",SQL)

    def test_supports_canonical_domain_or_primary_email_domain(self):
        self.assertIn("coalesce(v_domain,nullif(split_part(coalesce(v_email,''),'@',2),''))",SQL)
        self.assertIn("split_part(e.recipient_email,'@',2) = v_review_domain",SQL)

    def test_no_release_or_send_side_effect(self):
        self.assertNotIn("outreach_first_touch_release_gate','open'",SQL)
        self.assertNotIn("gmail.send",SQL)
        self.assertNotIn("delete from",SQL)

if __name__=="__main__":
    unittest.main()
