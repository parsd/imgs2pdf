"""Module to analyze the input images."""

import pathlib
from typing import Iterator, NamedTuple, Sequence

from PIL import Image


class ImagePathWithSize(NamedTuple):
    """Stores the `Path` to an image with its width and height in pixels."""

    path: pathlib.Path
    width: int
    height: int


def images(fnames: Sequence[str]) -> Sequence[ImagePathWithSize]:
    """Reads in all images by their file names to return `ImagePathWithSize`s.

    :param fnames: Sequence of strings containing the file names.
    :returns: Sequence of image file paths with the image's size.
    :raises FileNotFound: if one of the files in `fnames` cannot be opened.
    """
    images: Iterator[Image] = (Image.open(fname) for fname in fnames)
    return [
        ImagePathWithSize(
            pathlib.Path(image.filename).resolve(), image.width, image.height
        )
        for image in images
    ]
