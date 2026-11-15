
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("My Creative Turtle Drawing")

pen = turtle.Turtle()
pen.speed(5)

colors = ["red", "yellow", "cyan", "lime", "magenta"]

for i in range(36):
    pen.color(colors[i % 5])
    for j in range(4):
        pen.forward(100)
        pen.right(90)
    pen.right(10)

turtle.done()
