# ADR-0002

## Title

Markdown and JSON as the storage format

## Status

Accepted

## Context

VCO stores project memory, rules, state, requirements, tasks, decisions, and verification records. These artifacts must be human-readable, AI-readable, and versionable with Git. A database or custom binary format would add infrastructure and coupling.

## Decision

Use plain Markdown for documents and JSON for machine-readable records. Git provides history. No runtime storage is required.

## Alternatives Considered

- **SQLite / database** — rejected: adds a runtime dependency and is overkill for 0.1.
- **YAML for all files** — rejected: JSON is easier to validate deterministically; YAML supports many edge cases that produce errors.
- **Custom format** — rejected: would require parsers and tooling.

## Consequences

- Files can be edited with any editor.
- Standard `python3 -m json.tool` or equivalent validates JSON.
- CI is simple and dependency-free.
- Large binary assets (images, datasets) should not be kept in VCO memory files.

## Date

2026-09-10
