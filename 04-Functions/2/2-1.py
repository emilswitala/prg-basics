###
# Program for testing built-in functions
# the largest number: 7,5,6,3,8,2
# the smallest number: 4,7,2,3,9,8
# length of the phrase: "computer science"
# letter read from the keyboard
# number representing the string "20303"
# binary string representing decimal number 304
# hexadecimal string representing decimal number 304
# integer representing the Unicode code of the € sign
# absolute value of -17


max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter_from_keyboard = input("Enter letter from keyboard: ")
print("The entered letter is: ",letter_from_keyboard)

number = int("20303")
print('The number is', number)

binary = bin(304)
print("Binary string representing is", binary[2:])

hexadecimal = hex(304)
print("Hecadecimal string representing is", hexadecimal[2:])

integer = ord("€")
print("Integer representing the Unicode code of the € sign is", integer)

value = abs(-17)
print("The absolute value of - 17 is: ", value)