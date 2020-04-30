"""Integration test of the `imgs2pdf` package."""

import pathlib
from typing import Sequence

from _pytest.capture import CaptureFixture  # type: ignore

import imgs2pdf
from .conftest import remove_creation_date

THIS_DIR = pathlib.Path(__file__).resolve().parent


def test_images(capsysbinary: CaptureFixture, images: Sequence[pathlib.Path]) -> None:
    """Test PDF generation with test images."""
    # empty name result in stdout output
    imgs2pdf.convert([str(image) for image in images], "")
    result = remove_creation_date(capsysbinary.readouterr().out)

    with open(THIS_DIR / "reference.pdf", mode="rb") as reference_file:
        reference = remove_creation_date(reference_file.read())

    assert reference == result
