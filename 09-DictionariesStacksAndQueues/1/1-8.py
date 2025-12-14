price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
# Due to a seasonal sale, the store is reducing the price of each item by 10%
# prints a list of products and their prices before the discount
for product, price in price_list.items():
    print(f"{product}: {price}")
# prints the total value of the products before the discount
total_before = 0
for price in price_list.values():
    total_before += price
print(round(total_before,2))
# modifies the price list according to the discount (round prices to two decimal places)
for product in price_list:
    discounted_price = price_list[product] * 0.9    
    price_list[product] = round(discounted_price, 2)
# prints a list of products and their prices after the 10% discount
for product, price in price_list.items():
    print(f"{product}: {price}")
# prints the total value of the products after the discount
total_after = 0
for price in price_list.values():
    total_after += price
print(round(total_after,2))