import re
import sys
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM
# 12 AM to 12 PM

def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^((?P<hour>[0-9]{1}|[1]{1}[0-2]{1})(:(?P<min>[0-5]?[0-9]?))?)? (?P<time>[AP]M) to ((?P<hour1>[0-9]{1}|[1]{1}[0-2]{1})(:(?P<min1>[0-5]?[0-9]?))?)? (?P<time1>[AP]M)$"
    match = re.search(pattern, s)
    if match:
        hour = match.group("hour").strip()
        min = match.group("min")
        if not ":" in pattern:
            hour = int(hour) + int(min)
        time_extension = match.group("time").strip()
        hour1 = match.group("hour1").strip()
        min1 = match.group("min1")
        time_extension1 = match.group("time1").strip()
        #print(f"{hour} {min} {time_extension} {hour1} {min1} {time_extension1}")
        first_part = new_format(hour, min, time_extension)
        second_part = new_format(hour1, min1, time_extension1)
        return first_part + " to " + second_part
    if not match:
        raise ValueError
    if int(hour) > 12 or int(hour1) > 12:
        raise ValueError


def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ":00"
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time



if __name__ == "__main__":
    main()
