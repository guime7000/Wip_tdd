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

        temp_stringed_int = ""
        for digit in expression:
            temp_stringed_int += digit
            if digit == ",":
                calculatedSum += int(temp_stringed_int)
                temp_stringed_int = ""

    return calculatedSum
