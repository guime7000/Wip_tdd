def calculate(expression: str) -> int:
    for i in range(len(expression)):
        if expression[i] == ",":
            return int(expression[:i]) + int(expression[i + 1 :])

    return int(expression)
