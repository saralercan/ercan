"""Reklam Ajansı migration source, audit preservation and routing regression."""
import json
import tomllib
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SQL=(ROOT/"supabase/reklam-ajansi-unified-five-agents-20261009.sql").read_text(encoding="utf8")
MAN=json.loads((ROOT/"docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json").read_text(encoding="utf8"))
CODEX=(ROOT/".codex/agents/reklam-ajansi.toml").read_text(encoding="utf8")
SKILL=(ROOT/".agents/skills/reklam-ajansi/SKILL.md").read_text(encoding="utf8")
MASTER=(ROOT/"docs/agents/REKLAM_AJANSI.md").read_text(encoding="utf8")
LEGACY=("Paid Media Intelligence Agent","Campaign Creative Intelligence Agent",
        "Growth & Brand Orchestrator","Marketing Compliance Agent",
        "Marketing Source Discovery Agent")

class ConsolidatedAdvertisingAgency(unittest.TestCase):
    def test_single_canonical_active_agent(self):
        selected=[a for a in MAN["agents"] if a["name"]=="Reklam Ajansı" or a["name"] in LEGACY]
        self.assertEqual(len(selected),5)
        self.assertEqual([a["name"] for a in selected if a["status"]=="active"],["Reklam Ajansı"])
        self.assertEqual(len([a for a in selected if a["status"]=="inactive"]),4)
        self.assertEqual(MAN["active_agent_count"],112)
        self.assertEqual(MAN["runtime_agent_count"],116)
        self.assertEqual(MAN["canonical_advertising_agent"]["name"],"Reklam Ajansı")

    def test_no_legacy_handoffs_in_active_registry(self):
        names=[a["name"] for a in MAN["agents"] if a["status"]=="active"]
        self.assertIn("Ayvalık Reklam Baş Uzman Ajanı",names)
        for a in MAN["agents"]:
            if a["status"]=="active":
                self.assertNotIn(a["name"],a.get("handoffs",[]))
                for former in LEGACY:
                    self.assertNotIn(former,a.get("handoffs",[]))
        orchestrator=next(a for a in MAN["agents"] if a["name"]=="Orchestrator")
        self.assertIn("Reklam Ajansı",orchestrator["handoffs"])

    def test_historical_source_records_not_deleted(self):
        self.assertIn("count(distinct source_uri)",SQL)
        self.assertIn("SINGLE_AGENT_VERIFY_FAILED",SQL)
        self.assertIn("'source_merge_mode','lossless_donor_preservation'",SQL)
        self.assertIn("on conflict (organization_id,agent_id,source_uri) do update",SQL.lower())
        self.assertNotIn("delete from public.ercan_os_agent_sources",SQL.lower())
        self.assertNotIn("delete from public.ercan_os_agent_learning_events",SQL.lower())
        self.assertNotIn("delete from public.ercan_os_agents",SQL.lower())

    def test_transaction_guards_and_scoped_rollback(self):
        self.assertIn("begin;",SQL.lower())
        self.assertIn("commit;",SQL.lower())
        self.assertIn("MERGE_REFUSED",SQL)
        self.assertIn("v_external_runs>0",SQL)
        self.assertIn("status='inactive'",SQL)
        self.assertIn("organization_id='1805532c-8bbe-4280-8164-dac244ed46b4'::uuid",SQL)
        self.assertIn("Reklam Ajansı",SQL)

    def test_new_learning_is_not_self_certified(self):
        self.assertIn("'pending_qa'",SQL)
        self.assertIn("PENDING_INDEPENDENT_REVALIDATION",SQL)
        self.assertIn("actual_live_exam_passes',0",SQL)
        self.assertIn("media_account_write_authority',false",SQL)

    def test_agent_codex_contract_and_skill(self):
        parsed=tomllib.loads(CODEX)
        self.assertIn("REKLAM AJANSI",parsed["developer_instructions"])
        self.assertIn("independent QA",parsed["developer_instructions"])
        self.assertIn("FIRST",parsed["developer_instructions"].upper())
        self.assertIn("Reklam Ajansı",SKILL)
        self.assertIn("blocked",SKILL.lower())
        self.assertIn("b2acac02-29d7-418c-9f04-24552e947776",MASTER)

    def test_live_campaign_and_billing_are_still_blocked(self):
        canon=MAN["canonical_advertising_agent"]
        self.assertFalse(canon["media_mutation_permission"])
        self.assertEqual(canon["qualification_exams_passed"],0)
        self.assertEqual(canon["real_model_executions"],0)
        lead=next(a for a in MAN["agents"] if a["name"]=="Reklam Ajansı")
        self.assertNotIn("campaign.publish",lead["permissions"])
        self.assertNotIn("ads.modify",lead["permissions"])
        self.assertIn("QA Agent",lead["handoffs"])

if __name__=="__main__":
    unittest.main()
