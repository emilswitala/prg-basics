## a program that calculates the distance to the horizon
# from a height given in meters from the keyboard

import math

h = input('Height: ')
h = float(h)

d = 3.57 * math.sqrt(h)

print(f'The distance to the horizon from {h} meters is: ', d)