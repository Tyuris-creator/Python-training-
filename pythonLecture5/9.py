import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

#if mistakes happened program will stop and didnt reach the final print (indexError)

print("Hello, my name is", sys.argv[1])
