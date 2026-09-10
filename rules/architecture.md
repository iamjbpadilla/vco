# Architecture & Decisions

This rule answers: **how are architectural decisions made, recorded, and respected?**

## Follow documented architecture

The project's architecture documentation (typically `docs/architecture/` in a VCO-enabled project) is authoritative. Agents implement within it. Deviating from documented architecture is an architectural change and requires an explicit decision — never an improvisation inside a build task.

## ADRs

Settled decisions are recorded as Architecture Decision Records in `.vco/decisions/`, using [templates/ADR.md](../templates/ADR.md):

```text
ADR-XXXX
Title
Status
Context
Decision
Alternatives Considered
Consequences
Date
```

Purpose: prevent future agents (and humans) from repeatedly reconsidering already-settled decisions.

## Rules

- Before proposing an architectural approach, read existing ADRs. If an ADR already settles the question, follow it.
- To change a settled decision, propose a **new** ADR that supersedes the old one. Do not edit or delete historical ADRs; mark them `Superseded by ADR-XXXX`.
- ADR statuses: `Proposed`, `Accepted`, `Superseded`, `Rejected`.
- Number ADRs sequentially (`ADR-0001`, `ADR-0002`, …) and never reuse numbers.
- New dependencies, new services, new storage formats, and cross-cutting structural changes all warrant an ADR.

## Existing code first

Prefer existing patterns, components, utilities, and conventions over inventing new ones. If two patterns conflict in the codebase, surface the conflict rather than silently picking one and propagating it.
