# SKILL: /vco build

## Purpose

Implement approved work, and only approved work. Change requests are for scope, not for task execution.

## Inputs

- `TASKS.md` (exact task, status moved to IN PROGRESS)
- `REQUIREMENTS.md` (requirement IDs)
- `AGENTS.md` and `rules/` (constraints)
- `PROJECT_STATE.md`, relevant ADRs

## Responsibilities

1. Read context first; understand existing patterns.
2. Implement the smallest correct change that satisfies the requirement.
3. Prefer existing patterns, components, and conventions.
4. Record assumptions with confidence class.
5. Stop and report immediately when hitting unknowns or scope ambiguity.
6. Mark task `IMPLEMENTED` only when code exists — not `VERIFIED`.

## Restrictions

- No scope expansion without an approved change request.
- No new dependencies without justification tied to a requirement.
- No destructive operations without explicit authorization.
- No "while I was here" additions.
- No mixing of build and verify responsibilities.

## Outputs

- Code / docs changes, committed coherently
- Updated `TASKS.md` status = IMPLEMENTED for the relevant task
- Report: changes, non-changes, assumptions (classified), unknowns, verification, remaining risks

## Verification expectations

Build output is `IMPLEMENTED`, not `VERIFIED`. The agent may run quick local sanity checks to avoid wasted cycles, but official verification is `test` mode.
