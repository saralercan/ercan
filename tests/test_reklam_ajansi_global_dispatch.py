"""Master all-agents/Vinterro One invocation MUST include one Reklam Ajansı and ALL NINE scoped subskills."""
from __future__ import annotations
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from route_reklam_ajansi_subskills import route
from plan_reklam_ajansi_workflow import plan

DATA=json.loads((ROOT/"docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json").read_text(encoding="utf8"))
ALL_IDS={s["id"] for s in DATA["skills"]}

class GlobalReklamAjansiDispatch(unittest.TestCase):
    def test_global_all_agent_command_includes_nine_skills(self):
        for text in ("tüm ajanları çalıştır","bütün ajanları çalıştır",
                     "Vinterro One çalıştır","Vinterro One'ı çalıştır",
                     "vinterro one'i çalıştır","run all agents","use all agents",
                     "run Vinterro One","start Vinterro One"):
            with self.subTest(text=text):
                result=route(text)
                self.assertTrue(result["global_invocation"])
                self.assertTrue(result["parent_agent_included"])
                self.assertEqual(result["canonical_agent"],"Reklam Ajansı")
                self.assertEqual(len(result["selected"]),9)
                self.assertEqual({s["id"] for s in result["selected"]},ALL_IDS)
                self.assertEqual(result["deferred_matches"],[])
                self.assertTrue(all(s["participation"]=="SCOPE_CHECK_ONLY" for s in result["selected"]))
                self.assertFalse(result["can_mutate_ad_accounts"])
                self.assertEqual(result["execution_state"],"NOT_EXECUTED_PLANNING_ONLY")

    def test_global_task_adds_material_ads_scope_but_keeps_all_nine(self):
        p=plan("tüm ajanları çalıştır, Drag&Drop Meta Ads Pixel Purchase kontrolü yap")
        self.assertTrue(p["global_invocation"])
        self.assertTrue(p["parent_agent_included"])
        self.assertEqual(p["workstreams"],9)
        self.assertEqual(set(p["selected_skill_ids"]),ALL_IDS)
        self.assertIn("meta-ads",p["material_skill_ids"])
        self.assertIn("analytics-attribution",p["material_skill_ids"])
        self.assertGreater(len(p["scope_check_only_skills"]),0)
        self.assertTrue(all(s["status"]=="NOT_STARTED" for s in p["stages"] if s["type"]=="skill_workstream"))
        self.assertFalse(p["parallel_model_work_executed"])
        self.assertFalse(p["provider_receipt_verified"])
        self.assertFalse(p["independent_qa_done"])
        self.assertEqual(p["gates"]["ads_account_write"],"BLOCKED")
        self.assertEqual(p["gates"]["first_touch_email"],"BLOCKED")

    def test_non_ads_global_task_still_includes_scope_checks(self):
        p=plan("Vinterro One çalıştır, Shopify menü hatasını incele")
        self.assertTrue(p["global_invocation"])
        self.assertEqual(p["workstreams"],9)
        self.assertEqual(p["scope_check_only_skills"],sorted(p["scope_check_only_skills"],key=lambda x:next(i for i,s in enumerate(DATA["skills"]) if s["id"]==x)))
        self.assertTrue(all(s["status"]=="NOT_STARTED" for s in p["stages"] if s["type"]=="skill_workstream"))
        self.assertFalse(p["campaign_data_read_from_accounts"])

    def test_normal_reklam_request_stays_qualified_and_capped(self):
        result=route("Meta Ads Pixel Purchase CAPI ve reklam kreatifleri analizi")
        self.assertFalse(result["global_invocation"])
        self.assertLessEqual(len(result["selected"]),3)
        self.assertIn("meta-ads",{x["id"] for x in result["selected"]})
        self.assertIn("analytics-attribution",{x["id"] for x in result["selected"]})
        self.assertTrue(all(s["participation"]=="MATERIAL_WORKSTREAM" for s in result["selected"]))

    def test_complicated_normal_task_still_exposes_deferred(self):
        s="Google Ads Meta Ads Pinterest kreatif tasarım GA4 Purchase bütçe KVKK Japonya Shopee"
        r=route(s)
        self.assertFalse(r["global_invocation"])
        self.assertLessEqual(len(r["selected"]),3)
        self.assertTrue(r["deferred_matches"])
        self.assertTrue(plan(s)["scope_split_recommended"])

    def test_global_calls_never_create_new_agent_identity(self):
        self.assertEqual(DATA["global_invocation"]["include_parent_agent"],"Reklam Ajansı")
        self.assertEqual(DATA["global_invocation"]["subskills_count"],9)
        self.assertEqual(DATA["legacy_agents_archived"],4)
        self.assertEqual(DATA["total_runtime_agent_identities_created"],0)
        self.assertFalse(DATA["global_invocation"]["ad_account_mutation_authority"])
        self.assertTrue(DATA["global_invocation"]["independent_qa_required"])

    def test_explicit_global_publish_request_remains_approval_blocked(self):
        p=plan("tüm ajanları çalıştır ve Meta reklam kampanyasını yayınla, bütçeyi artır")
        self.assertTrue(p["requested_live_mutation"])
        self.assertTrue(p["human_approval_required"])
        self.assertEqual(p["stages"][-1]["id"],"human-approval")
        self.assertIsNone(p["stages"][-1]["authorization"])
        self.assertEqual(p["gates"]["ads_account_write"],"BLOCKED")
        self.assertEqual(p["gates"]["production_release"],"BLOCKED")

    def test_multiple_language_variants_and_cli(self):
        result=subprocess.run([sys.executable,str(ROOT/"scripts/plan_reklam_ajansi_workflow.py"),
                               "Vinterro One çalıştır"],capture_output=True,check=True,text=True)
        p=json.loads(result.stdout)
        self.assertEqual(p["workstreams"],9)
        self.assertEqual(p["mode"],"PLAN_ONLY_NO_REMOTE_EFFECTS")
        self.assertFalse(p["provider_receipt_verified"])

    def test_all_contract_surfaces_tell_same_global_rule(self):
        required=[
           "AGENTS.md",
           "docs/standards/QUALIFIED_AGENT_ROUTING.md",
           "plugins/vinterro-one/skills/vinterro-one-router/SKILL.md",
           ".agents/skills/reklam-ajansi/SKILL.md",
           ".codex/agents/reklam-ajansi.toml",
           "docs/agents/REKLAM_AJANSI.md",
           "docs/agents/REKLAM_AJANSI_EVIDENCE_WORKFLOW.md",
        ]
        for rel in required:
            with self.subTest(path=rel):
                content=(ROOT/rel).read_text(encoding="utf8")
                self.assertIn("Vinterro One çalıştır",content)
                self.assertIn("tüm ajanları çalıştır",content)
                self.assertIn("Reklam Ajansı",content)
        doc=(ROOT/"AGENTS.md").read_text(encoding="utf8")
        self.assertIn("nine",doc.lower())
        self.assertIn("NOT_STARTED",doc)

if __name__=="__main__":
    unittest.main()
