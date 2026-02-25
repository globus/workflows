# This file is a part of the Globus GitHub Workflows project.
# https://github.com/globus/workflows
# Copyright 2021-2026 Globus <support@globus.org>
# Copyright 2024-2026 Kurt McKee <contactme@kurtmckee.org>
# SPDX-License-Identifier: MIT

import pathlib
import sys

# Add the `src/` directory to the Python path.
src_path = pathlib.Path(__file__).parent.parent / "src"
sys.path.append(str(src_path))
