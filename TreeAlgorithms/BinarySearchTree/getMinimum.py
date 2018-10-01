# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimum(self, root):

        while root.left:
            root = root.left

        if not root.right:
            return root.data

        root = root.right

        while root.left:
            root = root.left

        return root.val


def getCost(row, col, size):
    return (row * size) + col

def roverMove(matrixSize, cmds):
    i, j = 0, 0
    for command in cmds:

        if command == 'LEFT':
            if j - 1 >= 0:
                j -= 1
        elif command == 'RIGHT':
            if j + 1 < matrixSize:
                j += 1
        elif command == 'UP':
            if i - 1 >= 0:
                i -= 1
        elif command == 'DOWN':
            if i + 1 < matrixSize:
                i += 1

    cost = getCost(i, j, matrixSize)
    print(cost)
    return cost


roverMove(4, ['RIGHT', 'DOWN', 'LEFT', 'LEFT', 'DOWN'])



def huffmanDecode (dictionary, text):
    decoded_result = ""
    while text:
        for key in dictionary:
            if text.startswith(key):
                decoded_result += dictionary[key]
                text = text[len(key):]
    return decoded_result
