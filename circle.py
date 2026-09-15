import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(3)
t.pensize(3)
radius = 100

t.penup()
t.goto(0, -radius)
t.pendown()

t.color("black", "orange")
t.begin_fill()
t.circle(radius)
t.end_fill()

t.hideturtle()
turtle.done()
