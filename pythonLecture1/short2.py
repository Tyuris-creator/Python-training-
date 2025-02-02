# n! = n * (n-1)!
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

result = factorial(3)
