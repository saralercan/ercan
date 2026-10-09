"""Regression checks: model-usage ledger never equals control-plane routing."""
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
SQL=(ROOT/"supabase/ercan-os-observability-verified-usage-20261009.sql").read_text(encoding="utf-8").lower()

class ModelUsageEvidence(unittest.TestCase):
    def test_private_existing_trigger_preserved(self):
        self.assertIn("create or replace function private.ercan_os_capture_run_observability()",SQL)
        self.assertIn("returns trigger",SQL)
        self.assertIn("security definer",SQL)
        self.assertIn("set search_path to 'pg_catalog', 'public'",SQL)

    def test_only_model_execution_can_record_tokens(self):
        self.assertIn("if new.status in ('success','error')",SQL)
        self.assertIn("new.output->>'provider'",SQL)
        self.assertIn("new.output->>'model'",SQL)
        self.assertIn("and jsonb_typeof(u) = 'object'",SQL)
        self.assertIn("if v_input > 0 or v_output > 0 or v_cached > 0",SQL)
        self.assertNotIn("coalesce(new.output->>'provider','unknown')",SQL)

    def test_invalid_provider_count_does_not_abort_run(self):
        self.assertEqual(SQL.count("~ '^[0-9]{1,18}$'"),3)
        self.assertIn("else 0 end",SQL)
        self.assertIn("case when",SQL)

    def test_usage_status_is_not_claimed_paid_billing(self):
        self.assertIn("'pricing_status','unpriced'",SQL)
        self.assertIn("'cost_not_verified',true",SQL)
        self.assertIn("'source','run_output_provider_usage'",SQL)

    def test_errors_still_generate_incident(self):
        self.assertIn("if new.status='error' then",SQL)
        self.assertIn("public.ercan_os_incidents",SQL)
        self.assertIn("return new;",SQL)

    def test_agents_not_graded_by_queued_and_blocked_jobs(self):
        self.assertNotIn("update public.ercan_os_agents",SQL)
        self.assertNotIn("recent_total",SQL)
        self.assertNotIn("recent_success",SQL)

    def test_no_external_effects(self):
        for forbidden in ["gmail.send","net.http_post","delete from","set status='success'"]:
            self.assertNotIn(forbidden,SQL)

if __name__=="__main__":
    unittest.main()
