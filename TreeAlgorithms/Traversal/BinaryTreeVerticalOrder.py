from collections import deque
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def verticalOrder(self, root):
        queue = deque()
        queue.append(root)

        while (queue):
            node = queue.popleft()
            print("popping node", node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def verticalOrderOfTree(self, root):
        queue = deque()
        dict = defaultdict(list)
        queue.append([root, 0])

        while (queue):
            nodePair = queue.popleft()
            node = nodePair[0]
            hd = nodePair[1]
            print("popping node", node.val)
            dict[hd].append(node.val)

            if node.left:
                queue.append([node.left, hd - 1])
            if node.right:
                queue.append([node.right, hd + 1])

        print(dict)
        l = sorted(dict.items())
        print(l)


root1 = TreeNode(1)
root2 = TreeNode(2)
root3 = TreeNode(3)
root4 = TreeNode(4)
root5 = TreeNode(5)
root6 = TreeNode(6)
root7 = TreeNode(7)

root1.left = root2
root1.right = root3

root2.left = root4
root2.right = root5

root3.left = root6
root3.right = root7

root1.verticalOrder(root1)
