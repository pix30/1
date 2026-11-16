# turtle makes random turns and moves forward random amounts
import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(5)
t.pensize(2)
t.color("purple")
steps = 50

for _ in range(steps):
    angle = random.randint(0, 360)
    distance = random.randint(10, 50)
    t.right(angle)
    t.forward(distance)

t.hideturtle()
turtle.done()
