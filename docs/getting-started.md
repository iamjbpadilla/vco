# Getting Started with VCO

This guide walks you through adopting VCO in a real project. It is concrete, step-by-step, and assumes you already have an AI coding agent and a project to operate on.

## 1. What you need

- A project repository
- An AI coding agent that can read files (Devin, Claude, Codex, Cursor, etc.)
- No new tooling or services — VCO 0.1 is plain Markdown and JSON

## 2. Install VCO into your project

1. Copy every file from `vco/templates/` into your project root:

```text
AGENTS.md
PROJECT_STATE.md
SCOPE.md
REQUIREMENTS.md
TASKS.md
```

2. Create `.vco/` in your project root with these subdirectories:

```text
.vco/
├── manifest.json
├── state.json
├── decisions/
├── context/
└── verification/
```

3. Create `.vco/manifest.json` from the schema in [architecture.md](architecture.md). Example:

```json
{
  "vco": {
    "version": "0.1.0"
  },
  "project": {
    "name": "My Project",
    "profile": "web"
  },
  "author": {
    "name": "Jubet M. Padilla",
    "title": "Systems Engineer • AI Specialist"
  }
}
```

4. Choose a [profile](../profiles/) that matches your project type. Profiles are recommendation-only: you can substitute any technology.

## 3. Fill in the first documents

Before any code is written, fill in:

- `PROJECT_STATE.md` — what is this, what phase is it in, what is being built?
- `SCOPE.md` — what is IN SCOPE and what is OUT OF SCOPE for this cycle?
- `REQUIREMENTS.md` — the requirements you will satisfy, with IDs like `REQ-001`.
- `TASKS.md` — the tasks that implement those requirements.

## 4. Run a full work cycle

### 4.1 Plan

Tell the agent: `/vco plan REQ-001, REQ-002`.

The agent:

1. Reads `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `AGENTS.md`.
2. Produces a plan: files to touch, steps, risks, assumptions.
3. Updates `TASKS.md` with `TODO` items.

### 4.2 Build

Tell the agent: `/vco build {task}`.

The agent:

1. Implements the task.
2. Records only observable implementation evidence (e.g. "files created").
3. Updates the task to `IMPLEMENTED`. **Not `VERIFIED`.**

### 4.3 Test

Tell the agent: `/vco test {task}`.

The agent:

1. Runs the exact gates declared for the task (typecheck, tests, build, etc.).
2. Records commands and results in `.vco/verification/`.
3. Updates the task to `VERIFIED` only if all gates pass.

### 4.4 Review

Ask the agent or a human: `/vco review`.

The agent checks:

- Does the change match the requirement?
- Is there scope creep?
- Is the evidence recorded and valid?
- Are there unstated assumptions?

### 4.5 Audit

Before release: `/vco audit`.

The agent checks VCO compliance (scope, traceability, evidence, anti-slop). See `skills/audit/SKILL.md` for the exact checklist.

### 4.6 Ship

When everything is `VERIFIED`: `/vco ship`.

The agent:

1. Confirms all in-scope requirements are VERIFIED.
2. Confirms the tree is clean.
3. Confirms CI passes on the exact commit.
4. Updates `CHANGELOG.md`.
5. Tags the release.

## 5. Record evidence correctly

Evidence is not a claim. It is a record:

```text
Command: npm run test
Result:  42/42 PASS
Date:    2026-09-10
File:    .vco/verification/req-001.md
```

`IMPLEMENTED` and `VERIFIED` are different. Only evidence makes the second true.

## 6. File a change request when scope shifts

If, during work, you discover something that belongs outside `SCOPE.md`:

1. Stop the task.
2. Use `templates/CHANGE_REQUEST.md` to propose the change.
3. Get it APPROVED.
4. Update `SCOPE.md` and `REQUIREMENTS.md`.
5. Only then plan and build it.

"While I was here" is not a justification.

## 7. Agent-specific setup

| Agent | What to do |
| --- | --- |
| Devin | Put `AGENTS.md` in the project root; use `/vco plan` etc. as prompts |
| Claude | Load `AGENTS.md` into project instructions; reference `skills/` for mode contracts |
| Codex | Pass `AGENTS.md` and `SKILL.md` at the start of the session |
| Cursor | Reference `AGENTS.md` in `.cursorrules` or project instructions |

See [agent-compatibility.md](agent-compatibility.md) for more.

## FAQ / Troubleshooting

**Q: The agent keeps ignoring scope. What do I do?**
A: Point it back at `AGENTS.md` rule 3 and `SCOPE.md`. If it persists, add stronger project-specific examples and consequences.

**Q: What counts as evidence?**
A: Observable output: test results, typecheck output, build logs, security scan output, visual diffs. "I believe it works" is not evidence.

**Q: Can I skip a verification gate?**
A: Only if your profile or requirements explicitly say it is not applicable. Document the omission; do not silently skip.

**Q: Does VCO 0.1 have a CLI?**
A: No. The CLI is a future roadmap item. 0.1 is a documentation and protocol package.

**Q: Can the agent build the context engine for me now?**
A: No. The context engine is a future roadmap item. It is documented but not implemented in 0.1.
