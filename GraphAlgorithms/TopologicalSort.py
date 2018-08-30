from collections import defaultdict


class Graph:
    def __init__(self,total):
        self.adj = defaultdict(list)
        self.totalNodes = total

    def addEdge(self, x, y):
        self.adj[x].append(y)


    
