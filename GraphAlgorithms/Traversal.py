from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def addEdge(self, x, y):
        self.adj[x].append(y)


    def BFS(self,root):



        pass

    def DFS(self,root):
        pass




g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(3,5)
print(g.adj)


#                 1
#              2  3   4
#                 5