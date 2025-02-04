from hello import hello

def main():
    test_hello()


def test_hello():
    hello("David") == "hello, David"
    hello() == "hello, world"





if __name__ == "__main__":
    main()