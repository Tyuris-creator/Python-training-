import inflect
p = inflect.engine()
list = []
def main():
    while True:
        try:
            user_input = input("Input: ")
            list.append(user_input)
        except EOFError:
            names = p.join(list)
            print(f"Adieu, adieu, to {names}")
            break

main()