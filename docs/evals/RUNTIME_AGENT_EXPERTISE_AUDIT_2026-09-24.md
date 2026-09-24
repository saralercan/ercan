# Vinterro One — 89-Agent Runtime Expertise Audit

Date: 2026-09-24
Scope: live production `ercan_os_agents` inventory + continual-expertise plane

## Interpretation

- `CURRENT`: at least one non-expired verified learning event exists and authority sources are mapped.
- `READY_TO_LEARN`: source map is present, but the agent has not yet completed a fresh verified learning cycle.
- Source count is not a skill score. It measures available evidence routes, not expertise by itself.
- Every material task triggers JIT current-source research through `AGENT_CONTINUAL_EXPERTISE_ENGINE.md`; agents must not wait for a scheduled refresh when the task depends on volatile facts.

## Current summary

- Runtime agents: **89/89**
- CURRENT: **3**
- READY_TO_LEARN: **86**
- Registered source routes: **3140** agent-source links
- Authority source routes: **2360**
- Verified learning events: **23**

Shopify received the first deep refresh in this expansion and is CURRENT across `Shopify Agent`, `Shopify Theme Developer`, and `Shopify Web Builder Intelligence Agent`. Other agents remain READY_TO_LEARN until they complete an actual source-backed learning cycle; this is intentional claim discipline.

## 1→89 expertise inventory

| # | Agent | Role | Source packs | Refresh | Sources / authority | Verified learning | State |
|---:|---|---|---|---:|---:|---:|---|
| 1 | Content Agent | web_research | seo, content_editorial, agent_runtime, research | 14d | 51 / 38 | 0 | READY_TO_LEARN |
| 2 | Developer Agent | web_research | seo, web_engineering, agent_runtime, research | 14d | 51 / 39 | 0 | READY_TO_LEARN |
| 3 | DevOps Agent | web_research | seo, devops, agent_runtime, research | 14d | 56 / 43 | 0 | READY_TO_LEARN |
| 4 | Graphic Agent | web_research | seo, design, agent_runtime, research | 14d | 53 / 41 | 0 | READY_TO_LEARN |
| 5 | Orchestrator | research | seo, agent_runtime, research | 7d | 38 / 24 | 0 | READY_TO_LEARN |
| 6 | QA Agent | web_research | seo, qa, agent_runtime, research | 14d | 50 / 37 | 0 | READY_TO_LEARN |
| 7 | Research Agent | research | seo, agent_runtime, research | 7d | 40 / 24 | 0 | READY_TO_LEARN |
| 8 | SEO/GEO Agent | web_research | seo, agent_runtime, research | 14d | 40 / 28 | 0 | READY_TO_LEARN |
| 9 | Shopify Agent | web_research | shopify, seo, agent_runtime, research | 1d | 73 / 60 | 11 | CURRENT |
| 10 | WordPress Agent | web_research | wordpress, seo, agent_runtime, research | 14d | 66 / 52 | 0 | READY_TO_LEARN |
| 11 | Discovery Agent | discovery | agent_runtime, local_discovery | 7d | 29 / 21 | 0 | READY_TO_LEARN |
| 12 | Event Agent | event | agent_runtime, local_discovery | 7d | 29 / 21 | 0 | READY_TO_LEARN |
| 13 | Keşif Editorial Agent | editorial | content_editorial, agent_runtime, local_discovery | 7d | 34 / 24 | 0 | READY_TO_LEARN |
| 14 | Keşif QA Agent | qa | qa, agent_runtime, local_discovery | 7d | 39 / 29 | 0 | READY_TO_LEARN |
| 15 | Keşif SEO/GEO Agent | seo | seo, agent_runtime, local_discovery | 7d | 37 / 27 | 0 | READY_TO_LEARN |
| 16 | Venue Agent | venue | agent_runtime, local_discovery | 7d | 29 / 21 | 0 | READY_TO_LEARN |
| 17 | Vinterro Keşif Agent | vinterro_kesif_lead | agent_runtime, local_discovery | 7d | 29 / 21 | 0 | READY_TO_LEARN |
| 18 | City Discovery Agent | city_discovery | agent_runtime, local_discovery | 7d | 29 / 21 | 0 | READY_TO_LEARN |
| 19 | Geo Enrichment Agent | geo_enrichment | agent_runtime, local_discovery | 7d | 33 / 25 | 0 | READY_TO_LEARN |
| 20 | National SEO/GEO Agent | national_seo | seo, agent_runtime, local_discovery | 7d | 37 / 27 | 0 | READY_TO_LEARN |
| 21 | Place Deduplication Agent | place_dedup | agent_runtime, local_discovery | 7d | 29 / 21 | 0 | READY_TO_LEARN |
| 22 | Place Intelligence Agent | place_intelligence | agent_runtime, local_discovery | 7d | 29 / 21 | 0 | READY_TO_LEARN |
| 23 | Source Verification Agent | source_verification | agent_runtime, local_discovery | 7d | 32 / 22 | 0 | READY_TO_LEARN |
| 24 | Türkiye Expansion Lead | turkey_expansion | local_discovery | 7d | 17 / 11 | 0 | READY_TO_LEARN |
| 25 | GitHub Trending Intelligence Agent | github_trending | seo, agent_runtime, research | 7d | 40 / 24 | 0 | READY_TO_LEARN |
| 26 | Accessibility Agent | web_research | seo, qa, agent_runtime, research | 14d | 51 / 38 | 0 | READY_TO_LEARN |
| 27 | GitHub Web Intelligence Agent | github_intelligence | seo, agent_runtime, research | 7d | 40 / 24 | 0 | READY_TO_LEARN |
| 28 | Motion & Glass Agent | web_research | seo, design, agent_runtime, research | 14d | 53 / 41 | 0 | READY_TO_LEARN |
| 29 | Performance Agent | web_research | seo, qa, agent_runtime, research | 14d | 50 / 37 | 0 | READY_TO_LEARN |
| 30 | Pinterest Design Intelligence Agent | web_research | seo, design, agent_runtime, research | 14d | 59 / 47 | 0 | READY_TO_LEARN |
| 31 | PixelMatch Agent | web_research | seo, qa, agent_runtime, research | 14d | 50 / 37 | 0 | READY_TO_LEARN |
| 32 | Responsive QA Agent | web_research | seo, qa, agent_runtime, research | 14d | 50 / 37 | 0 | READY_TO_LEARN |
| 33 | ScreenshotToCode Agent | web_research | seo, agent_runtime, research | 14d | 46 / 35 | 0 | READY_TO_LEARN |
| 34 | Security & License Agent | web_research | seo, security, agent_runtime, research | 14d | 62 / 49 | 0 | READY_TO_LEARN |
| 35 | Shopify Web Builder Intelligence Agent | web_research | shopify, seo, agent_runtime, research | 14d | 78 / 63 | 6 | CURRENT |
| 36 | UI Systems Agent | web_research | seo, agent_runtime, research | 14d | 46 / 35 | 0 | READY_TO_LEARN |
| 37 | Web Asset Curator Agent | web_research | seo, agent_runtime, research | 14d | 46 / 35 | 0 | READY_TO_LEARN |
| 38 | Web SEO/GEO Intelligence Agent | web_research | seo, agent_runtime, research | 14d | 46 / 35 | 0 | READY_TO_LEARN |
| 39 | WordPress Web Builder Intelligence Agent | web_research | wordpress, seo, agent_runtime, research | 14d | 66 / 52 | 0 | READY_TO_LEARN |
| 40 | Analytics & Attribution Agent | web_research | seo, analytics, agent_runtime, research | 14d | 57 / 45 | 0 | READY_TO_LEARN |
| 41 | Brand Systems Agent | web_research | seo, design, agent_runtime, research | 14d | 53 / 41 | 0 | READY_TO_LEARN |
| 42 | Content Distribution Agent | web_research | seo, content_editorial, agent_runtime, research | 14d | 51 / 38 | 0 | READY_TO_LEARN |
| 43 | Conversion & CRO Agent | web_research | ecommerce, seo, agent_runtime, research | 14d | 62 / 50 | 0 | READY_TO_LEARN |
| 44 | Creative QA & Brand Consistency Agent | web_research | seo, qa, design, agent_runtime | 14d | 48 / 37 | 0 | READY_TO_LEARN |
| 45 | Local SEO & Merchant Agent | web_research | ecommerce, seo, agent_runtime, research | 14d | 56 / 44 | 0 | READY_TO_LEARN |
| 46 | Marketing Compliance Agent | web_research | seo, growth_ads, agent_runtime, research | 14d | 60 / 47 | 0 | READY_TO_LEARN |
| 47 | Paid Media Intelligence Agent | web_research | seo, growth_ads, agent_runtime, research | 14d | 60 / 47 | 0 | READY_TO_LEARN |
| 48 | SEO Meta & Schema Agent | web_research | seo, agent_runtime, research | 14d | 46 / 35 | 0 | READY_TO_LEARN |
| 49 | Social Creative Agent | web_research | seo, growth_ads, agent_runtime, research | 14d | 60 / 47 | 0 | READY_TO_LEARN |
| 50 | Social Media Intelligence Agent | web_research | seo, growth_ads, agent_runtime, research | 14d | 60 / 47 | 0 | READY_TO_LEARN |
| 51 | Campaign Creative Intelligence Agent | web_research | seo, growth_ads, agent_runtime, research | 14d | 60 / 47 | 0 | READY_TO_LEARN |
| 52 | Competitive & Trend Intelligence Agent | web_research | seo, agent_runtime, research | 14d | 49 / 36 | 0 | READY_TO_LEARN |
| 53 | Growth & Brand Orchestrator | web_research | seo, design, agent_runtime, research | 14d | 53 / 41 | 0 | READY_TO_LEARN |
| 54 | Marketing Source Discovery Agent | web_research | seo, growth_ads, agent_runtime, local_discovery | 14d | 62 / 48 | 0 | READY_TO_LEARN |
| 55 | Social Preview & OG Agent | web_research | seo, growth_ads, agent_runtime, research | 14d | 60 / 47 | 0 | READY_TO_LEARN |
| 56 | Agent Health Agent | agent_health | agent_runtime | 7d | 30 / 23 | 0 | READY_TO_LEARN |
| 57 | Agent Lifecycle Agent | agent_lifecycle | agent_runtime | 7d | 30 / 23 | 0 | READY_TO_LEARN |
| 58 | Asset Discovery Agent | asset_discovery | agent_runtime, local_discovery | 7d | 37 / 27 | 0 | READY_TO_LEARN |
| 59 | Capability Risk Agent | capability_risk | security, agent_runtime | 7d | 37 / 29 | 0 | READY_TO_LEARN |
| 60 | CI Failure Investigator Agent | ci_failure_investigator | devops, agent_runtime | 7d | 37 / 27 | 0 | READY_TO_LEARN |
| 61 | Deterministic Hook Agent | deterministic_hook | agent_runtime | 7d | 20 / 17 | 0 | READY_TO_LEARN |
| 62 | Durable Workflow Agent | durable_workflow | agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 63 | Egress Guard Agent | egress_guard | security, agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 64 | Handoff Guard Agent | handoff_guard | agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 65 | Human Approval Agent | human_approval | agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 66 | Issue Triage Agent | issue_triage | agent_runtime | 7d | 7 / 3 | 0 | READY_TO_LEARN |
| 67 | Language Freshness Agent | language_freshness | javascript, agent_runtime | 7d | 8 / 4 | 0 | READY_TO_LEARN |
| 68 | MCP Risk Scanner Agent | mcp_risk_scanner | security, agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 69 | Policy Engine Agent | policy_engine | security, agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 70 | Repo Automation Agent | repo_automation | devops, agent_runtime | 7d | 7 / 3 | 0 | READY_TO_LEARN |
| 71 | Runtime Guard Agent | runtime_guard | agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 72 | Sandbox Worker Agent | sandbox_worker | security, agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 73 | Supply Chain Guard Agent | supply_chain_guard | security, agent_runtime | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 74 | Browser QA | browser_verification | qa | 14d | 10 / 7 | 0 | READY_TO_LEARN |
| 75 | Content & SEO Editor | content_seo | seo, content_editorial | 21d | 7 / 4 | 0 | READY_TO_LEARN |
| 76 | Creative Director | art_direction | web_engineering | 21d | 10 / 7 | 0 | READY_TO_LEARN |
| 77 | Debugger | root_cause_fix | web_engineering | 14d | 10 / 7 | 0 | READY_TO_LEARN |
| 78 | Deploy Guardian | deploy_gate | devops | 7d | 7 / 3 | 0 | READY_TO_LEARN |
| 79 | Firebase Engineer | firebase_engineering | web_engineering | 14d | 10 / 7 | 0 | READY_TO_LEARN |
| 80 | Next.js + Supabase Engineer | nextjs_supabase_engineering | web_engineering | 14d | 10 / 7 | 0 | READY_TO_LEARN |
| 81 | Project Mapper | repo_discovery | local_discovery | 14d | 10 / 7 | 0 | READY_TO_LEARN |
| 82 | QA Auditor | release_qa_gate | qa | 7d | 7 / 3 | 0 | READY_TO_LEARN |
| 83 | Security Auditor | security_review | security | 7d | 11 / 8 | 0 | READY_TO_LEARN |
| 84 | Shopify Theme Developer | shopify_engineering | shopify, web_engineering | 14d | 27 / 24 | 6 | CURRENT |
| 85 | Social Media Director | social_media | growth_ads | 21d | 9 / 6 | 0 | READY_TO_LEARN |
| 86 | UI/UX Director | ui_ux_review | design | 21d | 10 / 7 | 0 | READY_TO_LEARN |
| 87 | WordPress Plugin Developer | wordpress_engineering | wordpress, web_engineering | 14d | 10 / 7 | 0 | READY_TO_LEARN |
| 88 | E-commerce Expert Agent | ecommerce_expert | ecommerce, agent_runtime | 7d | 41 / 38 | 0 | READY_TO_LEARN |
| 89 | Finance Expert Agent | finance_expert | finance, agent_runtime | 30d | 9 / 6 | 0 | READY_TO_LEARN |

## Completion policy

`READY_TO_LEARN` is not a failure. It means the agent has a qualified curriculum/source map but still owes a fresh behavioral learning pass. The runtime automatically injects the ACTIVE pod's authority-source context and forces current research for material work. A specialist moves toward `CURRENT` only through verified learning, not by changing a label.

## Next learning waves

Prioritize by execution frequency and volatility:
1. WordPress / frontend / JavaScript / QA / security / SEO.
2. E-commerce / analytics / paid media / social / brand/design.
3. Finance / DevOps / agent-runtime governance.
4. Local discovery / editorial / mapping / national SEO.

Each wave uses the same cycle: discover broadly → qualify authority → distill → apply → deterministic/independent QA → record learning → expire/recheck.
