from collections import deque
from collections import defaultdict



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        que = deque()
        decode = ""
        que.append(root)

        while (que):
            node = que.popleft()
            if node.left:
                que.append(node.left)
                decode += str(node.left.val)
            else:
                decode += "#"
            if node.right:
                que.append(node.right)
                decode += str(node.right.val)
            else:
                decode += "#"

        return decode



    def levelOrder(self, root):
        queue = deque()
        queue.append(root)

        while (queue):
            node = queue.popleft()
            print("popping node", node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def levelOrderWithNextLine(self, root):
        queue = deque()
        queue.append(root)
        answerList = []
        while (queue):
            print("new line")
            list = []
            for i in range(0, len(queue)):
                node = queue.popleft()
                list.append(node.val)
                print("popping node", node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answerList.append(list)
        print(answerList)
        return answerList




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

# root1.verticalOrderOfTree(root1)
serialize = root1.serialize(root1)
print(serialize)
