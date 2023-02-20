def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """
    calculatedSum = 0

    if len(expression) == 0:
        return 0

    else:
        for elem in expression:
            if elem != ",":
                elem += elem
            calculatedSum += int(elem)

    return calculatedSum
