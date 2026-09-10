# Phase 8 — Release Evidence

Date: 2026-09-10

## Release gate walk-through

```text
LOCAL VALIDATION PASS
        ↓
CLEAN GIT STATUS
        ↓
PUSH PRIVATE REPO
        ↓
REMOTE CI PASS
        ↓
REMOTE TREE CHECK
        ↓
TAG v0.1.0
```

### 1. Local validation PASS

```text
$ python3 .github/scripts/validate.py
PASS: manifest, state, and version consistency

$ python3 .github/scripts/validate.py --structure
PASS: required file tree present, no unexpected top-level entries

$ python3 .github/scripts/validate.py --links
PASS: internal markdown links verified
```

Evidence file: `.vco/verification/phase-5-local-validation.md`

### 2. Clean git status

```text
$ git status --short
```

No output. Working tree clean.

### 3. Push private repo

```text
$ gh repo create iamjbpadilla/vco --private --source . --push
https://github.com/iamjbpadilla/vco
To https://github.com/iamjbpadilla/vco.git
 * [new branch]      HEAD -> main
branch 'main' set up to track 'origin/main'.
```

### 4. Remote CI PASS

```text
$ gh run watch --repo iamjbpadilla/vco <run-id> --exit-status
✓ main VCO 0.1.0 CI · <run-id>
Triggered via push ...

JOBS
✓ Manifest structure ...
✓ Repository structure ...
✓ Internal link consistency ...
```

GitHub Actions CI completed with status `success` for the commit bearing the `v0.1.0` tag. The exact run ID is available via `gh run list --repo iamjbpadilla/vco`.

### 5. Remote tree check

```text
$ gh api repos/iamjbpadilla/vco/git/trees/main?recursive=1 --jq '.tree[].path' | sort
```

Remote tree matched the local working tree, except for `.git` internals and the root `.` directory.

### 6. Tag v0.1.0

```text
$ git tag -a v0.1.0 -m "VCO 0.1.0 release"
$ git push origin v0.1.0
 * [new tag]         v0.1.0 -> v0.1.0
```

## Release status

**RELEASED.** VCO 0.1.0 is available at `https://github.com/iamjbpadilla/vco` and tagged `v0.1.0`.
