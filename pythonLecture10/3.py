# global variable if we put it outside of all functions
balance = 0

def main():
    # balance = 0 - local variable only local in this function belong to function main()
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance # now we allow to change global variable
    balance += n


def withdraw(n):
    global balance
    balance -=n



if __name__ == "__main__":
    main()