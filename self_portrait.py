import turtle

# ====================== Setup ======================
screen = turtle.Screen()
screen.bgcolor("#fdf0d5")
screen.title("My Self-Portrait")
screen.setup(750, 800)
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)


def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


def fill_circle(x, y, r, color):
    """Filled circle centred at (x, y)."""
    pen.pencolor(color)
    pen.fillcolor(color)
    move(x, y - r)
    pen.setheading(90)
    pen.begin_fill()
    pen.circle(r)
    pen.end_fill()


def fill_rect(cx, cy, w, h, color):
    """Filled rectangle centred at (cx, cy), width w, height h."""
    pen.pencolor(color)
    pen.fillcolor(color)
    move(cx - w / 2, cy - h / 2)   # bottom-left corner
    pen.setheading(0)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(w)
        pen.left(90)
        pen.forward(h)
        pen.left(90)
    pen.end_fill()


# ====================== Body ======================
fill_circle(0, -280, 130, "#ef8354")   # chest
fill_rect(0, -360, 230, 130, "#ef8354")  # widen into the screen bottom

# ====================== Neck ======================
fill_rect(0, -160, 62, 120, "#e2b57a")

# ====================== Head ======================
head_cx, head_cy, head_r = 0, -40, 115
fill_circle(head_cx, head_cy, head_r, "#f0c38e")

# ====================== Hair ======================
HAIR = "#35231c"
import math
for ang in range(160, 19, -14):        # sweep across the top
    a = math.radians(ang)
    px = head_cx + head_r * 1.02 * math.cos(a)
    py = head_cy + head_r * 1.15 * math.sin(a)
    fill_circle(px, py, 55, HAIR)
# connect hair across the brow
fill_rect(0, head_cy + head_r * 0.62, 2 * head_r * 1.1, 70, HAIR)

# ====================== Eyes ======================
for ex in (-44, 44):
    fill_circle(ex, 18, 22, "white")     # eyeball
    fill_circle(ex, 28, 13, "#6b4b33")   # iris
    fill_circle(ex, 33, 7, "#111010")    # pupil
    fill_circle(ex, 24, 4, "white")      # sparkle

# ====================== Eyebrows ======================
pen.color(HAIR)
pen.pensize(8)
pen.penup()
for ex in (-44, 44):
    move(ex - 30, 60)
    pen.pendown()
    pen.goto(ex + 30, 62)
    pen.penup()

# ====================== Nose ======================
pen.color("#c07a57")
pen.pensize(5)
move(4, -8)
pen.pendown()
pen.goto(4, -45)
pen.penup()

# ====================== Smile ======================
pen.color("#7a2630")
pen.pensize(5)
pen.penup()
move(-40, -60)
pen.setheading(-55)
pen.pendown()
pen.circle(42, 100)   # downward smile arc
pen.penup()

# ====================== Blush ======================
for hx in (-84, 84):
    fill_circle(hx, -45, 13, "#e9a0a0")

# ====================== Finish ======================
pen.hideturtle()
screen.update()
turtle.done()
