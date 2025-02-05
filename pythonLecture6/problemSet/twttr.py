def main():
    user_twit = input("Input: ")
    print(shorten(user_twit))


def shorten(word):
    exclude = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    phrase = []
    for letter in word:
        if letter in exclude:
            continue
        else:
            phrase.append(letter)
    return ''.join(phrase)


if __name__ == "__main__":
    main()
