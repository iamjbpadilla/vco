# SKILL: Adopt and operate VCO

Use this skill when a project uses VCO (a `.vco/` directory or VCO files like `SCOPE.md` and `REQUIREMENTS.md` exist), or when asked to set VCO up in a project.

## What VCO is

VCO (Verity Coding OS) is a protocol that governs AI-assisted development. Its rule: **AI may implement what is known. AI must not invent what is unknown.** Its distinction: **CONFIDENCE ≠ EVIDENCE.**

## Adopting VCO in a project

1. Copy the files from `templates/` into the project root: `AGENTS.md`, `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `TASKS.md`.
2. Create `.vco/manifest.json` using the schema in `docs/architecture.md`. Pick a profile from `profiles/`.
3. Create `.vco/decisions/`, `.vco/context/`, `.vco/verification/` directories.
4. Fill in `SCOPE.md` and `REQUIREMENTS.md` with the human before writing any code.

Full walkthrough: `docs/getting-started.md`.

## Operating under VCO

1. Read `AGENTS.md` (the constitution), then `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `TASKS.md`.
2. Enter exactly one mode and follow its skill contract:

| Mode | Skill | Purpose |
| --- | --- | --- |
| plan | [skills/plan/SKILL.md](skills/plan/SKILL.md) | Plan work; no implementation |
| build | [skills/build/SKILL.md](skills/build/SKILL.md) | Implement approved work only |
| test | [skills/test/SKILL.md](skills/test/SKILL.md) | Validate implementation with evidence |
| review | [skills/review/SKILL.md](skills/review/SKILL.md) | Find defects and risks |
| audit | [skills/audit/SKILL.md](skills/audit/SKILL.md) | Check VCO compliance |
| ship | [skills/ship/SKILL.md](skills/ship/SKILL.md) | Release only verified work |

3. Record evidence in `.vco/verification/` and update `PROJECT_STATE.md` and `TASKS.md` as you go.
4. Anything outside `SCOPE.md` requires a change request (`templates/CHANGE_REQUEST.md`) before work begins.

## Hard rules

- Never claim `VERIFIED` without observable evidence (`rules/verity.md`).
- Never expand scope silently (`rules/scope.md`).
- Never re-open settled ADRs without a new ADR proposal (`rules/architecture.md`).
- Report changes, non-changes, assumptions, unknowns, verification, and remaining risks after every unit of work.
