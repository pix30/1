import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(3)
t.pensize(5)
t.color("blue")
top = 40
bottom = -40

# Z
x = -245
t.penup()
t.goto(x, top)
t.pendown()
t.goto(x + 50, top)
t.goto(x, bottom)
t.goto(x + 50, bottom)

# I
x = x + 70
t.penup()
t.goto(x, top)
t.pendown()
t.goto(x + 50, top)
t.penup()
t.goto(x + 25, top)
t.pendown()
t.goto(x + 25, bottom)
t.penup()
t.goto(x, bottom)
t.pendown()
t.goto(x + 50, bottom)

# C
x = x + 70
t.penup()
t.goto(x + 50, top)
t.pendown()
t.goto(x, top)
t.goto(x, bottom)
t.goto(x + 50, bottom)

# H
x = x + 70
t.penup()
t.goto(x, top)
t.pendown()
t.goto(x, bottom)
t.penup()
t.goto(x + 50, top)
t.pendown()
t.goto(x + 50, bottom)
t.penup()
t.goto(x, 0)
t.pendown()
t.goto(x + 50, 0)

# E
x = x + 70
t.penup()
t.goto(x + 50, top)
t.pendown()
t.goto(x, top)
t.goto(x, bottom)
t.goto(x + 50, bottom)
t.penup()
t.goto(x, 0)
t.pendown()
t.goto(x + 40, 0)

# N
x = x + 70
t.penup()
t.goto(x, bottom)
t.pendown()
t.goto(x, top)
t.goto(x + 50, bottom)
t.goto(x + 50, top)

# G
x = x + 70
t.penup()
t.goto(x + 50, top)
t.pendown()
t.goto(x, top)
t.goto(x, bottom)
t.goto(x + 50, bottom)
t.goto(x + 50, 0)
t.goto(x + 25, 0)

t.hideturtle()
turtle.done()
