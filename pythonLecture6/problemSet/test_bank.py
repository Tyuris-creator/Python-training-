from bank import value

def main():
    test_first()
    test_second()
    test_third()
    test_four()


def test_first():
    assert value("HELLO") == 0
    assert value("hello") == 0
    assert value("hello dear client") == 0
    assert value(" hello") == 0
    assert value(" HeLLo dear cleint, we are happy to see you") == 0


def test_second():
    assert value("How are u") == 20
    assert value("Hey") == 20
    assert value("Hi") == 20
    assert value("hi") == 20
    assert value("hey how are you?!") == 20
    assert value(" h") == 20

def test_third():
    assert value("1") == 100
    assert value("!?.x/") == 100
    assert value("What u need MATE?") == 100
    assert value("ok helo") == 100
    assert value(".hi") == 100
    assert value(" ") == 100
    assert value("dear client hello") == 100

def test_four():
    assert value("                    ") == 100




if __name__ == "__main__":
    main()
