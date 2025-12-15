categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = expenses.index(max(expenses))
pricy_cat = categories[max_index]

third_index = expenses.index(1000)
print(categories[third_index])
print(pricy_cat)