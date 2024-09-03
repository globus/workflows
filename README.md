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
    uses: globus/workflows/.github/workflows/pr_has_changelog.yaml@v1.0
```
