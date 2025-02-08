# *args **kwargs key, word arguments
def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25) # will be tuple