count = int(input("Enter the no of the you want to give ?\n "))

numbers = []

for i in range(count):
    num = int(input("Enter the numbers:"))
    numbers.append(num)

print(numbers)


Total_sum = sum(numbers)
print(Total_sum)