try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else: # выполняется в том случае если try блок True
    print(f"x is {x}")