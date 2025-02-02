# function - def - define
def main(): #function main - entry to the programm
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="user"):  #defining function hello
    print("Hello,", to)


main() #calling function name

#scope - variable only exist in the context where you defined it 
