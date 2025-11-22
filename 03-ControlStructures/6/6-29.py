import math

n = int(input("Enter number: "))

counter = 0
num = 2    # pierwsza liczba pierwsza

while counter < n:
    is_prime = True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
        counter += 1
    
    num += 1