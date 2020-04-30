"""Module to render the images into a PDF document."""

from contextlib import contextmanager
from typing import Iterator, NamedTuple, Sequence

from fpdf import FPDF  # type: ignore

from .analyze import ImagePathWithSize


class Size(NamedTuple):
    """Width and height."""

    width: float
    height: float


class Margins(NamedTuple):
    """Left and top margins for the pages.

    The right margin is always equal to the left one.
    """

    left: float
    top: float


UNIT = "mm"
PAPER_FORMAT = "A4"
PAPER_ORIENTATION = "P"  # Portrait
PAPER_SIZE = Size(210, 297)
MARGINS = Margins(5, 5)

EFFECTIVE_SIZE = Size(
    PAPER_SIZE.width - 2 * MARGINS.left, PAPER_SIZE.height - 2 * MARGINS.top
)


def images(imgs: Sequence[ImagePathWithSize], pdf_name: str) -> None:
    """Render the images and creates a new PDF document.

    :param imgs: Sequence of image files with their sizes.
    :param pdf_name: Name of the PDF to store.
    """
    with _pdf_document(pdf_name) as pdf:
        for image in imgs:
            _new_page_with_image(pdf, image)


@contextmanager
def _pdf_document(file_name: str) -> Iterator[FPDF]:
    """Context that creates a PDF document and stores it when the context is closed.

    :param file_name: Name of the PDF document to store.
    :returns: PDF document.
    """
    document = FPDF(orientation=PAPER_ORIENTATION, unit=UNIT, format=PAPER_FORMAT)

    yield document

    document.output(file_name)


def _new_page_with_image(pdf: FPDF, image: ImagePathWithSize) -> None:
    """Renders the image top-centered as a new page to the PDF document.

    :param pdf: Document to render to.
    :param image: Image to render.
    """
    pdf.add_page()
    px_per_mm = image.height / EFFECTIVE_SIZE.height
    width_in_mm = image.width / px_per_mm
    if image.width >= image.height or width_in_mm >= EFFECTIVE_SIZE.width:
        pdf.image(
            str(image.path), x=MARGINS.left, y=MARGINS.top, w=EFFECTIVE_SIZE.width
        )
    else:
        pdf.image(
            str(image.path),
            x=MARGINS.left + (EFFECTIVE_SIZE.width - width_in_mm) / 2,
            y=MARGINS.top,
            h=EFFECTIVE_SIZE.height,
        )
