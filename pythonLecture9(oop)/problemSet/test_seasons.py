from seasons import checker, minutes
import pytest

def main():
    test_one()
    test_two()
    test_three()

def test_one():
    assert checker("1999-01-02") == True
    assert checker("2001-12-14") == True


def test_two():
    assert minutes("1999-01-02") == "Thirteen million, seven hundred thirty-three thousand, two hundred eighty minutes"
    assert minutes("2001-12-14") == "Twelve million, one hundred eighty-two thousand, four hundred minutes"

def test_three():
    with pytest.raises(SystemExit):
        checker("2001-15-12")

if __name__ == "__main__":
    main()
