"""Reklam Ajansı: one parent, nine scoped subskills, safe deterministic planning."""
from __future__ import annotations
import json
from pathlib import Path
import subprocess
import sys
import unittest
from importlib.util import module_from_spec, spec_from_file_location

ROOT=Path(__file__).resolve().parents[1]
ROUTER=ROOT/"docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json"
spec=spec_from_file_location("route_reklam_ajansi_subskills", ROOT/"scripts/route_reklam_ajansi_subskills.py")
routing=module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(routing)

DATA=json.loads(ROUTER.read_text(encoding="utf8"))

class UnifiedAgencySubSkills(unittest.TestCase):
    def test_one_parent_nine_distinct_subskills(self):
        self.assertEqual(DATA["canonical_agent_name"],"Reklam Ajansı")
        self.assertEqual(DATA["canonical_agent_id"],"b2acac02-29d7-418c-9f04-24552e947776")
        self.assertEqual(len(DATA["skills"]),9)
        self.assertEqual(len(set(s["id"] for s in DATA["skills"])),9)
        self.assertEqual(DATA["total_runtime_agent_identities_created"],0)

    def test_real_skill_files_are_readable_and_scoped(self):
        for skill in DATA["skills"]:
            path=ROOT/skill["path"]
            self.assertTrue(path.exists(),f"missing {path}")
            doc=path.read_text(encoding="utf8")
            self.assertTrue(doc.startswith("---\n"))
            self.assertIn("name: reklam-ajansi-"+skill["id"],doc)
            self.assertIn("Reklam Ajansı",doc)
            self.assertIn("alt skill",doc)
            self.assertIn("BLOCKED",doc)
            self.assertIn("bağımsız",doc.lower())
            self.assertIn("## Teslimat sözleşmesi",doc)
            self.assertIn("## Uzmanlık iş akışı",doc)

    def test_automatic_selection_for_all_fields(self):
        cases=[
            ("Google Ads arama anahtar kelime planı","google-ads"),
            ("Meta Ads reklam seti stratejisi","meta-ads"),
            ("Pinterest sponsorlu Pin fikri","paid-social-video"),
            ("Banner tasarım kreatif briefi","creative-studio"),
            ("GA4 Purchase ölçümünü incele","analytics-attribution"),
            ("Günlük bütçe dağılımını analiz et","growth-budget"),
            ("KVKK veri gizliliği ve reklam reddi","compliance-privacy"),
            ("Japonya Naver olmayan yerel reklam kaynakları","global-market-research"),
            ("Amazon Ads ve Shopee sponsored products katalog uygunluğu","retail-marketplaces"),
        ]
        for query, expected in cases:
            with self.subTest(query=query):
                ids=[x["id"] for x in routing.route(query)["selected"]]
                self.assertIn(expected,ids)

    def test_multidisciplinary_skills_are_composable(self):
        ids=[x["id"] for x in routing.route("Meta Ads Pixel Purchase event_id CAPI ölçüm")["selected"]]
        self.assertIn("meta-ads",ids)
        self.assertIn("analytics-attribution",ids)
        self.assertLessEqual(len(ids),3)

    def test_global_shopping_considers_local_retail_platforms(self):
        ids=[x["id"] for x in routing.route("Japonya pazarı için Shopee Shopping reklam uygunluğu araştır")["selected"]]
        self.assertIn("global-market-research",ids)
        self.assertIn("retail-marketplaces",ids)

    def test_no_match_falls_back_to_one_parent(self):
        result=routing.route("Yeni ekip üyeleri için toplantı notu")
        self.assertEqual(result["selected"],[])
        self.assertEqual(result["fallback_parent_skill"],"reklam-ajansi")
        self.assertEqual(result["canonical_agent"],"Reklam Ajansı")

    def test_no_phantom_execution_or_approval(self):
        result=routing.route("Meta Ads kampanyasını hemen yayınla ve bütçeyi artır")
        self.assertEqual(result["execution_state"],"NOT_EXECUTED_PLANNING_ONLY")
        self.assertFalse(result["real_parallel_workers_verified"])
        self.assertFalse(result["can_mutate_ad_accounts"])
        self.assertTrue(result["requested_live_mutation"])
        self.assertEqual(result["first_touch_email_gate"],"BLOCKED")
        self.assertEqual(result["independent_qa_state"],"REQUIRED_NOT_PERFORMED")

    def test_no_duplicate_skill_slots_or_run_authority(self):
        ids=[x["id"] for x in routing.route("Meta Pixel Purchase CAPI reklam bütçe ve kreatif")["selected"]]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertLessEqual(len(ids),DATA["orchestration"]["select_max"])
        for x in DATA["skills"]:
            self.assertEqual(x["execution_authority"],"read_research_and_approved_workspace_drafts_only")
            self.assertEqual(x["actual_run_status"],"NOT_EXECUTED")
            self.assertTrue(x["independent_reviewer_candidates"])

    def test_router_and_parent_linked_in_codex(self):
        parent=(ROOT/".agents/skills/reklam-ajansi/SKILL.md").read_text(encoding="utf8")
        codex=(ROOT/".codex/agents/reklam-ajansi.toml").read_text(encoding="utf8")
        docs=(ROOT/"docs/agents/REKLAM_AJANSI.md").read_text(encoding="utf8")
        for txt in (parent,codex,docs):
            self.assertIn("REKLAM_AJANSI_SUBSKILL_ROUTER.json",txt)
            self.assertIn("reklam-ajansi-google-ads",txt)
        self.assertIn("reklam-ajansi-meta-ads",parent)

    def test_cli_json_planning(self):
        cmd=[sys.executable,str(ROOT/"scripts/route_reklam_ajansi_subskills.py"),"Google Ads PMax kampanyası planla"]
        result=subprocess.run(cmd,check=True,text=True,capture_output=True)
        data=json.loads(result.stdout)
        self.assertEqual(data["canonical_agent"],"Reklam Ajansı")
        self.assertFalse(data["can_mutate_ad_accounts"])

if __name__=="__main__":
    unittest.main()
