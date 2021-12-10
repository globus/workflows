# Reusable Workflows

This repository defines reusable workflows for use within Globus.

## Workflows

### run_tox

Checkout, then install and run tox with specified options.

Usage example:

```yaml
name: build
on:
  push:
  pull_request:
jobs:
  lint:
    uses: globus/reusable-workflows/.github/workflows/run_tox.yaml@v1
    with:
      python-version: "3.10"
      tox-env: lint
```

Supported inputs:

- `python-version` (required): python version to use
- `tox-env`: the tox environment to run, defaults to `py` (which runs tests
    under `python-version` for most tox configs)
- `runs-on`: a runner to use, defaults to ubuntu-latest
- `tox-command`: an alternate invocation of `tox`
- `args`: arguments to pass to tox *after* the env

### pr_has_changelog

Check if a PR has changelog fragments in `changelog.d/`, identified as new
files with a desired suffix (`.md`).

Usage example:

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
