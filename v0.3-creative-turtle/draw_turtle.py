
import turtle
import math
from pathlib import Path
from PIL import Image

# ==================================================
# CREATIVE GEOMETRIC SEA TURTLE
# v0.3 - Integration of Turtle and Pillow
# ==================================================

# -----------------------------
# 1. CREATE BACKGROUND WITH PILLOW
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent
background_file = BASE_DIR / "background.gif"

WIDTH = 1200
HEIGHT = 900

background = Image.new("RGB", (WIDTH, HEIGHT), "#03030A")
background.save(background_file, "GIF")

print("Pillow: background created successfully!")


# -----------------------------
# 2. SET UP TURTLE SCREEN
# -----------------------------

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Creative Geometric Sea Turtle")
screen.bgpic(str(background_file))
screen.tracer(0, 0)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()

BLACK = "#03030A"

COLORS = [
    "#FF1744",  # Red
    "#00BCD4",  # Cyan
    "#FF9800",  # Orange
    "#FFEB3B",  # Yellow
    "#00C853",  # Green
    "#FFFFFF",  # White
    "#E040FB",  # Purple
    "#2196F3",  # Blue
    "#F48FB1",  # Pink
]


# -----------------------------
# 3. REUSABLE DRAWING FUNCTIONS
# -----------------------------

def polygon(points, color, outline=BLACK, width=3):
    """Draw a filled polygon using Turtle."""
    pen.penup()
    pen.goto(points[0])
    pen.pencolor(outline)
    pen.fillcolor(color)
    pen.pensize(width)
    pen.pendown()

    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)

    pen.goto(points[0])
    pen.end_fill()
    pen.penup()


def circle(x, y, radius, color):
    """Draw a filled circle."""
    pen.penup()
    pen.goto(x, y - radius)
    pen.pencolor(color)
    pen.fillcolor(color)
    pen.pensize(1)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()
    pen.penup()


def line(points, color=BLACK, width=5):
    """Draw a connected line."""
    pen.penup()
    pen.goto(points[0])
    pen.pencolor(color)
    pen.pensize(width)
    pen.pendown()

    for point in points[1:]:
        pen.goto(point)

    pen.penup()


# -----------------------------
# 4. FOUR BROAD FLIPPERS
# Drawn first so the shell overlaps
# their attachment points.
# -----------------------------

# Front lower-left flipper
polygon([
    (-115, -105), (-205, -140), (-280, -215),
    (-330, -315), (-405, -370), (-365, -245),
    (-300, -155), (-205, -85)
], "#00BCD4")

polygon([
    (-205, -140), (-280, -215), (-405, -370),
    (-330, -315), (-270, -225)
], "#FF1744")

polygon([
    (-280, -215), (-330, -315), (-405, -370),
    (-345, -245)
], "#FFEB3B")

polygon([
    (-300, -155), (-270, -225), (-205, -140),
    (-245, -105)
], "#2196F3")


# Front lower-right flipper
polygon([
    (90, -145), (175, -190), (225, -265),
    (305, -365), (385, -420), (330, -300),
    (255, -210), (170, -135)
], "#00BCD4")

polygon([
    (175, -190), (225, -265), (385, -420),
    (305, -365), (245, -255)
], "#FF1744")

polygon([
    (225, -265), (305, -365), (385, -420),
    (285, -290)
], "#FF9800")

polygon([
    (175, -190), (245, -255), (255, -210),
    (170, -135)
], "#2196F3")


# Rear upper-right flipper
polygon([
    (270, 100), (350, 145), (425, 215),
    (485, 300), (395, 275), (325, 205)
], "#00BCD4")

polygon([
    (350, 145), (425, 215), (485, 300),
    (410, 235)
], "#FF9800")

polygon([
    (425, 215), (485, 300), (395, 275),
    (410, 235)
], "#FF1744")


# Rear lower-right flipper
polygon([
    (270, -100), (350, -145), (425, -215),
    (485, -300), (390, -270), (320, -200)
], "#00BCD4")

polygon([
    (350, -145), (425, -215), (485, -300),
    (405, -235)
], "#00C853")

polygon([
    (425, -215), (485, -300), (390, -270),
    (405, -235)
], "#FF1744")


# -----------------------------
# 5. TAIL
# -----------------------------

polygon([
    (330, 0), (410, -15), (465, -45),
    (515, -70), (460, -65), (400, -40)
], "#FF1744")

polygon([
    (410, -15), (465, -45), (515, -70),
    (460, -30)
], "#FF9800")


# -----------------------------
# 6. NECK
# -----------------------------

polygon([
    (-205, 65), (-280, 95), (-365, 45),
    (-355, -35), (-270, -105), (-185, -75)
], "#00BCD4")

polygon([
    (-280, 95), (-365, 45), (-355, -35),
    (-300, 0)
], "#FF1744")

polygon([
    (-355, -35), (-270, -105), (-185, -75),
    (-265, -15)
], "#2196F3")


# -----------------------------
# 7. ROUNDED GEOMETRIC SHELL
# -----------------------------

CENTER_X = 80
CENTER_Y = 0

SHELL_WIDTH = 285
SHELL_HEIGHT = 205

# Create rows of points inside an oval.
# Alternating triangles create a mosaic effect.

row_positions = [-0.93, -0.68, -0.35, 0, 0.35, 0.68, 0.93]
columns = 8

shell_rows = []

for row_index, fraction_y in enumerate(row_positions):

    y = CENTER_Y + fraction_y * SHELL_HEIGHT

    width_at_y = SHELL_WIDTH * math.sqrt(
        1 - fraction_y ** 2
    )

    row = []

    for col in range(columns + 1):

        fraction_x = -1 + (2 * col / columns)

        x = CENTER_X + fraction_x * width_at_y

        # Small irregular offsets create an artistic mosaic.
        if col not in (0, columns):
            x += ((row_index * 13 + col * 7) % 15) - 7

        if row_index not in (0, len(row_positions) - 1):
            y_point = y + ((row_index * 9 + col * 11) % 11) - 5
        else:
            y_point = y

        row.append((x, y_point))

    shell_rows.append(row)


# Draw colourful triangular shell panels.

color_index = 0

for row_index in range(len(shell_rows) - 1):

    for col in range(columns):

        top_left = shell_rows[row_index][col]
        top_right = shell_rows[row_index][col + 1]
        bottom_left = shell_rows[row_index + 1][col]
        bottom_right = shell_rows[row_index + 1][col + 1]

        if (row_index + col) % 2 == 0:

            polygon(
                [top_left, bottom_left, top_right],
                COLORS[color_index % len(COLORS)]
            )

            polygon(
                [top_right, bottom_left, bottom_right],
                COLORS[(color_index + 3) % len(COLORS)]
            )

        else:

            polygon(
                [top_left, bottom_left, bottom_right],
                COLORS[(color_index + 2) % len(COLORS)]
            )

            polygon(
                [top_left, bottom_right, top_right],
                COLORS[(color_index + 5) % len(COLORS)]
            )

        color_index += 1


# Draw a smooth-looking dark shell boundary.

outline_points = []

for angle_degree in range(0, 360, 6):
    angle = math.radians(angle_degree)

    x = CENTER_X + SHELL_WIDTH * math.cos(angle)
    y = CENTER_Y + SHELL_HEIGHT * math.sin(angle)

    outline_points.append((x, y))

line(outline_points + [outline_points[0]], BLACK, 10)


# -----------------------------
# 8. SHELL DECORATIVE DETAILS
# -----------------------------

circle(-20, 65, 9, "#008FA3")
circle(190, 45, 11, "#050505")
circle(75, -60, 9, "#050505")
circle(245, -85, 8, "#050505")


# -----------------------------
# 9. HEAD
# -----------------------------

polygon([
    (-520, 65), (-505, 150), (-440, 195),
    (-365, 175), (-315, 115), (-295, 55),
    (-345, -10), (-440, -30), (-505, 5)
], "#00BCD4")

# Geometric face sections
polygon([
    (-520, 65), (-505, 150), (-440, 195),
    (-450, 110)
], "#FF1744")

polygon([
    (-440, 195), (-365, 175), (-385, 105),
    (-450, 110)
], "#FF9800")

polygon([
    (-450, 110), (-385, 105), (-345, -10),
    (-440, -30)
], "#E040FB")

polygon([
    (-520, 65), (-450, 110), (-440, -30),
    (-505, 5)
], "#FFEB3B")


# -----------------------------
# 10. EYE AND FACE DETAILS
# -----------------------------

circle(-435, 120, 28, BLACK)
circle(-435, 120, 19, "#00BCD4")
circle(-435, 120, 10, BLACK)
circle(-441, 128, 4, "#FFFFFF")

# Small nostril
circle(-330, 45, 7, "#050505")


# -----------------------------
# 11. FINAL DISPLAY
# -----------------------------

screen.update()

print("Turtle drawing completed successfully!")
print("Pillow and Turtle integration: successful.")
print("Close the drawing window when you finish viewing.")

screen.mainloop()
