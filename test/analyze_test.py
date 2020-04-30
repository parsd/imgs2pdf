"""Integration test of the `imgs2pdf.analyze` module."""

import pathlib

import pytest  # type: ignore

from imgs2pdf import analyze

THIS_DIR = pathlib.Path(__file__).resolve().parent


def test_images() -> None:
    """"""
    input_images = [
        THIS_DIR / "320x200.png",
        THIS_DIR / "480x640.png",
        THIS_DIR / "595x842.png",
    ]
    reference = [
        analyze.ImagePathWithSize(file, *[int(n) for n in file.stem.split("x")])
        for file in input_images
    ]

    assert reference == analyze.images([str(fname) for fname in input_images])


def test_empty_sequence() -> None:
    """Test that an empty input sequence results in an empty output sequence."""
    result = analyze.images([])

    assert not result


def test_invalid_fname() -> None:
    """Test that an invalid file name raises an exception."""
    with pytest.raises(FileNotFoundError):
        analyze.images(["not-present-file.png"])
