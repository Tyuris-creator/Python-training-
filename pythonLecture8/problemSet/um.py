import re

def main():
    print(count(input("Text: ")))

def count(s):
    um_list = re.findall(r"\b\W*(u){1}(m){1}\W*\b", s, re.IGNORECASE)
    return len(um_list)

if __name__ == "__main__":
    main()
