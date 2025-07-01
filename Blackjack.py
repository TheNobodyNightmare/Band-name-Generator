import string
import random

number = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
Game = False 
while Game is False :
    start  = input("Do you want ot play a Game of blackjack? type y for yes or n for no \n")
    if start == "y":
         Your_Cards = random.choices(number,k=2)
         Score = Your_Cards[0] + Your_Cards[1]
         Computer_Cards = random.choices(number,k=1)
         print (f"Your Cards : {Your_Cards},Current Score : {Score}") 
         print(f"Computer Cards : {Computer_Cards}")
         Second_card = random.choices(number)
             
    if start == "n":
        print("Thank you for Playing Blackjack")
        Game = True 