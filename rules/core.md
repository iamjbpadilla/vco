# Core Protocol

This rule answers: **what is the fundamental operating model of a VCO project?**

## The flow

```text
Human → Intent → Specification → VCO → AI Agent → Code → Evidence → Verified
```

VCO sits between the specification and the agent. The agent implements; VCO constrains and verifies.

## Core principle

> AI may implement what is known. AI must not invent what is unknown.

Known means: stated in the specification, recorded in requirements, settled in an ADR, or confirmed by the human. Everything else is unknown and must be surfaced, not fabricated.

## Implementation is not verification

```text
IMPLEMENTED ≠ VERIFIED
```

Work reaches `IMPLEMENTED` when code exists. It reaches `VERIFIED` only when evidence exists (see [verity.md](verity.md)). Status reporting must never conflate the two.

## Anti-slop standard

The following are prohibited as justification for changes, unless the change was explicitly authorized:

```text
"I thought it would be useful."
"I assumed."
"While I was here."
"I also added."
"I improved it."
```

Preferred behavior:

```text
Smallest correct change.
Existing pattern first.
Requirement before assumption.
Evidence before confidence.
Explicit decision before architectural change.
```

## Git discipline

Git is historical evidence. Therefore:

- Small coherent commits — one concern per commit
- Meaningful commit messages — why, not just what
- Reviewable diffs — no unrelated changes mixed in
- Traceability — commits reference the requirement or task they serve where practical
- Never rewrite history unless explicitly required and authorized

## Mode separation

An agent operates in exactly one mode at a time (`plan`, `build`, `test`, `review`, `audit`, `ship` — see [skills/](../skills/)). Planning does not implement. Building does not silently redesign. Shipping does not skip verification.
