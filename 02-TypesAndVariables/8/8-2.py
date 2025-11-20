###
# Calculation of circle area and circumference 
# r = 1 --> circumference = 6.28, area = 3.14
# r = 3 --> circumference = 18.84, area = 28.26

# determine radius and PI values
# calculate area 
# calculate circumference 
# print results

radius = float(input('Enter radius: '))
pi = 3.14

area = pi * radius**2
circumference = 2 * pi * radius

print(f'The radius of your circle was {radius}. Its area is {area}. Its circumference is {circumference}.')
