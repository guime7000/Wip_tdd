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
        if len(delimiter) == 1:
            for digit in expression[4:]:
                if (
                    (str.isdigit(digit) == False)
                    and (ord(digit) != 10)
                    and (digit != delimiter)
                ):
                    raise SyntaxError(
                        f"Invalid expression: '{str(''.join(expression))}'"
                    )
        # else :
        #     for i range(5+len(delimiter),len(expression)-3):
        #         if


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


def keep_lesser_than_limit(expression: list, limit: int = 1000) -> list:
    """
    Will return expression without integers greater than limit
    """
    keptIntegers = [i for i in expression if i <= limit]

    if len(keptIntegers) == 0:
        keptIntegers = [0]

    return keptIntegers


def rewrite_empty_expression(expression: list) -> bool:
    """
    returns "0" if the length of expression equals 0
    """

    if len(expression) == 0:
        expression = "0"

    return expression


def extract_delimiters(expression: str) -> str:
    """
    Finds the Delimiter pattern to be used in the expression
    Returns the pattern
    """
    # calculate("//{***}\n5***20") == 25
    if expression[2] == "{":
        delimiter = ""
        for elem in expression[3:]:
            if elem != "}":
                # break
                delimiter += elem
    else:
        delimiter = expression[2]

    return delimiter


def shrink_expression(expression: list, delimiter: str = ",") -> list:
    """
    Rewrites input expression if a user specified delimiter is given by popping out
    delimiter definition :

    "//@\n1@2" becomes "1@2"
    """
    if expression[0] == "/":
        if len(delimiter) == 1:
            print("BOB: ", expression[4:])
            return expression[4:]
        else:
            return expression[6 + len(delimiter) :]


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


def calculate(expression: str) -> int:
    """
    Returns the sum of integers written in expression
    """

    expression = rewrite_empty_expression(expression)

    delimiter = ","
    if expression[0] == "/":
        delimiter = extract_delimiters(expression)

    expression = list(expression)
    # delimiterLength = len(delimiter)

    try:
        check_expression_validity(expression, delimiter)
        print(expression, "DELIMITER:", delimiter)
        print("-----------")
        print(delimiter)
        if expression[0] == "/":
            i = 0
            while expression[i] != "\n":
                i += 1
            expression = expression[i + 1 :]
            print("Bob", expression)

            # expression = shrink_expression(expression, delimiter)

        integerSplit = split_expression(expression, delimiter)

        check_negative_numbers(integerSplit)

        integerSplit = keep_lesser_than_limit(integerSplit)

        return sum(integerSplit)

    except SyntaxError as err:
        return err.args[0]

    except ArithmeticError as err:
        return err.args[0]


print(calculate("//{*}\n5*20"))
