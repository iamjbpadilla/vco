# Agent Compatibility

VCO is protocol-first. The protocol is stored as files. Any AI agent that can read files can use it.

## Supported agents

The core rules do not hard-code any single agent. They reference the following adapters:

| Agent | How to load VCO | Notes |
| --- | --- | --- |
| **Devin** | `AGENTS.md` is the primary instruction file; `/vco plan`, `/vco build`, etc. map to the skills in `skills/` | VCO was originally designed for this workflow |
| **Claude / Claude Code** | Load `AGENTS.md` as project instructions; map VCO modes to custom commands or session prompts | Use `rules/` for behavior, `templates/` for project setup |
| **Codex (OpenAI)** | Provide `AGENTS.md` and `SKILL.md` as instructions; use `/vco build` as a prompt convention | API or CLI usage both possible |
| **Cursor** | Use `.cursorrules` or project instructions to reference `AGENTS.md` and `rules/` | Keep VCO files at project root |
| **Other agents** | Read `AGENTS.md` directly and follow `rules/` and `skills/` | Adapter is any mapping to the agent's own instruction format |

## The adapter concept

```text
VCO protocol (Markdown + JSON)
        ↓
Agent adapter (small mapping to agent's instruction format)
        ↓
AI Agent
```

Adapters may be:

- A project instruction file (Devin, Claude, Cursor)
- A custom slash command prefix (`/vco build`)
- A wrapper that pre-loads `AGENTS.md` before each task

VCO 0.1 does not include adapter implementations. Adapters are a roadmap item for 0.4.

## Agent-agnostic boundaries

VCO does not require:

- A specific model provider
- A specific IDE
- A specific language or framework
- A specific CI platform

The agent adapter may use any of these. The VCO files themselves are plain text.

## Getting started per agent

1. Copy `templates/` into the project root.
2. Create `.vco/manifest.json` using the schema in [architecture.md](architecture.md).
3. Fill `PROJECT_STATE.md`, `SCOPE.md`, and `REQUIREMENTS.md`.
4. In the agent's settings, load `AGENTS.md` as project instructions.
5. Work through the modes: `plan`, `build`, `test`, `review`, `audit`, `ship`.

For a fuller walkthrough, see [getting-started.md](getting-started.md).
