import random
import string
print("Welcome to secure Password Generator!")

letter = int(input("How many letters Would you like in Your Password? \n"))

symbols = int(input("How many Symbols Would you like ?\n"))

numbers = int(input("How many numbers would you like ?\n"))


Pass1 = string.ascii_letters 
Pass2 = string.digits
Pass3 = string.punctuation 




lett = random.choices(Pass1, k = letter )
  
sym = random.choices(Pass3, k = symbols)

num = random.choices(Pass2, k = numbers)


final_result = lett + sym + num


random.shuffle(final_result)
    
print(final_result)

password = ''.join(final_result)

print(f"Your password is: {password}")