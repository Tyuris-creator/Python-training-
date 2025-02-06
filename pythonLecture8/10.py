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
# \d - decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitesace character
# \w word character as wel as numbers and the underscore
# \W not a word character
# a | b either A or B
# (...) a group
# (?:...) not-capturing version

# flags re.IGNORECASE re.MULTILINE re.DOTALL
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE): # ("..*@..*")
    print("Valid")
else:
    print("Invalid")