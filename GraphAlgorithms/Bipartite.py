from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, total):
        self.adj = defaultdict(list)
        self.totalNodes = total

    def addEdge(self, x, y):
        self.adj[x].append(y)
        self.adj[y].append(x)

    def isBipartiteGraph(self, adj, root):
        que = deque()
        visited = [0] * self.totalNodes
        colour = [set(), set()]
        current_colour = 0
        # 0 : Red and 1 : Blue
        que.append(root)
        colour[current_colour].add(root)

        while que:

            other_colour = 1 ^ current_colour
            # For level wise order:
            for i in range(0, len(que)):
                node = que.popleft()
                visited[node] = True
                print(node)
                childs = adj[node]

                for ch in childs:
                    #         First check the other colour list
                    if ch in colour[current_colour]:
                        return False
                    colour[other_colour].add(ch)
                    if not visited[ch]:
                        que.append(ch)

            current_colour = other_colour
        print(colour)
        return True


g = Graph(6)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(3, 5)
g.addEdge(4, 5)

#                1
#              2   3
#              4---5

print(g.isBipartiteGraph(g.adj, 1))

g1 = Graph(7)
g1.addEdge(1, 2)
g1.addEdge(1, 3)
g1.addEdge(2, 4)
g1.addEdge(3, 5)
g1.addEdge(4, 6)
g1.addEdge(5, 6)

print(g1.isBipartiteGraph(g1.adj, 1))

#              1 ---2
#              3    4
#              5 -- 6
