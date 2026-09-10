# Scope — VCO 0.1.0

Work not listed as IN SCOPE requires an approved change request (`templates/CHANGE_REQUEST.md`) before it begins. "While I was here" is never a justification.

## IN SCOPE

- Core protocol and identity docs: README, LICENSE, CONTRIBUTING, CHANGELOG, AGENTS.md, SKILL.md
- Official logo at `assets/logo.png` (user-authorized addition to the §08 tree)
- Rules: `rules/` (8 files)
- Skills: `skills/` (6 files)
- Templates: `templates/` (7 files)
- Profiles: `profiles/` (6 files)
- Documentation: `docs/` (5 files, including user-requested getting-started guide)
- Future CLI specification: `packages/cli/README.md`
- GitHub configuration: `.github/workflows/ci.yml`, `.github/scripts/validate.py`, `.github/ISSUE_TEMPLATE/*.md`
- Dogfood layer: `.vco/`, `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `TASKS.md`
- Local + CI validation, audit, and dogfood review for 0.1.0

## OUT OF SCOPE

- CLI implementation
- Context engine implementation
- Agent adapter implementations
- Cryptographic signing implementation
- Dashboard, SaaS, user accounts, billing
- Authentication or authorization systems
- Marketplace
- Cloud backend or hosted services
- Automatic code generation service

## Changing scope

1. Draft a change request from `templates/CHANGE_REQUEST.md`.
2. Get it APPROVED.
3. Update this file and `REQUIREMENTS.md`.
4. Only then plan and implement.
