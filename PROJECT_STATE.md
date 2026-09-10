# Project State — VCO

Last updated: 2026-09-10

## What is this?

VCO (Verity Coding OS) 0.1.0 is a protocol foundation for AI-assisted software engineering: rules, templates, profiles, documentation, and validation. It is a greenfield repository created at `_dev_tools/vco/` and released as a private GitHub repo.

## What phase is it in?

Build is complete; in **release-candidate** phase (validation, audit, dogfood, release).

## What is being built right now?

- REQ-009 Manifest validation enforcement
- REQ-011 CI validation passes
- REQ-014 Dogfood layer completion

## What is complete?

- Core identity docs (REQ-001, partial)
- All 8 rules files (REQ-001, REQ-002, REQ-003, REQ-007)
- All 7 templates
- All 6 skills (REQ-006)
- All 6 profiles (REQ-008)
- All 5 docs including getting-started (REQ-016)
- GitHub CI and deterministic validator (REQ-009, REQ-011)

## What is blocked?

- Nothing.

## What is unknown?

- Whether the first remote CI run will surface any workflow syntax or link issues (INFERRED — will be CONFIRMED by evidence after push).

## What decisions exist?

- ADR-0001: protocol-first, agent-agnostic core
- ADR-0002: Markdown and JSON as the storage format
- ADR-0003: MIT License

## What was last verified?

- Local scaffold and file creation completed (git log shows all commits present).
- No formal verification has been run yet; this is the current task.

## What happens next?

1. Run `.github/scripts/validate.py` locally for all three modes.
2. Produce and record the audit.
3. Produce and record the dogfood acceptance review.
4. Push to GitHub, wait for CI green.
5. Tag `v0.1.0`.
