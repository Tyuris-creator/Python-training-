#square
def main():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #print(i)
        # for each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        #print(i)
        print()

main()