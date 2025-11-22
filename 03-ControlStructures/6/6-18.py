#Let x and y denote the coordinates of a point on the plane. 
# Write a program that determines in which quadrant of the coordinate system the point 
# P(x, y) is located or on which axis it is located, or that it is located in the position (0,0) of the coordinate system.

x = float(input("Enter x: "))
y = float(input("Enter y: "))

if x < 0 and y < 0:
    print(f"Point ({x}, {y}) is in the third quadrant of the coordinate system!")
elif x > 0 and y > 0:
    print(f"Point ({x}, {y}) is in the first quadrant of the coordinate system!")
elif x < 0 and y > 0:
    print(f"Point ({x}, {y}) is in the second quadrant of the coordinate system!")
elif x > 0 and y < 0:
    print(f"Point ({x}, {y}) is in the fourth quadrant of the coordinate system!")
elif x == 0 and y == 0:
    print(f"Point ({x}, {y}) is located on the beginning of the coordinate system!")
elif x == 0:
    print(f"Point ({x}, {y}) is located on the y-axis!")
elif y == 0:
    print(f"Point ({x}, {y}) is located on the x-axis!")
else:
    print('Choose a different one buddy')