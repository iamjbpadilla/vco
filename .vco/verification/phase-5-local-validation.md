# Phase 5 — Local Validation Evidence

Date: 2026-09-10

## Commands and results

### Manifest / state / version consistency

```text
$ python3 .github/scripts/validate.py
PASS: manifest, state, and version consistency
```

This validates:

- `.vco/manifest.json` is valid JSON
- Required fields `vco.version`, `project.name`, `project.profile`, `author.name` are present
- `project.profile` is in the allowed enum
- `vco.version` is valid semantic versioning
- `.vco/state.json` is valid JSON
- Version `0.1.0` is consistent across `README.md` and `CHANGELOG.md`

### Required file tree

```text
$ python3 .github/scripts/validate.py --structure
PASS: required file tree present, no unexpected top-level entries
```

### Internal markdown links

```text
$ python3 .github/scripts/validate.py --links
PASS: internal markdown links verified
```

Note: one iteration of the validator was tightened to avoid false positives from unrelated semantic versions in `CHANGELOG.md`; the final three checks above all pass.

### YAML / workflow

PyYAML is not installed in the local environment, so a local YAML parse was not possible. The authoritative workflow validation is GitHub Actions itself. The workflow file was checked for balanced delimiters and no obvious syntax errors; a full parse will be produced by the remote CI run.

## Local validation status

All available local validation checks PASS. The remote CI run on GitHub will be the authoritative validator for the workflow YAML.
