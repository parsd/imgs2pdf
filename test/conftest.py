"""Fixtures for the tests."""

import pathlib
import re
from typing import Sequence

import pytest  # type: ignore


THIS_DIR = pathlib.Path(__file__).resolve().parent
CREATION_DATE_RE = re.compile(rb"CreationDate \(D:[0-9]+\)")


@pytest.fixture
def images() -> Sequence[pathlib.Path]:
    """Get the test images."""
    return [
        THIS_DIR / "200x320.png",
        THIS_DIR / "320x200.png",
        THIS_DIR / "480x640.png",
        THIS_DIR / "595x842.png",
    ]


def remove_creation_date(pdf_data: bytes) -> bytes:
    """Masks out the creation date to be able to compare against stored reference."""
    return CREATION_DATE_RE.sub(b"CreationDate (D:00000000000000)", pdf_data)
