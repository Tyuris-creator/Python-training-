names = []
with open("names.csv", "r") as file:
    #lines = file.readlines() #read all lines from file and return as a list
    for line in file:
        print("hello,", line.rstrip())


for name in sorted(names):
    print(f"hello, {name}")


    