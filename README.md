# Reusable Workflows

This repository defines reusable workflows for use within Globus.

## Workflows

### pr_has_changelog

Check if a PR has changelog fragments in `changelog.d/`, identified as new
files with a desired suffix (`.md`).

Usage:

```yaml
name: Validate main PR

on:
  pull_request:
    branches:
      - main

jobs:
  check_changelog:
    uses: globus/reusable-workflows/.github/workflows/pr_has_changelog.yaml@v1
```

## Versioning

Versions are maintained as branches (v1, v2, etc) of the repo.

A new version is created whenever the behaviors of the branch change in a way
that is backwards incompatible.

### Versioning Prior to v1.0

Until a version can be tagged as "v1.0", the main development branch will be
"v1". Until that time, the interface provided by these workflows may change as
necessary.
