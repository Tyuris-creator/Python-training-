students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

#print(students["Draco"]) #keys, values pairs
    
for student in students:
    print(student, students[student], sep=", ") #only keys will be shown if we use iterable on dict

#for student in range(len(students)):
    #print(student+1)
