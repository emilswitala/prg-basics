## Write a program that allows you to convert 
# time in 24-hour format to 12-hour format. 
# The time in 24-hour format (hh:mm) is read from the keyboard.


format_24h = input("Enter the time in 24-hour format: ")
format_12h = ""

if int(format_24h[0:2]) == 00:
    format_12h += str(int(format_24h[0:2]) + 12 ) + format_24h[2:5] + "AM"
elif int(format_24h[0:2]) <= 11:
    format_12h += format_24h + "AM"
elif int(format_24h[0:2]) == 12:
    format_12h += str(int(format_24h[0:2])) + format_24h[2:5] + "PM"
elif int(format_24h[0:2]) <= 23:
    format_12h += str(int(format_24h[0:2]) - 12 ) + format_24h[2:5] + "PM"
else:
    print("Invalid time")

print(f"Time in 12-hour format: {format_12h}")


