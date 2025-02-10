import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>", s):
        pattern = r"(https?:\/\/(?:www\.)?youtube\.com\/embed\/(?P<URL>[a-zA-Z0-9_-]+))"
        match = re.search(pattern, s)
        if match:
            url = match.group("URL")
            return f"https://youtu.be/{url}"


if __name__ == "__main__":
    main()
