###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]
middle = len(arr)//2
print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Second to last value', arr[-2])
print('Sum of the first and last', arr[0]+arr[-1])
print('Middle value', arr[middle])
print('All array values separated by a single space ', end='')
for value in arr:
    print(value, end=' ')


