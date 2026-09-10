<p align="center">
  <img src="assets/logo.png" alt="VCO logo" width="180" />
</p>

# VCO · Verity Coding OS

**Version 0.1.0**

> Build with AI. Verify everything.

## About

VCO is a development operating system and protocol for AI-assisted software engineering. It governs the environment in which AI coding agents operate: scope, requirements, memory, decisions, tasks, and verification.

VCO is **not** an AI model, a coding assistant, a SaaS dashboard, an IDE, or a replacement for your agent or for Git. It is the verification layer around them.

Latest release: [`v0.1.0`](https://github.com/iamjbpadilla/vco/releases/tag/v0.1.0)

## The model

```text
Human
  ↓
Intent
  ↓
Specification
  ↓
VCO
  ├── Rules
  ├── Scope
  ├── Requirements
  ├── Memory
  ├── Architecture
  ├── Decisions
  ├── Tasks
  └── Verification
        ↓
     AI Agent
        ↓
      Code
        ↓
    Evidence
        ↓
     Verified
```

Core principle:

> **AI may implement what is known. AI must not invent what is unknown.**

Core distinction:

```text
CONFIDENCE ≠ EVIDENCE
```

An agent saying "this should work" is not verification. Evidence comes from observable results: typecheck output, test results, build logs, review records. VCO separates `IMPLEMENTED` from `VERIFIED`, and evidence produces PASS — never the other way around.

## Get it

No package manager install is needed for VCO 0.1. It is a file-based protocol.

```bash
git clone https://github.com/iamjbpadilla/vco.git
cd vco

# Copy templates and the .vco skeleton into your project
cp templates/* /path/to/my-project/
mkdir -p /path/to/my-project/.vco/{decisions,context,verification}
cp .vco/manifest.json /path/to/my-project/.vco/
```

## Quickstart

1. Read the [Getting Started guide](docs/getting-started.md).
2. Edit the templates you copied into your project.
3. Create `.vco/manifest.json` for your project (schema in [docs/architecture.md](docs/architecture.md)).
4. Choose a [profile](profiles/).
5. Point your AI agent at your project's `AGENTS.md` and work through the six modes: `plan → build → test → review → audit → ship`.

## Repository contents

| Path | Purpose |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | The Agent Constitution — rules every agent must follow |
| [`SKILL.md`](SKILL.md) | Entry-point skill: how an agent adopts VCO |
| [`rules/`](rules/) | The core protocol rules (verity, scope, security, testing, …) |
| [`skills/`](skills/) | The six agent modes: plan, build, test, review, audit, ship |
| [`templates/`](templates/) | Files you copy into your own project |
| [`profiles/`](profiles/) | Recommended practices per project type |
| [`docs/`](docs/) | Guide, philosophy, architecture, workflow, agent compatibility |
| [`packages/cli/`](packages/cli/) | Future CLI (specification only — not implemented in 0.1) |

## Compatible agents

VCO is agent-agnostic. It works with Devin, Claude, Codex, Cursor, and any agent that can read project files. See [docs/agent-compatibility.md](docs/agent-compatibility.md).

## Roadmap

VCO 0.1 is the protocol foundation. Future versions (documented, not implemented): CLI tooling, context engine, agent adapters, cryptographic provenance. See [CHANGELOG.md](CHANGELOG.md) and [packages/cli/README.md](packages/cli/README.md).

## License

[MIT](LICENSE)

---

```text
────────────────────────────────

VCO · Verity Coding OS

Created and maintained by

Jubet M. Padilla
Systems Engineer • AI Specialist

────────────────────────────────
```

*This block is authorship metadata, not cryptographic proof of origin.*
