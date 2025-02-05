def main():
    while True:
        try:
            fraction = convert(input("Fraction: "))
            print(gauge(fraction))
            break
        except:
            pass


def convert(fraction):
    x,y = fraction.split("/")
    x = int(x)
    y = int(y)
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    percentage = round((x / y) * 100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()