# VCO CLI

> **Not implemented in VCO 0.1. This file is a specification document for future work.**

The VCO CLI is the command-line companion to the VCO protocol. It is planned for VCO 0.2 and beyond. The CLI does not exist in the `vco` package today; the protocol is currently driven by file-based Markdown and JSON files.

## Planned commands

### `vco init`

Initialize a VCO-managed project in the current directory by copying the VCO templates and creating a `.vco/` skeleton.

```text
vco init
  ↓
creates .vco/manifest.json
  ├── .vco/state.json
  ├── .vco/decisions/
  ├── .vco/context/
  └── .vco/verification/
copies templates/ → project root
```

### `vco context "modify runner registration"`

The context engine (planned for 0.3) accepts a natural-language intent and returns focused context:

```text
Input
 ↓
Intent
 ↓
Relevant requirements
 ↓
Relevant architecture
 ↓
Relevant decisions
 ↓
Relevant files
 ↓
Relevant tests
 ↓
Focused context
```

The objective: **relevant context over maximum context.**

### `vco sign`

Sign a release or ADR using established cryptographic standards (planned for 0.5). Never a custom algorithm.

### `vco verify-signature`

Verify a previously generated VCO signature.

## Why not implement now

VCO 0.1 is the protocol foundation. Implementing a CLI before the protocol is proven would couple the protocol to a particular tool and likely cause rework. The file-based protocol is intentionally agent-agnostic; the CLI will be an optional convenience layer on top of it.

## Versioning plan

- **0.2:** basic CLI (`init`, `validate`, `plan` entry point)
- **0.3:** context engine
- **0.4:** agent adapters
- **0.5:** cryptographic provenance (`sign`, `verify-signature`)
- **1.0:** stable ecosystem
