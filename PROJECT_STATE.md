# Project State — VCO

Last updated: 2026-09-10

## What is this?

VCO (Verity Coding OS) 0.1.0 is a protocol foundation for AI-assisted software engineering: rules, templates, profiles, documentation, and validation. It is released at `https://github.com/iamjbpadilla/vco` and tagged `v0.1.0`.

## What phase is it in?

**Released.**

## What is being built right now?

Nothing actively in progress. The package is released and awaiting change requests for 0.2 roadmap items.

## What is complete?

All VCO 0.1.0 deliverables are VERIFIED:

- Core identity docs (REQ-001, REQ-015)
- All 8 rules files (REQ-001, REQ-002, REQ-003, REQ-007)
- All 7 templates (REQ-003, REQ-010)
- All 6 skills (REQ-006)
- All 6 profiles (REQ-007, REQ-008)
- All 5 docs including getting-started (REQ-004, REQ-005, REQ-013, REQ-016)
- GitHub CI and deterministic validator (REQ-009, REQ-011)
- Dogfood layer (REQ-014)

## What is blocked?

Nothing.

## What is unknown?

Nothing.

## What decisions exist?

- ADR-0001: protocol-first, agent-agnostic core
- ADR-0002: Markdown and JSON as the storage format
- ADR-0003: MIT License

## What was last verified?

- Local: `python3 .github/scripts/validate.py` (manifest), `--structure`, `--links` — all PASS.
- Remote: GitHub Actions CI run succeeded on commit `b92b1c5` (see `.vco/verification/phase-8-release.md`).
- Audit: all 12 §33 questions PASS (`.vco/verification/audit-0.1.0.md`).
- Dogfood: §34 acceptance test PASS (`.vco/verification/dogfood-0.1.0.md`).

## What happens next?

1. Complete the final §37 report.
2. Future work (0.2+) is gated through change requests per `CONTRIBUTING.md`.
