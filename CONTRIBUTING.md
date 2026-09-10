# Contributing to VCO

VCO practices what it specifies: contributions follow the VCO change-control process.

## Before you start

1. Read [`AGENTS.md`](AGENTS.md), [`SCOPE.md`](SCOPE.md), and [`docs/philosophy.md`](docs/philosophy.md).
2. Check `REQUIREMENTS.md` and open issues — the change may already be tracked or already rejected.

## Process

All changes — human or AI-authored — follow the change-control lifecycle:

```text
PROPOSED → REVIEWED → APPROVED → PLANNED → IMPLEMENTED → VERIFIED
```

1. **Propose.** Open an issue using the feature request or bug report template. For non-trivial changes, fill in [`templates/CHANGE_REQUEST.md`](templates/CHANGE_REQUEST.md) in the issue body.
2. **Wait for approval** before opening a pull request. Unapproved scope expansion is closed without review.
3. **Implement** in a branch: smallest correct change, existing patterns first, no unrelated edits, no new dependencies without justification.
4. **Verify.** CI must pass. Include evidence in the PR description (what you checked and the observed results), not just claims.
5. **Report** in the PR: changes, non-changes, assumptions, unknowns, verification, remaining risks.

## Standards

- Documentation answers a clear question; no marketing fluff, no repetition, no contradictory terminology.
- Version references stay consistent with the current release.
- Anything that touches settled architecture requires a new ADR proposal (see `.vco/decisions/`).
- Never rewrite git history on shared branches.

## Out of scope for 0.x contributions

Implementations of the CLI, context engine, dashboards, hosted services, or cryptographic signing — these are roadmap items (see [CHANGELOG.md](CHANGELOG.md)) and are documented, not built, in 0.1.
