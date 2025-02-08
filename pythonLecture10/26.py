# generators 
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n): # can make overload your memmory
    flock = []
    for i in range(n):
        flock.append("🐑" * (i+1))
    return flock


if __name__ == "__main__":
    main()

