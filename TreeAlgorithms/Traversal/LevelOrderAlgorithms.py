from collections import deque
from collections import defaultdict


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

    # N ary Tree : Level order traversal

    """
    # Definition for a Node.
    class Node(object):
        def __init__(self, val, children):
            self.val = val
            self.children = children
    """

    class Solution(object):
        def levelOrder(self, root):
            """
            :type root: Node
            :rtype: List[List[int]]
            """
            if not root:
                return []
            q = deque()
            q.append(root)
            final_list = []
            while q:
                result = []
                for i in range(len(q)):
                    node = q.popleft()
                    result.append(node.val)
                    childs = node.children
                    for ch in childs:
                        q.append(ch)

                final_list.append(result)
            return final_list



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