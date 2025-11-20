###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a= ')
b = input('b= ')
c = input('c= ')

a = float(a)
b = float(b)
c = float(c)

volume = a*b*c 
surface_area = 2 * (a * b + b * c + a * c)

print('The volume of your cuboid is: ', volume)
print('The surface area of your cuboid is: ', surface_area)