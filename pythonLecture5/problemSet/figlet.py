import random
from pyfiglet import Figlet
import sys
figlet = Figlet()
def main():
    if len(sys.argv) == 2:
        sys.exit("Invalid usage")
    if len(sys.argv) == 1:
        user_input = input("Input: ")
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font)
        rendered_text = figlet.renderText(user_input)
        print(rendered_text)
    elif len(sys.argv) == 3:
        fonts = figlet.getFonts()
        if (sys.argv[1] not in ["-f", "--font"]) or sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        else:
            user_input = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            rendered = figlet.renderText(user_input)
            print(rendered)


main()