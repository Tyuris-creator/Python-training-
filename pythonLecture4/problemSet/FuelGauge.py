def main():
    while True:
        try:
            fraction = input("Fraction: ")
            x,y = fraction.split("/")
            print(checker(x,y))
            break
        except (ValueError, ZeroDivisionError):
            pass
def checker(a,b):
    a = int(a)
    b = int(b)
    if a <= b:
        fuel_level = round((a / b) * 100)
        if fuel_level <= 1:
            return "E"
        elif fuel_level >= 99:
            return "F"
        else:
            return f"{fuel_level}%"
    else:
        raise ValueError
main()
