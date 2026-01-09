# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.color("green")
# timmy.forward(20)
# my_Screen = Screen()
# print(my_Screen.canvheight)
# my_Screen.exitonclic

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmandar"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)

