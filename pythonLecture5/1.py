# libraries are the code that comeone wrote before ot it is your code
# thta u published
# docs.python.org/3/library/random.html

height = int(input("What's height? "))

for i in range(height):
    for j in range(height - (i + 1)):
        print(" ", end="")
    for k in range(height - (height - (i + 1))):
        print("#", end="")
    print()


