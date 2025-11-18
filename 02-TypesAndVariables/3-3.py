###
# A program for swapping two varable values
#
x = input('Enter your x: ')
y = input('Enter your y: ')

x = int(x)
y = int(y)

z = x # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values

x = y
y = z

print("After swapping: x=", x, "y=", y)