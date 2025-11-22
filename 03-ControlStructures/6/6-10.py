### Write a program that calculates a dog's age in dog's years. 
## For the first two years, a dog's life is equal to 10.5 human years. 
## After that, each dog year is equal to 4 human years. 
#
# Sample result:
#
## Enter the dog's age in human years: 15
## The dog's age in dog's years is 73 years.
#
#

age = int(input("Enter your dog's age: "))

if age <= 2:
    dog_years = age * 10.5
elif age > 2:
    dog_years = 21 + (age - 2) * 4

print(f"Your dog is {dog_years} years old!")