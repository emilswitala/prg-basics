###
# A program that calculates
# how many letters are between two given letters
# A and D (2 letters)
# B and M (10 letters)
# K and K (0 letters)

first = input('Enter first letter: ')
last = input('Enter your second letter: ')

first_letter_code = ord(first)
last_letter_code = ord(last)
if first_letter_code != last_letter_code:
    number_of_letters = last_letter_code - first_letter_code - 1
else:
    number_of_letters = 0

print(f'Between {first} and {last} is {number_of_letters} letters')