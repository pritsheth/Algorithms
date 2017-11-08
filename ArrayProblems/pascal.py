def generate(self, numRows):
    result = [[]] * numRows
    for i in range(numRows):
        result[i] = [1] * (i + 1)

    for i in range(1, numRows):
        for j in range(1, i):
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result
