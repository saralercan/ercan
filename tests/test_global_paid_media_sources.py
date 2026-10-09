"""Vinterro global advertising academy source integrity and unearned-certification safeguards."""
from pathlib import Path
from urllib.parse import urlparse
import json
import unittest

ROOT=Path(__file__).resolve().parents[1]
PACK=json.loads((ROOT/"docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json").read_text(encoding="utf-8"))
TEXT=(ROOT/"docs/academy/VINTERRO_GLOBAL_PAID_MEDIA_ACADEMY_TR.md").read_text(encoding="utf-8")

class WorldAdvertisingSources(unittest.TestCase):
    def test_geographical_and_linguistic_coverage(self):
        s=PACK["sources"]
        self.assertEqual(len(s),35)
        self.assertGreaterEqual(len({x["region"] for x in s}),15)
        langs={l for x in s for l in x["languages"]}
        for l in ("ja","ko","zh","ru","pt-BR","es-419","ar","de","fr","en"):
            self.assertIn(l,langs)

    def test_only_distinct_credible_urls(self):
        s=PACK["sources"]
        self.assertEqual(len({x["url"] for x in s}),len(s))
        self.assertEqual(len({x["id"] for x in s}),len(s))
        for x in s:
            u=urlparse(x["url"])
            self.assertEqual(u.scheme,"https")
            self.assertTrue(u.netloc)
            self.assertTrue(x["limitation"] and x["lesson"])
            self.assertIn(x["authority_tier"],(1,2,3))
            self.assertFalse(x["training_passed"])

    def test_important_native_platforms(self):
        h={urlparse(x["url"]).hostname for x in PACK["sources"]}
        for x in ("www.lycbiz.com","ads.naver.com","business.kakao.com",
                  "yard.yandex.ru","academy.mercadoads.com","ads.shopee.sg",
                  "seller.flipkart.com","ads.tiktok.com"):
            self.assertIn(x,h)

    def test_mathematically_cautious_research(self):
        ids={x["id"]:x for x in PACK["sources"]}
        for key in ("GL32","GL33","GL34","GL35"):
            self.assertIn(key,ids)
        self.assertIn("not universally transferable",ids["GL34"]["limitation"])
        self.assertIn("not store-level lift",ids["GL35"]["limitation"])

    def test_no_fake_worldwide_exhaustiveness(self):
        self.assertIn("not exhaustive",PACK["coverage"])
        self.assertFalse(PACK["default_read_only"] is False)
        self.assertEqual(PACK["model_exam_passes"],0)
        self.assertEqual(PACK["certificates_awarded"],0)

    def test_all_fourteen_exam_cases_have_sources_and_review(self):
        self.assertEqual(len(PACK["exams"]),14)
        ids={x["id"] for x in PACK["sources"]}
        for case in PACK["exams"]:
            self.assertTrue(set(case["source_ids"])<=ids)
            self.assertTrue(case["independent_review"])
            self.assertEqual(case["pass_status"],"PENDING_EXECUTOR")
            self.assertIn("unapproved spend",case["forbidden"])

    def test_turkish_pedagogy_and_limitations(self):
        for term in ("Japonya","Güney Kore","Çin","Rusça","Latin Amerika","Avustralya","MENA","henüz"):
            self.assertIn(term,TEXT)
        self.assertIn("kampanya yayınlama",TEXT)

if __name__=="__main__":
    unittest.main()
