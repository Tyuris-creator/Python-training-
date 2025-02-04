name = input("What's your name? ")
# name of file, what we gonna do with it
file = open("names.txt", "w")
file.write(name) #replasing the old content, always recreating file
file.close()