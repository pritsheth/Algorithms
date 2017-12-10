from collections import defaultdict


class Graph:
    def __init__(self,total):
        self.adj = defaultdict(list)
        self.totalNodes = total

    def addEdge(self, x, y):
        self.adj[x].append(y)

    def BFS(self, root):

        pass

    def DFS(self, root):
        visited = [False] * self.totalNodes

        # visited[root] = True
        self.dfsUtil(root, visited)

        pass

    def dfsUtil(self, root, visited):
        visited[root] = True
        print(root)
        for node in self.adj[root]:
            if not visited[node]:
                self.dfsUtil(node,visited)


g = Graph(6)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(3, 5)
print(g.adj)
g.DFS(1)


#                 1
#              2  3   4
#                 5
