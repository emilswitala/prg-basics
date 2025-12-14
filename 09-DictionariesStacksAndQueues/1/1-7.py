products = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

# prints list and quantity
for key, value in products.items():
    print(f"{key}: {value}")

# the total number of products in the store
total = 0
for quantity in products.values():
    total += quantity
print(total)