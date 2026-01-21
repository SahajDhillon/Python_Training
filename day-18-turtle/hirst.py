import random
from turtle import Turtle, Screen

# Hirst painting color palette
colors = [
    (248, 238, 219), (223, 155, 90), (214, 240, 228), (240, 206, 90),
    (104, 170, 203), (36, 109, 149), (199, 227, 239), (113, 193, 161),
    (153, 61, 94), (208, 78, 109)
]

# Configuration constants
DOTS_PER_ROW = 10
ROWS = 10
DOT_SIZE = 30
DOT_SPACING = 50

# Setup
screen = Screen()
screen.colormode(255)

hirst = Turtle()
hirst.speed("fastest")
hirst.hideturtle()


def draw_row():
    """Draw a single row of dots"""
    for _ in range(DOTS_PER_ROW):
        dot_color = random.choice(colors)
        hirst.dot(DOT_SIZE, dot_color)
        hirst.penup()
        hirst.forward(DOT_SPACING)


def move_to_next_row():
    """Move turtle to the start of the next row"""
    hirst.left(90)
    hirst.forward(DOT_SPACING)
    hirst.left(90)
    hirst.forward(DOT_SPACING * DOTS_PER_ROW)
    hirst.setheading(0)


def position_turtle_at_start():
    """Position turtle at bottom-left corner"""
    hirst.penup()
    hirst.setheading(225)
    hirst.forward(300)
    hirst.setheading(0)


# Main execution
position_turtle_at_start()

for _ in range(ROWS):
    draw_row()
    move_to_next_row()

screen.exitonclick()