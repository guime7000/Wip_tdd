def rewrite_empty_expression(expression: str) -> bool:
    """returns "0" if the length of expression equals 0"""
    if len(expression) == 0:
        expression = "0"

    return expression


def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """
    calculatedSum = 0
    integerSplit = []
    expressionLength = len(expression)

    expression = rewrite_empty_expression(expression)

    # A string to build integers digit after digit along expression
    temp_stringed_int = ""
    for idx in range(expressionLength):
        digit = expression[idx]
        if digit != ",":
            temp_stringed_int += digit
        if digit == "," or idx == expressionLength - 1:
            integerSplit.append(temp_stringed_int)
            temp_stringed_int = ""

    calculatedSum = sum(list(map(int, integerSplit)))

    return calculatedSum
