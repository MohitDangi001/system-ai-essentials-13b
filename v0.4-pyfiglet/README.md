
# v0.4 — Pyfiglet Library Exploration

## What is pyfiglet?

Pyfiglet is a Python library that converts ordinary text into large ASCII-art banners.

## Installation

```bash
python -m pip install pyfiglet
```

## First working program

```python
import pyfiglet

banner = pyfiglet.figlet_format("MOHIT", font="slant")
print(banner)
```

## Run the program

From the project root:

```bash
python v0.4-pyfiglet/first_banner.py
```

## Experiment

Changed the text from MOHIT to CREATIVE. The output changed as expected.

## Deliberate error

Used a font that does not exist.

Actual error:

`pyfiglet.FontNotFound: font_that_does_not_exist`

The error indicated that the requested font was unavailable.

## What I learned

- How to install a Python library.
- How to use pyfiglet.figlet_format().
- How to customise text and fonts.
- How to use the help command.
- How to identify and understand a FontNotFound exception.
