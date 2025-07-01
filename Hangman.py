import random

word_list = ("Itlay","London","France","England")
Random_word_list = random.choice(word_list).lower()

lives = 6

print(Random_word_list)
print("Guess the Word :",end="")


Blanck = len(Random_word_list)


for char in range(Blanck):
    print("_",end="")
print()
   

corrent_display = []

game_over = False 

while not game_over:
    guess = input("Guess the word = ").lower()
    
    display = ""
    
    for char in Random_word_list:
        if char == guess:
            display += char
            corrent_display.append(guess)  
        elif char in corrent_display:   
            display += char 
        else :
            display += "_"

    print(display)        
    
    if guess not in Random_word_list:
        live -= 1
        if live == 0:
            game_over = True 
            print("YOu lose")
    if "_" not in display :
        print("You win")
        game_over = True 
        

