"""Static regression checks for mail/outreach agent routing and fail-closed runtime policies."""
from __future__ import annotations

import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GATE = "outreach_first_touch_release_gate"
VIN = "VINTERRO_OUTREACH_CANONICAL_TEMPLATE.html"
DD = "DRAGDROP_OUTREACH_CANONICAL_TEMPLATE.html"


def content(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


class OutreachAgentPolicies(unittest.TestCase):
    def test_root_contract_requires_live_open(self):
        s = content("AGENTS.md")
        self.assertIn(GATE, s)
        self.assertIn("OPEN", s)
        self.assertIn("do not send", s)
        self.assertIn("direct Gmail", s)

    def test_codex_role_files_are_parseable_toml(self):
        for path in [
            ".codex/agents/vinterro-outreach.toml",
            ".codex/agents/vinterro-mail-agent.toml",
            ".codex/agents/dragdrop-outreach.toml",
        ]:
            with self.subTest(path=path):
                parsed = tomllib.loads(content(path))
                self.assertIn("developer_instructions", parsed)

    def test_vinterro_codex_roles_enforce_gate(self):
        for path in [
            ".codex/agents/vinterro-outreach.toml",
            ".codex/agents/vinterro-mail-agent.toml",
        ]:
            with self.subTest(path=path):
                s = content(path)
                self.assertIn(GATE, s)
                self.assertIn("OPEN", s)
                self.assertIn("direct Gmail", s)

    def test_vinterro_outreach_role_sources_exact_shell(self):
        s = content(".codex/agents/vinterro-outreach.toml")
        self.assertIn(VIN, s)
        self.assertIn("ONLY allowed outreach shell", s)

    def test_dragdrop_codex_role_sources_exact_shell(self):
        s = content(".codex/agents/dragdrop-outreach.toml")
        self.assertIn("6. docs/standards/" + DD, s)
        self.assertNotIn("6. docs/standards/DRAGDROP_MAIL_CANONICAL_TEMPLATE.html", s)

    def test_dragdrop_first_touch_skill_sources_only_outreach(self):
        s = content(".agents/skills/dragdrop-outreach-intro/SKILL.md")
        self.assertIn(DD, s)
        self.assertNotIn("DRAGDROP_MAIL_CANONICAL_TEMPLATE.html", s)

    def test_generic_vs_cold_differentiate_sources(self):
        for path,token in [
            ("docs/standards/VINTERRO_MAIL_AGENT.md", VIN),
            ("docs/standards/DRAGDROP_MAIL_AGENT.md", DD),
            (".agents/skills/vinterro-mail-agent/SKILL.md", VIN),
            (".agents/skills/dragdrop-mail-agent/SKILL.md", DD),
        ]:
            with self.subTest(path=path):
                self.assertIn(token, content(path))

    def test_vinterro_nonconforming_connector_block_explicit(self):
        s=content("docs/standards/VINTERRO_MAIL_AGENT.md")
        self.assertIn("Direct Gmail access is not an exception", s)
        self.assertIn("BLOCKED", s)
        self.assertIn("Only after an explicitly QA-approved release state", s)


if __name__ == "__main__":
    unittest.main()
