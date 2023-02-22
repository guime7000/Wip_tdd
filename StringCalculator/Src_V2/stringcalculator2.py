def calculate(expression: str) -> str:
    if len(expression) == 1:
        somme = int(expression)
    else:
        somme = int(expression[0]) + int(expression[2])

    return somme
