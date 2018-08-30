from collections import defaultdict


class Graph:
    def __init__(self, total):
        self.adj = defaultdict(list)
        self.totalNodes = total

    def addEdge(self, x, y):
        self.adj[x].append(y)


g = Graph(6)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(3, 5)
print(g.adj)

#                 1
#              2  3   4
#                 5
