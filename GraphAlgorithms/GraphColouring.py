from collections import defaultdict


class Graph:
    def __init__(self, total):
        self.adj = defaultdict(list)
        self.totalNodes = total

    def addEdge(self, x, y):
        self.adj[x].append(y)

    def graphColouring(self, adj, total_color):
        pass

    def graphColourUtil(self,adj,vertex,colour):
        pass

    def isColouringSafe(self, adj, colour, vertex, current_colour):

        for node in adj[vertex]:
            if colour[node] == current_colour:
                return False

        return True
