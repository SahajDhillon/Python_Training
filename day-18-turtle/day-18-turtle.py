from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fast")
#colors = ["red", "green", "blue", "cyan", "magenta", "yellow", "orange", "purple"]
angles = [90.0, 180.0, 270.0, 0.0]
colors = colorgram.extract("hirst.jpg", 10)
all_colors = []

for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    t = (r, g, b)
    all_colors.append(t)


def square():
    for _ in range(4):
        timmy.forward(100)
        timmy.left(90)


def dotted_line():
    for _ in range(50):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()


def draw_shapes():
    for i in range(3, 15):
        turn_angle = 360 / i
        timmy.color(random.choice(colors))
        for _ in range(i):
            timmy.right(int(turn_angle))
            timmy.forward(100)


def gen_random_lines():
    for i in range(100):
        timmy.color(random.choice(colors))
        timmy.pensize(10)
        timmy.setheading(random.choice(angles))
        timmy.forward(40)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


if __name__ == '__main__':
    print(all_colors)

screen = Screen()
screen.exitonclick()
