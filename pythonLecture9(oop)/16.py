import random

class Hat:
    # class variable
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    @classmethod  
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Harry")

#hat = Hat()
#hat.sort("Harry")
#hat.sort("Draco")