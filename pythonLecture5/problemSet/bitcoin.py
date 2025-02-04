import sys
import requests
import json

def main():
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument ")
    elif len(sys.argv) == 2:
        try:
            if_integer = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number")

    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        dictionary = r.json()
        price = dictionary["bpi"]["USD"]["rate_float"]
        price = price * if_integer
        print(f"${price:,.4f}")

    except requests.RequestException:
        ...


main()