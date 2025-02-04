with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} in in {house}")