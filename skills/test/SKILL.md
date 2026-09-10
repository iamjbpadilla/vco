# SKILL: /vco test

## Purpose

Validate implementation with observable evidence and record it.

## Inputs

- `TASKS.md` (task is IMPLEMENTED)
- `REQUIREMENTS.md` (verification method for the relevant requirement)
- `rules/testing.md` and the project profile (required gates)

## Responsibilities

1. Run the exact gates declared for the task/requirement.
2. Record every command and its observed result in `.vco/verification/`.
3. Distinguish `IMPLEMENTED` from `VERIFIED` — only evidence produces PASS.
4. Fail the task if any required gate fails; do not downgrade or skip gates.
5. Mark `TASKS.md` `VERIFIED` only with evidence links.

## Restrictions

- Do not adjust tests to make them pass without authorization.
- Do not skip a gate because the environment is broken — report the blocker.
- "The tests would pass" is not evidence.

## Outputs

- Evidence files in `.vco/verification/`
- Updated `REQUIREMENTS.md` and `TASKS.md` status = VERIFIED where gates passed
- Report: what gates were run, their results, evidence locations, blockers

## Verification expectations

Evidence must be independently reproducible: exact command, environment, output. A gate is `PASS` only when the command output (or its explicit PASS summary) is recorded.
