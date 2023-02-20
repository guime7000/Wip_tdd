def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """
    calculatedSum = 0

    if len(expression) == 0:
        return 0

    else:
        if expression[-1] != ",":
            calculatedSum += int(expression)

    return calculatedSum
