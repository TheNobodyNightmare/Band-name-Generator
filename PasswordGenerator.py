import random
import string
print("Welcome to secure Password Generator!")

letter = int(input("How many letters Would you like in Your Password? \n"))

#symbols = input("How many Symbols Would you like ?\n")

#numbers = input("How many numbers would you like ?\n")


Pass1 = string.ascii_letters 
Pass2 = string.digits
Pass3 = string.punctuation 

Final_letter = []
Final_digits = []
Final_symbols = []




for i in range(letter):
    lett = random.choices(Pass1)
    Final_letter.append(lett)

print(Final_letter)

result = ''.join(Final_letter)
print(result)

    