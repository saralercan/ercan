# Drag&Drop — Single Existing Shopify Draft Theme (Operator Lock)
Effective: 2026-10-13. Scope: Drag&Drop Shopify storefront at `www.draganddrop.tr` and all Vinterro One / Codex / project agents working on its theme.

## Only authorized theme for edits
- Theme name: **DD Kurumsal Siparisler Fotograflar 2026-10-12**
- Numeric theme ID: **198480756902**
- GraphQL ID: `gid://shopify/OnlineStoreTheme/198480756902`
- Required role before write: **UNPUBLISHED**.
- The `MAIN` theme is production-only and must remain unchanged until a separate explicit user instruction to publish.

## Immutable operation rules until changed explicitly by the operator
1. **Never create, duplicate, copy, import, upload or generate another Shopify theme**, whether called backup, QA, test, development, migration, preview, staging or draft. Do not run `themeDuplicate`, `themeCreate`, CLI `theme push --unpublished` or other equivalent theme-creation workflows.
2. All permitted Shopify theme changes, including B2B, product, shipping, photos, menu, UI, localization and theme QA, must target **only the existing draft ID 198480756902**. Do not switch to a differently named, newer or live theme automatically.
3. Before each Shopify theme write, query current theme ID, name and role. Fail closed if the target is absent, has become MAIN, or the identity is ambiguous. Stop, report evidence and request a fresh explicit operator instruction rather than silently choosing a substitute.
4. Never publish, replace or patch MAIN, and never delete or rename any theme, merely because the user asks for a storefront fix. Each of those actions requires separately explicit approval.
5. Avoid overwriting unrelated working code. Read before write, apply the smallest change on the authorized theme, then read back the saved file and verify checksum/content; test the relevant UI and browser flows when possible. Recorded file presence is **not** proof that checkout, B2B discounts, inventory or shipping configurations work end to end.
6. Avoid "merge by entire theme" and uncontrolled wholesale file copies. Merge only individually inspected, necessary changes inside the authorized existing draft. Local diffs/patch files are allowed but they must not create a new Shopify theme.
7. This rule binds ChatGPT, Codex, Vinterro One, @DragDrop, Shopify specialists, QA, reviewers, agents and automation. Agents may not reinterpret an ordinary instruction such as `devam et`, `düzelt`, `test et` or `tüm ajanları çalıştır` as permission to create a new draft.
8. Explicit operator instructions can update the authorized target or authorize a particular otherwise-prohibited action. Record the new instruction and verify the target before proceeding. Do not infer authorization from an earlier or third-party message.

## Verification baseline (2026-10-13)
Shopify returned exactly one `UNPUBLISHED` theme (`198480756902`) and one `MAIN` theme at the time of this contract change. Before any later write, verify again. Policy commits and agent routing changes **do not** themselves prove deployment, live runtime agent enforcement or provider action.
