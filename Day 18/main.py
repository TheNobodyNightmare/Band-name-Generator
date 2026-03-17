import turtle
from turtle import Turtle, Screen
from random import random, choice ,randint
Bob = Turtle()
Bob.shape("turtle")
Bob.color("red")
Bob.speed(0)
turtle.colormode(255)
def random_colour():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_colour = (r,g,b)
    return random_colour
def draw_spirograph(size_in_gap):
    for _ in range(int(360/size_in_gap)):
        Bob.color(random_colour())
        Bob.circle(100)
        Bob.setheading(Bob.heading() + size_in_gap)





def draw_shape():
    x = 3
    z = 3
    color = ["red","yellow","Green","Blue","purple"]
    while z <= 10:
        for _ in range(z):
            y = 360/x
            Bob.forward(100)
            Bob.right(y)
        x +=1
        z +=1
        Bob.color(choice(color))
def random_walk():
    color = ["red","yellow","Green","Blue","purple"]
    angles = [0, 90, 180, 270, 360]
    for i in range(100):
        Bob.pensize(10)
        Bob.forward(40)
        Bob.setheading(choice(angles))
        Bob.color(random_colour())
# for value in range(36):
#     Bob.forward(10)
#     Bob.penup()
#     Bob.right(10)
#     Bob.forward(9)
#     Bob.pendown()
# for _ in range(50):
#     Bob.forward(10)
#     Bob.penup()
#     Bob.left(10)
#     Bob.forward(9)
#     Bob.pendown()

screen = Screen()
screen.exitonclick()

