class Trie:
    def __init__(self, isCompleted=None, value=None):
        self.isCompleted = isCompleted
        self.char = value
        self.value = 0
        self.childs = dict()


class solution:

    # TODO: Trie basics
    def addWord(self, word, value, trieRoot):
        for i in range(len(word)):
            if word[i] in trieRoot.childs:
                trieRoot = trieRoot.childs[word[i]]
            else:
                trieNode = Trie(None, word[i])
                trieRoot.childs[word[i]] = trieNode
                trieRoot = trieNode

        trieRoot.isCompleted = True
        trieRoot.value = value

    def getRoot(self, word, trieRoot):
        for i in range(len(word)):
            if trieRoot.isCompleted:
                return trieRoot
            if word[i] in trieRoot.childs:
                trieRoot = trieRoot.childs[word[i]]
            else:
                return None

    def getSumofGivenPrefix(self, prefix, trieRoot):
        for char in prefix:
            childs = trieRoot.childs
            if char in childs:
                trieRoot = childs[char]
            else:
                return 0

        print(trieRoot.char)
        return self.getSum(trieRoot)

    # To get the sum of all nodes starting from given root node
    def getSum(self, trieRoot):
        sum = 0

        for node in trieRoot.childs.values():
            sum += self.getSum(node)

        return sum + trieRoot.value

    # search("pad") -> false
    # search("bad") -> true
    # search(".ad") -> true
    # search("b..") -> true

    def getValid(self, word, root, index):
        if index == len(word) and root.isCompleted:
            return True

        if index == len(word) and not root.isCompleted:
            return False

        if word[index] in root.childs:
            return self.getValid(word, root.childs[word[index]], index + 1)

        flag = False
        if word[index] == '.':
            for child in root.childs.values():
                flag = flag or self.getValid(word, child, index + 1)
            return flag
        else:
            return False


trieRoot = Trie(None, ' ')
s = solution()
s.addWord('apple', 3, trieRoot)
# addWord('app', 2, trieRoot)
# addWord('ho', 2, trieRoot)
print(s.getSumofGivenPrefix('ap', trieRoot))
