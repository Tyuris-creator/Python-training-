weight = float(input("Enter your weght: "))
unit = input("K or L: ")

try:
    if unit == "K":
        weight = weight * 2.205
        unit = "Lbs"
    elif unit == "L":
        weight = weight / 2.205
        unit = "Kgs"
    elif unit not in ["K", "L"]:
        raise ValueError()
except ValueError:
    print(f"{unit} was not valid")
else:
    print(f"Your weight is {round(weight,1)} {unit}")
finally:
    print("Thanks for using our converter!")
