import re
# re.sub(pattern, repl, string, count=0, flags=0) substitute - замена
url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")