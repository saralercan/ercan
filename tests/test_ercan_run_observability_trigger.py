"""Block regressions of the Vinterro One run observability trigger."""
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SQL=(ROOT/"supabase/ercan-os-run-observability-column-fix.sql").read_text(encoding="utf-8").lower()

class ObservabilityTriggerRepair(unittest.TestCase):
    def test_recreates_correct_trigger(self):
        self.assertIn("create or replace function private.ercan_os_capture_run_observability()", SQL)
        self.assertIn("returns trigger", SQL)
        self.assertIn("security definer",SQL)
        self.assertIn("set search_path to 'pg_catalog', 'public'",SQL)

    def test_only_existing_agent_columns_written(self):
        self.assertIn("update public.ercan_os_agents set health",SQL)
        self.assertNotIn("updated_at=now()",SQL)
        self.assertIn("where id=new.agent_id",SQL)

    def test_no_fake_completion_or_runtime_execution(self):
        self.assertIn("if new.status in ('success','error','blocked')",SQL)
        self.assertIn("public.ercan_os_usage_costs",SQL)
        self.assertIn("public.ercan_os_incidents",SQL)
        self.assertIn("return new;",SQL)
        self.assertNotIn("gmail.send",SQL)
        self.assertNotIn("delete from",SQL)

    def test_retains_unique_cost_upsert(self):
        self.assertIn("on conflict (run_id) where run_id is not null do update",SQL)

if __name__ == "__main__":
    unittest.main()
