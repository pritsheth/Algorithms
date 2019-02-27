# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def recur(root):
            if not root:
                result.append(None)
                return

            result.append(root.val)
            recur(root.left)
            recur(root.right)

        recur(root)

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def recur(data):
            if data[0] is None:
                data.pop(0)
                return None

            root = TreeNode(data[0])
            data.pop(0)
            root.left = recur(data)
            root.right = recur(data)
            return root

        return recur(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
