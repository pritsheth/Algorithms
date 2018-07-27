class Trie:
    def __init__(self, isCompleted=None, value=None):
        self.isCompleted = isCompleted
        self.isCompleted = value
        self.childs = dict()




def addWord(word,trieRoot):
    for i in range(len(word)):
        if word[i]  in trieRoot.childs:
             trieRoot = trieRoot.childs[word[i]]
        else:
            trieRoot.childs[word[i]] = Trie(None,word[i])
            trieRoot = trieRoot.childs[word[i]]

trieRoot = Trie(None,' ')

addWord('hello',trieRoot)
addWord('hel',trieRoot)
addWord('helo',trieRoot)
print(trieRoot)
