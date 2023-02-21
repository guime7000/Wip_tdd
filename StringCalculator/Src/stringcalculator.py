def check_expresssion_validity(expression: str) -> str:
    """
    Input expression validity checker !
    Raises an error <with specific message in case of invalidity
    """
    try:
        return "BLABLA"
    except:
        if expression == "0":
            raise Exception(f'Invalid expression: {"".join(expression)}')


def rewrite_empty_expression(expression: str) -> bool:
    """
    returns "0" if the length of expression equals 0
    """

    if len(expression) == 0:
        expression = "0"

    return expression


def extract_delimiter(expression: str) -> str:
    """
    Extracts a specific delimiter, different from a comma, from the input expression
    """
    delimiter = ","

    return delimiter


def split_expression(expression: str) -> list:
    """
    Splits input expression according to the given delimiter.
    Returns a list of integer
    """

    delimiter = extract_delimiter(expression)

    temp_integer = ""
    integerSplit = []
    for idx in range(len(expression)):
        if expression[idx] == "\n":
            expression[idx] = ","
        digit = expression[idx]
        if digit != delimiter:
            temp_integer += digit
        if digit == delimiter or idx == len(expression) - 1:
            integerSplit.append(temp_integer)
            temp_integer = ""

    return list(map(int, integerSplit))


def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """

    expression = list(expression)

    expression = rewrite_empty_expression(expression)

    integerSplit = split_expression(expression)

    return sum(integerSplit)
