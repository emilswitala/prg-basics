# Write a program to separate 
# even and odd numbers 
# of a given array of integers. 
# Put all even numbers first, 
# and then odd numbers.

arr = [2, 5, 6, 7, 8, 9]
even = []
odd = []

for x in arr:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

arr = even + odd
print(arr)
print(even)
print(odd)