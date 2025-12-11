# second largest - sl

def sl(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array[1]

def min_and_max(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array[-1] - array[0]

def median(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    if len(array) % 2 != 0:
        return array[len(array)//2]
    elif len(array) % 2 == 0:
        return (array[len(array)//2] + array[len(array)//2 - 1])/2

def max_and_min(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array[0] - array[-1]

def largest_and_smallest(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return [array[-1], array[0]]

def string_minus(array):
    string = '-'.join(str(x) for x in array)
    return string

if __name__ == "__main__":
    print(sl([2,5,6,3,1]))
    print(min_and_max([2,5,6,3,1]))
    print(median([2,5,6,3,1]))
    print(median([2,5,6,4,3,1]))
    print(max_and_min([2,5,6,3,1]))
    print(largest_and_smallest([2,5,6,3,1]))
    print(string_minus([2,5,6,3,1]))