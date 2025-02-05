import random

def main():
    score = 0
    tries = 3
    lvl = get_level()
    for problem_given in range(10):
        int1 = generate_integer(lvl)
        int2 = generate_integer(lvl)
        expression = int1 + int2
        while True:
            try:
                answer = input(f"{int1} + {int2} = ")
                if int(answer) == expression:
                    score += 1
                    break
                elif int(answer) != expression:
                    tries -= 1
                    print("EEE")
                    if tries <= 0:
                        print(f"{int1} + {int2} = {expression}")
                        tries = 3
                        break

            except:
                tries -= 1
                print("EEE")
                if tries <= 0:
                    print(f"{int1} + {int2} = {expression}")
                    tries = 3
                continue

        tries = 3
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1,2,3]:
                raise ValueError
            else:
                return level
        except:
            pass

def generate_integer(level):
    if level == 1:
        integer = random.randint(0,9)
        return integer
    elif level == 2:
        integer = random.randint(10,99)
        return integer
    elif level == 3:
        integer = random.randint(100,999)
        return integer

if __name__ == "__main__":
    main()