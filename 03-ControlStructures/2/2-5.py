###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1-12): '))

if month >= 10 and month <= 12:
    quarter = 4
    print(f'Month {month} is in quarter {quarter}')
elif month >= 7 and month < 10:
    quarter = 3
    print(f'Month {month} is in quarter {quarter}')
elif month >= 4 and month < 7:
    quarter = 2
    print(f'Month {month} is in quarter {quarter}')
elif month >= 1 and month < 4:
    quarter = 1
    print(f'Month {month} is in quarter {quarter}')
else:
    print("There are 12 months homie. You can pick from 1 to 12. Nothing else. Sorry.")