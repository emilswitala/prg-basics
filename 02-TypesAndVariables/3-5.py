###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = input('Enter side a: ')
b = input('Enter side b: ')

a = int(a)
b = int(b)

diagonal = math.sqrt(a**2 + b**2)
print('The diagonal of this rectangle is: ', diagonal)