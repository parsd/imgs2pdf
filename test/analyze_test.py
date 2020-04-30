"""Integration test of the `imgs2pdf.analyze` module."""

import pathlib
from typing import Sequence

import pytest  # type: ignore

from imgs2pdf import analyze


def test_images(images: Sequence[pathlib.Path]) -> None:
    """Test that the correct image sizes are extracted from reference images."""
    reference = [
        analyze.ImagePathWithSize(file, *[int(n) for n in file.stem.split("x")])
        for file in images
    ]

    assert reference == analyze.images([str(fname) for fname in images])


def test_empty_sequence() -> None:
    """Test that an empty input sequence results in an empty output sequence."""
    result = analyze.images([])

    assert not result


def test_invalid_fname() -> None:
    """Test that an invalid file name raises an exception."""
    with pytest.raises(FileNotFoundError):
        analyze.images(["not-present-file.png"])
