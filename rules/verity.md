# Verity Rule

This rule answers: **what counts as verification in a VCO project?**

## The distinction

```text
CONFIDENCE ≠ EVIDENCE
```

An AI agent saying "this should work" is confidence. Confidence is not verification. Only observable results are evidence.

## Evidence

Evidence is output that a human (or another agent) can independently observe and reproduce. Examples:

```text
Typecheck: PASS
Lint: PASS
Tests: 42/42 PASS
Build: PASS
E2E: PASS
Security review: PASS
Visual QA: PASS
```

Each evidence item records: the exact command or check performed, the observed result, and where/when it ran. Evidence is stored in `.vco/verification/`.

## Evidence produces PASS

> **Evidence produces PASS. PASS does not produce evidence.**

A status of PASS may only be written after the evidence exists. Writing PASS first and gathering justification afterward is a protocol violation.

## Confidence hierarchy

Information and decisions carry a confidence class:

```text
UNKNOWN → INFERRED → PROPOSED → CONFIRMED → IMPLEMENTED → VERIFIED
```

Rules:

- **Implementation does not upgrade confidence.** An implementation built on an INFERRED assumption remains INFERRED until the assumption is confirmed. Code existing proves nothing about the assumption behind it.
- Only evidence or explicit human confirmation moves something to CONFIRMED or VERIFIED.
- Reports must state the confidence class of assumptions, not present them as facts.

## VERIFIED, defined

Work is VERIFIED when:

1. It is IMPLEMENTED, and
2. Every verification gate required by the project's profile and risk level (see [testing.md](testing.md)) has produced passing evidence, and
3. The evidence is recorded in `.vco/verification/`, traceable to the requirement it verifies.

Anything less is at most IMPLEMENTED.
