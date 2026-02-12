# Reusable Workflows

This repository defines reusable workflows for use within Globus.

## Workflows

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
    uses: globus/workflows/.github/workflows/pr_has_changelog.yaml@v1
```


### tox

Run tox quickly and reproducibly. Includes caching.

This workflow is [documented](https://github.com/kurtmckee/github-workflows/blob/main/docs/tox.rst) at its source.
It is copied here for convenient administration and business continuity.
It is strongly recommended that changes be made via PRs in the source repo.


### create-pr

Run a tox label and create a PR from the resulting changes.

Use this workflow to collect changelog fragments and prepare a release PR,
or to perform automated updates to tools and dependencies in a repository.

This workflow is [documented at its source](https://github.com/kurtmckee/github-workflows/blob/main/docs/create-pr.rst).
It is copied here for convenient administration and business continuity.
It is strongly recommended that changes be made via PRs in the source repo.


### create-tag-and-release

Create an annotated git tag and a GitHub release.

Use this workflow to update the state of the repository
when merging to a release branch.

This workflow is [documented at its source](https://github.com/kurtmckee/github-workflows/blob/main/docs/create-tag-and-release.rst).
It is copied here for convenient administration and business continuity.
It is strongly recommended that changes be made via PRs in the source repo.


### build-python-package

Build a Python package using the `build` module and upload an artifact.

Use this workflow just prior to pushing built packages to PyPI.

This workflow is [documented at its source](https://github.com/kurtmckee/github-workflows/blob/main/docs/build-python-package.rst).
It is copied here for convenient administration and business continuity.
It is strongly recommended that changes be made via PRs in the source repo.
