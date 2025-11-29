

format_24h = input("Enter time in 24h format: ")

def format_12h(format_24h):
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
    return format_12h

correction = format_12h(format_24h)
print(f"Your time is {correction} in 12h format")
