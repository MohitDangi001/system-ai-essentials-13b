
# AI Learning Log — v0.1 Turtle

## Desired output
I wanted to create a colourful geometric drawing using Python Turtle.

## Prompt used
Help me create a colourful geometric drawing using Python Turtle. Explain the code and help me understand how the drawing works.

## Did the code run first time?
The smallest Turtle example ran successfully. I later customised it into a colourful geometric drawing.

## One line I learned
`pen.forward(100)` moves the Turtle pen forward by 100 units.

## Deliberate error
I changed `pen.forward(100)` to `pen.forward("100")`.

## First error line
`TypeError: can't multiply sequence by non-int type 'float'`

## What the error means
The forward distance must be numeric. I supplied a string instead of an integer.

## How I checked it
I restored the integer value and ran the drawing again successfully.

## Commit
Initial Turtle exploration commit: `c3e361b`

## Something AI got wrong
The initial folder and file-location guidance did not match the final project structure. I checked the folders and corrected the file location.

## How I verified it
I checked that the Turtle program was in the correct folder and ran it again.
