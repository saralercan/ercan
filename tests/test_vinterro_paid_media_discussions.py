from pathlib import Path
import unittest

DOC=(Path(__file__).resolve().parents[1]/"docs/academy/PAID_MEDIA_PUBLIC_DISCUSSION_CASES_2026.md").read_text(encoding="utf8").lower()

class PaidMediaPublicDiscussions(unittest.TestCase):
    def test_public_verifiable_cases(self):
        self.assertIn("https://github.com/facebookexperimental/robyn/issues/789",DOC)
        self.assertIn("https://github.com/facebookexperimental/robyn/issues/1034",DOC)

    def test_community_not_policy_or_proven_experiment(self):
        self.assertIn("tier 5",DOC)
        self.assertIn("doğrulanmış genel sonuç değildir",DOC)
        self.assertIn("bağımsız qa",DOC)

    def test_cases_do_not_autonomously_grant_budget(self):
        self.assertIn("bütçe değiştirmek yasak",DOC)
        self.assertIn("gerçek yürütücü sınavı pending",DOC)

if __name__=="__main__":
    unittest.main()
