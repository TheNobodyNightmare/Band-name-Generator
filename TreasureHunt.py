print("Welcome To THe Treasure Hunt!")
print("Your Mission is to find The Treasure ")

way = input("You have Two ways Left and Right?\n")

if way == "Left" :
    print("You have Reached an Ocean. There is a visble island in the ocean ")
    way2 = input ("Type \"wait\" to wait for the boat or Type \"swin\" To swin across the island \n" )
    if way2 == "wait":
        print('You reached the oceean unharmed .'
          'The island has a House with Three Doors'
          "Red,Yellow and Blue ")
    
        door = input("Which Door will you pick ? \n")

        if door == "Red":
            print("Burned by Fire!")
            print("Game Over!")
        elif door == "Blue" :    
            print("Eaten by Beast")
            print("Game Over!")
        else:
            print("You Win!")
    else:
        print('Attacked by sea monster in the Oceam\n'
              '          Game Over                 ')
        
else: 
    print('You Fell in a Hole \n'
          '    Game Over      ')
          