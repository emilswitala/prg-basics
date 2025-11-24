
def time_string(hours, minutes, time_format):
    match time_format:
        case "24":
            return f"{hours:02}:{minutes:02}"
        case "12":
            match hours:
                case 0:
                    suffix = "am"
                    display_hour = 12
                case 12:
                    suffix = "pm"
                    display_hour = 12
                case hours if hours > 12:
                    suffix = "pm"
                    display_hour = hours - 12
                case _:
                    suffix = "am"
                    display_hour = hours
            return f"{display_hour}:{minutes:02}{suffix}"
        case _:
            return "Invalid format"
    
print(time_string(15, 38, '24'))
print(time_string(8, 3, '24'))
print(time_string(0, 5, '24'))
print(time_string(11, 15, '12'))
print(time_string(0, 7, '12'))
print(time_string(7, 30, '12'))
print(time_string(12, 46, '12'))
print(time_string(13, 10, '12'))
print(time_string(19, 2, '12'))