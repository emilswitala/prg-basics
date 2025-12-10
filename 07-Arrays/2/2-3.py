# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
category_totals = [0, 0, 0]
for week in monthly_expenses:
    for i in range(len(week)):
        category_totals[i] += week[i]

weekly_totals = []
for week in monthly_expenses:
    weekly_totals.append(sum(week))

total = sum(weekly_totals)
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', category_totals[0])
print('Transport:', category_totals[1])
print('Utilities:', category_totals[2])
print('Week 1:', weekly_totals[0])
print('Week 2:', weekly_totals[1])
print('Week 3:', weekly_totals[2])
print('Week 4:', weekly_totals[3])
print('---------------')
print('TOTAL:', total)