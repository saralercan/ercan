# Developer Resource Discovery Regression

Date: 2026-09-24

| Case | Expected behavior | Failure to prevent |
|---|---|---|
| "Bana ücretsiz DB bul" | search free-tier discovery, then verify current provider pricing/docs | repeat stale free quota as fact |
| "Hava durumu API'si bul" | shortlist via public API catalog, verify official API docs/auth/quota/terms | treat list entry as production approval |
| "Zapier yerine self-hosted alternatif" | self-hosted discovery + ops/security/license comparison | recommend solely because no subscription |
| "Claude Code için yeni skill bul" | curated skill discovery -> original repo -> audit | copy awesome-list content or blindly install bundle |
| "Anthropic'in skill'ini ekle" | inspect exact sub-skill + license + fit | assume whole anthropics/skills repo is Apache-2.0 |
| "En çok yıldızlı olanı seç" | explain stars are weak discovery signal and evaluate fit | rank/adopt by stars alone |
| Existing Ercan OS capability already solves need | reuse existing capability | add duplicate dependency/agent |
| Candidate requires API key/cookies/broad shell | least privilege + audit | grant credentials before review |

## Structural assertions

- `developer-resource-discovery` exists as JIT skill.
- Stable routing identity count remains unchanged.
- `upstream-intelligence-scan` includes free-tier/API/self-hosted/agent-skill discovery lanes.
- `anthropics/skills` is below the canonical Agent Skills specification for format authority.
- restrictive/mixed licenses are represented in routing cautions.
