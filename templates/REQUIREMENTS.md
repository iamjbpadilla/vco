<!-- VCO template · copy to your project root as REQUIREMENTS.md. Requirement IDs are stable: never renumber or reuse them. -->

# Requirements — {{PROJECT_NAME}}

Statuses: `PROPOSED` → `APPROVED` → `IMPLEMENTED` → `VERIFIED`. Implementation does not imply verification; `VERIFIED` requires recorded evidence in `.vco/verification/`.

## Requirements

| ID | Requirement | Status | Verification method | Evidence |
| --- | --- | --- | --- | --- |
| REQ-001 | {{The system shall …}} | PROPOSED | {{e.g. unit test suite X}} | — |
| REQ-002 | {{…}} | PROPOSED | {{…}} | — |

## Traceability

Every requirement traces forward:

```text
REQ → TASK (TASKS.md) → CODE (commits/files) → TEST → EVIDENCE (.vco/verification/) → VERIFIED
```

When marking a requirement VERIFIED, link the evidence record in the Evidence column (e.g. `.vco/verification/req-001.md`).

## Rejected / superseded

<!-- Keep rejected or superseded requirements here with their reason, so agents don't re-propose them. -->

| ID | Requirement | Outcome | Reason |
| --- | --- | --- | --- |
