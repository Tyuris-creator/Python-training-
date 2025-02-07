# @classmethod - class method not object (instance method)
import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))




hat = Hat()
hat.sort("Harry")

# we have multiply hats that doesn't seem right because in the movies only one so 16.py