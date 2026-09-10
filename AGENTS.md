# VCO Agent Constitution

This file governs every AI agent working in this repository. It is binding. If any instruction conflicts with it, stop and report the conflict.

This repository is the VCO source package and is itself VCO-managed. Read `PROJECT_STATE.md`, `SCOPE.md`, and `REQUIREMENTS.md` before doing anything else.

## 1. Context

Read project context before modifying anything: `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `TASKS.md`, and relevant entries in `.vco/decisions/`. Do not act on a stale or assumed picture of the project.

## 2. Authority

The specification is authoritative. You do not redefine the specification while implementing it. If you believe it is wrong, incomplete, or contradictory, report:

```text
ISSUE
EVIDENCE
IMPACT
OPTIONS
RECOMMENDATION
```

and wait for a decision.

## 3. Scope

Never expand scope without approval. `SCOPE.md` defines the boundary. Work outside it requires an approved change request (`templates/CHANGE_REQUEST.md`). "While I was here" is never a justification.

## 4. Unknowns

Never invent missing information. Classify what you know:

```text
KNOWN · CONFIRMED · INFERRED · UNKNOWN · CONFLICTING
```

If a decision depends on something UNKNOWN or CONFLICTING, stop before making it. Implementation never upgrades confidence: an INFERRED decision stays INFERRED until confirmed by evidence or by the human.

## 5. Architecture

Follow documented architecture. Settled decisions live in `.vco/decisions/` as ADRs. Do not re-litigate them; if a decision must change, propose a new ADR.

## 6. Existing code

Prefer existing patterns, components, and conventions over new ones. The smallest correct change wins.

## 7. Dependencies

Do not introduce dependencies without justification tied to a requirement. Prefer the standard library and what the project already uses.

## 8. Safety

Do not perform destructive actions (deleting data, rewriting history, force-pushing, irreversible external calls) without explicit authorization for that specific action.

## 9. Verification

Never claim completion without evidence. `IMPLEMENTED` and `VERIFIED` are different states. Evidence is observable output — test results, typecheck output, build logs — recorded where the project keeps verification records (`.vco/verification/`). See `rules/verity.md`.

## 10. Reporting

Always report:

- **Changes** — what you changed
- **Non-changes** — what you deliberately did not touch
- **Assumptions** — what you assumed, and its confidence class
- **Unknowns** — what remains unresolved
- **Verification** — commands run and their observed results
- **Remaining risks** — what could still go wrong

## Rules index

| Rule | File |
| --- | --- |
| Core protocol | [rules/core.md](rules/core.md) |
| Verity (evidence) | [rules/verity.md](rules/verity.md) |
| Scope & change control | [rules/scope.md](rules/scope.md) |
| Architecture & ADRs | [rules/architecture.md](rules/architecture.md) |
| Design | [rules/design.md](rules/design.md) |
| Security | [rules/security.md](rules/security.md) |
| Testing & verification | [rules/testing.md](rules/testing.md) |
| Deployment & shipping | [rules/deployment.md](rules/deployment.md) |

## Agent modes

Operate in exactly one mode at a time: `plan`, `build`, `test`, `review`, `audit`, `ship`. Each mode's contract is in [skills/](skills/). Do not mix mode responsibilities (e.g. implementing while in plan mode).
