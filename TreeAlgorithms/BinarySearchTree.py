from collections import defaultdict

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

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

    # Must do question
    def longestUnivaluePath(self, root):

        self.longPath = 0

        def getPath(root):
            if root is None:
                return 0

            lpath = getPath(root.left)
            rpath = getPath(root.right)

            lnode, rnode = 0, 0
            if root.left and root.left.val == root.val:
                lnode = lpath + 1
            if root.right and root.right.val == root.val:
                rnode = rpath + 1
            self.longPath = max(self.longPath, lnode + rnode)
            return max(lnode, rnode)

        getPath(root)
        return self.longPath

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

    def trimBST(self, root, L, R):
        if L > root.val or root.val > R:
            return None

        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)



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

    def connect(self, root):

            if root is None:
                return

            def getNextNode(root):
                node = root.next
                while (node is not None):
                    if node.left is not None:
                        return node.left
                    elif node.right is not None:
                        return node.right
                    node = node.next
                return None

            if root.left is not None:
                root.left.next = root.right if root.right is not None else getNextNode(root)
            if root.right is not None:
                root.right.next = getNextNode(root)
            self.connect(root.left)
            self.connect(root.right)










            # 1
       # 2           3
    # 4    5       6   7

    def levelOrder(self,root):
        que = []
        que.append(root)
        d = 1

        while (len(que)!=0):
            x = 0
            print("--------")
            for i in range(d):
                root = que.pop(0)
                print(root.val)
                if root.left is not None:
                    que.append(root.left)
                    x +=1
                if root.right is not None:
                    que.append(root.right)
                    x +=1

            d = x


    def findFrequentTreeSum(self, root):

        self.dict1 = defaultdict(int)

        def getTreeSum(self, root):

            if root is None:
                return 0

            l = self.getTreeSum(root.left)
            r = self.getTreeSum(root.right)
            root.val = l + r + root.val
            self.dict1[root.val] += 1
            return root.val


        getTreeSum(root)
        print(self.dict1)
        d = defaultdict(list)
        for i in self.dict:
            d[i].append(dict[i])
        print(d)



        """
        :type root: TreeNode
        :rtype: List[int]
        """


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

# print(root1.getDiameter(root1))
# root1.levelOrder(root1)