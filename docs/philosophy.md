# VCO Philosophy

## What VCO is

VCO (Verity Coding OS) is a development operating system and protocol for AI-assisted software engineering. It is not a model, an IDE, or a SaaS product. It governs the environment in which AI coding agents operate.

The model:

```text
Human
  ↓
Intent
  ↓
Specification
  ↓
VCO
  ├── Rules
  ├── Scope
  ├── Requirements
  ├── Memory
  ├── Architecture
  ├── Decisions
  ├── Tasks
  └── Verification
        ↓
     AI Agent
        ↓
      Code
        ↓
    Evidence
        ↓
     Verified
```

## Core principle

> **AI may implement what is known. AI must not invent what is unknown.**

The human owns intent and specification. The agent owns implementation. VCO owns the boundary.

## The Verity rule

```text
CONFIDENCE ≠ EVIDENCE
```

An AI agent saying "this should work" is not verification. Evidence comes from observable results: test outputs, build logs, typecheck output, security scans. In VCO, `IMPLEMENTED` and `VERIFIED` are different states, and evidence produces `PASS` — never the reverse.

## Final principle

```text
AI is the builder.
The specification is the authority.
Project memory is the context.
Scope is the boundary.
Tests are evidence.
Git is history.
VCO is the verification layer.
Build with AI. Verify everything.
```

## What 0.1 is and is not

VCO 0.1.0 is the protocol foundation: rules, templates, profiles, documentation, and a validation strategy. It does not include a CLI, a context engine, agent adapters, a backend, or cryptographic provenance. Those are future roadmap items, documented but not implemented.
