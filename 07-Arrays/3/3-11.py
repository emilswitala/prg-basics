def bubblesort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == "__main__":
    print(bubblesort([12, 435, 24, 245, 353]))
    print(bubblesort([12, 3, 2,4,5,6]))
    print(bubblesort([12,234,76,43]))