# Ercan OS Project Adapters

These folders are the shared project-routing layer. They do not replace the actual application/theme/plugin source repositories.

| Project | Agent | Platform route | Adapter |
|---|---|---|---|
| DragDrop | `@DragDrop` | Shopify | `projects/dragdrop/` |
| Vinterro Digital | `@VinterroDigital` | Hostinger + WordPress | `projects/vinterro-digital/` |
| Ayvalık Vibes | `@AyvalıkVibes` | Hostinger + WordPress | `projects/ayvalik-vibes/` |
| GoAyvalık | `@GoAyvalık` | Hostinger + WordPress | `projects/goayvalik/` |

## Rule
When an actual source repository is connected, add a small repo-local `AGENTS.md` that points back to the central Ercan OS contract and copies only project-specific delta/context. Do not fork the entire constitution into every repository.

## Deployment reality
A project adapter is routing policy, not proof of current hosting/Git linkage. Before production writes, inspect the actual Shopify/Hostinger/WordPress account state and current source. Existing live WordPress sites must be reconciled/backed up before connecting a Git deployment that can overwrite files.
