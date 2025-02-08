import sys
from PIL import Image, ImageOps

def main():
    check = checker()
    if check == True:
        try:
            shirt = Image.open("shirt.png")
            user_picture = Image.open(sys.argv[1])
            size = shirt.size
            user_picture = ImageOps.fit(user_picture, size)
            user_picture.paste(shirt, (0,0), shirt)
            user_picture.save(sys.argv[2])

        except FileNotFoundError:
            sys.exit("Input does not exist")


def checker():
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    elif len(sys.argv) == 3:
        try:
            _, extension1 = sys.argv[1].split(".")
            _, extension2 = sys.argv[2].split(".")
        except:
            sys.exit("Invalid output")
        if extension1 not in ["jpg", "jpeg", "png"] or extension2 not in ["jpg", "jpeg", "png"]:
            sys.exit("Invalid output")
        elif extension1 in ["jpg", "jpeg", "png"] and extension2 in ["jpg", "jpeg", "png"]:
            if extension1 == extension2:
                return True
            elif extension1 != extension2:
                sys.exit("Input and output have different extensions")



if __name__ == "__main__":
    main()
