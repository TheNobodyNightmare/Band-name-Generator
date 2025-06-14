print("Welcome to the Pythons Pizza Deliveries Service!")

size = input("What size Do you want your pizza ? Small(S), Medium(M), Large(L)\n   ")

pepperoni = input("Do you want Pepperoni on yout PIzza ?\n")

extra_chesse = input("Do you want extra chesse on your pizza ?\n")

bill = 0

Small_pizza = 15
Medium_pizza = 20
Large_pizza = 25
#Size prize 

if size == "S":
  bill = bill + Small_pizza
elif size == "M" :
  bill = bill + Medium_pizza
elif size == "L" :
  bill = bill + Large_pizza

  
#Pepperoni 

if pepperoni == "Y" and size == "S":
  bill += 2
else :
 bill += 3 
 
 #Extra chesse
 if extra_chesse == "Y":
   bill += 1

print("Your Total bill is :$",bill)
  
#  print(bill)
  

      