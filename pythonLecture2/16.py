#switch
name = input("What's your name? ")
g = "Gryffindor"
c = "Slytherin"

match name:
    case "Harry":
        print(g)
    case "Hermione":
        print(g)
    case "Ron":
        print(g)
    case "Draco":
        print(c)
    case _:
        print("Who?")