def main():
    pace = get_pace(miles=26.2, minutes=180)
    print(f"You need to run each mile in {round(pace, 2)} minutes")

def get_pace(miles, minutes):
    if not minutes > 0:
        raise ValueError("Invalid value")
    return minutes / miles

#to alert user u need to use raise exception block of code

main()