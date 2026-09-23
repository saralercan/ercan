# Provider/Upstream Scan — heypcb / Circuit World / AI PCB tooling

Date: 2026-09-24

Input:
https://heypcb.ai/world

## Retrieval status

Direct fetch of `/world` was blocked by the site's robots policy in the current web retrieval path. No unobserved World-card data or private project details are asserted.

Public heypcb home/challenge/legal pages were available and provide enough evidence to characterize the product and Circuit World publishing model.

## heypcb

Current home page describes:
- natural-language board creation;
- schematic, layout and fabrication outputs;
- real parts, verified libraries/pin maps/datasheet limits;
- electrical/layout/fabrication checking;
- Gerbers, STEP and editable portable CAD;
- persistent project workspaces;
- reference designs including open hardware projects.

Decision:
`ADOPT_WHEN_NEEDED / AI_PCB_DESIGN_PROVIDER / CLOSED_SOURCE_SAAS`.

## Engineering responsibility

Current heypcb Terms explicitly state:
- AI/automated output can be incorrect, incomplete, non-manufacturable or unsafe;
- heypcb is a design aid rather than a substitute for qualified engineering/manufacturer review/safety certification;
- the user is responsible for reviewing, testing and validating before fabrication/deployment.

Ercan OS adopts this as a hard completion boundary.

## Data/IP/privacy

Current Privacy Policy states:
- project/design data includes prompts, schematics, PCB files, Gerbers and revision history;
- project context may be sent to configured language-model providers;
- project files are not used to train public foundation models;
- a redacted technical copy of agent turns/verification results may be stored up to one year;
- generic engineering lessons may be distilled/shared across accounts after specified cross-project confirmation conditions;
- raw attachments/project files are not copied into that learning store.

Decision:
cloud processing requires explicit project/IP/NDA/export-control consideration.

## Circuit World

Current heypcb Challenge page establishes that users can:
- publish a board to Circuit World;
- attach title, licence and author identity;
- share/fork boards;
- retain real CAD/project artifacts;
- keep chat/research private when publishing;
- enter original/substantially modified work into the challenge.

Decision:
`HARDWARE_REFERENCE_DISCOVERY`.

Public visibility does not override the board's stated licence.

## Open-source references

### biosshot/kicad-copilot
Observed:
- KiCad file-oriented MCP automation;
- schematic edits;
- component search;
- checkpoints;
- PCB sync/placement/routing;
- native `kicad-cli` ERC/DRC/export integration.
License: MIT.
Decision: ADOPT_WHEN_NEEDED.

### circuit-synth/circuit-synth
Observed:
- Python-defined/version-controlled circuits;
- KiCad generation/import/edit workflow;
- standard KiCad verification and manufacturing export remains downstream.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

### LGAI-Research/PCBWorld
Observed:
- KiCad PNS-grounded routing environment;
- DRC-based actions/rewards/evaluation;
- shared evaluation of RL/LLM/rule-based routers.
Licensing:
- BSD-3-Clause environment/evaluation;
- GPLv3 engine submodule.
Decision: ADOPT_PATTERN_ONLY / BENCHMARK_WHEN_NEEDED.

### IxTechCrypto/kicad-skills
Observed:
- JIT domain packs for high-current, high-speed, RF/low-power and custom parts;
- deterministic routing/verification tools;
- DFM/3D/ERC/DRC patterns.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Numeric engineering rules must be independently verified for the actual design/fab/standards.

### buildwithtrace/trace
Observed:
- KiCad-derived AI-native PCB environment.
Root README/LICENSE describe KiCad-derived code under GPLv3.
Current `trace/LICENSE` marks `trace/` proprietary/all-rights-reserved and prohibits copying/use without explicit permission.
Decision: WATCHLIST / PATTERN_ONLY / MIXED_LICENSE.
Do not copy proprietary AI modules.

## Architecture decision

Create one JIT `hardware-design-engine` capability rather than new stable agents.

`requirements -> KiCad-native source -> deterministic engineering gates -> fabrication package -> independent engineering review -> prototype feedback`

Stable routing identity count remains 52.
