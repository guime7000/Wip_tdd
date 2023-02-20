def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """
    calculatedSum = 0
    expressionSplit = []

    if len(expression) == 0:
        return 0

    else:
        expressionLength = len(expression)
        temp_stringed_int = ""
        for idx in range(expressionLength):
            digit = expression[idx]
            if digit != ",":
                temp_stringed_int += digit
            if digit == "," or idx == expressionLength - 1:
                expressionSplit.append(temp_stringed_int)
                expressionSplit.append(digit)
                temp_stringed_int = ""

        for idx in range(0, len(expressionSplit), 2):
            calculatedSum += int(expressionSplit[idx])
    return calculatedSum
