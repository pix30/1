# setup
import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightblue")

# reset
t.speed(0)
t.pensize(3)
face_width = 180
face_height = 220
ear_size = 40
eye_size = 30
pupil_size = 12

# draw face
t.penup()
t.goto(-90, 110)
t.pendown()
t.color("black", "tan")
t.begin_fill()
for _ in range(2):
    t.forward(face_width)
    t.right(90)
    t.forward(face_height)
    t.right(90)
t.end_fill()

# draw ears
for ear_x in [-130, 90]:
    t.penup()
    t.goto(ear_x, 40)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(ear_size)
        t.right(90)
    t.end_fill()

# draw eyes
for eye_x in [-50, 20]:
    t.penup()
    t.goto(eye_x, 60)
    t.pendown()
    t.color("black", "white")
    t.begin_fill()
    for _ in range(4):
        t.forward(eye_size)
        t.right(90)
    t.end_fill()

    t.penup()
    t.goto(eye_x + 9, 51)
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    for _ in range(4):
        t.forward(pupil_size)
        t.right(90)
    t.end_fill()

# draw mouth
t.color("saddlebrown")
t.penup()
t.goto(0, 20)
t.pendown()
t.goto(-15, -20)
t.goto(15, -20)
t.goto(0, 20)
t.color("red")
t.pensize(5)
t.penup()
t.goto(-40, -50)
t.pendown()
t.goto(-20, -68)
t.goto(20, -68)
t.goto(40, -50)

# draw hair
t.color("saddlebrown")
t.pensize(4)
for hair_x in range(-90, 91, 10):
    t.penup()
    t.goto(hair_x, 110)
    t.pendown()
    t.goto(hair_x, 150)
# hide turtle
t.hideturtle()

turtle.done()
