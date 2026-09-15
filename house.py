# draw a house
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(3)
t.pensize(3)
house_size = 200
door_width = 50
door_height = 90
window_size = 40

# walls
t.penup()
t.goto(-100, -100)
t.pendown()
t.color("black", "tan")
t.begin_fill()
for _ in range(4):
    t.forward(house_size)
    t.left(90)
t.end_fill()

# roof
t.penup()
t.goto(-120, 100)
t.pendown()
t.color("black", "firebrick")
t.begin_fill()
t.goto(120, 100)
t.goto(0, 200)
t.goto(-120, 100)
t.end_fill()

# door
t.penup()
t.goto(-25, -100)
t.pendown()
t.color("black", "saddlebrown")
t.begin_fill()
for _ in range(2):
    t.forward(door_width)
    t.left(90)
    t.forward(door_height)
    t.left(90)
t.end_fill()

# window
t.penup()
t.goto(40, 20)
t.pendown()
t.color("black", "lightblue")
t.begin_fill()
for _ in range(4):
    t.forward(window_size)
    t.left(90)
t.end_fill()

t.hideturtle()
turtle.done()
