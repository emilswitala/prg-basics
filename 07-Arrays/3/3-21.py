# Write a program that checks 
# whether the first array 
# is a subset of the second one 
# (whether all elements of the first array 
# appear in the second array).

def subset(array1, array2):
    is_subset = True
    for x in array1:
        if x not in array2:
            is_subset = False
    return is_subset

if __name__ == "__main__":
    print(subset([2,4], [1,2,3,4,5]))
    print(subset([1,3], [1,2,4,5]))