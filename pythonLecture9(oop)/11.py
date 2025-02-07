class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name 
        self.house = house

    def __str__(self): # instead of the placement  of new object it shows string coz object goes in self
        return f"{self.name} from {self.house}"
    # creating methods
    
def main():
    student = get_student()
    #WE CAN CHANGE CLASS
    student.house = "Number Four, Privet Drive" # we changed thats bad 
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ == "__main__":
    main()
