## The parking meter calculates the parking fee based on the number of hours the car was parked according to the following rules:
#
# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
#
## Write a program that asks for the number of hours of parking, then calculates and prints the correct fee.
#

time = int(input("How many hours have you been parked here?: "))

if time < 1:
    print("You're good homie")
elif time <= 2:
    print("Your fee is 5 PLN")
elif time <= 6:
    print("Your fee is 15 PLN")
elif time > 6:
    print("Your fee is 20 PLN")