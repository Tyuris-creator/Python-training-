def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        for j in range(i+1):
            print(j, end="")
        print()


if __name__ == "__main__":
    main()
