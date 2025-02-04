from emoji import emojize


def main():
        user_input = input("Input: ")
        print(f"Output: {convert(user_input)}")

def convert(input):
        return emojize(input, language='alias')


main()