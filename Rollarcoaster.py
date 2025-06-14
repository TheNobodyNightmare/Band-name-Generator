print("Welcome to the Rollercoaster!")
height = int(input("Enter Your Height (cm) :")) 

bill = 0


if height > 120:
  print("You can ride the Rollarcoster ")
  
  age = int(input("Please Enter your age :"))
  
  if age <= 45:
    print("YOur Fare Prize is $18")
    bill = 18
  
  elif age <= 12:
    bill = 5
    print("Your Fare prize is $5")
  
  elif age >= 45 and age <= 55:
    bill = 0
    print("Your Fare is covered by us")
  else:
    bill = 12
    print ("Your Fare Prize is $12")

  print("Do you Want Us to take Photo")
    
  Photo = input()
  if Photo == "yes" and age <= 45 and age >= 55:
    bill = bill+3  
    print("Your Total Fare Prize is:",bill)
    if Photo == "yes" and age >= 45 and age <= 55 :
        bill = 0
  else:
    print("Your Total bill is:",bill)
else:
  print("Sorry You Cant Ride The Rollarcoster ")
