import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(3)
t.pensize(3)
t.color("gold")
side_length = 200

t.penup()
t.goto(-100, 30)
t.pendown()

for _ in range(5):
    t.forward(side_length)
    t.right(144)

t.hideturtle()
turtle.done()
