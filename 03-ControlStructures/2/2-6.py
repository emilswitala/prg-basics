## Write a program that checks if the number is positive, negative or a zero
# Determine the number - input 
# if the number is bigger than 0 it's positive
# if the number is less than 0 it's negative
# if the number is 0 it's... zero...
# if something other than a valid number was entered, print a message 
##
#

print('Check if your number is positive, negative or a zero!')
number = int(input('Please enter your number: '))

if number > 0:
    print('Your number is bigger than 0, so it is positive!')
elif number < 0:
    print('Your number is less than 0, so it is negative!')
elif number == 0:
    print('Your number is a zero!')