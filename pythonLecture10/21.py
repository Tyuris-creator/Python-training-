students = [
    "Hermione",
    "Harry",
    "Ron"
]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})


print(gryffindors)

# we can use dictionary comprehension to do it more easier way