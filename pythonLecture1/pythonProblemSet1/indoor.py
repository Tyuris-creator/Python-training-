def lower():
    phrase = input("Write a phrase? ")
    phrase = phrase.lower()
    return phrase
def main():
    user_phrase = lower()
    print(user_phrase)
main()