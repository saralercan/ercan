# Ercan OS — Hardware Design Engine

Status: active
Date: 2026-09-24

## Purpose

Define an evidence-driven AI-assisted electronics/PCB workflow using KiCad-native source, deterministic electrical/layout validation and independent engineering review.

Execution skill:
`.agents/skills/hardware-design-engine/SKILL.md`.

Stable routing identities remain **52**.

## Architecture

`requirements -> architecture -> component verification -> schematic -> ERC -> placement/stackup -> routing -> DRC -> DFM/physics/mechanical review -> fabrication package -> prototype/bring-up -> measured feedback`

AI proposes and edits.
Deterministic engineering tools and human/qualified review accept.

## Primary design source

Prefer KiCad-native editable project files and portable manufacturing outputs.

A rendered image, textual netlist summary or AI chat is not sufficient to certify the board state.

## Provider map

| Provider/source | Role | Decision |
|---|---|---|
| heypcb.ai | managed AI-assisted KiCad PCB design | ADOPT_WHEN_NEEDED / CLOSED_SOURCE_SAAS |
| heypcb Circuit World | licensed reference/fork discovery | HARDWARE_REFERENCE_DISCOVERY |
| biosshot/kicad-copilot | KiCad MCP/file automation | ADOPT_WHEN_NEEDED / MIT |
| circuit-synth/circuit-synth | code-defined/parametric circuits | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT |
| LGAI-Research/PCBWorld | KiCad-grounded routing benchmark | ADOPT_PATTERN_ONLY / BENCHMARK |
| IxTechCrypto/kicad-skills | domain DFM/verification skill patterns | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT |
| buildwithtrace/trace | AI-native KiCad fork/reference | WATCHLIST / PATTERN_ONLY / MIXED_LICENSE |

## heypcb / Circuit World

Current public heypcb materials establish:
- real KiCad project files;
- schematic/layout/fabrication outputs;
- design/fab checking;
- downloadable portable manufacturing/CAD outputs;
- public Circuit World publishing with author/title/licence;
- forking/sharing of published boards.

Each public board licence is evaluated independently.

Circuit World is a discovery/reference layer, not a universal reusable component library.

## Cloud/IP rule

Because heypcb processes project/design data and may send relevant board context to configured AI providers, confidential/NDA-controlled/export-sensitive designs require an explicit cloud-processing decision before upload.

Current provider privacy language says raw project files are not used to train public foundation models, but a redacted technical learning store and cross-account generic lessons may be used under described conditions. This is still a material project-data consideration.

## Verification hierarchy

1. official component datasheets
2. official fabrication capabilities/design rules
3. KiCad deterministic ERC/DRC/native tools
4. simulation/analysis tools appropriate to the circuit
5. mechanical/3D/stackup review
6. prototype measurements
7. AI/provider suggestions

AI confidence never outranks a failed deterministic check or measured result.

## Board regime

Classify the board before layout:
- general low-speed
- high-current/power
- high-speed digital
- RF/wireless
- mixed-signal/analog
- battery/power-management
- high-voltage
- safety-critical/regulated

Load only the relevant domain constraints.

## Fabrication readiness

Fabrication readiness requires manufacturing outputs and design-rule closure.

Production readiness additionally requires application-specific engineering validation, prototype/test evidence and any required compliance/certification.

Never collapse these states.

## Licensing

For any imported/forked/reference design:
- record source;
- record licence;
- identify modifications;
- preserve notices/attribution where required;
- review copyleft obligations before distribution;
- re-run engineering verification.

## Completion vocabulary

Hardware work may use:
- DESIGN_VERIFIED
- PHYSICALLY_VALIDATED
- PARTIAL
- BLOCKED
- NOT_VERIFIED

`DESIGN_VERIFIED` means source/deterministic review passed to the defined scope.
It does not mean the physical board has been validated.

`PHYSICALLY_VALIDATED` requires real prototype/test evidence appropriate to the project.
