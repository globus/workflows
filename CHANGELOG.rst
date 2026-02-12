..
    This file is a part of the Globus GitHub Workflows project.
    https://github.com/globus/workflows
    Copyright 2021-2026 Globus <support@globus.org>
    Copyright 2024-2026 Kurt McKee <contactme@kurtmckee.org>
    SPDX-License-Identifier: MIT


Globus GitHub Workflows
#######################

Unreleased changes
==================

Unreleased changes to the code are documented in
`changelog fragments <https://github.com/globus/workflows/tree/main/changelog.d/>`_
in the ``changelog.d/`` directory on GitHub.

..  scriv-insert-here

.. _changelog-1.4:

1.4 — 2026-01-05
================

``tox.yaml``
------------

- Separate tox environment creation from execution.
- Add the tox-gh plugin to group tox environment output.
- Update check-jsonschema to v0.35.0.
- Use uv for venv creation and check-jsonschema execution.

.. _changelog-1.3:

1.3 — 2025-10-03
================

``pr_has_changelog.yaml``
-------------------------

- Add ``skip-users``, ``changelog-type``, and ``base-branch`` workflow call arguments.
- Update action versions.

``tox.yaml``
------------

- Add ``tox-skip-environments`` and ``tox-skip-environments-regex`` config inputs.
- Update action versions.

.. _changelog-1.2:

1.2 — 2025-03-04
================

- Update ``actions/cache`` versions to resolve test suite failures.

.. _changelog-1.1:

1.1 — 2024-11-05
================

``tox.yaml``
------------

- Initial version.

.. _changelog-1.0:

1.0 — 2021-12-10
================

- Rename repository from ``globus/reusable-workflows`` to ``globus/workflows``.
