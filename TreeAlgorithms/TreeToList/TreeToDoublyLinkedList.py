# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# TODO: Do with good solutions
class Solution:
    def convertToDoubly(self, root):

        head = TreeNode(0)
        pre = [head]

        def doublyUtil(root, pre):
            if not root:
                return

            doublyUtil(root.left, pre)

            node = pre[0]
            node.right = root
            root.left = node

            # save previous node for future double link
            pre[0] = root

            doublyUtil(root.right, pre)

        doublyUtil(root, pre)

        print("last node value",pre[0].val)
        root = head
        while head:
            print(head.val)
            head = head.right




s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(6)

root.right = TreeNode(3)
root.right.left = TreeNode(12)

s.convertToDoubly(root)


