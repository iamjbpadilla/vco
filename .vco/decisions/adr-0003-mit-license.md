# ADR-0003

## Title

MIT License

## Status

Accepted

## Context

VCO's templates, manifest schema, and rules are designed to be copied into users' projects. The license must not obstruct that. The package is expected to eventually include a CLI under `packages/cli/`, but even then it should remain permissive.

## Decision

License VCO 0.1.0 under the MIT License.

## Alternatives Considered

- **Apache-2.0** — rejected because the patent grant adds legal text without benefit for a docs/protocol package.
- **CC-BY-4.0** — rejected because it is awkward for a package that will eventually contain code under `packages/`.

## Consequences

- Templates can be copied into proprietary projects with attribution only.
- Future CLI code can also be under MIT.
- The license is simple and well understood.

## Date

2026-09-10
