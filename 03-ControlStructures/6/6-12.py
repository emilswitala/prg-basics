###
# In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products and the product price from the keyboard. 
# Sample result:
# Number of products purchased: 5
# Product price: 40
# Amount to pay: 170.00
## 
#

number = int(input("Number of products purchased: "))
price = float(input("Product price: "))
price = round(price,2)

if number <= 2:
    price = price * number
else:
    price = price * 2 + (number - 2) * price * 0.75

print("Amount to pay: ", price)