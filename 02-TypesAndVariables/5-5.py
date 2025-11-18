## The price of the product on the price tag is given 
# before and after the discount is applied. 
# Write a program that allows you to enter the product price and discount.
# Print the product price, discount, 
# discounted product price, 
# and the difference between the product price before 
# and after the discount. Print all prices with two decimal places.

price = input('Enter the price of the product in PLN: ')
price = float(price)
discount = input('Enter your discount in %: ')
discount = float(discount)

dropped_price = (price * (100 - discount))/100
price = round(price,2)
dropped_price = round(dropped_price,2)
diff = price - dropped_price 


print(f"The price of this product before was {price} PLN. A discount of {discount}% was applied. Your new price is {dropped_price} PLN. You have saved {diff} PLN.")