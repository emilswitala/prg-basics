### A computer program analyses the price of a product in an online store. 
# If the product price decreases by at least 10%, the program prints a purchase recommendation:
## Buy the product!!
## Product price reduced by 17%
#
# Create such program. The current and previous price of the product are included in variables. 
#
# Sample result:
# Current product price: 140.00
# Previous product price: 200.00
# Buy the product!!
# Product price reduced by 30%

price_dropped = float(input("Enter the current price of the product: "))
price_dropped = round(price_dropped,2)

original_price = float(input("Enter the previous price of the product: "))
original_price = round(original_price,2)

discount = 100 - (price_dropped * 100 / original_price )
discount = round(discount,2)

while price_dropped < original_price:
    if discount < 10:
      print("Don't bother")
      print(f"Product price reduced by {discount}%")
    else:
      print("Buy the product!!")
      print(f"Product price reduced by {discount}%")
    break
else:
   print("This isn't even reduced bro.")