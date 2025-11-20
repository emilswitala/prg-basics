###
# A program that prints your height both in cm and in feet and inches.
#
# cm = 170
# feet = ...
# inches = ...
# calculate the number of feet

height = float(input('Enter your height in centimeters: '))

feet = height // 30.48
inches = (height / 2.54) - 12 * feet
inches = round(inches,2)

print(f'I am {height}cm tall, i.e. {feet} feet and {inches} inches.')