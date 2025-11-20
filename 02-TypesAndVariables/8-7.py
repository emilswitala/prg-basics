## calculates a decimal number to binary and hexadecimal

number = int(input('Enter your number: '))

binary = bin(number)
hexadecimal = hex(number)

print(f'Your decimal number was {number}. It is {binary} in bin and {hexadecimal} in hex.')