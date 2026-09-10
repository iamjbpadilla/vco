# Deployment & Shipping

This rule answers: **when may work be released, and how?**

## The prime rule

> **Ship only verified work.**

Nothing reaches a release, tag, or production deployment unless it is VERIFIED per [verity.md](verity.md) and [testing.md](testing.md). "It worked locally" is not a release criterion.

## Release gates

A release proceeds through explicit gates, each producing evidence:

```text
ALL IN-SCOPE WORK VERIFIED
↓
CLEAN WORKING TREE (no temp files, debug artifacts, secrets, generated junk)
↓
CI PASS ON THE EXACT RELEASE COMMIT
↓
CHANGELOG UPDATED
↓
VERSION CONSISTENT EVERYWHERE
↓
TAG / RELEASE
```

- Never tag a release if CI has not passed on the exact commit being tagged.
- Local validation and remote CI are **separate evidence sources**; both are recorded. Remote CI is authoritative for the release gate.
- A red pipeline blocks release. Fix forward, re-verify, then release.

## Rollback thinking

Before shipping, know the answer to: *how is this undone if it is wrong?* If a change cannot be rolled back (data migrations, irreversible external calls), it requires explicit human authorization and extra verification, not less.

## Environments

- Configuration differs per environment; code does not silently branch on environment to hide problems.
- Never test in production. Never point development tooling at production data stores without explicit authorization.

## Agent obligations

- In `ship` mode ([skills/ship/SKILL.md](../skills/ship/SKILL.md)), verify the gates in order and stop at the first failure.
- Report the release evidence: commit hash, CI run result, version, changelog entry.
- Do not create a release while any critical verification is failing — no exceptions.
