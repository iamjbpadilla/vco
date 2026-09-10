# VCO Workflow

## End-to-end flow

```text
Intent → Specification → Plan → Build → Test → Review → Audit → Ship
         ↑_____________|      |       |       |       |       |
            update state       evidence evidence evidence  release
```

Each arrow is a handoff with evidence. No stage can claim completion without it.

## Requirement traceability

This is one of the fundamental properties of VCO:

```text
REQ
 ↓
TASK
 ↓
CODE
 ↓
TEST
 ↓
EVIDENCE
 ↓
VERIFIED
```

Every requirement maps to one or more tasks. Every task maps to code (commits and files). Every code change is tested. Every test produces evidence. Evidence, and only evidence, makes a requirement VERIFIED.

## The six modes

| Mode | Trigger | Authority | Output |
| --- | --- | --- | --- |
| `plan` | New work or unclear path | `SCOPE.md` + `REQUIREMENTS.md` | Plan in `TASKS.md` |
| `build` | Approved plan | `AGENTS.md` + architecture | Code; `IMPLEMENTED` status |
| `test` | Code exists | `rules/testing.md` + profile | Evidence; `VERIFIED` status |
| `review` | Code verified or mid-cycle | Human + `rules/verity.md` | Review record; conditions for ship |
| `audit` | Any time, especially pre-release | VCO rules + project state | Audit report; compliance findings |
| `ship` | All in-scope work VERIFIED | `rules/deployment.md` | Release; tag; updated state |

## Change control

```text
PROPOSED
   ↓
REVIEWED
   ↓
APPROVED
   ↓
PLANNED
   ↓
IMPLEMENTED
   ↓
VERIFIED
```

Any work outside `SCOPE.md` follows this lifecycle using `templates/CHANGE_REQUEST.md`. No skipping. No silent expansion.

## Context engineering (future, documented, not implemented in 0.1)

```text
Input
 ↓
Intent
 ↓
Relevant requirements
 ↓
Relevant architecture
 ↓
Relevant decisions
 ↓
Relevant files
 ↓
Relevant tests
 ↓
Focused context
```

The objective is: **relevant context over maximum context**. VCO 0.1 only defines the protocol and expected behavior. A context engine is a future implementation.
