## A program that reads an amount from the keyboard. 
# Then, it calculates and prints both the amount and its VAT.

amount = input('Enter your amount: ')
amount = float(amount)

vat = amount * 0.23 

print(f'Your amount is {amount}. A 23% VAT from that amount is {vat}')