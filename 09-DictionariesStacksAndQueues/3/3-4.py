# Division	Remainder
# 18 / 2 = 9	0
# 9 / 2 = 4	1
# 4 / 2 = 2	0
# 2 / 2 = 1	0
# 1 / 2 = 0	1
# Natural number: 18
# Binary number: 10010 

import queue

number = int(input("Enter a natural number: "))
stack = queue.LifoQueue()

n = number

while n > 0:
    stack.put(n % 2) # puts the remainder on the stack (the binary number is remainders backwards)
    n //= 2

binary = ""
while not stack.empty():
    binary += str(stack.get())

print("Natural number:", number)
print("Binary number:", binary)