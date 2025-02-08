import sys
from tabulate import tabulate
import csv
#print(tabulate(table, headers, tablefmt="grid"))
#
def main():
    control = sys_control()
    if control == True:
        data = []
        while True:
            try:
                with open(sys.argv[1], "r") as csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        data.append(row)
                print(data)
                print(reader.fieldnames)
                print(tabulate(data, headers="keys", tablefmt="grid"))
                sys.exit()
            except FileNotFoundError:
                sys.exit("File does not exist")



def sys_control():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 2:
        while True:
            try:
                _, extension = sys.argv[1].split(".")
                if "csv" in extension:
                    return True
                else:
                    sys.exit("Not a CSV file")
            except:
                sys.exit("Not a CSV file")

main()