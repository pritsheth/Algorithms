from GraphAlgorithms.Graph import Graph

#  Transitive Closure of a Graph using DFS
class GraphTransitivity:

    def get_transit_matrix(self, graph):
        adjacency = graph.adj
        print(adjacency)


gt = GraphTransitivity()
g = Graph(6)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(3, 5)

gt.get_transit_matrix(g)
