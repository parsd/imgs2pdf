imgs2pdf
========

Converts images as they are into a PDF document. Supports JPG, PNG and GIF.

This is a front-end for `fpdf2` and `pillow` which do the heavy lifting.

Execute Script
--------------

Developed with Python 3.8.

1. Create virtual environment:

    ```bash
    python3 -m venv venv
    ```

    or if on Windows and not using the Windows Store installer:

    ```cmd
    python -m venv venv
    ```

2. Activate the environment

    ```bash
    . venv/Scripts/activate
    ```

    or on Windows _cmd_:

    ```cmd
    venv\Scripts\acivate.bat
    ```

    or _PowerShell_:

    ```ps
    venv\Scripts\Acivate.ps1
    ```

3. Install runtime dependencies

    ```bash
    pip3 install -r requirements.txt
    ```

    Windows:

    ```cmd
    pip install -r requirements.txt
    ```

4. Generate PDF:

    ```bash
    python3 main.py
    ```

    Windows:

    ```cmd
    python main.py
    ```

Command Line Arguments
----------------------

```cmd
usage: main.py [-h] [-o OUTPUT] IMAGE [IMAGE ...]

Generates a PDF from images

positional arguments:
  IMAGE                 Path to an image to embed to PDF

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Name PDF to create
```

Development
-----------

Additionally install the development dependencies:

```bash
pip3 install -r dev-requirements.txt
```

Windows:

```cmd
pip install -r dev-requirements.txt
```

Tests can be run via `pytest`. Coverage can be run via `coverage run`. `coverage report` gives a short coverage report on the files. `coverage html` generate an in-depth HTML report.

Linting is done via `mypy` and `pylint`. Formatting is done via `black`.
