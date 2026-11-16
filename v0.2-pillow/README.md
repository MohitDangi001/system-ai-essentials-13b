
# v0.2 — Pillow Library

## 1. What is Pillow?
Pillow is a Python library used to create, open, edit, manipulate, and save images.

## 2. Official Documentation
https://pillow.readthedocs.io/en/stable/

## 3. Installation
```bash
python -m pip install Pillow
```

## 4. First Working Program
File: `first_image.py`

```python
from PIL import Image

image = Image.new("RGB", (400, 300), "white")
image.save("first_image.png")
```

## 5. My Experiment
I changed the background colour from white to blue. The program successfully created a blue PNG image.

## 6. Breaking the Code on Purpose
I changed the colour to `"not-a-color"`.

Error:
`ValueError: unknown color specifier: 'not-a-color'`

Pillow could not recognise the supplied colour. I restored `"blue"` and successfully ran the program again.

## 7. What I Learned
- Installing Pillow using pip.
- Importing Pillow with `from PIL import Image`.
- Creating images using `Image.new()`.
- Saving images using `image.save()`.
- Understanding and debugging a ValueError.
