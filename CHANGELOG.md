# CHANGELOG

The changelog is continuous. All changes are made to the current version branch.

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
