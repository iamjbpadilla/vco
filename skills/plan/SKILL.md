# SKILL: /vco plan

## Purpose

Plan work before implementation. No implementation, no file creation, no package installs, no code — only planning.

## Inputs

- `PROJECT_STATE.md` (current state)
- `SCOPE.md` (boundary)
- `REQUIREMENTS.md` (what must be satisfied)
- Existing code, architecture docs, and `.vco/decisions/` for context

## Responsibilities

1. Restate the intent and the requirement IDs to be satisfied.
2. Identify relevant context: files, ADRs, dependencies, unknowns.
3. Propose the smallest set of changes that satisfy the requirement.
4. Identify risks, assumptions (with confidence class), and unknowns.
5. Produce a concrete plan: steps, files to touch, verification approach.
6. Hand over to the build skill; do not build.

## Restrictions

- Do not write code.
- Do not create files except plan artifacts (e.g. task list in `TASKS.md`, draft change request).
- Do not introduce dependencies.
- If a required detail is UNKNOWN or CONFLICTING, stop and report it instead of planning forward.

## Outputs

- Updated or new plan in `TASKS.md` (status TODO)
- Clear statement of assumptions and unknowns
- Estimated verification approach per task
- Report: changes planned, non-changes, assumptions, unknowns, risks

## Verification expectations

Plan is not verified by tests. It is verified by review:

- Does each planned task map to one or more requirement IDs?
- Is every task inside `SCOPE.md` or an approved change request?
- Are unknowns surfaced rather than hidden?
