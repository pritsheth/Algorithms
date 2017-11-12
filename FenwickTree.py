def getPrefixSum(fenwickTree, index):
    index += 1
    prefixSum = 0

    while index > 0:
        prefixSum += fenwickTree[index]
        index -= index & (-index)
    return prefixSum


def updateValue(fenwickTree, n, index, value):
    index += 1

    while (index <= n):
        fenwickTree[index] += value
        index += index & (-index)


def buildFenwickTree(array):
    n = len(array)
    fenwickTree = [0] * (n + 1)

    for i in range(n):
        updateValue(fenwickTree, n, i, array[i])

    return fenwickTree


freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
BITTree = buildFenwickTree(freq)
print(BITTree)
print("Sum of elements in arr[0..5] is " + str(getPrefixSum(BITTree, 5)))
freq[3] += 6
updateValue(BITTree, len(freq), 3, 6)
