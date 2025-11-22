# Write a program that creates a multiplication table in the range 1 to 10 for any number entered by the user

number = int(input("Enter your number: "))
i = 1

while i <= 10:
    meow = i * number
    print(f"{number} * {i} = {meow}")
    i += 1