dict = {}

def main():
    while True:
        try:
            item = input().lower()
            if not item in dict:
                dict[item] = 1
            elif item in dict:
                dict[item] += 1
        except EOFError:
            dict_keys = sorted(dict)
            for i in dict_keys:
                print(dict[i], i.upper())
            break


main()
