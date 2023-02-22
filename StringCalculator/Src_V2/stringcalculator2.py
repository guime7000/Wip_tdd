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

        for i in range(len(delimiterIndex)):
            if i == len(delimiterIndex) - 1:
                totalSum = totalSum + int(expression[delimiterIndex[i] + 1 :])
            else:
                totalSum = totalSum + int(
                    expression[delimiterIndex[i] + 1 : delimiterIndex[i + 1]]
                )

    return totalSum
