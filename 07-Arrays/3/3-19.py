# Write a program that, 
# for the given array of real numbers, 
# prints the number of elements 
# that are greater than the 
# given value entered from the keyboard.

array = [7,2,4,5,8]

def the_great_function(number):
    greater = [x for x in array if x > number]
    return greater

number = int(input('Enter number: '))
print(the_great_function(number))