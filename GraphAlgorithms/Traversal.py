from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, total):
        self.adj = defaultdict(list)
        self.totalNodes = total

    def addEdge(self, x, y):
        self.adj[x].append(y)

    def BFS(self, graph, root):
        q = deque()
        visited = [False] * self.totalNodes
        q.append(root)
        while (q):
            root = q.popleft()
            visited[root] = True
            print(root)
            for child in graph[root]:
                if not visited[child]:
                    q.append(child)

    def DFS_with_stack(self, root):
        visited = [False] * self.totalNodes
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            print(root)
            visited[root] = True
            for node in self.adj[root]:
                if not visited[node]:
                    stack.append(node)

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
                self.dfsUtil(node, visited)


g = Graph(6)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(3, 5)
print(g.adj)
print("DFS traversal")
g.DFS(1)
print("DFS Stack traversal")
g.DFS_with_stack(1)
print("BFS traversal")
g.BFS(g.adj, 1)

#                 1
#              2  3   4
#                 5
