# properties are the attributes where we have more control over
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(
        self,
    ):  # instead of the placement of new object it shows string coz object goes in self
        return f"{self.name} from {self.house}"

    # creating methods
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # getter
    @property  # decorators are must!
    def house(
        self,
    ):  # now when we tryna assign to attributes it will go through functions
        return self._house

    # setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    # student.house = "Number Four, Privet Drive"
    student._house = "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
