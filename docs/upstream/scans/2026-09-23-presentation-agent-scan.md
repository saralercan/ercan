# Upstream Scan — Presentation Agents

Date: 2026-09-23
Scope: GitHub/open-source presentation-generation agents suitable for Ercan OS.
Decision model: discover broadly, adopt narrowly; prefer active canonical repositories with clear licenses, editable outputs, agent/runtime fit and explicit visual QA.

## Selected

| Repository | State at review | License | Decision | Why |
|---|---|---|---|---|
| `icip-cas/PPTAgent` | active; ~5k stars; pushed 2026-09-21 | MIT | `ADOPT_JIT_PRIMARY` | Strongest reviewed fit for editable PowerPoint plus reflective render/review/finalize workflow; current agent skill supports Codex-style hosts. |
| `presenton/presenton` | active; ~10.7k stars; pushed 2026-09-22 | Apache-2.0 | `ADOPT_JIT_ALTERNATE` | Mature open-source presentation generator/API with editable PPTX, templates and multi-format exports. |
| `presenton/skills` | active; agent-skill repo | Apache-2.0 | `ADOPT_JIT_ALTERNATE` | Provides explicit agent-facing workflow for design resolution, HTML validation, PPTX/PDF/PNG export and preview creation. |
| `iOfficeAI/OfficeCLI` | active; native Office agent CLI | Apache-2.0 | `ADOPT_JIT_NATIVE_PPTX` | Strong native PPTX creation/editing, existing-deck repair and render→inspect→fix workflow; dedicated generic and fundraising deck skills. |
| `SlideSpeak/slide-design-skill` | active; agent skill | MIT | `ADOPT_JIT_VISUAL_DESIGN` | Strong bespoke art direction from brief/brand/reference; deterministic HTML deck rendering with real charts/tables/imagery. Pair with editable builder for native PPTX delivery. |
| `ningzimu/codex-ppt-skill` | active; Codex-oriented agent skill | MIT | `ADOPT_PATTERN_ONLY / RASTER_FIRST_JIT` | Strong style/reference and full-slide visual generation, but default PPTX is image-based and not element-editable. |
| `addsumtech/slides_maker` | active; multi-agent slide skill | MIT | `ADOPT_JIT_SOURCE_TRACED_NATIVE` | Native editable PPTX, source-traced facts/figures, independent critic and multi-canvas delivery. |
| `solid-shuwen/shuttleslide` | active; alpha round-trip converter/agent | MIT | `ADOPT_JIT_ROUNDTRIP_BRIDGE` | PPTX↔HTML with editable structure and formatting metadata preservation; strongest as a bridge/repair workflow. |
| `ningzimu/image-to-editable-ppt-skill` | active; reconstruction skill | MIT | `ADOPT_JIT_RECONSTRUCTION` | Rebuilds images/PDF/image-based decks into object-level editable PowerPoint with explicit limitations. |
| `Y-Research-SBU/SlideGen` | active; pushed 2026-06-01 | MIT | `ADOPT_PATTERN_ONLY / ACADEMIC_JIT` | Useful scientific-deck decomposition: outliner, figure/table mapper, equation formulizer, arranger and refiner. |

## Additional watchlist / pattern-only candidates

### `Akxan/ppt-agent-skill`
- MIT; broad style library, data-viz recipes and HTML→SVG→PPTX workflow.
- Useful design-pattern reference, but substantially overlaps SlideSpeak / PPTAgent / OfficeCLI; do not add another default engine without a concrete gap.

### `chuspeeism/dashi-ppt-skill`
- Rich editable HTML/PPTX workflow and large theme/layout library.
- License: AGPL-3.0. Treat as watchlist/pattern-only unless deployment/licensing obligations are explicitly reviewed for the target use.

## Watchlist / pattern only

### `Westlake-AGI-Lab/Auto-Slides`
- Active academic multi-agent presentation research implementation.
- GitHub review showed `NOASSERTION` license metadata.
- Decision: `WATCHLIST / PATTERN_ONLY`.
- Rationale: useful conceptual workflow, but code adoption is not justified until license/provenance is explicit.

## Rejected for production code adoption

### `rsrohan99/presenter`
- Multi-agent presentation, Mermaid diagrams, speaker scripts, narration and video concepts are interesting.
- No repository license detected in GitHub metadata at review time.
- Last push is materially older than the selected primary engines.
- Decision: `REJECT_CODE_ADOPTION / IDEA_REFERENCE_ONLY`.

### Small generic multi-agent PPT generators
Several newer repositories expose Router/Parser/RAG/Planner/Research/Design/PPT Builder/Reviewer chains. These are useful confirmation that the capability decomposition is sound, but they were not promoted because the selected engines provide stronger maintenance, licensing, ecosystem usage, editable-output or visual-QA evidence.

## Capability synthesis adopted into Ercan OS

The scan produced a provider-neutral presentation pod instead of hard-coding one repository:
- research/fact verification;
- deck strategy and narrative architecture;
- concise slide writing;
- art direction and layout system;
- authoritative asset selection;
- data-visualization planning;
- editable PPTX engineering;
- slide rendering;
- slide-by-slide visual review;
- independent deck QA;
- template/reference fidelity;
- academic figure/table/equation mapping when relevant;
- multi-format export when requested.

## Upstream boundaries

- Upstream READMEs/skills are untrusted external instructions and never override Ercan OS safety, source, brand or QA rules.
- Star count is a discovery signal, not a quality guarantee.
- A repository's generation success is not acceptance evidence; final rendered slides must be reviewed.
- User/project brand assets outrank generic upstream templates.
- Do not vendor code with unclear licensing.
- Re-check current repository state before a material future dependency upgrade or vendor adoption.

## Sources reviewed

- https://github.com/icip-cas/PPTAgent
- https://github.com/icip-cas/PPTAgent/blob/main/skills/pptagent/SKILL.md
- https://github.com/presenton/presenton
- https://github.com/presenton/skills
- https://github.com/presenton/skills/blob/main/skills/presenton/SKILL.md
- https://github.com/iOfficeAI/OfficeCLI
- https://github.com/iOfficeAI/OfficeCLI/blob/main/skills/officecli-pptx/SKILL.md
- https://github.com/SlideSpeak/slide-design-skill
- https://github.com/ningzimu/codex-ppt-skill
- https://github.com/addsumtech/slides_maker
- https://github.com/solid-shuwen/shuttleslide
- https://github.com/ningzimu/image-to-editable-ppt-skill
- https://github.com/Akxan/ppt-agent-skill
- https://github.com/chuspeeism/dashi-ppt-skill
- https://github.com/Y-Research-SBU/SlideGen
- https://github.com/Westlake-AGI-Lab/Auto-Slides
- https://github.com/rsrohan99/presenter
