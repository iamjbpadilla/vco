# Profile: web

A VCO profile for traditional multi-page or single-page websites served over HTTP.

## What this profile means

This profile recommends a default set of practices and verification gates for web projects. These are recommendations, not mandates. VCO remains technology-agnostic; you may substitute any equivalent stack.

## Typical recommended stack (non-mandatory)

- TypeScript
- React or Next.js
- Tailwind CSS
- shadcn/ui or Radix UI
- Lucide icons
- Zod for schema validation
- PostgreSQL or equivalent

## Default verification gate matrix

| Gate | Required | Notes |
| --- | --- | --- |
| TYPECHECK | yes | Static type check, where applicable |
| LINT | yes | Linting / formatting check |
| UNIT | yes | Unit tests for business logic and utilities |
| INTEGRATION | yes | API or component integration tests |
| E2E | recommended | Full browser / critical-path tests |
| BUILD | yes | Production build or static export |
| SECURITY | yes | At minimum dependency scan + secret scan |
| VISUAL QA | recommended | Screenshots, responsive checks, a11y scan |

## Project-specific additions

A web project should add to its own `REQUIREMENTS.md`:

- Responsive breakpoints verified
- Keyboard navigation verified
- Focus and hover states present
- Core pages render within performance budget

## Omissions

Mobile-native APIs, offline-first architecture, and app-store distribution are not part of the default web profile; use `mobile` or `pwa` if those matter.
