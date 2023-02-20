def rewrite_empty_expression(expression: str) -> bool:
    """
    returns "0" if the length of expression equals 0
    """

    if len(expression) == 0:
        expression = "0"

    return expression


def split_expression(expression: str, delimiter: str = ",") -> list:
    """
    Splits input expression according to the given delimiter.
    Returns a list of integer stored as string
    """

    temp_integer = ""
    integerSplit = []
    for idx in range(len(expression)):
        digit = expression[idx]
        if digit != delimiter:
            temp_integer += digit
        if digit == delimiter or idx == len(expression) - 1:
            integerSplit.append(temp_integer)
            temp_integer = ""

    return integerSplit


def calculate(expression: str, delimiter: str = ",") -> int:
    """
    Returns the sum of integers written in expression
    """

    calculatedSum = 0
    integerSplit = []
    # expressionLength = len(expression)

    expression = rewrite_empty_expression(expression)

    # A string to build integers digit after digit along expression
    # temp_stringed_int = ""
    # for idx in range(expressionLength):
    #     digit = expression[idx]
    #     if digit != delimiter:
    #         temp_stringed_int += digit
    #     if digit == delimiter or idx == expressionLength - 1:
    #         integerSplit.append(temp_stringed_int)
    #         temp_stringed_int = ""

    integerSplit = split_expression(expression)

    calculatedSum = sum(list(map(int, integerSplit)))

    return calculatedSum
