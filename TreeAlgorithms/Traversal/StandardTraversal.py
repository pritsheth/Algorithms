class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Traversal:

    def inorder(self, root):
        if not root:
            return None

        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)



    def inorder_iterative(self,root):

        stk = []

        if not root:
            return

        stk.append(root)
        while stk and stk[-1]:

            root = stk.pop()
            print(root.val)
            stk.append(root.right)
            stk.append(root)
            stk.append(root.left)


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

tr = Traversal()
tr.inorder(root1)
print("--------------")
tr.inorder_iterative(root1)

#
#             1
#     2            3
# 4      5       6   7
#
