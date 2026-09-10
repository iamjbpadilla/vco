# Requirements — VCO 0.1.0

Statuses: `PROPOSED` → `APPROVED` → `IMPLEMENTED` → `VERIFIED`. Implementation does not imply verification; `VERIFIED` requires recorded evidence in `.vco/verification/`.

## Requirements

| ID | Requirement | Status | Verification method | Evidence |
| --- | --- | --- | --- | --- |
| REQ-001 | Agent constitution exists and covers the 10 sections of §11. | VERIFIED | AGENTS.md content review + CI structure check | `.vco/verification/phase-5-local-validation.md` |
| REQ-002 | Verity rule: evidence-based verification defined; IMPLEMENTED vs VERIFIED distinguished; "evidence produces PASS" principle stated. | VERIFIED | rules/verity.md content review + audit checklist | `.vco/verification/audit-0.1.0.md` |
| REQ-003 | Scope system + change control lifecycle defined with reusable template. | VERIFIED | rules/scope.md and templates/CHANGE_REQUEST.md exist + audit | `.vco/verification/audit-0.1.0.md` |
| REQ-004 | Requirement traceability chain documented (REQ→TASK→CODE→TEST→EVIDENCE→VERIFIED). | VERIFIED | docs/workflow.md and this file content review | `.vco/verification/phase-5-local-validation.md` |
| REQ-005 | Project memory model (.vco/ + markdown files) defined. | VERIFIED | docs/architecture.md + `.vco/` content + structure check | `.vco/verification/phase-5-local-validation.md` |
| REQ-006 | Six agent modes defined with purpose, inputs, responsibilities, restrictions, outputs, and verification expectations. | VERIFIED | skills/ contains six SKILL.md files + audit | `.vco/verification/audit-0.1.0.md` |
| REQ-007 | Verification chain defined and risk-based, profile-scoped. | VERIFIED | rules/testing.md and profiles/ content review | `.vco/verification/phase-5-local-validation.md` |
| REQ-008 | Six profiles exist and are technology-agnostic. | VERIFIED | profiles/ contains six .md files; no mandatory stack enforced | `.vco/verification/phase-5-local-validation.md` |
| REQ-009 | Normative manifest schema defined (required/optional fields, profile enum, semver format) and enforced by CI structural validation. | VERIFIED | docs/architecture.md defines schema; validate.py enforces it; CI passes | `.vco/verification/phase-5-local-validation.md` |
| REQ-010 | Templates are usable standalone. | VERIFIED | templates/ files are self-explanatory with placeholders | `.vco/verification/dogfood-0.1.0.md` |
| REQ-011 | CI validates manifest structure, YAML, repo structure, and links — and passes. | VERIFIED | GitHub Actions CI run on commit `2837119` (tag `v0.1.0`) completed `success` | `.vco/verification/phase-8-release.md` |
| REQ-012 | VCO is agent-agnostic (no vendor coupling in core rules). | VERIFIED | No vendor APIs, commands, or assumptions in rules/ or AGENTS.md; agent-compatibility.md exists | `.vco/verification/phase-5-local-validation.md` |
| REQ-013 | Roadmap documents future features (CLI, context engine, adapters, signing) without implementing them. | VERIFIED | docs/architecture.md, packages/cli/README.md, CHANGELOG.md | `.vco/verification/phase-5-local-validation.md` |
| REQ-014 | Repo is dogfooded (.vco/, PROJECT_STATE, SCOPE, REQUIREMENTS, TASKS present and accurate). | VERIFIED | Dogfood files exist and reference each other; §34 acceptance test PASS | `.vco/verification/dogfood-0.1.0.md` |
| REQ-015 | Authorship metadata present (§29 block in README), not represented as cryptographic proof. | VERIFIED | README.md contains the authorship block with that disclaimer | `.vco/verification/phase-5-local-validation.md` |
| REQ-016 | Getting-started user guide exists, linked from README Quickstart, covering adoption, first setup, the six-mode work cycle with a worked example, evidence recording, and change requests. | VERIFIED | docs/getting-started.md exists and is linked from README.md; link check PASS | `.vco/verification/phase-5-local-validation.md` |

## Traceability

```text
REQ → TASK (TASKS.md) → CODE (commits/files) → TEST → EVIDENCE (.vco/verification/) → VERIFIED
```

Each requirement maps to one or more tasks in `TASKS.md`. The CI validation and local `validate.py` output are the evidence for the structural requirements (REQ-001..016). Work on the package is VERIFIED after the validate, audit, dogfood, and release gates complete.

## Rejected / superseded

None.
