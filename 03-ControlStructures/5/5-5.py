###
# Sums numbers entered by user
# calculates the average (arithmetic mean)

total_sum = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    x = len(str(number))
    average = total_sum / x

print(f"The total sum of the numbers is: {total_sum} with the average of {average}")