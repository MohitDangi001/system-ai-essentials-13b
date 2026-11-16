
# Worksheet 13b — Final Reflection

## v0.1 — Turtle

**Purpose:** Turtle is a Python drawing library used to create graphics through programming instructions.

**Documentation:** https://docs.python.org/3/library/turtle.html

**Smallest working program:**
```python
import turtle

turtle.forward(100)
turtle.done()
```

**Customisation:** Created a colourful geometric drawing using loops and different colours.

**Deliberate mistake:** Changed `pen.forward(100)` to `pen.forward("100")`.

**First error line:**
`TypeError: can't multiply sequence by non-int type 'float'`

**Explanation:** The drawing distance must be a number. `"100"` is a string, not an integer.

**Result:** Restored `pen.forward(100)` and successfully ran the program.

---

## v0.2 — Pillow

**Purpose:** Pillow is a Python library for creating, opening and processing images.

**Documentation:** https://pillow.readthedocs.io/en/stable/

**Smallest working program:**
```python
from PIL import Image

image = Image.new("RGB", (400, 300), "blue")
image.save("first_image.png")
```

**Customisation:** Changed the image background colour and generated a blue image.

**Deliberate mistake:** Used an invalid colour name: `"not-a-color"`.

**First error line:**
`ValueError: unknown color specifier: 'not-a-color'`

**Explanation:** Pillow could not recognise the supplied colour name.

**Result:** Changed the colour back to a valid colour and successfully created the image.

---

## v0.3 — Turtle + Pillow Integration

### What I wanted to build
### My prediction before coding

I expected Pillow to create a black background GIF and Turtle to draw a colourful geometric sea turtle over it. The final window should show a recognisable turtle with a patterned shell, head, four flippers, an eye and a tail.

A colourful geometric sea turtle on a black background, using Pillow to create the background and Turtle to draw the turtle.

**Documentation note:** I recorded this prediction during my final documentation review, after implementing the program. It describes the output I intended to create.

### Prompt used

Help me create a colourful geometric sea turtle using Python Turtle and Pillow. I want a black background, a colourful polygonal shell, a head, four flippers and a tail. Explain the code and combine both libraries.

### Development iterations

I went through several iterations:

1. Created a black background using Pillow.
2. Drew the first geometric shell using Turtle.
3. Added the turtle's head and eye.
4. Added four flippers and a tail.
5. Replaced the code with one complete integrated program.

### Something AI got wrong

Some early designs did not match my reference image closely. The flippers looked disconnected and the shell initially looked like a pinwheel.

### How I identified the problem

I ran the program, inspected the actual output and compared screenshots with my reference image. I requested changes based on what I observed.

### Final output

The program successfully created a colourful geometric sea turtle on a black background.

It achieved the main objective, although it was not an exact reproduction of the reference image.

### Libraries working together

- Pillow creates and saves the background GIF.
- Turtle loads that GIF and draws the sea turtle over it.

---

## Four Information Sources

| Source | Speed | Reliability |
|---|---|---|
| Help flag | Fast for command options | Reliable for supported options |
| Manual | Not tested | Not evaluated |
| Official documentation | Medium | Highly reliable for library usage |
| AI | Very fast | Must be checked against documentation |

**Fastest:** AI is generally fastest for getting an initial explanation.

**Most reliable:** Official documentation is the best source for verifying library functions and behaviour.

**Were they the same?** No.

---

## Five Steps for Meeting a New Library

1. What is this for?
2. Find the shape.
3. Run the smallest thing that works.
4. Change exactly one thing.
5. Break it on purpose and understand the error.

---


## Homework — pyfiglet

- What it is for: Creates large ASCII-art text banners.
- Installation command: python -m pip install pyfiglet
- Installed version: 1.0.4
- Help command: pyfiglet --help
- Python function: pyfiglet.figlet_format()
- First successful output: MOHIT
- Customisation: Changed MOHIT to CREATIVE.
- Deliberate mistake: Used font="font_that_does_not_exist".
- First error line: pyfiglet.FontNotFound: font_that_does_not_exist
- What the error means: The requested font could not be found.
- What I would try next: Explore other available fonts using pyfiglet --list_fonts.
