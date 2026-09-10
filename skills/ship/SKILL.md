# SKILL: /vco ship

## Purpose

Release verified work. Nothing unverified ships.

## Inputs

- `TASKS.md` (all in-scope tasks VERIFIED)
- `REQUIREMENTS.md` (all in-scope requirements VERIFIED)
- `.vco/verification/` (evidence for every gate)
- `rules/deployment.md`

## Responsibilities

Walk the release gates in order:

1. All in-scope work is `VERIFIED`.
2. Working tree is clean — no temp files, debug artifacts, secrets, generated junk.
3. CI passes on the exact release commit.
4. `CHANGELOG.md` is updated.
5. Version is consistent across `manifest.json`, `CHANGELOG.md`, `README.md` (if present), and any tags.
6. Tag the release only after the above gates pass.

## Restrictions

- Never tag a commit before CI passes on that exact commit.
- Never ship if critical verification is failing.
- Never bypass a gate to meet a deadline.

## Outputs

- Release tag and any release artifact
- Updated `PROJECT_STATE.md` and `CHANGELOG.md`
- Report: release evidence (commit hash, CI result, version, tag)

## Verification expectations

Shipping is the final verification of the release process. The release is `VERIFIED` only when all gates are documented and green.
