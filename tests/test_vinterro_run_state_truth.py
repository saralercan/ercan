"""Check routing-only run creation never reports executor success."""
import unittest
from pathlib import Path

SRC=(Path(__file__).resolve().parents[1]/"supabase/functions/ercan-os-api/index.ts").read_text(encoding="utf-8")

class RunStatusTruth(unittest.TestCase):
    def test_router_creates_queued_runs(self):
        self.assertIn("if (action === 'start_ai_run' || action === 'create_run')",SRC)
        self.assertIn("const status = decision === 'deny' ? 'blocked' : decision === 'approval_required' ? 'awaiting_approval' : 'queued'",SRC)
        self.assertNotIn("(action === 'start_ai_run' ? 'running' : 'success')",SRC)

    def test_no_claim_of_execution_before_worker(self):
        self.assertIn("execution: status === 'queued' ? 'not_started' : 'not_permitted'",SRC)
        self.assertNotIn("output: status === 'success' ?",SRC)
        self.assertIn("completed_at: status === 'blocked' ? now() : null",SRC)

    def test_real_completion_requires_review(self):
        self.assertIn("if (action === 'complete_ai_run')",SRC)
        self.assertIn("status: modelSucceeded ? 'under_review' : 'error'",SRC)
        self.assertIn("action: 'review_run'",SRC)

    def test_supervision_is_not_skipped(self):
        self.assertIn("action: 'plan_run'",SRC)
        self.assertIn("code: 'supervision_required'",SRC)

if __name__=="__main__":
    unittest.main()
