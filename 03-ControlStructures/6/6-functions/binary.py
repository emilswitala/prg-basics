# define a function that will convert any decimal
# number to a binary number
# to do that, you have to divide the dec number by 2
# and add the remainder to the front
# repeat till 0

decimal = int(input("Enter your number: "))

def binary(decimal):
    binary = ""
    n = decimal
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n //= 2
    return binary

final = binary(decimal)

print(f"Your decimal number converts to {final} in binary code.") 