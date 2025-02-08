import sys
import csv
def main():
    check = checker()
    if check == True:
        try:
            with open(sys.argv[2], "w", newline='') as csvfile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                with open(sys.argv[1], "r") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        last, first = row["name"].strip().split(",")
                        writer.writerow({"first": first.strip(), "last": last.strip(), "house": row["house"]})
            sys.exit()
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")


def checker():
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 3:
        return True



if __name__ == "__main__":
    main()



'''
with open(sys.argv[2], 'w') as csvfile:
                            fieldnames = ['first', 'last', 'house']
                            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                            writer.writeheader()
                            writer.writerow["first": first, "last": last, "house": row["house"]]
'''
