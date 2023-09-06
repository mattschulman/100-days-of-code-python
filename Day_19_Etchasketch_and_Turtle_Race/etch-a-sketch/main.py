# W = forward, S = Backwards, A = Counter-clockwise, D = Clockwise , C = Clear Drawing

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counterclock():
    tim.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="a", fun=move_counterclock)
screen.onkey(key="d", fun=move_clockwise)
screen.exitonclick()
