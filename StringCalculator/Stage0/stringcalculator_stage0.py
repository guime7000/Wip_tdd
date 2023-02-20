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
    Returns a list of integer
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

    return list(map(int, integerSplit))


def calculate(expression: str, delimiter: str = ",") -> int:
    """
    Returns the sum of integers written in expression
    """

    expression = rewrite_empty_expression(expression)

    integerSplit = split_expression(expression)

    calculatedSum = sum(integerSplit)

    return calculatedSum
