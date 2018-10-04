from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        que = deque()
        decode = ""
        que.append(root)
        decode += str(root.val)

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

    # TODO: complete on leetcode
    def deserialize(self, data):
        # TreeNode root =

        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # for i in range(len(data)):
