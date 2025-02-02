#pypi.org #pypi the collection of python packages
# pip allows u install libraries on python
import cowsay
import sys

if len(sys.argv) == 2:
    print(cowsay.trex("hello, " + sys.argv[1]))
