# print unique elements in an array
array =[2,2,34,5,6,7,5]
for i in array:
    if array.count(i) == 1:
        print(i, end=' ')


unique = [x for x in array if array.count(x) == 1]
print(unique)