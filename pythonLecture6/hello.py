def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    # print("hello,", to) #this function has side effect of printing
    # so it cant be tested
    return f"hello, {to}"
     


if __name__ == "__main__":
    main()
    