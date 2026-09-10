# Tasks — VCO 0.1.0

A task is `VERIFIED` only when its evidence is recorded in `.vco/verification/`.

## Active

| Task | REQ | Status | Owner | Evidence |
| --- | --- | --- | --- | --- |
| Run validate.py (manifest, structure, links) | REQ-009, REQ-011 | TODO | — | — |
| Produce §33 audit record | REQ-014 | TODO | — | — |
| Produce §34 dogfood acceptance review | REQ-014 | TODO | — | — |
| Push to GitHub and confirm CI green | REQ-011, REQ-014 | TODO | — | — |
| Tag v0.1.0 after CI pass | REQ-015 | TODO | — | — |

## Done (VERIFIED)

| Task | REQ | Evidence |
| --- | --- | --- |
| Scaffold repo and core identity docs | REQ-001, REQ-015 | git commit 069924c |
| Add rules (8) | REQ-001, REQ-002, REQ-003, REQ-007 | git commits |
| Add templates (7) | REQ-003, REQ-010 | git commits |
| Add skills (6) | REQ-006 | git commits |
| Add profiles (6) | REQ-007, REQ-008 | git commits |
| Add docs (5 incl. getting-started) | REQ-004, REQ-005, REQ-013, REQ-016 | git commits |
| Add GitHub CI and validator | REQ-009, REQ-011 | git commit ef2894 |
| Add dogfood layer | REQ-014 | git commit (pending) |
