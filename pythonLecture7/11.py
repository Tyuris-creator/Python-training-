students = []
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in range(len(sorted(students))):
    print(student+1, students[student])