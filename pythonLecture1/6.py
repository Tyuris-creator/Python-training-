name = input("What's your name? ").strip().title()
#split user's name into first name and last name
first, last = name.split(" ")
print(f"Hello, {first}!")
print(f"Hello, {last}!")
print(f"Hello, {name}!")
