# draw an equilateral triangle
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(3)
t.pensize(3)
t.color("blue")
side_length = 150

# all 3 sides are the same length, and the turtle turns 120 degrees
# at each corner so the inside angles are all 60 degrees
for _ in range(3):
    t.forward(side_length)
    t.left(120)

t.hideturtle()
turtle.done()
