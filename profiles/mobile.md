# Profile: mobile

A VCO profile for native or near-native mobile applications (iOS, Android, or cross-platform).

## What this profile means

This profile adds gates for native platforms, app store policies, and device-specific behavior. VCO is not tied to a framework; use any stack that can satisfy the gates.

## Typical recommended stack (non-mandatory)

- Swift / SwiftUI (iOS)
- Kotlin / Jetpack Compose (Android)
- React Native / Expo
- Flutter

## Default verification gate matrix

| Gate | Required | Notes |
| --- | --- | --- |
| TYPECHECK | yes | Type check / compile |
| LINT | yes | Lint / static analysis |
| UNIT | yes | Unit tests |
| INTEGRATION | yes | Module and API integration |
| E2E | yes | Device / simulator critical flows |
| BUILD | yes | Archive / app bundle build |
| SECURITY | yes | Dependency scan, secret scan, keychain/sandbox review |
| VISUAL QA | yes | Screenshots on target device sizes, dark mode, a11y |
| STORE | recommended | App store policy and metadata check |

## Project-specific additions

A mobile project should add to its own `REQUIREMENTS.md`:

- Supported OS versions
- Permissions rationale and approval flow
- Offline behavior
- App store metadata and review prep

## Omissions

Server-side infrastructure is not this profile's primary focus; use `api` or `saas` if the project has a significant backend.
