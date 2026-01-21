from turtle import Turtle, Screen

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    tim.right(5)


def anticlockwise():
    tim.left(5)


def clear_screen():
    tim.clear()


screen = Screen()
screen.listen()
screen.onkeypress(move_forward, "d")
screen.onkeypress(move_backwards, "a")
screen.onkeypress(clockwise, "w")
screen.onkeypress(anticlockwise, "s")
screen.onkeypress(clear_screen, "c")
screen.exitonclick()
