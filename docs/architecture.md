# VCO Architecture

## Protocol-first

VCO is designed as a protocol before any implementation. The core protocol is agent-agnostic: it is stored as plain Markdown and JSON files, and any AI agent that can read files can operate under it.

```text
VCO
  ↓
Agent Adapter
  ↓
AI Agent
```

An adapter is the lightweight mapping between the project files and the agent's own conventions (e.g. Devin uses `AGENTS.md` directly; Claude may use a project instruction to load it; Cursor may use a `.cursorrules` reference). VCO 0.1 defines the protocol; adapters are a future concern.

## Project package model

The VCO repository (`vco/`) is the source package. A VCO-enabled project is a project operating under that package's protocol.

### VCO source package

```text
vco/
├── README.md
├── AGENTS.md
├── SKILL.md
├── rules/
├── skills/
├── templates/
├── profiles/
├── docs/
└── packages/
```

### VCO-enabled project (after adoption)

```text
my-project/
├── .vco/
│   ├── manifest.json
│   ├── state.json
│   ├── decisions/
│   ├── context/
│   └── verification/
├── AGENTS.md
├── PROJECT_STATE.md
├── SCOPE.md
├── REQUIREMENTS.md
├── TASKS.md
└── docs/
    ├── architecture/
    ├── design/
    ├── product/
    └── operations/
```

A project copies `templates/` to its root, fills them in, and creates `.vco/`.

## Manifest schema

`.vco/manifest.json` is the minimal project record.

### Required fields

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

| Field | Type | Constraints |
| --- | --- | --- |
| `vco.version` | string | valid semantic version (`MAJOR.MINOR.PATCH`) |
| `project.name` | string | non-empty |
| `project.profile` | string | one of `web`, `pwa`, `mobile`, `saas`, `api`, `internal-tool` |
| `author.name` | string | non-empty |

### Optional fields

| Field | Type | Purpose |
| --- | --- | --- |
| `project.description` | string | one-line project summary |
| `project.modes` | array of strings | allowed agent modes for this project (default: all six) |
| `vco.min_version` | string | minimum VCO version this project requires |
| `author.email` | string | author contact |

## Memory model

VCO preserves project knowledge in structured, intentional memory, not one giant dump.

### Current state

- `.vco/state.json` — machine-readable summary
- `PROJECT_STATE.md` — human and agent-readable answers to the 9 state questions

### Decisions

- `.vco/decisions/adr-XXXX-*.md` — Architecture Decision Records; settled, not re-litigated

### Context

- `.vco/context/*.md` — focused indexes that help an agent find the right rules, ADRs, and files for a task

### Verification

- `.vco/verification/*.md` — records of evidence: commands, results, and PASS/FAIL status

### Requirements & tasks

- `REQUIREMENTS.md` — the what and why
- `TASKS.md` — the execution plan and current status

## Roadmap (documented, not implemented in 0.1)

- **0.2 — CLI:** `vco init`, `vco context`, `vco plan` — spec only in `packages/cli/README.md`
- **0.3 — Context engine:** intelligent, focused context retrieval
- **0.4 — Agent adapters:** first-class Devin / Claude / Codex / Cursor integrations
- **0.5 — Cryptographic provenance:** `vco sign` and `vco verify-signature` using established libraries
- **1.0 — Stable ecosystem:** stable protocol and tooling
