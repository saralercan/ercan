---
name: hardware-design-engine
description: Design, inspect and verify PCB/electronics projects using KiCad-native artifacts, deterministic electrical/layout checks, real component data, fabrication outputs and independent engineering review. Use for PCB design, schematic generation, component selection, routing, DRC/ERC/DFM, Gerber/BOM/STEP export, Circuit World reference discovery or AI-assisted hardware design.
---

# Hardware Design Engine

This is a JIT capability. It does not create new stable Ercan OS routing identities.

Primary reviewed SaaS provider:
- `heypcb.ai` — AI-assisted KiCad-native PCB design and Circuit World publishing/discovery.

Primary reviewed open-source references:
- `biosshot/kicad-copilot` — MIT
- `circuit-synth/circuit-synth` — MIT
- `LGAI-Research/PCBWorld` — BSD-3-Clause environment; GPLv3 engine
- `IxTechCrypto/kicad-skills` — MIT
- `buildwithtrace/trace` — mixed: KiCad-derived core GPLv3, `trace/` AI modules proprietary/all-rights-reserved

## JIT roles

These are capability lanes, not stable agents:
- HardwareArchitect
- SchematicEngineer
- ComponentLibrarian
- PCBLayoutEngineer
- RoutingEngineer
- DFMReviewer
- FabricationQA
- HardwareReferenceResearcher

## Core workflow

`requirements -> operating regime -> architecture -> component/datasheet verification -> schematic -> ERC -> PCB stackup/placement -> routing -> DRC -> signal/power/thermal/mechanical review -> DFM -> fabrication package -> independent engineering review -> prototype/test feedback`

AI may accelerate design work, but deterministic tools and engineering review own acceptance.

## KiCad-native source of truth

Prefer editable, portable project artifacts:
- `.kicad_pro`
- `.kicad_sch`
- `.kicad_pcb`
- custom symbols/footprints where needed
- BOM
- pick-and-place/position files
- Gerbers/drill files
- STEP/3D outputs

Screenshots/previews are evidence aids, not source of truth.

## Requirements gate

Before committing topology/layout, resolve where applicable:
- input/output voltages and currents
- power budget and rail tolerances
- interfaces/protocols
- clock/data rates
- RF bands
- battery/charging requirements
- environmental/temperature constraints
- mechanical envelope/connectors
- board layer/size targets
- fabrication/assembly constraints
- compliance/safety class
- expected production volume
- cost/availability constraints

If high-voltage, medical, automotive safety, mains, battery protection, high-current, RF certification, hazardous actuator control or other safety-critical hardware is involved, require domain-specific engineering review and applicable standards. Do not present AI output as certified.

## Component/data contract

Every material component decision should resolve:
- exact MPN/manufacturer
- datasheet source
- supply/availability evidence when material
- voltage/current/power ratings
- absolute maximum vs recommended operating range
- package/footprint
- pin mapping
- polarity/orientation
- thermal limits
- lifecycle/substitution risk when material

Do not invent pinouts, packages or footprints.

Prefer real verified libraries and datasheets over placeholder symbols/footprints.

## Schematic gate

Before layout:
- ERC or equivalent deterministic checks;
- power-domain review;
- decoupling and protection;
- connector/polarity review;
- net labels and hierarchy consistency;
- component pin/footprint parity;
- datasheet-critical reference circuitry;
- test/programming/debug access;
- design assumptions recorded.

ERC passing is necessary but not sufficient.

## PCB/layout gate

Before fabrication:
- DRC clean or every waiver documented;
- stackup/fab rules explicit;
- return paths/grounding reviewed;
- power/current density reviewed;
- clearance/creepage appropriate to application;
- differential/high-speed constraints where relevant;
- RF/antenna keepouts where relevant;
- thermal paths reviewed;
- mechanical keepouts/holes/connectors verified;
- silkscreen/orientation/pin-1 marks checked;
- board edge and enclosure compatibility checked;
- zone fills/refill state verified;
- 3D/STEP visual inspection where useful.

## Routing policy

Direct LLM-generated geometry is never trusted by itself.

Preferred order:
1. deterministic/native KiCad routing and design-rule constraints;
2. specialized routing engines/solvers;
3. AI-selected strategies/actions;
4. deterministic DRC after modifications;
5. rollback/checkpoint on violations.

`PCBWorld` is a strong benchmark/reference because it scores routing actions against KiCad's actual design-rule checker. Use its environment/evaluation patterns; do not import its GPL engine into incompatible code without license review.

## Fabrication package

Before calling a design fabrication-ready, produce/review where applicable:
- Gerbers
- drill files
- board outline
- BOM
- pick-and-place
- assembly drawing
- fabrication notes
- stackup
- impedance constraints
- test points
- STEP/3D
- revision/version metadata

Fabrication-ready does not mean electrically safe, certified or validated in the physical world.

## Prototype/bring-up

For material hardware:
- prototype before production scale;
- define current-limited first power-up;
- verify rails before loading downstream systems;
- perform thermal inspection;
- exercise interfaces;
- compare measured behavior to design assumptions;
- record failures/rework;
- feed results back into the next revision.

## heypcb provider role

Current public heypcb materials describe:
- natural-language PCB generation;
- real KiCad project files;
- schematic, layout and fabrication outputs;
- verified parts/pin maps/datasheet limits;
- design-rule/fabrication checks;
- portable Gerber/STEP/editable CAD exports.

Ercan OS decision:
`ADOPT_WHEN_NEEDED / AI_PCB_DESIGN_PROVIDER / CLOSED_SOURCE_SAAS`.

HeyPCB is a design acceleration provider, not final engineering authority.

### Privacy / data boundary

Current heypcb Privacy Policy states:
- project/design data includes prompts, schematics/PCB files, Gerbers and revision metadata;
- prompts/board context/tool results may be sent to configured third-party model providers;
- public foundation models are not trained directly on project files;
- heypcb may retain a redacted technical copy of agent turns/verification results for up to one year and derive generic engineering lessons that can be shared across accounts after confirmation criteria;
- raw project files/attachments are not placed into that learning store.

Therefore:
- do not upload confidential client hardware without project approval;
- review IP/NDA/export-control implications;
- remove secrets/credentials from board notes/files;
- prefer local/open-source KiCad workflows where cloud processing is unacceptable.

### Terms / engineering responsibility

Current heypcb Terms explicitly state AI designs may be incorrect, non-manufacturable or unsafe and remain the user's responsibility to review/test/validate before fabrication/deployment.

Ercan OS adopts that as a hard completion rule.

## Circuit World discovery

`heypcb.ai/world` is treated as `HARDWARE_REFERENCE_DISCOVERY`.

Current heypcb challenge/public materials establish that Circuit World boards:
- are published with title, licence and author;
- can be shared/forked;
- retain editable CAD/project context;
- require substantial original work for challenge-derived forks to count as original entries.

Rules:
- inspect the licence on each board before reuse;
- never assume public visibility means unrestricted commercial reuse;
- cite/record source board and licence;
- use references for architecture/layout inspiration and comparison;
- do not present a fork/minor variation as original design;
- re-run all deterministic verification after forking.

## Open-source provider decisions

### biosshot/kicad-copilot
`ADOPT_WHEN_NEEDED / MIT`.

Useful for:
- KiCad file-oriented MCP automation;
- schematic generation/modification;
- real component search;
- recoverable checkpoints;
- schematic-to-PCB sync;
- placement previews;
- local routing;
- native `kicad-cli` ERC/DRC/exports.

Do not install globally without project need.

### circuit-synth/circuit-synth
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT`.

Useful when software-style, version-controlled, parametric circuit definition is advantageous. Generated KiCad output still goes through visual/deterministic engineering review.

### LGAI-Research/PCBWorld
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED_FOR_BENCHMARKING`.

Use for:
- engine-grounded routing evaluation;
- deterministic DRC-based reward/evaluation;
- benchmarking routing agents.

Licensing is split: BSD-3-Clause environment/evaluation, GPLv3 engine.

### IxTechCrypto/kicad-skills
`ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT`.

Useful reference for:
- high-current
- high-speed
- RF/low-power
- custom-footprint
- deterministic DRC/ERC
- closed-loop routing
- DFM review

Treat numeric design rules as hypotheses/reference values unless verified against the actual component datasheet, fab capabilities, stackup and applicable standards.

### buildwithtrace/trace
`WATCHLIST / PATTERN_ONLY / MIXED_LICENSE`.

Root KiCad-derived areas are GPLv3, while current `trace/` AI-native modules are proprietary/all-rights-reserved.

Do not copy or reuse proprietary Trace AI modules.

## Completion states

A hardware task is VERIFIED only when the required subset is evidenced:
- requirements resolved;
- exact parts/datasheets known;
- editable KiCad/native source exists;
- ERC checked;
- DRC checked;
- relevant electrical/power/signal/thermal/mechanical/DFM review completed;
- fabrication outputs generated/inspected where requested;
- independent engineering review completed;
- prototype/test validation completed when physical correctness is required.

If no physical prototype/test exists, clearly distinguish:
- DESIGN_VERIFIED
from
- PHYSICALLY_VALIDATED.

Never call an untested AI-generated board "production-ready" or "certified".
