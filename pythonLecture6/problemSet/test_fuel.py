from fuel import convert, gauge
import pytest

def main():
    test_one()
    test_two()
    test_three()

def test_one():
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_two():
    assert gauge(25) == "25%"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("1/4") == 25 and gauge(25) == "25%"

def test_three():
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

if __name__ == "__main__":
    main()