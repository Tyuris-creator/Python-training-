# . any character except new line
# * 0 or more repetitions
# + 1 or more repetitions
# ? 0 or 1 repetitions
# {m} m repetitions
# {m,n} m-n repetitions
# ^ matches the start of the string
# $ matches the end of the string 
# [] set of characters
# [^] complementing the set any character except ...
import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email): # ("..*@..*")
    print("Valid")
else:
    print("Invalid")