while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
#break prgram when x is an integer and then print x "else" wont happen 
#till try will ne True