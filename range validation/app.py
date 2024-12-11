# number salection is between 1-20

num = int(input("Enter number (1 - 20): "))

while num < 1 or num > 20:
    print(f"{num} is not a valid number")
    num = int(input("Enter number : "))

print(num)