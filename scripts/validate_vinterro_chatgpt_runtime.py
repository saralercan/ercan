#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROOT_AGENTS = ROOT / "AGENTS.md"
CHATGPT_STANDARD = ROOT / "docs/standards/CHATGPT_VINTERRO_ONE_RUNTIME.md"
PORTABLE = ROOT / "docs/standards/PORTABLE_AGENT_RUNTIME.md"
RUNTIME = ROOT / "docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
BUNDLED_RUNTIME = ROOT / "plugins/vinterro-one/skills/vinterro-one-router/references/VINTERRO_RUNTIME_AGENT_MANIFEST.json"
ROUTER = ROOT / "plugins/vinterro-one/skills/vinterro-one-router/SKILL.md"
PLUGIN = ROOT / "plugins/vinterro-one/plugin.json"
CONTROL_PLANE = ROOT / "supabase/functions/ercan-os-api/index.ts"
MCP = ROOT / "supabase/functions/vinterro-one-chatgpt-mcp/index.ts"
MCP_DENO = ROOT / "supabase/functions/vinterro-one-chatgpt-mcp/deno.json"

REQUIRED = (
    ROOT_AGENTS,
    CHATGPT_STANDARD,
    PORTABLE,
    RUNTIME,
    BUNDLED_RUNTIME,
    ROUTER,
    PLUGIN,
    CONTROL_PLANE,
    MCP,
    MCP_DENO,
)


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def main() -> int:
    failures: list[str] = []
    for path in REQUIRED:
        if not path.is_file():
            fail(f"missing ChatGPT runtime file: {path.relative_to(ROOT)}", failures)
    if failures:
        for item in failures:
            print(f"FAIL: {item}", file=sys.stderr)
        return 2

    runtime = json.loads(RUNTIME.read_text(encoding="utf-8"))
    bundled = json.loads(BUNDLED_RUNTIME.read_text(encoding="utf-8"))
    plugin = json.loads(PLUGIN.read_text(encoding="utf-8"))

    agents = runtime.get("agents") or []
    if not agents:
        fail("runtime agent manifest is empty", failures)

    incompatible = [
        a.get("name", "<unknown>")
        for a in agents
        if (a.get("adapters") or {}).get("chatgpt") is not True
        or (a.get("adapters") or {}).get("openai") is not True
    ]
    if incompatible:
        fail(f"agents missing ChatGPT/OpenAI adapters: {incompatible}", failures)

    if runtime != bundled:
        fail("ChatGPT plugin runtime mirror drifted from canonical runtime manifest", failures)

    compatibility = runtime.get("runtime_compatibility") or {}
    chatgpt = compatibility.get("chatgpt") or {}
    if chatgpt.get("supported") is not True:
        fail("runtime_compatibility.chatgpt.supported must be true", failures)
    if chatgpt.get("preferred_live_bridge") != "vinterro-one-chatgpt-mcp":
        fail("preferred ChatGPT live bridge must be vinterro-one-chatgpt-mcp", failures)

    root = ROOT_AGENTS.read_text(encoding="utf-8")
    standard = CHATGPT_STANDARD.read_text(encoding="utf-8")
    portable = PORTABLE.read_text(encoding="utf-8")
    router = ROUTER.read_text(encoding="utf-8")
    control = CONTROL_PLANE.read_text(encoding="utf-8")
    mcp = MCP.read_text(encoding="utf-8")

    for needle in (
        "ChatGPT / GPT Vinterro One hard route",
        "CHATGPT_VINTERRO_ONE_RUNTIME.md",
        "vinterro-one-chatgpt-mcp",
        "Never use the historical fixed 5/8-agent ceiling",
    ):
        if needle not in root:
            fail(f"AGENTS.md missing ChatGPT hard-route rule: {needle}", failures)

    for needle in (
        "Vinterro One ChatGPT MCP",
        "Connected Supabase app/plugin",
        "Connected GitHub / repository mirror",
        "There is **no fixed 5-agent or 8-agent ceiling**",
        "producer -> independent reviewer -> correction/retest -> applicable Release Gate",
    ):
        if needle not in standard:
            fail(f"ChatGPT runtime standard missing rule: {needle}", failures)

    for needle in (
        "ChatGPT live-connection priority",
        "Vinterro One ChatGPT MCP -> connected Supabase app/plugin -> versioned GitHub/repository mirror",
    ):
        if needle not in portable:
            fail(f"portable runtime missing ChatGPT connection rule: {needle}", failures)

    for needle in (
        "ChatGPT/OpenAI + Codex",
        "vinterro_route_task",
        "do not use a fixed 5/8-agent ceiling",
        "producer -> independent reviewer -> correction/retest -> release gate",
    ):
        if needle not in router:
            fail(f"Vinterro One router missing ChatGPT rule: {needle}", failures)

    if "const maxActive = masterMode ? 8 : 5" in control:
        fail("live control-plane source regressed to fixed 5/8-agent ceiling", failures)
    for needle in (
        "function resolveProject(",
        "projectLead",
        "no-fixed-agent-cap",
        "selectedProjectId = routing.project?.id || body.project_id || null",
        "Vinterro One Security Director",
        "Security Auditor",
    ):
        if needle not in control:
            fail(f"live control-plane source missing GPT routing rule: {needle}", failures)

    for needle in (
        "withOAuthProtectedResource()",
        "withSupabase({ auth: 'user' })",
        "createMcpHandler(() => createServer",
        "'vinterro_status'",
        "'vinterro_route_task'",
        "'vinterro_get_agent'",
        "'vinterro_get_project'",
        "'vinterro_get_supervision'",
        "/functions/v1/ercan-os-api",
        "/functions/v1/vinterro-one-supervision",
    ):
        if needle not in mcp:
            fail(f"ChatGPT MCP bridge missing contract: {needle}", failures)

    if "SUPABASE_SERVICE_ROLE_KEY" in mcp:
        fail("ChatGPT MCP bridge must not receive/use service-role credentials", failures)

    if "ChatGPT" not in str(plugin.get("description", "")):
        fail("plugin description must include ChatGPT support", failures)
    keywords = set(plugin.get("keywords") or [])
    if not {"chatgpt", "openai"}.issubset(keywords):
        fail("plugin keywords must include chatgpt and openai", failures)

    if failures:
        print("Vinterro One ChatGPT runtime validator: FAIL", file=sys.stderr)
        for item in failures:
            print(f"  - {item}", file=sys.stderr)
        return 1

    print("Vinterro One ChatGPT runtime validator: PASS")
    print(f"Portable ChatGPT/OpenAI agents: {len(agents)}/{len(agents)}")
    print("Live control-plane: dynamic project lead + no fixed pod ceiling")
    print("ChatGPT MCP: OAuth protected + user/RLS scoped + read-first")
    print("Fallbacks: Supabase app/plugin -> GitHub portable mirror")
    print("Supervision: independent review/release-gate contract present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
