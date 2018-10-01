# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        head = TreeNode(0)
        pre = [head]

        def inorderUtil(root, pre):
            if not root:
                return None

            inorderUtil(root.left, pre)

            node = pre[0]
            node.right = root
            node.left = None

            pre[0] = root
            inorderUtil(root.right, pre)

        inorderUtil(root, pre)
        pre[0].left = None
        return head.right
