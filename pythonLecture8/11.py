import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# re.match(pattern, string, flag=0)
# re.fullmatch(pattern, string, flags=0)