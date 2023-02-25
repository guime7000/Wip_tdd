def find_delimiter_indexes(expression: str, delimiterList: list = [",", "\n"]) -> list:
    """
    Finds the index of delimiter in the input expression
    Returns those index(es) as a list
    """
    delimiterIndex = []
    for i in range(len(expression)):
        if expression[i : i + len(delimiterList[0])] in delimiterList:
            delimiterIndex.append(i)

    return delimiterIndex


def expression_syntax_error_handling(expression: str) -> SyntaxError:
    """
    Raises SyntaxError if expression does not start with a number and ends up with a number.
    """
    if expression[0] == "," or expression[-1] == ",":
        raise SyntaxError(f"Invalid expression : '{expression}'")


def expression_invalid_separator_error_handling(
    expression: str, delimiterList: list, startIndex: int
) -> SyntaxError:
    """
    Raises Syntax error if expression contains some delimiter different frome the ones defined
    """
    i = startIndex
    while i < len(expression):
        print("Func:", i, expression[i], delimiterList)
        if (
            not expression[i].isdigit()
            and expression[i : i + len(delimiterList[0])] not in delimiterList
        ):
            if expression[i] == delimiterList[0][0]:
                i += len(delimiterList[0])
            else:
                raise SyntaxError((f"Invalid expression : '{expression}'"))
        else:
            i += 1


def calculate(expression: str) -> int:
    if expression == "":
        return 0

    delimiterList = ["\n"]

    try:
        # Syntax error handling (bad beginning or end character inside expression)
        expression_syntax_error_handling(expression)

        # User defined Delimiter parsing
        userDelimiter = ""

        if expression[0:2] == "//":
            currentDigitPosition = 2
            if expression[currentDigitPosition] == "{":
                currentDigitPosition += 1

                for digit in expression[currentDigitPosition:]:
                    currentDigitPosition += 1
                    if digit == "\n":
                        break
                    if digit != "}":
                        userDelimiter += digit

                delimiterList = [userDelimiter] + ["\n"]
                startIndex = currentDigitPosition

                expression_invalid_separator_error_handling(
                    expression, delimiterList, startIndex
                )

            else:
                for digit in expression[currentDigitPosition:]:
                    currentDigitPosition += 1
                    if digit == "\n":
                        break
                    if digit != "}":
                        userDelimiter += digit

                delimiterList = [userDelimiter] + ["\n"]
                startIndex = currentDigitPosition

                expression_invalid_separator_error_handling(
                    expression, delimiterList, startIndex
                )

            expression = expression[startIndex:]

        delimiterList = delimiterList + [","]

        delimiterIndex = find_delimiter_indexes(expression, delimiterList)

        # Default delimiter with checking of integers over 1000
        if not delimiterIndex:
            if int(expression) > 1000:
                expression = "0"
            return int(expression)

        # Sum calculation
        totalSum = int(expression[: delimiterIndex[0]])
        negativeNumbersList = []

        for i in range(len(delimiterIndex)):
            currentDelimiterPos = delimiterIndex[i]
            if i == len(delimiterIndex) - 1:
                rightFromDelimiter = int(
                    expression[currentDelimiterPos + len(delimiterList[0]) :]
                )
                if rightFromDelimiter >= 0:
                    if rightFromDelimiter > 1000:
                        rightFromDelimiter = 0
                    totalSum = totalSum + rightFromDelimiter
                else:
                    negativeNumbersList.append(expression[currentDelimiterPos + 1 :])
            else:
                nextDelimiterPos = delimiterIndex[i + 1]
                if int(expression[currentDelimiterPos + 1 : nextDelimiterPos]) > 0:
                    if (
                        int(expression[currentDelimiterPos + 1 : nextDelimiterPos])
                        > 1000
                    ):
                        expression[currentDelimiterPos + 1 : nextDelimiterPos] = 0

                    totalSum = totalSum + int(
                        expression[currentDelimiterPos + 1 : nextDelimiterPos]
                    )
                else:
                    negativeNumbersList.append(
                        expression[currentDelimiterPos + 1 : nextDelimiterPos]
                    )

        if negativeNumbersList:
            raise ArithmeticError(
                f"negatives not allowed: {', '.join(negativeNumbersList)}"
            )

    except SyntaxError as syntaxE:
        print(syntaxE.args[0])
        return syntaxE.args[0]

    except ArithmeticError as arithmE:
        print(arithmE.args[0])
        return arithmE.args[0]

    return totalSum


calculate("//;\n1;2\n3")
# calculate("//{;}\n102;5")
# calculate("//{***}\n5***20")
