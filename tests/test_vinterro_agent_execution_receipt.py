"""Fail-closed Vinterro One proof-of-execution and supervision contracts."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SQL = (ROOT/"supabase/vinterro-agent-execution-receipt-gate-20261009.sql").read_text(encoding="utf-8").lower()
API = (ROOT/"supabase/functions/ercan-os-api/index.ts").read_text(encoding="utf-8")
SUP = (ROOT/"supabase/functions/vinterro-one-supervision/index.ts").read_text(encoding="utf-8")

class ExecutionReceiptSecurity(unittest.TestCase):
    def test_receipts_are_private_and_immutable_from_clients(self):
        self.assertIn("vinterro_internal.agent_execution_receipts",SQL)
        self.assertIn("enable row level security",SQL)
        self.assertIn("from public, anon, authenticated",SQL)
        self.assertIn("grant select, insert on table",SQL)
        self.assertNotIn("grant update on table",SQL)
        self.assertNotIn("grant delete on table",SQL)

    def test_provider_evidence_is_nonempty(self):
        for required in ("provider_request_id text not null", "input_tokens bigint not null",
                         "output_tokens bigint not null", "input_tokens + output_tokens > 0"):
            self.assertIn(required,SQL)

    def test_only_registered_active_worker_counts(self):
        for required in ("public.vinterro_sales_worker_credentials",
                         "w.worker_id = e.worker_id", "w.active is true",
                         "w.last_seen_at is not null",
                         "w.last_seen_at >= e.receipt_recorded_at"):
            self.assertIn(required,SQL)

    def test_client_cannot_call_receipt_lookup_or_write_status(self):
        self.assertIn("revoke execute on function public.vinterro_has_agent_execution_receipt(uuid)",SQL)
        self.assertIn("before insert or update of status on public.ercan_os_runs",SQL)
        self.assertIn("new.status in ('under_review','success')",SQL)
        self.assertIn("agent_execution_receipt_required",SQL)

    def test_success_requires_independent_review(self):
        for required in ("s.final_gate_state='verified'","r.verdict='pass'",
                         "r.reviewer_agent_id is distinct from s.producer_agent_id",
                         "independent_supervision_required"):
            self.assertIn(required,SQL)

    def test_api_rejects_precompletion_before_any_mutation(self):
        ix=API.index("if (action === 'complete_ai_run')")
        s=API[ix:API.index("if (action === 'decide_approval')",ix)]
        self.assertIn("current.status !== 'running'",s)
        self.assertIn("vinterro_has_agent_execution_receipt",s)
        self.assertIn("hasReceipt !== true",s)
        self.assertLess(s.index("hasReceipt !== true"),s.index("status: modelSucceeded ? 'under_review' : 'error'"))

    def test_supervision_rejects_missing_producer_evidence(self):
        self.assertIn("if (receiptError || hasReceipt !== true)",SUP)
        self.assertIn("state='NOT_VERIFIED'",SUP)
        self.assertIn("state!=='NOT_VERIFIED'",SUP)
        self.assertIn("R0 cannot bypass independent review",SUP)
        self.assertIn("r.reviewer_agent_id!==supervision.producer_agent_id",SUP)

    def test_unattested_review_does_not_invoke_paid_reviewer(self):
        start=SUP.index("if (action==='review_run')")
        end=SUP.index("if (action==='submit_review')",start)
        section=SUP[start:end]
        self.assertIn("vinterro_has_agent_execution_receipt",section)
        self.assertLess(section.index("hasReceipt !== true"),section.index("callReviewer(authHeader"))
    
    def test_no_unnecessary_transport_or_billing_side_effect(self):
        self.assertNotIn("gmail.send",SQL)
        self.assertNotIn("net.http_post",SQL)
        self.assertNotIn("outreach_first_touch_release_gate','open'",SQL)
        self.assertNotIn("INSERT INTO public.ercan_os_runs",SQL.upper())

if __name__=="__main__":
    unittest.main()
