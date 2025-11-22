# Fibonacci

n = 20
first = 0
second = 1
print(f"{first} {second} ")

for i in range(3, n+1): 
    next_num = first + second
    print(next_num, end=' ')
    first, second = second, next_num