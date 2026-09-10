# Profile: internal-tool

A VCO profile for tools used inside an organization: scripts, CLI tools, dashboards, bots, documentation packages, and similar.

## What this profile means

Internal tools can relax some gates compared to customer-facing products, but they must still separate `IMPLEMENTED` from `VERIFIED` and record evidence. VCO itself uses this profile.

## Typical recommended stack (non-mandatory)

- Python, TypeScript, Go, Rust, or Bash as appropriate
- CLI libraries (Click, Commander, Cobra, clap)
- Markdown or simple web interface
- SQLite, flat files, or existing internal data stores

## Default verification gate matrix

| Gate | Required | Notes |
| --- | --- | --- |
| TYPECHECK | yes | When applicable to the language |
| LINT | yes | Lint / format, if a linter exists |
| UNIT | recommended | Unit tests for non-trivial logic |
| INTEGRATION | if used | Test against the systems it touches |
| BUILD | yes | The tool runs/builds correctly in the target environment |
| SECURITY | yes | No secrets in code, input validation where applicable |
| VISUAL QA | no | Not applicable unless the tool has a UI; then use `web` |

## Project-specific additions

An internal-tool project should add to its own `REQUIREMENTS.md`:

- Target users and environment
- Input/output contract or CLI interface
- Installation and run instructions
- Operational dependencies (credentials, APIs, network)

## Omissions

User-facing polish, public accessibility, and multi-tenancy are not assumed. Add them explicitly if the tool needs them.
