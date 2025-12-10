# Prints the array elements in reverse

arr = [15, 8, 31, 47, 2, 19]

for i in range(len(arr)):
    print(arr[i], end=" ")

print() 

for i in reversed(range(len(arr))):
    print(arr[i], end=" ")