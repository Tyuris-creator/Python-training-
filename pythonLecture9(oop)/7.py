class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(type(student.name))
    print(type(student))

def get_student():
    student = Student()
    # classes have attributes we acces them by dot . 
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()

    # каждый раз когда мы обращаемя к классу мы создаем объект
    # instances тип образцы
    # мы можем создавать свои data type