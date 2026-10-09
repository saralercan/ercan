"""Verify the Reklam Ajansı workflow plans do not impersonate real work or approvals."""
from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from plan_reklam_ajansi_workflow import plan
from route_reklam_ajansi_subskills import route

class EvidenceWorkflowQA(unittest.TestCase):
    def test_one_owner_and_bounded_skills(self):
        p=plan("Meta Ads Pixel Purchase ve CAPI ölçümünü kontrol et")
        self.assertEqual(p["canonical_agent"],"Reklam Ajansı")
        self.assertEqual(p["canonical_agent_id"],"b2acac02-29d7-418c-9f04-24552e947776")
        self.assertEqual(p["mode"],"PLAN_ONLY_NO_REMOTE_EFFECTS")
        self.assertIn("meta-ads",p["selected_skill_ids"])
        self.assertIn("analytics-attribution",p["selected_skill_ids"])
        self.assertLessEqual(len(p["selected_skill_ids"]),3)
        self.assertEqual(len(p["selected_skill_ids"]),len(set(p["selected_skill_ids"])))

    def test_intake_precedes_skill_and_merge(self):
        p=plan("Google Ads Search kampanyası anahtar kelime araştırması")
        stages={x["id"]:x for x in p["stages"]}
        self.assertEqual(stages["intake"]["depends_on"],[])
        work=[s for s in p["stages"] if s["type"]=="skill_workstream"]
        self.assertGreaterEqual(len(work),1)
        for s in work:
            self.assertEqual(s["depends_on"],["intake"])
            self.assertEqual(s["status"],"NOT_STARTED")
            self.assertTrue(s["evidence_required"])
            self.assertTrue(s["deliverable_keys"])
            self.assertIsNone(s["actual_model_receipt"])
        self.assertEqual(set(stages["synthesis"]["depends_on"]),{s["id"] for s in work})
        self.assertEqual(stages["independent-qa"]["depends_on"],["synthesis"])

    def test_no_fake_qa_or_platform_execution(self):
        p=plan("Facebook Meta Pixel Purchase analiz et")
        self.assertFalse(p["parallel_model_work_executed"])
        self.assertFalse(p["campaign_data_read_from_accounts"])
        self.assertFalse(p["provider_receipt_verified"])
        self.assertFalse(p["independent_qa_done"])
        self.assertEqual(p["stages"][-1]["verdict"],"PENDING")
        self.assertEqual(p["gates"]["ads_account_write"],"BLOCKED")
        self.assertEqual(p["gates"]["production_release"],"BLOCKED")
        self.assertEqual(p["gates"]["first_touch_email"],"BLOCKED")
        self.assertFalse(any(x["type"]=="live_execution" for x in p["stages"]))

    def test_real_campaign_activation_request_requires_human_approval(self):
        p=plan("Meta Ads reklam setini aktif et, bütçeyi değiştir")
        self.assertTrue(p["requested_live_mutation"])
        self.assertTrue(p["human_approval_required"])
        self.assertEqual(p["stages"][-1]["id"],"human-approval")
        self.assertIn("LIVE_AD_ACCOUNT_MUTATION",p["stages"][-1]["required_for"])
        self.assertIsNone(p["stages"][-1]["authorization"])
        self.assertEqual(p["stages"][-1]["status"],"NOT_REQUESTED")

    def test_stop_pause_delete_and_bid_changes_are_guarded(self):
        for cmd in ("Google Ads kampanyasını sil",
                    "Meta reklamlarını durdur",
                    "Facebook reklam setini devre dışı bırak",
                    "Google Ads teklif değiştir",
                    "Amazon Ads delete campaign"):
            with self.subTest(cmd=cmd):
                p=plan(cmd)
                self.assertTrue(p["requested_live_mutation"])
                self.assertTrue(p["human_approval_required"])
                self.assertEqual(p["gates"]["ads_account_write"],"BLOCKED")

    def test_customer_data_risk_escalates_even_without_spend(self):
        p=plan("Meta Ads için customer list yükle ve lookalike audience oluştur")
        self.assertTrue(p["sensitive_customer_data_requested"])
        self.assertTrue(p["human_approval_required"])
        self.assertIn("CUSTOMER_DATA_PROCESSING_OR_UPLOAD",p["stages"][-1]["required_for"])
        self.assertEqual(p["gates"]["production_release"],"BLOCKED")
        self.assertFalse(p["campaign_data_read_from_accounts"])

    def test_plain_strategy_proposal_does_not_imply_billing(self):
        p=plan("Google Ads PMax kampanya stratejisi araştır")
        self.assertFalse(p["requested_live_mutation"])
        self.assertFalse(p["human_approval_required"])
        self.assertEqual(p["stages"][-1]["id"],"independent-qa")
        self.assertEqual(p["gates"]["ads_account_write"],"BLOCKED")

    def test_complex_tasks_expose_deferred_skills(self):
        task=("Google Ads Meta Ads Pinterest kreatif tasarım GA4 Purchase bütçe KVKK "
              "Japonya Shopee pazar araştırması")
        r=route(task)
        p=plan(task)
        self.assertEqual(p["selected_skill_ids"],[x["id"] for x in r["selected"]])
        self.assertTrue(p["scope_split_recommended"])
        self.assertGreater(len(p["deferred_skill_ids"]),0)
        self.assertEqual(
            set(p["selected_skill_ids"]) & set(p["deferred_skill_ids"]),set()
        )
        self.assertLessEqual(len(p["selected_skill_ids"]),3)

    def test_parent_fallback_with_nonspecialized_input(self):
        p=plan("Toplantı gündemini hazırla")
        self.assertEqual(p["selected_skill_ids"],[])
        self.assertEqual([s["id"] for s in p["stages"] if s["type"]=="parent_intake"],["parent-scoping"])
        self.assertEqual(p["stages"][-1]["id"],"independent-qa")

    def test_genuine_independent_review_not_self_verification(self):
        p=plan("Pinterest video reklam kreatif storyboard")
        review=next(s for s in p["stages"] if s["type"]=="independent_external_review")
        self.assertEqual(review["status"],"NOT_PERFORMED")
        self.assertTrue(review["reviewer_must_differ_from_producer"])
        self.assertIn("QA Agent",review["reviewer_candidates"])
        self.assertNotIn("Reklam Ajansı",review["reviewer_candidates"])

    def test_legal_privacy_task_includes_compliance_specialist(self):
        p=plan("KVKK GDPR consent Meta Ads policy denetimi")
        self.assertIn("compliance-privacy",p["selected_skill_ids"])
        self.assertEqual(p["gates"]["production_release"],"BLOCKED")

    def test_international_retail_task_includes_both_dimensions(self):
        p=plan("Japonya Shopee Shopping reklam uygunluğu")
        self.assertIn("global-market-research",p["selected_skill_ids"])
        self.assertIn("retail-marketplaces",p["selected_skill_ids"])

    def test_cli_runs_offline_and_returns_json(self):
        cmd=[sys.executable,str(ROOT/"scripts/plan_reklam_ajansi_workflow.py"),
             "Meta Pixel Purchase CAPI kontrol et"]
        res=subprocess.run(cmd,check=True,text=True,capture_output=True)
        obj=json.loads(res.stdout)
        self.assertEqual(obj["mode"],"PLAN_ONLY_NO_REMOTE_EFFECTS")
        self.assertIn("independent-qa",[s["id"] for s in obj["stages"]])

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            plan(" ")

    def test_documents_advertise_nonexecuted_scope(self):
        doc=(ROOT/"docs/agents/REKLAM_AJANSI_EVIDENCE_WORKFLOW.md").read_text(encoding="utf8")
        self.assertIn("REKLAM_AJANSI_SUBSKILL_ROUTER.json",doc)
        self.assertIn("plan_reklam_ajansi_workflow.py",doc)
        self.assertIn("PLAN",doc)
        self.assertIn("first_touch_email_gate",doc)

if __name__=="__main__":
    unittest.main()
