#horizontal bricks

def main():
    print_row(4)

def print_row(width):
    #print("?" * width)
    for _ in range(width):
        print("?", end="")


main()