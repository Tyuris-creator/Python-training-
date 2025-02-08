students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = [
    key["name"] for key in students if key["house"] == "Gryffindor"
]

for i in range(len(gryffindors)):
    print(gryffindors[i])

