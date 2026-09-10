# Requirements — VCO 0.1.0

Statuses: `PROPOSED` → `APPROVED` → `IMPLEMENTED` → `VERIFIED`. Implementation does not imply verification; `VERIFIED` requires recorded evidence in `.vco/verification/`.

## Requirements

| ID | Requirement | Status | Verification method | Evidence |
| --- | --- | --- | --- | --- |
| REQ-001 | Agent constitution exists and covers the 10 sections of §11. | IMPLEMENTED | File exists at AGENTS.md; inspect content | — |
| REQ-002 | Verity rule: evidence-based verification defined; IMPLEMENTED vs VERIFIED distinguished; "evidence produces PASS" principle stated. | IMPLEMENTED | File exists at rules/verity.md; inspect content | — |
| REQ-003 | Scope system + change control lifecycle defined with reusable template. | IMPLEMENTED | Files rules/scope.md and templates/CHANGE_REQUEST.md exist | — |
| REQ-004 | Requirement traceability chain documented (REQ→TASK→CODE→TEST→EVIDENCE→VERIFIED). | IMPLEMENTED | Traceability stated in docs/workflow.md and this file | — |
| REQ-005 | Project memory model (.vco/ + markdown files) defined. | IMPLEMENTED | Files docs/architecture.md and .vco/ exist | — |
| REQ-006 | Six agent modes defined with purpose, inputs, responsibilities, restrictions, outputs, and verification expectations. | IMPLEMENTED | skills/ contains six SKILL.md files | — |
| REQ-007 | Verification chain defined and risk-based, profile-scoped. | IMPLEMENTED | rules/testing.md and profiles/ define gates | — |
| REQ-008 | Six profiles exist and are technology-agnostic. | IMPLEMENTED | profiles/ contains six .md files; no mandatory stack enforced | — |
| REQ-009 | Normative manifest schema defined (required/optional fields, profile enum, semver format) and enforced by CI structural validation. | IMPLEMENTED | docs/architecture.md defines schema; validate.py enforces it | — |
| REQ-010 | Templates are usable standalone. | IMPLEMENTED | templates/ files are self-explanatory with placeholders | — |
| REQ-011 | CI validates manifest structure, YAML, repo structure, and links — and passes. | IMPLEMENTED | .github/workflows/ci.yml and .github/scripts/validate.py exist | — |
| REQ-012 | VCO is agent-agnostic (no vendor coupling in core rules). | IMPLEMENTED | No vendor APIs, commands, or assumptions in rules/ or AGENTS.md | — |
| REQ-013 | Roadmap documents future features (CLI, context engine, adapters, signing) without implementing them. | IMPLEMENTED | docs/architecture.md, packages/cli/README.md, CHANGELOG.md | — |
| REQ-014 | Repo is dogfooded (.vco/, PROJECT_STATE, SCOPE, REQUIREMENTS, TASKS present and accurate). | IMPLEMENTED | Dogfood files exist and reference each other | — |
| REQ-015 | Authorship metadata present (§29 block in README), not represented as cryptographic proof. | IMPLEMENTED | README.md contains the authorship block with that disclaimer | — |
| REQ-016 | Getting-started user guide exists, linked from README Quickstart, covering adoption, first setup, the six-mode work cycle with a worked example, evidence recording, and change requests. | IMPLEMENTED | docs/getting-started.md exists and is linked from README.md | — |

## Traceability

```text
REQ → TASK (TASKS.md) → CODE (commits/files) → TEST → EVIDENCE (.vco/verification/) → VERIFIED
```

Each requirement maps to one or more tasks in `TASKS.md`. The CI validation and local `validate.py` output are the evidence for the structural requirements (REQ-001..016). Work on the package is VERIFIED after the validate, audit, dogfood, and release gates complete.

## Rejected / superseded

None.
