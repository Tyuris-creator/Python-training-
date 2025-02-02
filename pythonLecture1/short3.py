def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I am not sure what you mean"

greeting = greet("hello, computer")
print(greeting)
