# command line arguments
import sys

try:
    print("Hello, my name is", sys.argv[1])
    print(f"The name of the programm {sys.argv[0]}")
except IndexError:
    print("Too few arguments")
    
