# ADR-0001

## Title

Protocol-first, agent-agnostic core

## Status

Accepted

## Context

VCO must work with multiple AI agents: Devin, Claude, Codex, Cursor, and future agents. Coupling the protocol to one agent would make it brittle and reduce adoption. A backend service, SaaS, or CLI is out of scope for 0.1.

## Decision

VCO 0.1.0 will be a file-based protocol stored as Markdown and JSON. The core is agent-agnostic. A lightweight "agent adapter" concept is reserved for future versions. No executable tool is required for 0.1.

## Alternatives Considered

- **Agent-specific instructions only** — rejected because it fragments the protocol per agent.
- **CLI-first** — rejected because a CLI would couple the protocol to a particular runtime and is out of scope for 0.1.
- **Backend/SaaS** — rejected due to out-of-scope for 0.1 and unnecessary for the protocol foundation.

## Consequences

- Any agent that reads files can adopt VCO.
- Validation must be deterministic and run without dependencies.
- Future versions may introduce a CLI and agent adapters as optional layers, not replacements.

## Date

2026-09-10
