from collections import defaultdict


class Graph:
    def __init__(self, total):
        self.adj = defaultdict(list)
        self.totalNodes = total

    def addEdge(self, x, y):
        self.adj[x].append(y)

    def isCycleUtil(self, root, visited):
        visited[root] = True

        for node in self.adj[root]:
            if visited[node]:
                return True
            elif self.isCycleUtil(node, visited) == True:
                return True
            # return False

    def isCycle(self, root):
        visited = [False] * self.totalNodes
        # For disjoint nodes
        for i in range(1, self.totalNodes):
            if not visited[i]:
                if self.isCycleUtil(root, visited) == True:
                    return True
        return False


g = Graph(6)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(3, 5)
g.addEdge(5, 1)
print(g.adj)
print("DFS traversal")
# g.DFS(1)

print("BFS traversal")
# g.BFS(g.adj, 1)

print("Cycle detection")
print(g.isCycle(1))

#                 1
#              2  3   4
#                 5
