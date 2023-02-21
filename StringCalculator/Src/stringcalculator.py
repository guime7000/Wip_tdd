def check_expresssion_validity(expression: list) -> str:
    """
    Input expression validity checker !
    Raises an error <with specific message in case of invalidity
    """

    # Checks if expression is starting with anything else than a digit
    if ord(expression[0]) < 48 or ord(expression[0]) > 57:
        raise SyntaxError(f"Invalid expression: '{''.join(expression)}'")

    # Checks if expression is ending with anything else than a digit
    if ord(expression[-1]) < 48 or ord(expression[-1]) > 57:
        raise SyntaxError(f"Invalid expression: '{''.join(expression)}'")


def rewrite_empty_expression(expression: str) -> bool:
    """
    returns "0" if the length of expression equals 0
    """

    if len(expression) == 0:
        expression = "0"

    return expression


def extract_delimiters(expression: str) -> str:
    """
    Extracts one or more user specified delimiter(s) from the input expression
    and rewrites expression by replacing user defined delimiters by commas
    """

    delimiter = ","

    return delimiter


def split_expression(expression: str) -> list:
    """
    Splits input expression according to the given delimiter.
    Returns a list of integer
    """

    # delimiter = extract_delimiter(expression)
    delimiter = ","

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

    expression = rewrite_empty_expression(expression)

    expression = list(expression)
    print(expression)
    if expression[0] == "/":
        delimiter = expression[2]
        expression = expression[4:]
        print(expression)
        for i, elem in enumerate(expression):
            if elem == delimiter:
                expression[i] = ","
    print(expression)

    try:
        check_expresssion_validity(expression)

        integerSplit = split_expression(expression)

        return sum(integerSplit)

    except SyntaxError as err:
        return err.args[0]
