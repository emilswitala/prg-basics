## first number and second number are given (0, 1)
# prints n words

n = int(input('Enter how many words are supposed to be printed: '))
first = 0
second = 1
print(f"{first} {second}", end= " ")

def fibonacci(n):
    first = 0
    second = 1
    for i in range (3, n+1):
        next_num = first + second
        print(next_num, end =" ")
        first, second = second, next_num
    return fibonacci

rest = fibonacci(n)
