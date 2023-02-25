def find_delimiter_indexes(expression: str, delimiterList: list = [",", "\n"]) -> list:
    """
    Finds the index of delimiter in the input expression
    Returns those index(es) as a list
    """
    delimiterIndex = []
    for i in range(len(expression)):
        if (
            not expression[i].isdigit()
            and expression[i] not in delimiterList
            and expression[i] != "-"
        ):
            raise SyntaxError((f"Invalid expression : '{expression}'"))
        if expression[i] in delimiterList:
            delimiterIndex.append(i)
    return delimiterIndex


def calculate(expression: str) -> int:
    if expression == "":
        return 0

    delimiterList = [",", "\n"]

    try:
        if expression[0] == "," or expression[-1] == ",":
            print("BBBOOOOOOOOB3")
            raise SyntaxError(f"Invalid expression : '{expression}'")

        if expression[0] == "/":
            delimiterList = [expression[2]] + ["\n"]
            for i in range(4, len(expression)):
                if (
                    (not expression[i].isdigit())
                    and (expression[i] not in delimiterList)
                    and expression[i] != "-"
                ):
                    raise SyntaxError((f"Invalid expression : '{expression}'"))

            expression = expression[4:]

        delimiterIndex = find_delimiter_indexes(expression, delimiterList)

        if len(delimiterIndex) == 0:
            if int(expression) > 1000:
                expression = "0"
            return int(expression)

        totalSum = int(expression[: delimiterIndex[0]])
        negativeNumbersList = []

        for i in range(len(delimiterIndex)):
            currentDelimiterPos = delimiterIndex[i]
            if i == len(delimiterIndex) - 1:
                rightFromDelimiter = int(expression[currentDelimiterPos + 1 :])
                if rightFromDelimiter > 0:
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


calculate("1,-2")
