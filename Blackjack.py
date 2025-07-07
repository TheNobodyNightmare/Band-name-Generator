import string
import random
number = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
def Computer_play():
        Computer_Card = random.choice(number)      
        Comp_Card = Computer_Card + Computer_Cards
        Comp_score = sum(Comp_Card) 
        return Computer_Card , Comp_score
def Card_2():
    Second_card = random.choices(number)
    print("Your Cards: " + str(Your_Cards))
    Card = Your_Cards + Second_card
    print("Your Cards: " + str(Card))
    Card_score = sum(Card)
    print(Card_score)
    if Card_score > 21 :
        print(f"your Hand :{Card},Final Score = {Card_score}")
        print(f"Computer Final hand : {Computer_Cards}, Final Score :{Computer_score}")
        print("You went Over , You lose ")
        Game = True
        Phase = True  
    elif Card_score == 21:
        print(f"your Hand :{Card},Final Score = {Card_score}")
        print(f"Computer Final hand : {Computer_Cards}, Final Score :{Computer_score}")
        print("You have hit a Blackjack ,You Win ")
        Phase  = True       
    elif Card_score <= 21:
        print(f"your Hand :{Card},Final Score = {Card_score}")
        print(f"Computer Final hand : {Computer_Cards}, Final Score :{Computer_score}") 
    return Card , Card_score  
 
Game = False
  
while not Game:
     
    
    start  = input("Do you want ot play a Game of blackjack? type y for yes or n for no \n")
    if start ==  "y":
        Your_Cards = random.choices(number,k=2)
    Score = Your_Cards[0] + Your_Cards[1]
    Computer_Cards = random.choices(number,k=1)
    Computer_score = Computer_Cards[0]
    print (f"Your Cards : {Your_Cards},Current Score : {Score}") 
    print(f"Computer Cards : {Computer_Cards}")       
    if Score == 21:
        print("you win")
        Game = True
    Second_card = random.choices(number)
    
    Phase = False 
    while not Phase:
        Direction = input("Would you like to Stand Or Take A Card ,y for a card and n for a Stand ")   
        if Direction == "y":
            Your_Cards, Card_Score = Card_2()
        else: 
            X = Computer_play()
            # if               ÷
            Phase = True 