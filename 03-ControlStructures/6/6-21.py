
number = int(input("The amount of money in PLN: "))

coins_5 = 0
coins_2 = 0
coins_1 = 0

coins_5 = number // 5
number %= 5

coins_2 = number // 2
number %= 2

coins_1 = number // 1
number %= 1

print("The amount of PLN 18 in coins:")
print(f"5 PLN coins: {coins_5}")
print(f"2 PLN coins: {coins_2}")
print(f"1 PLN coins: {coins_1}")