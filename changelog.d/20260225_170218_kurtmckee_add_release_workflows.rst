Breaking changes
----------------

*   ``tox``: Add a ``timeout-minutes`` key for configuring job timeouts.

    Jobs now timeout after 15 minutes by default.

Added
-----

*   Introduce a ``create-pr`` workflow.

    This workflow runs a tox label, commits the changes, and opens a PR.

*   Introduce a ``create-tag-and-release`` workflow.

    This workflow creates an annotated git tag and a GitHub release.

*   Introduce a ``build-python-package`` workflow.

    This workflow builds a Python package and uploads an artifact.

Changed
-------

*   Lock almost all software dependencies.
*   Update all software dependencies.

Documentation
-------------

*   Add extensive documentation for almost all of the workflows.

Development
-----------

*   Use templates to generate standalone reusable workflow files.

    Now, instead of disallowing edits to portions of the workflows,
    the underlying templates are fully editable.

*   Use prek to update pre-commit hook versions.

*   Wholesale copy all of the infrastructure from ``kurtmckee/github-workflows``.

    This ensures that this repo can evolve independently as needed.
