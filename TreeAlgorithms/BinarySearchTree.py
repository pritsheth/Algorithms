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

            # Most optimized diameter solution

    def getDiameterOptimized(self,root):
        if root is None:
            return 0

        self.maxD = 0

        def getMaxDiameter(root):
            if root is None:
                return 0

            leftHeight = getMaxDiameter(root.left)
            rightHeight = getMaxDiameter(root.right)

            currentD = leftHeight + rightHeight
            self.maxD = max(self.maxD,currentD)
            return max(leftHeight,rightHeight) + 1

        getMaxDiameter(root)
        return self.maxD

    def isEqualtree(self, s, t):

        if s is None and t is None:
            return True

        if s is None or t is None:
            return False


        return s.val == t.val and self.isEqualtree(s.left,t.left) and self.isEqualtree(s.left,t.left)

    def isSubTree(self,s,t):

        if s is None:
            return True


        return self.isEqualtree(s,t) or self.isEqualtree(s.left,t) or self.isEqualtree(s.right,t)

    def constructMaximumBinaryTree(self, nums):
            """
            :type nums: List[int]
            :rtype: TreeNode
            """
            return self.constructMaxTree(nums,0,len(nums)-1)


    def constructMaxTree(self,nums,low,high):

        if high<low:
            return None
        if low == high:
            return TreeNode(nums[low])
        index = self.getMaxNode(nums, low, high)
        root = TreeNode(nums[index])
        root.left = self.constructMaxTree(nums,low,index-1)
        root.right = self.constructMaxTree(nums,index+1,high)
        return root

    def getMaxNode(self,nums,low,high):
        maxi,index = -10000,low
        for i in range(low,high):
             if maxi<nums[i]:
                maxi = nums[i]
                index = i

        return index









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
root1.constructMaximumBinaryTree([3,2,1,6,0,5])