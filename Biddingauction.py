def Bidders()
  )





bidders = False 
while not bidders:
  name = input("What is your name ?")
  bid = input("What is your bid ?")
  Data = {}
  Data[name] = bid 
  
  end = input("Are there any Other bidders ? Type yes or no ")
  if end == "no":
    bidders = True 
    print()
    


