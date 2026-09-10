# Testing & Verification

This rule answers: **which checks must pass, and when, for work to become VERIFIED?**

## The default verification chain

```text
IMPLEMENTED
↓
TYPECHECK
↓
LINT
↓
UNIT
↓
INTEGRATION
↓
E2E
↓
BUILD
↓
SECURITY
↓
VISUAL QA
↓
VERIFIED
```

Every gate that applies must produce recorded evidence ([verity.md](verity.md)) before the work is VERIFIED.

## Risk-based, profile-scoped

Verification is risk-based, not ritual. Profiles ([profiles/](../profiles/)) declare which gates apply by default for that project type; individual requirements may add gates when their risk warrants it.

- Do not blindly require every gate for every project. A docs-only package has no E2E suite; an API has no Visual QA.
- Omitting a gate is a documented decision (in the profile or the project's `SCOPE.md`/requirements), never a silent skip.
- Higher-risk changes (auth, payments, data migration, public interfaces) warrant more gates, not fewer.

## Test-first preference

Where test infrastructure exists, prefer demonstrating a bug with a failing test before fixing it, and prove the fix by the test passing. The failing→passing transition is strong evidence.

## Agent obligations

- Run the gates; do not simulate them. "The tests would pass" is confidence, not evidence.
- Record exact commands and observed results in `.vco/verification/`.
- A gate that cannot be run (missing infrastructure, broken environment) is reported as a blocker — it does not default to PASS.
- Never delete, skip, or weaken a failing test to make the chain green without explicit authorization.
