import sys
import csv

def main():
    check = checker()
    if check == True:
        count = 0
        while True:
            try:
                with open(sys.argv[1], "r") as file:
                    file = file.readlines()
                    for line in file:
                        if line.lstrip().startswith("#") or line.strip() == "":
                            continue
                        else:
                            count += 1
                    print(count)
                    break
            except FileNotFoundError:
                print("File does not exist")
                break
    else:
        print(check)


def checker():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        while True:
            try:
                _, extension = sys.argv[1].split(".")
                if "py" in extension:
                    return True
                else:
                    sys.exit("Not a Python file")
            except:
                sys.exit("Not a Python file")

if __name__ == "__main__":
    main()
