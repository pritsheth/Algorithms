# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        def util(root, low, high):
            if not root:
                return True

            return low < root.val and root.val < high and util(root.left, low, root.val) and util(root.right,
                                                                                                  root.val, high)

        return util(root, -float("INF"), float("INF"))
