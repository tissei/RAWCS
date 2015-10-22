from src.ExtendedDiGraph import ExtendedDiGraph


class DIMACSGraph(ExtendedDiGraph):
    def __init__(self, nodes, edges, edgesList):
        super(DIMACSGraph, self).__init__()
        self.nodes = nodes
        self.edges = edges
        [self.addEdge(edge.vertex, edge.adjacent) for edge in edgesList]
