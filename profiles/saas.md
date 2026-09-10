# Profile: saas

A VCO profile for multi-tenant software-as-a-service products with accounts, billing, and operations.

## What this profile means

SaaS adds operational, security, and compliance risk. This profile includes the full default verification chain and expects strong evidence around auth, data isolation, and payments.

## Typical recommended stack (non-mandatory)

- TypeScript
- React / Next.js or equivalent frontend
- Node / Python / Go / other backend
- PostgreSQL
- Auth provider or OIDC
- Stripe or equivalent billing
- Monitoring and alerting

## Default verification gate matrix

| Gate | Required | Notes |
| --- | --- | --- |
| TYPECHECK | yes | Full type check across services |
| LINT | yes | Lint / format |
| UNIT | yes | Unit tests |
| INTEGRATION | yes | Service-to-service and API integration |
| E2E | yes | Critical business flows, including auth and billing |
| BUILD | yes | Production build / container build |
| SECURITY | yes | Auth, authorization, tenant isolation, dependency, and secret scans |
| VISUAL QA | yes | Core UI / UX flows, responsive, a11y |
| COMPLIANCE | recommended | Any required checks (SOC2, GDPR, PCI, etc.) |

## Project-specific additions

A SaaS project should add to its own `REQUIREMENTS.md`:

- Multi-tenant data isolation
- AuthN/AuthZ model and test coverage
- Billing flow and idempotency
- Observability (logging, metrics, alerts)
- Backup and disaster recovery
- Onboarding and offboarding paths

## Omissions

This is not a compliance framework. Use specialist guidance where legal or regulatory certification is required.
