## There are coins of 1, 2 and 5 PLN
# Program that shows the number from the keyboard with 
# as few coins as possible
#
# Sample:
# Enter the amount in PLN: 18
# The amount of PLN 18 in coins:
# 5 PLN coins: 3
# 2 PLN coins: 1
# 1 PLN coins: 1

amount = int(input("Enter the amount in PLN: "))
amount_1 = amount

def coins(amount):
    coins_5 = amount // 5
    amount %= 5
    coins_2 = amount // 2
    amount %= 2
    coins_1 = amount // 1
    amount %= 1
    coins = coins_5 + coins_2 + coins_1

    return coins

total = coins(amount)
coins_5 = amount // 5
amount %= 5
coins_2 = amount // 2
amount %= 2
coins_1 = amount // 1
amount %= 1


print(f'The amount of PLN {amount_1} in coins:')
print(f"5 PLN coins: ", coins_5)
print(f'2 PLN coins: ', coins_2)
print(f'1 PLN coins: ', coins_1)
print("All coins: ", total)