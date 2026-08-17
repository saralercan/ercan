# Hostinger + WordPress Deployment Standard

This standard applies to Ercan OS projects hosted on Hostinger with WordPress/PHP/static code. It supplements `PLATFORM_ENGINEERING.md`; it does not replace WordPress-native engineering rules.

## Source of truth
- GitHub is the preferred versioned source of truth for custom theme/plugin/source code.
- WordPress database/media/content are environment data and are not reconstructed from Git source alone.
- Never commit credentials, `wp-config.php` secrets, database dumps containing private data, generated caches, or uploads unless an explicit secure archival process exists.
- Hostinger hPanel Git deployment officially supports PHP, WordPress and custom static projects on eligible web/cloud hosting plans; exact plan capability must be checked at runtime.

## Deployment model
1. inspect live + current source state;
2. reconcile any hPanel/File Manager/admin edits before overwriting;
3. create branch/PR;
4. run platform lint/tests/browser QA;
5. deploy to WordPress staging when available;
6. verify front end + wp-admin + forms/custom functionality;
7. take/confirm rollback point or backup appropriate to risk;
8. deploy production;
9. run post-deploy smoke and compare with acceptance criteria.

Direct production edits are emergency-only and must be reconciled back to Git immediately.

## WordPress boundaries
- Never edit WordPress core.
- Prefer custom plugin/hooks for persistent business logic and theme/child theme/block theme for presentation.
- Third-party plugin/theme vendor source is not a durable customization surface unless the project explicitly owns/forks it.
- Use WPCS/PHPCS and task-relevant PHPCompatibility/security checks.
- Use `wp-env` or an equivalent reproducible environment where practical; browser QA remains Playwright-first.
- Staging is the default verification surface for material WordPress changes where the Hostinger plan supports staging.

## Hostinger boundaries
- Hostinger account username/site identity must be read from the connected account; never guess it.
- Hostinger write/destructive operations follow the Hostinger connector confirmation policy.
- Do not use Hostinger Horizons tooling as a substitute for regular Hostinger WordPress/hosting management.
- Git deployment root/branch must match the actual project structure; a WordPress repo may represent a whole installation, a custom theme/plugin, or a deploy package. Determine this before linking hPanel Git.
- Do not connect a repository to production if doing so would overwrite unmanaged live files without a migration/reconciliation plan.

## Recommended repository shape for managed WordPress projects
```text
AGENTS.md
PROJECT.md
README.md
composer.json / package.json   # if used
src/ or plugin/theme source
assets/
tests/
playwright/
.github/workflows/
docs/
```
For a theme/plugin-only repo, keep the deployable package isolated from docs/tests/tooling when Hostinger deploy path requires it.

## Release gate
A material WordPress/Hostinger release is `VERIFIED` only when the selected risk-appropriate checks pass: PHPCS/WPCS, build, unit/integration, activation/runtime smoke, Playwright critical flows, responsive/visual QA, console/network review, security checks, staging verification, rollback readiness and post-production smoke.

## GitHub ↔ Hostinger
Use Hostinger's current official GitHub/Git deployment flow for eligible WordPress/PHP sites. Hostinger features, plan support and deployment UI are volatile runtime facts and must be checked from current official Hostinger docs/account state before changing deployment configuration.
