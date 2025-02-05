from plates import is_valid

def main():
    test_one()
    test_two()
    test_three()
    test_four()

def test_one():
    assert is_valid("CS50") == True
    assert is_valid("CSCS50") == True
    assert is_valid("CS5") == True
    assert is_valid("CS") == True

def test_two():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME ") == False

def test_three():
    assert is_valid("PI3.14") == False

def test_four():
    assert is_valid("123CS") == False


if __name__ == "__main__":
    main()
