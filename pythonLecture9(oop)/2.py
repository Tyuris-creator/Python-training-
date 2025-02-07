def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    name = input("Name: ")
    return name

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()