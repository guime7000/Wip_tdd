def find_delimiter_indexes(expression: str, delimiterList: list = [",", "\n"]) -> list:
    """
    Finds the index of delimiter in the input expression
    Returns those index(es) as a list
    """
    delimiterIndex = []
    for i in range(len(expression)):
        if expression[i] in delimiterList:
            delimiterIndex.append(i)
    return delimiterIndex


def calculate(expression: str) -> int:
    if expression == "":
        return 0

    try:
        if expression[0] == "," or expression[-1] == ",":
            raise SyntaxError(f"Invalid expression : '{expression}'")
    except SyntaxError as syntaxE:
        return syntaxE.args[0]

    if expression[0] == "/":
        delimiterList = [expression[2]] + ["\n"]
        expression = expression[4:]
        print(expression)

    else:
        delimiterList = [",", "\n"]

    delimiterIndex = find_delimiter_indexes(expression, delimiterList)

    if len(delimiterIndex) == 0:
        return int(expression)

    totalSum = int(expression[: delimiterIndex[0]])

    for i in range(len(delimiterIndex)):
        if i == len(delimiterIndex) - 1:
            totalSum = totalSum + int(expression[delimiterIndex[i] + 1 :])
        else:
            totalSum = totalSum + int(
                expression[delimiterIndex[i] + 1 : delimiterIndex[i + 1]]
            )

    return totalSum


calculate("//;\n1")
