students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)


for student in students:
    print(f"{student['name']} is in {student['house']}")
    print(student)

print()
for student in range(len(students)):
    print(f"{students[student]['name']} is in {students[student]['house']}")
    print(students[student])
