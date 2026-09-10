# SKILL: /vco review

## Purpose

Find defects, risks, and inconsistencies in work that is already implemented or verified.

## Inputs

- The diff, branch, or artifact to review
- `AGENTS.md`, `SCOPE.md`, `REQUIREMENTS.md`
- `rules/verity.md`, `rules/scope.md`, `rules/testing.md`, `rules/security.md`

## Responsibilities

1. Check that changes match the requirement and the specification.
2. Find scope creep, missing evidence, and unstated assumptions.
3. Check for security, correctness, consistency, and maintainability issues.
4. Verify that the changes follow existing patterns.
5. Ask questions for anything that is unclear or invented.
6. Produce a review record: findings (with severity), questions, approval conditions.

## Restrictions

- Do not fix the code during review.
- Do not approve work that claims `VERIFIED` without evidence.
- Findings without severity and concrete evidence are not useful.

## Outputs

- Review record in `.vco/verification/` or a PR review
- List of required changes before `VERIFIED` can stand
- Report: what was reviewed, findings with evidence, questions, remaining risks

## Verification expectations

A review is not itself `VERIFIED` — it produces conditions for verification. The `ship` skill checks that all review conditions are resolved before release.
