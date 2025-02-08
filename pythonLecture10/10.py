# - for single character (-c, -n etc) -- for words --number
# -h or --help show how to use any program
import argparse

parser  = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")