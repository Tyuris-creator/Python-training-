def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw" # будет изменен если лист возвращаем
        # c кортежом не будет
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] # list u can change [] () - tuple dont

if __name__ == "__main__":
    main()
