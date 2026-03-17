from turtle import Turtle,Screen
screen = Screen()

Dev = Turtle()

def move_forward():
    Dev.forward(20)

def move_backward():
    Dev.backward(20)

def move_clockwise():
    Dev.right(20)

def move_anticlockwise():
    Dev.left(20)
def clear_screen ():
    screen.resetscreen()


screen.listen()
screen.onkeyrelease(fun=move_forward,key="w")
screen.onkeyrelease(fun=move_backward,key="s")
screen.onkey(fun=move_clockwise,key="d")
screen.onkey(fun=move_anticlockwise,key="a")
screen.onkey(fun=clear_screen,key="c")








screen.exitonclick()