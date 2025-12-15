# An array contains integer numbers: 34,7,19,4,21,8. 
# Create a program that calculates and 
# prints the number of even values in the array. 
# Use the ‘while’ loop statement.

arr = [34, 7, 19, 4, 21, 8]

i = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i], end= " ")
    i += 1