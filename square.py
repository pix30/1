import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.speed(3)

side_length = 100
for _ in range(4):
    t.forward(side_length)
    t.right(90)
turtle.done()