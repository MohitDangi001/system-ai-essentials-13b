
# AI Learning Log — v0.2 Pillow

## Desired output
I wanted to create a simple image using Python Pillow.

## Prompt used
Help me create an image using Pillow, explain the code and show me how to change its background colour.

## Did the code run first time?
The image creation program ran successfully and generated an image file.

## One line I learned
`Image.new("RGB", (400, 300), "blue")` creates a new 400-by-300 pixel RGB image with a blue background.

## Deliberate error
I used the invalid colour name `"not-a-color"`.

## First error line
`ValueError: unknown color specifier: 'not-a-color'`

## What the error means
Pillow did not recognise the colour name.

## How I checked it
I restored a valid colour and ran the program again successfully.

## Commit
Pillow exploration commit: `1f7017a`

## Something AI got wrong
The initial image save-path guidance did not place the generated image in the intended project location. I checked where the image was saved and corrected the path.

## How I verified it
I ran the program again and checked that the image was generated in the expected folder.
