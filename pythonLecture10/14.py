# *args **kwargs key, word arguments
def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25) # will be dictionary

# print(*objects, sep='', end='\n', file=sys.stdout, flush=False)