from numb3rs import validate

def main():
    test_one()
    test_two()
    test_three()


def test_one():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("2.2.2") == False
    assert validate("255") == False

def test_two():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True

def test_three():
    assert validate("255.256.256.256") == False

if __name__ == "__main__":
    main()
