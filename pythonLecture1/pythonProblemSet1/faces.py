def main():
    user_input = input()
    print(convert(user_input))

def convert(input):
    msg = input.replace(":)", "🙂").replace(":(", "🙁")
    return msg

main()