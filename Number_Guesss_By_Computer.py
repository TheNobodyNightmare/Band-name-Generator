def Game(low,high):
    attempts = 0 
    while True:
        attempts += 1 
        guess = (high + low ) // 2 
        print(f"Is your Number : {guess}")
        Feedback = input("Enter A hint for the Computer:")
        if Feedback == "Higher" or Feedback == "H":
            low = guess + 1 
        elif Feedback == "Lower" or Feedback == "L":
            high = guess - 1
        elif Feedback == "Correct":
            print(f"\nYay The AI has Guess The Number")
            break
        elif Feedback == "Exit":
            break
        else:
            print("Please Enter Between 'Higher' or 'Lower' or 'correct'")           

def Start():
    print("Welcome to the Game of Guessing!")
    print("Give A Number And Range between The Number and The Ai will Guess The Number")
    low = int(input("Enter Your Low Number:"))
    high = int(input("Enter Your High Nummber:"))
    print(f"Think of a Number Between {low} and {high}")
    Game(low,high)

One = input("Do you want to play The Game of Guessing :")
if One == "Yes" or One == "y":
    Start()
else:
    print("Thank you For Visiting Us")





































                   