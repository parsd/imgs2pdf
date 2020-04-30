"""Embed a list of images in a PDF.

Images are placed top-centered.
"""

from typing import Sequence

from . import analyze


def convert(image_fnames: Sequence[str], pdf_name: str) -> None:
    """Converts the given image files into a PDF document.

    Images are embedded as they are and not converted to e.g. JPGs.

    :param image_fnames: Sequence of image file names.
    :param pdf_name: Name of PDF to store images in.
    :raises FileNotFound: if one of the files in `image_fnames` could not be opened.
    """
    images = analyze.images(image_fnames)
