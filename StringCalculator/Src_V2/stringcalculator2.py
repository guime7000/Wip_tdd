def calculate(expression: str) -> int:
    if len(expression) == 0:
        return 0

    delimiterIndex = []
    for i in range(len(expression)):
        if expression[i] == ",":
            delimiterIndex.append(i)

    if len(delimiterIndex) == 0:
        totalSum = int(expression)
    else:
        totalSum = int(expression[: delimiterIndex[0]])

        if len(delimiterIndex) == 1:
            i = 0
            totalSum = int(expression[: delimiterIndex[i]])
            totalSum = totalSum + int(expression[delimiterIndex[i] + 1 :])

        if len(delimiterIndex) == 2:
            i = 0
            totalSum = int(expression[: delimiterIndex[i]])
            totalSum = totalSum + int(
                expression[delimiterIndex[i] + 1 : delimiterIndex[i + 1]]
            )
            i = 1
            totalSum = totalSum + int(expression[delimiterIndex[i] + 1 :])

    return totalSum

    # return int(expression)
