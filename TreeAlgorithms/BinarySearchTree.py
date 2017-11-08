class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def preorder(self, node):
        if node is None:
            return
        print(node.val)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val)
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.val)


    def getHeight(self,root):
        if root is None:
            return 0
        return max(self.getHeight(root.left),self.getHeight(root.right))+1

    def getDiameter(self,root):

        if root is None:
            return 0

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        leftDiameter = self.getDiameter(root.left)
        rightDiameter = self.getDiameter(root.right)

        currentDiameter = leftHeight + rightHeight
        return max(currentDiameter,max(leftDiameter,rightDiameter))






            # 1
       # 2           3
    # 4    5       6   7


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

print(root1.getDiameter(root1))