import random
print("Welcome to the Rock, Paper, Scissor Game ")

turn = input("What do you choose ? Type \"R\" for Rock , \"P\" For paper and \"S\" for Scissors \n")
 
    

Rock = '''
    _______ 
____'   ____)
      (_____)
      (_____)
      (_____)
---.__(____)        
'''

Paper = '''

    _______  
___,    ____)____
          _______)
          _________) 
          _______)
---.__________)
'''

Scissor = '''
    ________      
____,    ____)____
            _______)
          ___________)    
        (_____)
---.____(____)
'''

if turn == "R" or turn == "Rock" or turn == "r":
    print(Rock)
elif turn == "P" or turn == "Paper" or turn == "p"  :
    print(Paper)
else:
    print(Scissor)

turn2 = [Rock, Paper, Scissor]
play = random.choice(turn2)  
print(play)

if turn == "R" and play == Scissor:
    print("You Win")
elif turn == "R" and play == Paper:
    print("You Lose ")       
elif turn == "P" and play == Scissor:
    print("You Lose")
elif turn == "P" and play == Rock:
    print("You Win")
elif turn == "S" and play == Rock:
    print("You Lose")
elif turn == "S" and play == Paper:
    print("You Win")       
else:
    print("Its a Tie ")