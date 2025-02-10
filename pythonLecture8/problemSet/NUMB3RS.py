import re
import sys

def main():
    check = checker()
    if check == True:
        print(validate(sys.argv[1]))

def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        ip_numbers = ip.split(".")
        for ip_number in ip_numbers:
            if int(ip_number) < 0 or int(ip_number) > 255:
                return False
            else:
                continue
        return True
    else:
        return False

def checker():
    if len(sys.argv) == 1:
        sys.exit("Cant find provided IP")
    elif len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif len(sys.argv) == 2:
        return True

if __name__ == "__main__":
    main()
