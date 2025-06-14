print("Welcome to the Tip Calculator")
print("What is the Total bill ?")
X = float(input("$"))

print("How much Would i like to tip ? %10 , %12, or %15")

B = int(input("%"))

print("How many people to spilt the bill?")

N = int(input())

F = X + X*B/100

P = F / N

print("Each person has to pay: ",P)