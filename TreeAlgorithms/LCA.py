# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root
        left, right = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)
        return root if left and right else left or right


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(6)

root.right = TreeNode(3)
root.right.left = TreeNode(12)


# node = s.lowestCommonAncestor(root, root.left.left, root.right.left)
# print(node.val)


def processInput(text):
    ax = text.split(' ')
    print(ax)


def processStack(stk):
    temp = stk[0]
    index = 0
    while (index != len(stk)):
        if stk[index] == 'AND':
            temp = temp & stk[index + 1]
            index += 2
        elif stk[index] == 'OR':
            temp = temp | stk[index + 1]
            index += 2
        else:
            index += 1
    print(temp)
    return temp


processStack([True, 'AND', True])
