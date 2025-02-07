# classes come with certain methods they are function inside class

class Student:
    def __init__(self, name, house): # we are adding instance variables to objects
        self.name = name 
        self.house = house
# self gives access to object that has been created
def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
    print(type(student))

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # now we must define types to class we have more control compared to 7.py
    return student

if __name__ == "__main__":
    main()
