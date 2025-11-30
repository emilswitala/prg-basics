from datetime import datetime

def f(time1, time2):
    def parse_time(t):
        if 'm' in t.lower():
            return datetime.strptime(t.upper(), "%I:%M%p")
        else:
            return datetime.strptime(t, "%H:%M")
    
    t1_obj = parse_time(time1)
    t2_obj = parse_time(time2)

    if t1_obj < t2_obj:
        return time1
    else:
        return time2

if __name__ == "__main__":
    print(f("11:00am", "02:30pm"))
    print(f("10:00pm", "22:05"))
    print(f("14:00", "01:00pm"))