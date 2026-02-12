# CHANGELOG

## v2.0

### `tox.yaml`

_Copied from v1.8 in its source repo._

- Add a `timeout-minutes` key for configuring job timeouts.
  Jobs now timeout after 15 minutes by default.

### `create-pr`

_Copied from v1.8 in its source repo._

- Runs a tox label, commits the changes, and opens a PR.

### `create-tag-and-release`

_Copied from v1.8 in its source repo._

- Creates an annotated git tag and a GitHub release.

### `build-python-package`

_Copied from v1.8 in its source repo._

- Builds a Python package and uploads an artifact.

## v1.4

### `tox.yaml`

- Separate tox environment creation from execution.
- Add the tox-gh plugin to group tox environment output.
- Update check-jsonschema to v0.35.0.
- Use uv for venv creation and check-jsonschema execution.

## v1.3

### `pr_has_changelog.yaml`

- Add `skip-users`, `changelog-type`, and `base-branch` workflow call arguments.
- Update action versions.

### `tox.yaml`

- Add `tox-skip-environments` and `tox-skip-environments-regex` config inputs.
- Update action versions.

## v1.2

- Update `actions/cache` versions to resolve test suite failures.

## v1.1

### `tox.yaml`

- Initial version.

## v1.0

- Rename repository from `globus/reusable-workflows` to `globus/workflows`.
