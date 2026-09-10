# Profile: pwa

A VCO profile for progressive web apps — web apps with offline, installable, and mobile-first behavior.

## What this profile means

This profile extends the `web` profile with additional gates for offline behavior, service workers, and installability. Technology suggestions are non-mandatory.

## Typical recommended stack (non-mandatory)

- TypeScript
- React / Next.js or a framework of choice
- Web app manifest
- Service Worker (Workbox or custom)
- Cache/storage strategy
- Tailwind CSS
- Zod

## Default verification gate matrix

| Gate | Required | Notes |
| --- | --- | --- |
| TYPECHECK | yes | Static type check |
| LINT | yes | Lint / format check |
| UNIT | yes | Business logic and utilities |
| INTEGRATION | yes | Component + API integration |
| E2E | yes | Critical flows in browser |
| BUILD | yes | Production build |
| OFFLINE | yes | Service worker and cache strategy tested |
| INSTALL | yes | Lighthouse PWA installability audit |
| SECURITY | yes | Dependency + secret scan |
| VISUAL QA | yes | Responsive, a11y, performance budgets |

## Project-specific additions

A PWA project should add to its own `REQUIREMENTS.md`:

- Offline fallback behavior defined
- Cache invalidation strategy documented in an ADR
- Notification and push behavior (if used) tested
- Add-to-homescreen flow verified

## Omissions

Native app stores and platform-specific native modules are not this profile's focus; use `mobile` if those matter.
