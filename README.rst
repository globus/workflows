..
    This file is a part of the Globus GitHub Workflows project.
    https://github.com/globus/workflows
    Copyright 2021-2026 Globus <support@globus.org>
    Copyright 2024-2026 Kurt McKee <contactme@kurtmckee.org>
    SPDX-License-Identifier: MIT


Globus GitHub Workflows
#######################

*Reusable workflows that reduce maintenance effort.*

---------------------------------------------------------------------------

This repo centralizes Globus' public GitHub workflows.

In many cases, workflows in other Globus repositories can be minimized
to a set of configuration values and a reference to the workflows here.


Table of contents
=================

*   `pr_has_changelog`_
*   `tox`_
*   `create-pr`_
*   `create-tag-and-release`_
*   `build-python-package`_


pr_has_changelog
================

Check if a PR has changelog fragments in ``changelog.d/``, identified as new
files with a desired suffix (``.md``).

Usage example:

..  code-block:: yaml

    name: Validate main PR

    on:
      pull_request:
        branches:
          - main

    jobs:
      check_changelog:
        uses: globus/workflows/.github/workflows/pr_has_changelog.yaml@v2


tox
===

`Workflow documentation <docs/tox.rst>`__

The ``tox.yaml`` workflow captures hard-earned lessons for running tox in CI
to optimize test suite execution, including tools, plugins, and caching.

..  code-block:: yaml

    name: "🧪 Test"

    on:
      pull_request:
      push:
        branches:
          - "main"

    jobs:
      test:
        permissions:
          contents: "read"
        strategy:
          matrix:
            runner:
              - "ubuntu-latest"
              - "macos-latest"
              - "windows-latest"

            # The single value in this `include` section will be added to each runner.
            include:
              - cpythons:
                  - "3.10"
                  - "3.11"
                  - "3.12"
                  - "3.13"
                  - "3.14"
                cpython-beta: "3.15"

        uses: "globus/workflows/.github/workflows/tox.yaml@???"
        with:
          config: "${{ toJSON(matrix) }}"


create-pr
=========

`Workflow documentation <docs/create-pr.rst>`__

The ``create-pr.yaml`` workflow cuts release PRs.
It helps kick off an automated release process.

..  code-block:: yaml

    name: "✨ Prep release"
    on:
      workflow_dispatch:
        inputs:
          version:
            description: "The version to release"
            type: "string"
            required: true

    jobs:
      prep-release:
        name: "Prep release v${{ inputs.version }}"

        permissions:
          contents: "write"
          pull-requests: "write"

        strategy:
          matrix:
            include:
              - branch-name: "release/$VERSION"
                commit-title: "Update project metadata for v$VERSION"
                pr-title: "Release v$VERSION"
                tox-label-create-changes: "prep-release"

        uses: "globus/workflows/.github/workflows/create-pr.yaml@???"
        with:
          config: "${{ toJSON(matrix) }}"
          version: "${{ inputs.version }}"


create-tag-and-release
======================

`Workflow documentation <docs/create-tag-and-release.rst>`__

The ``create-tag-and-release.yaml`` workflow creates a git tag and a GitHub release.
It adds the version's changelog fragment as the release body.

..  code-block:: yaml

    name: "🏷️ Tag and release"
    on:
      push:
        branches:
          - "releases"

    jobs:
      tag:
        name: "Tag and release"

        permissions:
          contents: "write"

        uses: "globus/workflows/.github/workflows/create-tag-and-release.yaml@..."


build-python-package
====================

`Workflow documentation <docs/build-python-package.rst>`__

The ``build-python-package.yaml`` workflow builds a Python sdist and wheel,
and uploads a GitHub artifact containing these.
It helps make automated releases to PyPI trivial.

..  code-block:: yaml

    name: "📦 Publish"
    on:
      push:
        branches:
          - "releases"

    jobs:
      build:
        name: "Build"

        permissions:
          contents: "read"

        uses: "globus/workflows/.github/workflows/build-python-package.yaml@..."

      publish:
        name: "Publish"
        needs:
          - "build"
        runs-on: "ubuntu-24.04"
        environment: "PyPI"
        permissions:
          id-token: "write"
        steps:
          - name: "Download artifact"
            uses: "actions/download-artifact@..."
            with:
              artifact-ids: "${{ needs.build.outputs.artifact-id }}"
              path: "${{ needs.build.outputs.packages-path }}"

          - name: "Publish package distributions to PyPI"
            uses: "pypa/gh-action-pypi-publish@???"
            with:
              packages-dir: "${{ needs.build.outputs.packages-path }}"
