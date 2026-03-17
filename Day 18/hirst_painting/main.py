# import colorgram
#
# rgb_colour =[]
#
# colours = colorgram.extract('image.jpg',30)
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r,g,b)
#     rgb_colour.append(new_colour)
#
# print(rgb_colour)




import turtle as turtle_bob
from random import choice
from turtle import Screen
turtle_bob.colormode(255)

colour_list = [ (144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]

tim = turtle_bob.Turtle()
tim.penup()
tim.speed(0.1)
tim.hideturtle()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1,number_of_dots):
    tim.dot(17,choice(colour_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
screen = Screen()
screen.exitonclick()
