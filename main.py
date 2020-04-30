"""Command line interface of the `imgs2pdf` package."""

from argparse import ArgumentParser, Namespace

import imgs2pdf


def main(args: Namespace):
    imgs2pdf.convert(args.images, args.output)


if __name__ == "__main__":
    parser = ArgumentParser(  # pylint: disable=invalid-name
        description="Generates a PDF from images"
    )
    parser.add_argument(
        "images", metavar="IMAGE", nargs="+", help=f"Path to an image to embed to PDF"
    )
    parser.add_argument(
        "-o", "--output", dest="output", help=f"Name PDF to create",
    )

    try:
        main(parser.parse_args())
    except Exception as ex:  # pylint: disable=broad-except
        print("Error saving PDF:", *ex.args)
