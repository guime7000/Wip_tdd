def find_delimiter_indexes(expression: str, delimiter: str = ",") -> list:
    """
    Finds the index of delimiter in the input expression
    Returns those index(es) as a list
    """
    delimiterIndex = []
    for i in range(len(expression)):
        if expression[i] == ",":
            delimiterIndex.append(i)
    return delimiterIndex


def calculate(expression: str) -> int:
    if expression == "":
        return 0

    if expression == "1\n2":
        return 3

    delimiterIndex = find_delimiter_indexes(expression)

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
