def main():
    user_time = input("What time is it? ")
    user_time = convert(user_time)
    if 7 <= user_time <= 8:
        print("breakfast time")
    elif 12 <= user_time <= 13:
        print("lunch time")
    elif 18 <= user_time <= 19:
        print("dinner time")


def convert(time):
    hour,minute =  time.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = minute / 60
    converted_time = hour + minute
    return converted_time

if __name__ == "__main__":
    main()
