<p align="center">
  <img src="assets/logo.png" alt="VCO logo" width="140" />
</p>

<h1 align="center">VCO · Verity Coding OS</h1>

<p align="center"><strong>Build with AI. Verify everything.</strong></p>

<p align="center">
  <a href="https://github.com/iamjbpadilla/vco/releases/tag/v0.1.0">Latest release: v0.1.0</a> ·
  <a href="LICENSE">MIT License</a>
</p>

---

## What VCO is

VCO is a development operating system and protocol for AI-assisted software engineering. It governs the environment in which AI coding agents operate: scope, requirements, memory, architecture, decisions, tasks, and verification.

VCO is **not** an AI model, a coding assistant, a SaaS dashboard, an IDE, or a replacement for your agent or for Git. It is the verification layer around them.

## Why VCO exists

AI agents can implement fast. They can also invent, assume, and over-reach. VCO gives them a structured contract to follow.

Core principle:

> **AI may implement what is known. AI must not invent what is unknown.**

Core distinction:

> **CONFIDENCE ≠ EVIDENCE**

An agent saying "this should work" is not verification. Evidence comes from observable results: typecheck output, test results, build logs, review records. VCO separates `IMPLEMENTED` from `VERIFIED`, and evidence produces PASS — never the other way around.

## How it works

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

## Get VCO

VCO 0.1 is a file-based protocol. No package manager install is required.

```bash
git clone https://github.com/iamjbpadilla/vco.git
cd vco

# Copy the templates and .vco skeleton into your project
cp templates/* /path/to/my-project/
mkdir -p /path/to/my-project/.vco/{decisions,context,verification}
cp .vco/manifest.json /path/to/my-project/.vco/
```

## Start using VCO

1. Read the [Getting Started guide](docs/getting-started.md).
2. Fill in the templates you copied into your project.
3. Create your project's `.vco/manifest.json` (schema in [docs/architecture.md](docs/architecture.md)).
4. Choose a [project profile](profiles/).
5. Point your AI agent at your project's `AGENTS.md` and run through the six modes:

```text
plan → build → test → review → audit → ship
```

## What is in this repository

| Path | Purpose |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | The Agent Constitution — rules every agent must follow |
| [`SKILL.md`](SKILL.md) | Entry-point skill: how an agent adopts VCO |
| [`rules/`](rules/) | The core protocol rules: verity, scope, security, testing, and more |
| [`skills/`](skills/) | The six agent mode contracts: plan, build, test, review, audit, ship |
| [`templates/`](templates/) | Files you copy into your own project |
| [`profiles/`](profiles/) | Recommended practices per project type |
| [`docs/`](docs/) | Guides: philosophy, architecture, workflow, agent compatibility, getting started |
| [`packages/cli/`](packages/cli/) | Future CLI specification — not implemented in 0.1 |

## Agent compatibility

VCO is agent-agnostic. It works with Devin, Claude, Codex, Cursor, and any agent that can read project files. See [docs/agent-compatibility.md](docs/agent-compatibility.md) for setup notes per agent.

## Roadmap

VCO 0.1 is the protocol foundation. Future versions (documented, not implemented): CLI, context engine, agent adapters, cryptographic provenance. See [CHANGELOG.md](CHANGELOG.md) and [packages/cli/README.md](packages/cli/README.md).

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
