"""imgs2pdf integration test package.

Ensures that pytest finds the package.
"""

import sys
import pathlib

sys.path.insert(
    0, str(pathlib.Path(__file__).resolve().parent.parent),
)
