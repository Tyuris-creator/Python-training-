def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What's x? "))
            #x = int(input("What's x? "))
            #return x
        except ValueError:
            print("x is not an integer")


main()