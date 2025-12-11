# Define a function rand_elem(array) 
# that returns a randomly 
# selected array element. 
# Using the function, 
# print a few randomly 
# selected array elements.
import random 

def rand_elem(array):
    n = len(array)
    i = random.randint(0, n-1)
    return array[i]

if __name__ == "__main__":
    print(rand_elem([1,2,3,4,5,6,7]))