def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__":
    main()


    # tuple is the collection of values in tuple you can't
    # change values 
    # tuple is immutable