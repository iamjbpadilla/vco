# Scope & Change Control

This rule answers: **what work is an agent allowed to do, and how does allowed work change?**

## The scope system

Every VCO project maintains a `SCOPE.md` with two lists:

```text
IN SCOPE
OUT OF SCOPE
```

- Work IN SCOPE may proceed through the normal plan → build → verify cycle.
- Work OUT OF SCOPE, or not listed at all, requires an approved change request first.
- "While I was here" is never a justification for additional work (see [core.md](core.md), anti-slop standard).

## Change control lifecycle

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

- **PROPOSED** — a change request exists ([templates/CHANGE_REQUEST.md](../templates/CHANGE_REQUEST.md)) stating what, why, and impact.
- **REVIEWED** — a human (or designated reviewer) has evaluated it.
- **APPROVED** — the human authorized it; `SCOPE.md` and `REQUIREMENTS.md` are updated.
- **PLANNED** — tasks exist in `TASKS.md`, linked to requirements.
- **IMPLEMENTED** — code exists.
- **VERIFIED** — evidence exists per [verity.md](verity.md).

No stage may be skipped. An agent may draft a change request at any time, but may not act on it before APPROVED.

## Agent obligations

- Before starting any task: confirm it maps to something IN SCOPE and to a requirement ID.
- On discovering adjacent problems: report them or draft a change request — do not fix them silently.
- On ambiguity about whether something is in scope: treat it as out of scope and ask.
