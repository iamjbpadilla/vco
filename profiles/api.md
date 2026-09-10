# Profile: api

A VCO profile for HTTP / gRPC / GraphQL / event-driven API services.

## What this profile means

APIs have no UI, so Visual QA is usually omitted. Verification focuses on contracts, serialization, error behavior, and integration. Technology is not mandated.

## Typical recommended stack (non-mandatory)

- TypeScript, Go, Python, Rust, or equivalent
- OpenAPI / protobuf / GraphQL schema
- PostgreSQL or a persistence layer
- zod, valibot, joi, or equivalent for validation

## Default verification gate matrix

| Gate | Required | Notes |
| --- | --- | --- |
| TYPECHECK | yes | Compile / type check |
| LINT | yes | Lint / format |
| UNIT | yes | Unit tests |
| INTEGRATION | yes | Endpoints / handlers against real or test deps |
| CONTRACT | yes | OpenAPI / schema / type definitions match implementation |
| E2E | recommended | Full request flows against a running service |
| BUILD | yes | Container or binary build |
| SECURITY | yes | Input validation, auth, dependency, and secret checks |
| VISUAL QA | no | Not applicable; use contract or documentation review instead |

## Project-specific additions

An API project should add to its own `REQUIREMENTS.md`:

- Endpoint / operation list
- Auth and rate-limiting strategy
- Input validation and error response contracts
- Backward-compatibility policy
- Documentation generation and accuracy

## Omissions

Frontend concerns are not this profile's focus; use `web` or `saas` if there is a UI.
