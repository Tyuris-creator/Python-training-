# to file close automatically after we done work with it we should use this syntax

name = input("What's your name? ")

with open("names.txt","a") as file:
    file.write(f"{name}\n")
    
    