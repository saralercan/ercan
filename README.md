# Ercan OS Control Plane

Shared agent standards, trusted-upstream policy and reusable GitHub Actions for Ercan AI Agency projects.

## What agents must read
1. `AGENTS.md`
2. `docs/standards/AGENT_ENGINEERING.md`
3. Relevant domain standard(s)
4. Project-local rules/context

## Standards
- `PLATFORM_ENGINEERING.md` — Shopify + WordPress production engineering
- `BRAND_SOCIAL.md` — brand, graphic design, Instagram organic/paid, logo and export QA
- `UPSTREAM_TOOLCHAIN.md` — GitHub upstream adoption, CI, security, design/code and social tooling

## Calling reusable workflows
A project repository can create a small caller workflow and pin this repository to a reviewed commit SHA/tag/ref according to its governance policy.

### Shopify example
```yaml
name: Shopify Quality
on: [pull_request]

jobs:
  quality:
    uses: saralercan/ercan/.github/workflows/reusable-shopify-quality.yml@<reviewed-ref>
    with:
      theme_root: .
      base_ref: main
```

### WordPress example
```yaml
name: WordPress Quality
on: [pull_request]

jobs:
  quality:
    uses: saralercan/ercan/.github/workflows/reusable-wordpress-quality.yml@<reviewed-ref>
    with:
      php_command: composer run phpcs
      e2e_command: npm run test:e2e
```

### Generic web example
```yaml
name: Web Quality
on: [pull_request]

jobs:
  quality:
    uses: saralercan/ercan/.github/workflows/reusable-web-quality.yml@<reviewed-ref>
    with:
      e2e_command: npm run test:e2e
      accessibility_command: npm run test:a11y
      performance_command: npm run test:performance
```

### Creative/social pipeline example
```yaml
name: Creative Quality
on: [pull_request]

jobs:
  quality:
    uses: saralercan/ercan/.github/workflows/reusable-creative-quality.yml@<reviewed-ref>
    with:
      export_test_command: npm run test:exports
      render_command: npm run render:smoke
      visual_command: npm run test:visual
```

## Project adoption pattern
Each project should keep a small local `AGENTS.md` that references this central contract and then adds only project-specific context, brand rules, architecture, do-not-touch constraints, current decisions and task ledger. Do not copy the whole central standard into every repository; centralize stable rules and keep project-local deltas local.

## Completion model
Use explicit states: `VERIFIED`, `PARTIAL`, `BLOCKED`, `NOT VERIFIED`.
A successful build or API response alone is not user-experience verification.
