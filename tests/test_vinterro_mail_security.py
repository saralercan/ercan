"""Fail-closed grants regression for Vinterro Digital MailAgent production state."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SQL = (ROOT / "supabase/vinterro-mail-rpc-owner-access-hardening.sql").read_text(encoding="utf-8").lower()

class MailAgentSecurity(unittest.TestCase):
    def test_transactional(self):
        self.assertIn("begin;",SQL)
        self.assertIn("commit;",SQL)

    def test_only_private_backend_can_write_state(self):
        for tbl in ("vinterro_outreach_account_claims","vinterro_sales_super_agent_state"):
            self.assertIn(f"revoke all on table public.{tbl}",SQL)
            self.assertIn(f"grant select on table public.{tbl}",SQL)
        self.assertNotIn("grant update on table",SQL)
        self.assertNotIn("grant insert on table",SQL)

    def test_mfa_only_policies_removed(self):
        for tbl in ("vinterro_outreach_account_claims","vinterro_sales_super_agent_state"):
            self.assertIn("drop policy if exists vinterro_one_mfa_guard\n  on public."+tbl,SQL)

    def test_claims_owner_uses_membership_and_aal2(self):
        self.assertIn("private.ercan_os_has_access(m.organization_id)",SQL)
        self.assertIn("m.role = 'owner'",SQL)
        self.assertIn("p.name = 'vinterro digital'",SQL)

    def test_all_four_atomic_rpcs_are_backend_only(self):
        for fn in ("vinterro_prepare_first_touch","vinterro_finalize_first_touch_sent",
                   "vinterro_mark_first_touch_ambiguous","vinterro_release_first_touch_after_no_send"):
            self.assertIn("revoke execute on function public."+fn,SQL)
            self.assertIn("grant execute on function public."+fn,SQL)
        self.assertEqual(SQL.count("from public, anon, authenticated;"),6)
        self.assertEqual(SQL.count("to service_role;"),4)

    def test_keep_owner_read_policy_unmodified(self):
        self.assertIn('existing "ercan os owner can read sales super agent state" remains',SQL)
        self.assertNotIn("drop policy if exists \"ercan os owner can read sales super agent state\"",SQL)

    def test_does_not_change_release_gate(self):
        self.assertNotIn("set health =",SQL)
        self.assertNotIn("outreach_first_touch_release_gate','open'",SQL)
        self.assertNotIn("delete from",SQL)

if __name__ == "__main__":
    unittest.main()
