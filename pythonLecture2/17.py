#switch
name = input("What's your name? ")
g = "Gryffindor"
c = "Slytherin"

match name:
    case "Harry" | "Hermione" | "Ron": # | 
        print(g)
    case "Draco":
        print(c)
    case _:
        print("Who?")