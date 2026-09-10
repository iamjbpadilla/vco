# Phase 7 — Dogfood Review

Date: 2026-09-10
Reviewer: implementation agent, self-review

## §34 question

> Can an unfamiliar AI agent enter this repository and understand what it is allowed to do without guessing?

## Test

A simulated entry path for an unfamiliar agent:

1. Open `AGENTS.md` (root constitution).
2. Rule 1: read `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `TASKS.md`, and relevant ADRs.
3. `PROJECT_STATE.md` answers: what is this, phase, current focus, completed work, blockers, unknowns, decisions, last verified, next steps.
4. `SCOPE.md` answers: what is IN SCOPE and OUT OF SCOPE for VCO 0.1.0.
5. `REQUIREMENTS.md` answers: what must be true, with IDs and traceability.
6. `TASKS.md` answers: what is in progress, what is done, and where evidence lives.
7. `.vco/context/index.md` provides a map to rules, skills, and decisions.
8. `AGENTS.md` rule 10 requires the agent to report: changes, non-changes, assumptions, unknowns, verification, remaining risks.

## Result

An unfamiliar agent can determine:

- Its binding rules (AGENTS.md)
- The current state and phase (PROJECT_STATE.md)
- The boundary of work (SCOPE.md)
- What is being built and why (REQUIREMENTS.md, TASKS.md)
- Where memory and evidence live (.vco/)
- What mode contracts apply (skills/)

It does not have to guess scope, authority, or process.

## Status

**PASS.** VCO successfully operates under its own protocol.

## Nonconformances

None.
