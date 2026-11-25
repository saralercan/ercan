# Agents SDK pilot (not production)

This isolated pilot checks a real OpenAI Agents SDK coordinator-to-reviewer handoff using synthetic data. It does not read or write the live queue, call external business tools, send email, or mark a production task complete.

## Verification
- Node.js 22+.
- Run `npm install --package-lock-only --ignore-scripts` and review/commit the generated lockfile before CI or deployment.
- Run `npm ci --ignore-scripts`, then `npm test`. These tests use mock SDK responses and are not evidence of live execution.
- In an authorized cloud environment, configure OPENAI_API_KEY via the secret store, OPENAI_MODEL to a model available to the account, and VINTERRO_SDK_ALLOW_PAID_SMOKE=true. Run `npm run smoke` manually. This can incur OpenAI API charges. Do not put secrets in git.
- A successful smoke is only evidence of a synthetic handoff. Provider quota, available model, runtime compatibility, trace evidence and costs must be independently verified.

## Integration gate
Only after the live smoke passes: inspect the existing authorized claim/fail/receipt contracts, implement a tenant-scoped adapter, add approved read-only tools with idempotency and budget guards, validate signed execution receipts, and test against an isolated queue. Preserve existing production workers. Do not run live queued jobs or enable side-effect tools without review. No deployment or paid infrastructure is enabled by this PR.
