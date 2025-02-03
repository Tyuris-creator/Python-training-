months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            date = input("Date: ").strip()
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
            elif "," in date:
                month_day, year1 = date.split(",")
                month1, day1 = month_day.split(" ")
                day1 = int(day1)
                if day1 <= 31:
                    if month1 in months:
                        print(f"{year1.strip()}-{(months.index(month1) + 1):02}-{day1:02}")
                        break
        except:
            pass

main()
