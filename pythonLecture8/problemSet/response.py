from validator_collection import validators

def main():
    user_email = input("What's your email address? ")
    print(checker(user_email))


def checker(email):
    while True:
        try:
            is_valid = validators.email(email)
            if is_valid == email:
                return "Valid"
        except:
            return "Invalid"


if __name__ == "__main__":
    main()
