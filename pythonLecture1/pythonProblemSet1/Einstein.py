c = 300000000

def main():
    user_input = int(input("What's the mass? "))
    user_input = energy(user_input)
    print(user_input)

def energy(mass):
    e = mass * pow(c,2)
    return e

main()
