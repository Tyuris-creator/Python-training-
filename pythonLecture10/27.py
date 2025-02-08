# generators 
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n): # can make overload your memmory
    for i in range(n):
        yield "🐑" * (i+1) # return one value at a time 
        # iterators


if __name__ == "__main__":
    main()
