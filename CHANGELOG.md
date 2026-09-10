# Changelog

All notable changes to VCO are documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and VCO adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-09-10

Initial release: the VCO protocol foundation.

### Added

- Agent Constitution (`AGENTS.md`) and entry-point skill (`SKILL.md`)
- Protocol rules: core, verity, scope, architecture, design, security, testing, deployment (`rules/`)
- Six agent modes: plan, build, test, review, audit, ship (`skills/`)
- Project templates: AGENTS, PROJECT_STATE, SCOPE, REQUIREMENTS, TASKS, CHANGE_REQUEST, ADR (`templates/`)
- Project profiles: web, pwa, mobile, saas, api, internal-tool (`profiles/`)
- Documentation: getting started, philosophy, architecture (incl. manifest schema and memory model), workflow, agent compatibility (`docs/`)
- CI validation: manifest structure, repository structure, internal links (`.github/`)
- Self-governance (dogfood) layer: `.vco/`, `PROJECT_STATE.md`, `SCOPE.md`, `REQUIREMENTS.md`, `TASKS.md`

### Documented but not implemented (future roadmap)

- 0.2 — CLI tooling (`vco init`, `vco context`) — spec in `packages/cli/README.md`
- 0.3 — Context engine
- 0.4 — Agent adapters
- 0.5 — Cryptographic provenance (`vco sign`, `vco verify-signature`)
- 1.0 — Stable ecosystem
