"""Research academy QA: provenance, breadth, risk rules, credible evaluation."""
import json
from pathlib import Path
from urllib.parse import urlsplit
import unittest

ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/"docs/academy/PAID_MEDIA_RESEARCH_CURRICULUM_2026.json").read_text(encoding="utf-8"))
GUIDE=(ROOT/"docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md").read_text(encoding="utf-8")

class PaidMediaAcademyQA(unittest.TestCase):
    def test_research_is_not_certification(self):
        self.assertEqual(DATA["status"],"RESEARCH_CURATED_NOT_AGENT_CERTIFIED")
        self.assertEqual(DATA["policy"]["learning_event_status"],"curated_not_verified")
        self.assertEqual(DATA["policy"]["evaluation_status"],"PENDING_REAL_AGENT_RUN")
        self.assertIn("henüz",GUIDE.lower())

    def test_source_depth_and_unique_valid_links(self):
        sources=DATA["sources"]
        self.assertGreaterEqual(len(sources),30)
        self.assertEqual(len({s["url"] for s in sources}),len(sources))
        self.assertEqual(len({s["id"] for s in sources}),len(sources))
        for s in sources:
            p=urlsplit(s["url"])
            self.assertEqual(p.scheme,"https")
            self.assertTrue(p.netloc)
            self.assertIn(s["tier"],[1,2,3,4])
            self.assertTrue(s["lesson"] and s["limitation"])
            self.assertGreater(s["freshness_days"],0)

    def test_cross_source_tiers(self):
        kinds={s["kind"] for s in DATA["sources"]}
        self.assertGreaterEqual(len([s for s in DATA["sources"] if s["kind"]=="official"]),15)
        self.assertTrue({"canonical_repo","peer_reviewed","preprint","thesis","official","reviewed_secondary"}<=kinds)

    def test_five_specialties_cover_all_sources(self):
        roles={"paid","creative","growth","compliance","discovery"}
        seen=set()
        for s in DATA["sources"]:
            self.assertTrue(set(s["roles"])<=roles)
            seen.update(s["roles"])
        self.assertEqual(seen,roles)

    def test_12_modules_are_wired_to_real_sources(self):
        ids={s["id"] for s in DATA["sources"]}
        self.assertEqual(len(DATA["curriculum"]),12)
        self.assertEqual(len({m["id"] for m in DATA["curriculum"]}),12)
        for m in DATA["curriculum"]:
            self.assertTrue(set(m["sources"])<=ids)
            self.assertGreaterEqual(len(m["focus"]),3)
            self.assertTrue(m["exam"])

    def test_12_cases_have_explicit_fail_rules(self):
        self.assertEqual(len(DATA["evaluations"]),12)
        self.assertEqual(len({e["id"] for e in DATA["evaluations"]}),12)
        for x in DATA["evaluations"]:
            self.assertTrue(x["required"])
            self.assertTrue(x["forbidden"])

    def test_hard_stop_on_spend_and_fabrication(self):
        policy=DATA["policy"]
        self.assertEqual(policy["read_only_default"],True)
        self.assertIn("publish",policy["approval_required_for"])
        self.assertIn("budget_change",policy["approval_required_for"])
        self.assertTrue(policy["no_fabricated_performance"])
        self.assertTrue(policy["no_certification_claims"])
        self.assertEqual(policy["mail_release_gate"],"BLOCKED")

    def test_critical_scenarios_caught(self):
        c={e["id"]:e for e in DATA["evaluations"]}
        for i in ("ad01","ad02","ad06","ad08","ad09"):
            self.assertEqual(c[i]["risk"],"critical")

if __name__=="__main__":
    unittest.main()
