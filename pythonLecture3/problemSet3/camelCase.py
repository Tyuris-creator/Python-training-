def main():
    user_input = input("camelCase: ")
    convert(user_input)

def convert(camelCase):
    letters = []
    for letter in camelCase:
        if letter.isupper():
            letter = letter.lower()
            letter = "_" + letter
        letters.append(letter)
    print("".join(letters))

main()
