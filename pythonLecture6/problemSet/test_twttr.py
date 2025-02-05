from twttr import shorten
import pytest

def main():
    test_shorten()
    test_shorten1()
    test_shorten2()
    test_shorten3()

def test_shorten():
    assert shorten("Misha") == "Msh"

def test_shorten1():
    assert shorten("mIshA") == "msh"

def test_shorten2():
    assert shorten("m,i,s,h,a") == "m,,s,h,"

def test_shorten3():
    assert shorten("123") == "123"


if __name__ == "__main__":
    main()