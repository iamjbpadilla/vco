# Security Rules

This rule answers: **what process-level security obligations apply to every VCO project?**

These are process requirements. Application-specific security requirements belong in the project's own `REQUIREMENTS.md` — agents must not invent them.

## Secrets

- Never hard-code secrets, keys, or tokens in source, config committed to git, logs, or documentation.
- Never print or echo secret values in command output or reports.
- Use the project's designated secret store or environment mechanism.

## Authentication & authorization

- Never weaken, bypass, or stub out authentication or authorization to make something work, even temporarily, without explicit authorization.
- Authorization checks belong on the server/trusted side, never only in the client.

## Input validation & injection

- Validate and constrain all external input at the trust boundary.
- Use parameterized queries / prepared statements; never build queries, shell commands, or markup by string-concatenating untrusted input.
- Encode output appropriately for its context (HTML, SQL, shell, URL).

## Dependencies & supply chain

- No new dependency without justification tied to a requirement.
- Prefer established, maintained packages; prefer versions published long enough ago to have been vetted.
- Do not disable, weaken, or bypass dependency security policies, lockfiles, or integrity checks to fix a build.

## Sensitive information

- Do not log personal data, credentials, or tokens.
- Do not copy production data into tests, fixtures, or documentation.

## Logging & error handling

- Log security-relevant events (auth failures, permission denials) without logging secrets.
- Error messages shown to users must not leak internals (stack traces, paths, queries).
- Fail closed: on error in a security check, deny.

## Access control

- Follow least privilege for services, tokens, and CI credentials.
- Never broaden permissions/scopes as a convenience fix.

## Agent obligations

- Security review is a verification gate where the profile requires it (see [testing.md](testing.md)).
- On discovering a vulnerability, report it immediately as a finding — do not silently patch it (the fix still goes through change control) and do not exploit it.
