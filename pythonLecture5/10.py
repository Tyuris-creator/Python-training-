import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in range(len(sys.argv)):
    if arg + 1 < len(sys.argv):
        print("hello, my name is", sys.argv[arg + 1])