def main():
    greeting = input("Greeting: ")
    greeting = value(greeting)
    print(f"${greeting}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting[0:5] == "hello":
        return 0

    if len(greeting) == 0:
        return 100

    elif greeting[0] == "h":
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()
