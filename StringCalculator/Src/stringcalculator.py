def check_expression_validity(expression: list, delimiter: str = ",") -> str:
    """
    Input expression validity checker !
    Raises an error <with specific message in case of invalidity
    """

    # Checks if expression is starting with anything else than a digit
    if (expression[0] != "/") and (ord(expression[0]) < 48 or ord(expression[0]) > 57):
        raise SyntaxError(f"Invalid expression: '{str(''.join(expression))}'")

    # Checks if expression is ending with anything else than a digit
    if ord(expression[-1]) < 48 or ord(expression[-1]) > 57:
        raise SyntaxError(f"Invalid expression: '{str(''.join(expression))}'")

    # Checks if there is only user specified 1 char long delimiter in expression
    if expression[0] == "/":
        for digit in expression[4:]:
            if (
                (str.isdigit(digit) == False)
                and (ord(digit) != 10)
                and (digit != delimiter)
            ):
                print(digit)
                raise SyntaxError(f"Invalid expression: '{str(''.join(expression))}'")


def check_negative_numbers(expression: list) -> str:
    """
    Checks if there are negative numbers in the input expression
    calculate("5,-4,1,-2") returns "negatives not allowed: -4, -2"
    """
    negativeNumbers = []
    for digit in expression:
        if digit < 0:
            negativeNumbers.append(str(digit))
    if len(negativeNumbers) != 0:
        raise ArithmeticError(
            f'negatives not allowed: {str(", ".join(negativeNumbers))}'
        )


def rewrite_empty_expression(expression: list) -> bool:
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
    delimiter = expression[2]

    return delimiter


def shrink_expression(expression: list) -> list:
    """
    Rewrites input expression if a user specified delimiter is given by popping out
    delimiter definition :

    "//@\n1@2" becomes "1@2"
    """
    if expression[0] == "/":
        return expression[4:]
    else:
        return expression


def split_expression(expression: str, delimiter: str = ",") -> list:
    """
    Splits input expression according to the given delimiter.
    Returns a list of integer
    """

    temp_integer = ""
    integerSplit = []
    for idx in range(len(expression)):
        if expression[idx] == "\n":
            expression[idx] = delimiter
        digit = expression[idx]
        if digit != delimiter:
            temp_integer += digit
        if digit == delimiter or idx == len(expression) - 1:
            integerSplit.append(temp_integer)
            temp_integer = ""

    return list(map(int, integerSplit))


def keep_lesser_than_limit(expression: list, limit: int = 1000) -> list:
    """
    Will return expression without integers greater than limit
    """
    keptIntegers = [i for i in expression if i <= limit]

    if len(keptIntegers) == 0:
        keptIntegers = [0]

    return keptIntegers


def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """
    expression = list(expression)

    expression = rewrite_empty_expression(expression)

    if expression[0] == "/":
        delimiter = extract_delimiters(expression)
    else:
        delimiter = ","

    try:
        check_expression_validity(expression, delimiter)

        expression = shrink_expression(expression)

        integerSplit = split_expression(expression, delimiter)

        # print(integerSplit)

        check_negative_numbers(integerSplit)

        integerSplit = keep_lesser_than_limit(integerSplit)

        # print(integerSplit)

        return sum(integerSplit)

    except SyntaxError as err:
        return err.args[0]

    except ArithmeticError as err:
        return err.args[0]


print(calculate("1001,1000"))
