import re

email = input("What's your email").strip()

if re.search("@", email):
    print("Valid")
else:
    print("Invalid")

    # . any character except new line
    # * 0 or more repetitions
    # + 1 or more repetitions
    # ? 0 or 1 repetitions
    # {m} m repetitions
    # {m,n} m-n repetitions