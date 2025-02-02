def main():
    expression = input("Expression: ")
    integer1, operator, integer2 = expression.split(" ")
    integer1 = float(integer1)
    integer2 = float(integer2)
    if operator == "+":
        result = integer1 + integer2
    if operator == "-":
        result = integer1 - integer2
    elif operator == "*":
        result = integer1 * integer2
    elif operator == "/":
        result = integer1 / integer2
    print(round(result, 2))
main()
