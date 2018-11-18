from collections import defaultdict


class TreeNode:
    def __init__(self, val):
        self.childs = []
        self.data = val


def buildTree(A, E):
    nodeMap = {}
    edgeMap = defaultdict(list)

    # Store index for each node
    for index in range(len(A)):
        node = TreeNode(A[index])
        nodeMap[index] = node

    # Each edge will contain index mapp [0-1,0-2,0-3,0-4]

    for edge in E:
        edgeMap[edge[0]].append(nodeMap[edge[1]])

    print("edgemap", edgeMap)
    print("nodemap", nodeMap)
    for keys in edgeMap:
        print(keys)
        root = nodeMap[keys]
        print(root.data)
        for child in edgeMap[keys]:
            root.childs.append(child)
    return getUniValuePath(nodeMap[0])


longestPath = 0


def getUniValuePath(root):
    def getLongPath(root):
        global longestPath

        if root is None:
            return 0

        sum = 0
        pathLength = 0

        for child in root.childs:
            childPAth = getLongPath(child)
            childPAth = childPAth + 1 if root.data == child.data else 0
            sum += childPAth
            pathLength = max(pathLength, childPAth)

        longestPath = max(longestPath, sum)
        return pathLength

    getLongPath(root)
    return longestPath


path = 10


def checkGlobal():
    global path

    def check():
        global path
        path += 1
        print(path)

    check()


# checkGlobal()


print("longest path is", buildTree([1, 4, 5, 4, 4, 5], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5]]))
