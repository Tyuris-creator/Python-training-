import random

def main():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input > 0:
                random_num = random.randint(1, user_input)
                break
        except:
            pass
    while True:
        try:
            user_input2 = int(input("Guess: "))
            if user_input2 > random_num:
                print("Too large!")
            elif user_input2 < random_num:
                print("Too small!")
            else:
                print("Just right!")
                return "Just right!"
        except (TypeError, ValueError):
            pass

if __name__ == "__main__":
    main()
