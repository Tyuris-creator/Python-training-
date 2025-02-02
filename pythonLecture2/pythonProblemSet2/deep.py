def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    user_input = user_input.replace("-", " ")
    if user_input == "42":
        print("Yes")
    elif user_input == "forty two":
        print("Yes")
    else:
        print("No")




main()