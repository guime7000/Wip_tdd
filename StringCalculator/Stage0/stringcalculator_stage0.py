def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """
    calculatedSum = 0
    integerList = []

    if len(expression) == 0:
        return 0

    else:
        # if expression[-1] != ",":
        #     calculatedSum += int(expression)
        #     return calculatedSum

        expressionLength = len(expression)
        temp_stringed_int = ""
        for idx in range(expressionLength):
            digit = expression[idx]
            if digit != ",":
                temp_stringed_int += digit
            if digit == "," or idx == expressionLength - 1:
                integerList.append(temp_stringed_int)
                integerList.append(digit)
                temp_stringed_int = ""

        for idx in range(0, len(integerList), 2):
            calculatedSum += int(integerList[idx])
    return calculatedSum
