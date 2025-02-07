def main():
    with open("alice.txt", "r", encoding="utf-8") as file:
        contents = file.read()
        contents1 = file.readlines()
    #print(contents)
    print(contents1[0])
main()