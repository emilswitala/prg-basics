arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
# creates a program that prints the numbers that
# don't appear in the second (so everything except 5&36)

result = [i for i in arr1 if i not in arr2]
print(result)

for i in arr1:
    if i not in arr2:
        print(i, end=' ')