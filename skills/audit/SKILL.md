# SKILL: /vco audit

## Purpose

Check the project for VCO compliance — does the project follow its own protocol?

## Inputs

- All VCO files: `AGENTS.md`, `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `TASKS.md`
- `.vco/manifest.json`, `.vco/state.json`, `.vco/decisions/`, `.vco/verification/`
- `rules/`

## Responsibilities

Answer the VCO audit checklist (from `rules/verity.md` and the project profile):

1. Does the project have explicit scope?
2. Does it prevent invented requirements?
3. Does it distinguish implementation from verification?
4. Does it preserve project memory?
5. Does it support requirement traceability?
6. Does it support change control?
7. Does it support the agent modes?
8. Does it define evidence?
9. Does it remain agent-agnostic?
10. Does it avoid unnecessary complexity?
11. Does it document its own unknowns?
12. Does it follow its own anti-slop philosophy?

## Restrictions

- Do not fix findings during the audit.
- Every failed item becomes a finding with evidence.
- Audit is not a mode for implementing new ideas.

## Outputs

- Audit report in `.vco/verification/`
- Findings list (or clean bill of health)
- Report: checklist results, evidence, severity, recommended next action

## Verification expectations

Audit findings must be addressed before `ship`. A clean audit is itself evidence but does not replace product-level verification.
