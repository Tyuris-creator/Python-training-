from datetime import date, timedelta
from validator_collection import validators
import inflect
import sys
p = inflect.engine()

def main():
    user_date = input("Date of Birth: ")
    print(minutes(user_date))

def minutes(user_date):
    if checker(user_date) == True:
        year_u, month_u, day_u = user_date.split("-")
        year_u = int(year_u)
        month_u = int(month_u)
        day_u = int(day_u)
        date2 = what_is_the_day()
        d = date2 - date(year_u, month_u, day_u)
        #print(type(d)) this is the delta
        days = d.days
        convert_to_minutes = days * 24 * 60
        #print(convert_to_minutes)
        convert_minutes_to_words = p.number_to_words(convert_to_minutes, andword="").capitalize()
        return f"{convert_minutes_to_words} minutes"

def checker(d):
    while True:
        try:
            passing_date = validators.date(d)
            if passing_date:
                return True
            else:
                return "Invalid date"
        except:
            sys.exit("Invalid date")

def what_is_the_day():
    return date.today()

if __name__ == "__main__":
    main()
