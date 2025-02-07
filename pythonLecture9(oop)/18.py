class Wizzard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name



class Student(Wizzard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    

    ...


class Professor(Wizzard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizzard = Wizzard("Albus")
student = Student("Harry", "Gryffindor")
professor = Student("Severus", "Defense Against the Dark Arts")
        