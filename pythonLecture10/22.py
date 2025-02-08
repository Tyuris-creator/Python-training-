# dictionary comprehension 23.py

students = [
    "Hermione",
    "Harry",
    "Ron"
]

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors)